#!/usr/bin/env python3
"""Given-When-Then tests for the non-mutating tag-preparation interface."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("prepare_release", ROOT / ".ai" / "scripts" / "prepare-ai-context-release.py")
assert SPEC and SPEC.loader
PREPARE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PREPARE)


class PrepareAiContextReleaseGwtTests(unittest.TestCase):
    def test_gwt_001_given_green_candidate_and_critical_gate_when_prepared_then_only_an_owner_command_is_returned(self):
        original_validate = PREPARE.release_state.validate
        original_release_record = PREPARE.release_state.release_record
        original_clean = PREPARE.release_state.assert_clean_worktree
        calls: list[list[str]] = []
        PREPARE.release_state.validate = lambda *_, **__: {
            "commit": "a" * 40,
            "branch": "main",
        }
        PREPARE.release_state.release_record = lambda *_: (
            Path("release.yaml"),
            {
                "compatibility": {
                    "breaking_changes": True,
                    "automatic_upgrade_sources": [
                        "v0.3.0",
                        "v0.4.0",
                        "v0.4.1",
                        "v0.4.2",
                    ],
                }
            },
            Path("release-notes.md"),
            Path("migration-guide.md"),
        )
        PREPARE.release_state.assert_clean_worktree = lambda *_: None
        try:
            command = PREPARE.prepare(
                Path("."),
                "v0.5.0",
                ai_model="OpenAI Codex (gpt-5.6-sol, xhigh)",
                command_runner=lambda _, args: calls.append(args) or "",
            )
        finally:
            PREPARE.release_state.validate = original_validate
            PREPARE.release_state.release_record = original_release_record
            PREPARE.release_state.assert_clean_worktree = original_clean
        self.assertEqual([["bash", ".ai/scripts/check-all.sh", "--critical"]], calls)
        self.assertIn("git tag -a v0.5.0 " + "a" * 40, command)
        self.assertIn(
            'AI-Model: OpenAI Codex (gpt-5.6-sol, xhigh)',
            command,
        )
        self.assertIn(
            "automatic sources v0.3.0, v0.4.0, v0.4.1, v0.4.2", command
        )
        self.assertNotIn("git push", command)

    def test_gwt_002_given_a_failed_candidate_gate_when_prepared_then_no_critical_gate_or_tag_command_runs(self):
        original_validate = PREPARE.release_state.validate
        calls: list[list[str]] = []
        PREPARE.release_state.validate = lambda *_, **__: (
            _ for _ in ()
        ).throw(PREPARE.release_state.ReleaseStateError("candidate failed"))
        try:
            with self.assertRaisesRegex(PREPARE.release_state.ReleaseStateError, "candidate failed"):
                PREPARE.prepare(
                    Path("."),
                    "v0.5.0",
                    ai_model="OpenAI Codex",
                    command_runner=lambda _, args: calls.append(args) or "",
                )
        finally:
            PREPARE.release_state.validate = original_validate
        self.assertEqual([], calls)

    def test_gwt_003_given_unmerged_branch_when_prepared_then_tag_command_is_refused(self):
        original_validate = PREPARE.release_state.validate
        PREPARE.release_state.validate = lambda *_, **__: {
            "commit": "a" * 40,
            "branch": "codex/release",
        }
        try:
            with self.assertRaisesRegex(RuntimeError, "merged main"):
                PREPARE.prepare(
                    Path("."),
                    "v0.5.0",
                    ai_model="OpenAI Codex",
                )
        finally:
            PREPARE.release_state.validate = original_validate

    def test_gwt_004_given_noncritical_command_when_runner_called_then_it_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "only the critical gate"):
            PREPARE.run(Path("."), ["git", "tag", "-a", "v0.5.0"])

    def test_gwt_005_given_non_utf8_gate_output_when_runner_succeeds_then_diagnostics_are_recoverable(self):
        result = SimpleNamespace(
            returncode=0,
            stdout=b"critical gate \xfb passed\n",
            stderr=b"",
        )
        with mock.patch.object(PREPARE.subprocess, "run", return_value=result) as run:
            output = PREPARE.run(
                Path("."), ["bash", ".ai/scripts/check-all.sh", "--critical"]
            )

        self.assertEqual("critical gate \ufffd passed\n", output)
        run.assert_called_once_with(
            ["bash", ".ai/scripts/check-all.sh", "--critical"],
            cwd=Path("."),
            check=False,
            capture_output=True,
        )

    def test_gwt_006_given_failed_gate_without_output_when_runner_runs_then_exit_code_is_reported(self):
        result = SimpleNamespace(returncode=17, stdout=None, stderr=None)
        with mock.patch.object(PREPARE.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(
                RuntimeError, "critical gate failed with exit code 17"
            ):
                PREPARE.run(
                    Path("."), ["bash", ".ai/scripts/check-all.sh", "--critical"]
                )


if __name__ == "__main__":
    unittest.main()
