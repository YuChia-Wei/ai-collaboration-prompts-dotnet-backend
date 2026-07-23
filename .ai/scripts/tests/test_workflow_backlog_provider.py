#!/usr/bin/env python3
"""GWT tests for optional repo-backlog workflow validation."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / ".ai/scripts/validate-workflow-artifacts.py"
SPEC = importlib.util.spec_from_file_location(
    "validate_workflow_backlog_provider", VALIDATOR_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load validator: {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def write_provenance(root: Path, enabled: bool) -> None:
    path = root / ".dev/ai-context/provenance.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(
        "\n".join(
            [
                'schema_version: "2.0"',
                "selection:",
                "  providers:",
                "    repo-backlog:",
                f"      enabled: {str(enabled).lower()}",
                "      preservation: preserve-existing-if-recorded",
                "",
            ]
        ),
        encoding="utf-8",
        newline="\n",
    )


class WorkflowBacklogProviderTests(unittest.TestCase):
    def test_gwt_001_given_provider_disabled_when_resolved_then_backlog_is_not_required(self) -> None:
        with tempfile.TemporaryDirectory(prefix="workflow-provider-off-") as value:
            root = Path(value)
            write_provenance(root, False)
            errors: list[str] = []
            self.assertFalse(VALIDATOR.backlog_provider_enabled(root, errors))
            self.assertEqual([], errors)

    def test_gwt_002_given_provider_enabled_without_backlog_when_validated_then_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="workflow-provider-on-") as value:
            root = Path(value)
            write_provenance(root, True)
            errors: list[str] = []
            self.assertTrue(VALIDATOR.backlog_provider_enabled(root, errors))
            self.assertEqual(0, VALIDATOR.validate_backlog(root, errors))
            self.assertTrue(any(".dev/backlog" in error for error in errors))

    def test_gwt_003_given_source_profile_when_resolved_then_backlog_remains_required(self) -> None:
        with tempfile.TemporaryDirectory(prefix="workflow-source-provider-") as value:
            root = Path(value)
            profile = root / ".ai/distribution/profiles/dotnet-backend.yaml"
            profile.parent.mkdir(parents=True)
            profile.write_text("schema_version: 2.0.0\n", encoding="utf-8")
            errors: list[str] = []
            self.assertTrue(VALIDATOR.backlog_provider_enabled(root, errors))
            self.assertEqual([], errors)

    def test_gwt_004_given_dual_provenance_when_resolved_then_it_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="workflow-provider-dual-") as value:
            root = Path(value)
            write_provenance(root, False)
            legacy = root / ".dev/AI-CONTEXT-SOURCE.yaml"
            legacy.write_text('schema_version: "1.0"\n', encoding="utf-8")
            errors: list[str] = []
            self.assertFalse(VALIDATOR.backlog_provider_enabled(root, errors))
            self.assertTrue(any("cannot coexist" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
