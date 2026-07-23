#!/usr/bin/env python3
"""GWT checks for the pluggable development test-execution contract."""

from __future__ import annotations

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
PROFILE = ROOT / ".ai/assets/skills/dev-workflow/references/capability-profile.yaml"


class DevWorkflowCapabilityContractGwtTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = yaml.safe_load(PROFILE.read_text(encoding="utf-8"))

    def test_gwt_001_given_test_execution_when_profile_loaded_then_it_is_optional_and_unmapped(self) -> None:
        self.assertEqual("1.1", self.profile["schema_version"])
        self.assertIn("test-execution", self.profile["allowed_slots"])
        self.assertNotIn("test-execution", self.profile["required_slots"])
        self.assertNotIn("test-execution", self.profile["mappings"])

    def test_gwt_002_given_no_dedicated_test_skill_when_provider_order_checked_then_target_truth_precedes_fallback(self) -> None:
        contract = self.profile["capability_contracts"]["test-execution"]
        self.assertEqual(
            ["target-profile-commands", "evaluated-external-skill", "fallback-contract"],
            contract["provider_order"],
        )
        self.assertEqual(["unit", "integration"], contract["default_levels"])

    def test_gwt_003_given_test_outcomes_when_closeout_classifies_results_then_blocked_is_not_passed(self) -> None:
        outcomes = self.profile["capability_contracts"]["test-execution"]["outcomes"]
        self.assertEqual(
            [
                "passed",
                "failed",
                "blocked-by-environment",
                "not-applicable",
                "deferred-with-owner",
            ],
            outcomes,
        )
        self.assertNotEqual("passed", "blocked-by-environment")

    def test_gwt_004_given_specialized_tests_when_profile_loaded_then_they_are_conditional(self) -> None:
        conditional = self.profile["capability_contracts"]["test-execution"]["conditional_levels"]
        self.assertEqual(
            ["e2e", "browser", "playwright", "environment-dependent"],
            conditional,
        )


if __name__ == "__main__":
    unittest.main()
