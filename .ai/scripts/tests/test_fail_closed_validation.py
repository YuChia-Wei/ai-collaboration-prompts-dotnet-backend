#!/usr/bin/env python3
"""GWT regression tests for fail-closed shell asset validation.

These tests intentionally operate only on synthetic Git repositories. They
must never change executable modes, index entries, or files in the real repo.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_SOURCE = REPO_ROOT / ".ai/scripts/validate-shell-assets.py"


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )


def real_repo_snapshot() -> tuple[str, str, str]:
    head = run(["git", "rev-parse", "HEAD"], REPO_ROOT)
    status = run(["git", "status", "--porcelain=v1"], REPO_ROOT)
    shell_stage = run(
        ["git", "ls-files", "--stage", "*.sh"],
        REPO_ROOT,
    )
    for result in (head, status, shell_stage):
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())
    return head.stdout, status.stdout, shell_stage.stdout


class SyntheticShellAssetRepo:
    """Own a disposable repository whose shape matches validator assumptions."""

    def __init__(self) -> None:
        self._temporary = tempfile.TemporaryDirectory(prefix="aic007-shell-assets-")
        self.root = Path(self._temporary.name)
        self.scripts = self.root / ".ai/scripts"
        self.scripts.mkdir(parents=True)
        shutil.copy2(VALIDATOR_SOURCE, self.scripts / VALIDATOR_SOURCE.name)
        initialized = run(["git", "init", "--quiet"], self.root)
        if initialized.returncode != 0:
            self.close()
            raise RuntimeError(initialized.stderr.strip())

    def close(self) -> None:
        self._temporary.cleanup()

    def add_shell(self, name: str, mode: str = "100755") -> str:
        relative = f".ai/scripts/{name}"
        path = self.root / relative
        path.write_text("#!/bin/bash\nexit 0\n", encoding="utf-8", newline="\n")
        added = run(["git", "add", "--", relative], self.root)
        self._require_success(added)
        mode_flag = "+x" if mode == "100755" else "-x"
        updated = run(["git", "update-index", f"--chmod={mode_flag}", "--", relative], self.root)
        self._require_success(updated)
        return relative

    def write_manifest(
        self,
        *,
        retained: list[str],
        retirement_candidates: list[str] | None = None,
        required_entrypoints: list[str] | None = None,
        check_all_required_scripts: list[str] | None = None,
    ) -> None:
        manifest = {
            "schema_version": "1.0",
            "retained": retained,
            "retirement_candidates": retirement_candidates or [],
            "required_entrypoints": required_entrypoints or [],
            "check_all_required_scripts": check_all_required_scripts or [],
        }
        (self.scripts / "shell-assets.yaml").write_text(
            yaml.safe_dump(manifest, sort_keys=False),
            encoding="utf-8",
            newline="\n",
        )

    def validate(self) -> subprocess.CompletedProcess[str]:
        return run([sys.executable, str(self.scripts / VALIDATOR_SOURCE.name)], self.root)

    @staticmethod
    def _require_success(result: subprocess.CompletedProcess[str]) -> None:
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())


class ShellAssetValidationGwtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.real_before = real_repo_snapshot()

    @classmethod
    def tearDownClass(cls) -> None:
        # Then the real checkout HEAD, status, and shell index are unchanged.
        cls.real_after = real_repo_snapshot()
        if cls.real_before != cls.real_after:
            raise AssertionError("synthetic fixture tests mutated the real repository")

    def test_gwt_002_given_retained_mode_100644_when_validated_then_it_fails(self) -> None:
        fixture = SyntheticShellAssetRepo()
        fixture_root = fixture.root
        try:
            # Given a retained shell tracked with Git mode 100644.
            script = fixture.add_shell("required.sh", mode="100644")
            fixture.write_manifest(retained=[script], required_entrypoints=[script])

            # When shell asset validation runs against the synthetic index.
            result = fixture.validate()

            # Then index truth rejects the path regardless of host executability.
            self.assertEqual(1, result.returncode)
            self.assertIn(script, result.stdout)
            self.assertIn("must use Git mode 100755, found 100644", result.stdout)
        finally:
            fixture.close()
        self.assertFalse(fixture_root.exists())

    def test_gwt_012_given_manifest_coverage_mismatch_when_validated_then_lists_both_sides(self) -> None:
        fixture = SyntheticShellAssetRepo()
        try:
            # Given one unclassified tracked shell and one nonexistent manifest path.
            classified = fixture.add_shell("classified.sh")
            missing = fixture.add_shell("missing-from-manifest.sh")
            extra = ".ai/scripts/extra-in-manifest.sh"
            fixture.write_manifest(retained=[classified, extra])

            # When shell asset validation compares manifest and index coverage.
            result = fixture.validate()

            # Then it fails with deterministic missing and extra lists.
            self.assertEqual(1, result.returncode)
            self.assertIn(f"missing=['{missing}']", result.stdout)
            self.assertIn(f"extra=['{extra}']", result.stdout)
        finally:
            fixture.close()

    def test_gwt_013_given_invalid_lifecycle_groups_when_validated_then_invariants_fail(self) -> None:
        cases = (
            ("overlap", ["lifecycle groups overlap"]),
            ("duplicate", ["retained contains duplicate paths"]),
            ("required-outside", ["required_entrypoints must be a subset of retained"]),
        )
        for case, messages in cases:
            with self.subTest(case=case):
                fixture = SyntheticShellAssetRepo()
                try:
                    # Given a manifest violating one lifecycle invariant.
                    retained = fixture.add_shell("retained.sh")
                    outside = fixture.add_shell("outside.sh")
                    if case == "overlap":
                        fixture.write_manifest(
                            retained=[retained, outside],
                            retirement_candidates=[retained],
                        )
                    elif case == "duplicate":
                        fixture.write_manifest(
                            retained=[retained, retained],
                            retirement_candidates=[outside],
                        )
                    else:
                        fixture.write_manifest(
                            retained=[retained],
                            retirement_candidates=[outside],
                            required_entrypoints=[outside],
                        )

                    # When shell asset validation checks lifecycle ownership.
                    result = fixture.validate()

                    # Then the matching invariant is reported as a failure.
                    self.assertEqual(1, result.returncode)
                    for message in messages:
                        self.assertIn(message, result.stdout)
                finally:
                    fixture.close()

    def test_gwt_014_given_valid_manifest_when_validated_then_counts_and_exit_pass(self) -> None:
        fixture = SyntheticShellAssetRepo()
        try:
            # Given complete classification, executable retained paths, and valid subsets.
            entrypoint = fixture.add_shell("entrypoint.sh")
            child = fixture.add_shell("child.sh")
            fixture.write_manifest(
                retained=[entrypoint, child],
                required_entrypoints=[entrypoint],
                check_all_required_scripts=[child],
            )

            # When shell asset validation runs.
            result = fixture.validate()

            # Then it passes with truthful retained, retirement, and tracked counts.
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertIn(
                "passed for 2 retained executable asset(s), 0 retirement candidate(s), "
                "and 2 tracked shell asset(s)",
                result.stdout,
            )
        finally:
            fixture.close()

    def test_gwt_015_given_failed_fixture_when_cleaned_then_real_repo_and_temp_root_are_safe(self) -> None:
        # Given a real-repository snapshot and a synthetic failing fixture.
        real_before = real_repo_snapshot()
        fixture = SyntheticShellAssetRepo()
        fixture_root = fixture.root
        script = fixture.add_shell("non-executable.sh", mode="100644")
        fixture.write_manifest(retained=[script])

        # When validation fails and fixture cleanup runs through finally.
        try:
            result = fixture.validate()
            self.assertEqual(1, result.returncode)
        finally:
            fixture.close()

        # Then temporary state is removed and the real Git state is unchanged.
        self.assertFalse(fixture_root.exists())
        self.assertEqual(real_before, real_repo_snapshot())


if __name__ == "__main__":
    unittest.main()
