#!/usr/bin/env python3
"""Fail-closed tests for repository-backed AI context load measurement."""

from __future__ import annotations

import copy
import importlib.util
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = ROOT / ".ai/scripts/measure-ai-context-load.py"


def load_module():
    spec = importlib.util.spec_from_file_location("ai_context_load_measurement", VALIDATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {VALIDATOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MEASURE = load_module()


class AiContextLoadMeasurementTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.repository = self.root / "repository"
        self.repository.mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "Context Load Fixture")
        self.git("config", "core.autocrlf", "false")
        self.files = {
            "AGENTS.md": "runtime collaboration context\n",
            ".agents/skills/example/SKILL.md": "skill routing context\n",
            ".dev/releases/example.md": "release context evidence\n",
            ".dev/workflows/example/handoff.yaml": "handoff: context\n",
            ".dev/specs/example.md": "development specification context\n",
        }
        for relative, content in self.files.items():
            path = self.repository / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "fixture")
        self.subject_commit = self.git("rev-parse", "HEAD").strip()
        self.traces_path = self.root / "traces.yaml"
        self.manifest = self.valid_manifest()
        self.write_manifest(self.manifest)

    def tearDown(self):
        self.temporary.cleanup()

    def git(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(self.repository), *args],
            text=True,
        )

    def event(self, path: str, event_kind: str) -> dict:
        object_id = self.git("rev-parse", f"{self.subject_commit}:{path}").strip()
        payload = subprocess.check_output(
            ["git", "-C", str(self.repository), "cat-file", "blob", object_id]
        )
        return {
            "event_kind": event_kind,
            "path": path,
            "git_blob": object_id,
            "bytes": len(payload),
            "whitespace_words": len(re.findall(rb"\S+", payload)),
        }

    def valid_manifest(self) -> dict:
        return {
            "schema_version": "1.0",
            "measurement_id": "synthetic-context-load",
            "subject_commit": self.subject_commit,
            "prompt_accounting": {
                "total_prompt_tokens": None,
                "total_prompt_tokens_source": None,
                "repository_corpus_is_prompt": False,
                "repository_token_heuristic": {
                    "method": "ceil-utf8-bytes-divided-by-four",
                    "scope": "repository_loaded",
                    "is_total_prompt_tokens": False,
                },
            },
            "traces": [
                {
                    "family": "runtime",
                    "events": [self.event("AGENTS.md", "runtime")],
                },
                {
                    "family": "skill-routing",
                    "events": [
                        self.event(".agents/skills/example/SKILL.md", "full-file")
                    ],
                },
                {
                    "family": "release",
                    "events": [
                        self.event(".dev/releases/example.md", "full-file")
                    ],
                },
                {
                    "family": "handoff",
                    "events": [
                        self.event(
                            ".dev/workflows/example/handoff.yaml", "full-file"
                        )
                    ],
                },
                {
                    "family": "development",
                    "events": [self.event(".dev/specs/example.md", "full-file")],
                },
            ],
        }

    def write_manifest(self, manifest: dict) -> None:
        self.traces_path.write_text(
            yaml.safe_dump(manifest, sort_keys=False),
            encoding="utf-8",
            newline="\n",
        )

    def test_given_clean_pinned_traces_when_measured_then_layers_are_exact(self):
        result = MEASURE.measure(self.repository, self.traces_path)
        self.assertEqual(self.subject_commit, result["subject_commit"])
        self.assertEqual(5, result["repository_corpus"]["file_count"])
        self.assertEqual(5, result["repository_loaded"]["family_count"])
        self.assertEqual(5, result["repository_loaded"]["event_count"])
        self.assertFalse(
            result["prompt_accounting"]["repository_token_heuristic"][
                "is_total_prompt_tokens"
            ]
        )
        self.assertRegex(result["measurement_sha256"], r"^[0-9a-f]{64}$")

    def test_given_dirty_repository_when_measured_then_it_fails_closed(self):
        (self.repository / "dirty.txt").write_text("dirty\n", encoding="utf-8")
        with self.assertRaisesRegex(MEASURE.MeasurementError, "clean"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_short_subject_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["subject_commit"] = self.subject_commit[:12]
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "full lowercase"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_path_escape_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["traces"][0]["events"][0]["path"] = "../AGENTS.md"
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "unsafe"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_duplicate_path_in_family_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        duplicate = copy.deepcopy(manifest["traces"][1]["events"][0])
        manifest["traces"][1]["events"].append(duplicate)
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "duplicate loaded path"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_missing_family_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["traces"] = [
            item for item in manifest["traces"] if item["family"] != "handoff"
        ]
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "families must be exactly"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_blob_digest_drift_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["traces"][2]["events"][0]["git_blob"] = "0" * 40
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "git_blob drifted"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_corpus_as_prompt_claim_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["prompt_accounting"]["repository_corpus_is_prompt"] = True
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "corpus size is not prompt"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_heuristic_total_prompt_claim_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["prompt_accounting"]["repository_token_heuristic"][
            "is_total_prompt_tokens"
        ] = True
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "not total prompt"):
            MEASURE.measure(self.repository, self.traces_path)

    def test_given_non_provider_total_when_measured_then_it_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["prompt_accounting"]["total_prompt_tokens"] = 100
        manifest["prompt_accounting"]["total_prompt_tokens_source"] = "heuristic"
        self.write_manifest(manifest)
        with self.assertRaisesRegex(MEASURE.MeasurementError, "provider_reported"):
            MEASURE.measure(self.repository, self.traces_path)


if __name__ == "__main__":
    unittest.main()
