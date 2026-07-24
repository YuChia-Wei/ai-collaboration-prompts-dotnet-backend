#!/usr/bin/env python3
"""Validate the staged v0.6 skill taxonomy and atomic compatibility transition."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path(".ai/assets/skills/transitions/v0.6.0.yaml")
FIXTURE = Path(".ai/evaluation/fixtures/identifier-compatibility.yaml")
CANONICAL_REGISTRY = Path(".ai/assets/skills/README.MD")
AGENTS_REGISTRY = Path(".agents/skills/README.md")
CLAUDE_REGISTRY = Path(".claude/skills/README.md")

EXPECTED_TRANSITIONS = {
    "repo-structure-sync": ("ai-context-init", "ai-context-lifecycle"),
    "dev-workflow": (
        "software-development-orchestrator",
        "software-development",
    ),
}
REQUIRED_DECISIONS = {
    "model",
    "judge",
    "repetitions",
    "prompt-and-context-inputs",
    "sampling-policy",
    "token-ceiling",
    "pass-threshold",
    "result-retention",
    "failure-disposition",
}
RUNTIME_ROOTS = (".agents/skills", ".claude/skills")


def mapping(value: Any, label: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{label}: must be a mapping")
        return {}
    return value


def string_list(value: Any, label: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        errors.append(f"{label}: must be a list of non-empty strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{label}: contains duplicates")
    return value


def load_yaml(root: Path, path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = yaml.safe_load((root / path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        errors.append(f"{path.as_posix()}: cannot read YAML: {exc}")
        return {}
    return mapping(value, path.as_posix(), errors)


def validate_registry(
    root: Path,
    path: Path,
    current: set[str],
    candidates: set[str],
    errors: list[str],
) -> None:
    try:
        text = (root / path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"{path.as_posix()}: cannot read registry: {exc}")
        return
    for identifier in sorted(current):
        if f"`{identifier}`" not in text:
            errors.append(
                f"{path.as_posix()}: active identifier is missing: {identifier}"
            )
    for identifier in sorted(candidates):
        if f"- `{identifier}`" in text:
            errors.append(
                f"{path.as_posix()}: inactive candidate is listed as active: "
                f"{identifier}"
            )


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    manifest = load_yaml(root, MANIFEST, errors)
    if not manifest:
        return errors
    if manifest.get("schema_version") != "1.0":
        errors.append(f"{MANIFEST}: schema_version must be 1.0")
    if manifest.get("transition_id") != "SKILL-001-v0.6.0":
        errors.append(f"{MANIFEST}: transition_id must be SKILL-001-v0.6.0")
    if manifest.get("state") != "awaiting-model-evaluation":
        errors.append(
            f"{MANIFEST}: state must remain awaiting-model-evaluation before approval"
        )
    if manifest.get("activation_mode") != "atomic":
        errors.append(f"{MANIFEST}: activation_mode must be atomic")

    transitions = manifest.get("transitions")
    if not isinstance(transitions, list):
        errors.append(f"{MANIFEST}: transitions must be a list")
        transitions = []
    actual: dict[str, tuple[str, str]] = {}
    for index, raw in enumerate(transitions):
        item = mapping(raw, f"{MANIFEST}: transitions[{index}]", errors)
        current = item.get("current_identifier")
        candidate = item.get("candidate_identifier")
        family = item.get("family")
        if not all(isinstance(value, str) and value for value in (current, candidate, family)):
            errors.append(
                f"{MANIFEST}: transitions[{index}] requires current, candidate, and family"
            )
            continue
        if current in actual:
            errors.append(f"{MANIFEST}: duplicate current identifier: {current}")
        actual[current] = (candidate, family)
        if item.get("current_lifecycle") != "active":
            errors.append(f"{MANIFEST}: {current} must remain active before activation")
        if item.get("candidate_lifecycle") != "inactive-candidate":
            errors.append(f"{MANIFEST}: {candidate} must remain an inactive candidate")
        if item.get("compatibility_lifecycle_after_activation") != "deprecated":
            errors.append(
                f"{MANIFEST}: {current} must become deprecated after activation"
            )
        if item.get("removal_target") is not None:
            errors.append(f"{MANIFEST}: {current} must not have a removal target")
        if item.get("historical_identifier_rewrite") is not False:
            errors.append(
                f"{MANIFEST}: {current} must not authorize historical rewrites"
            )
    if actual != EXPECTED_TRANSITIONS:
        errors.append(
            f"{MANIFEST}: transition mapping drifted: expected "
            f"{EXPECTED_TRANSITIONS}, found {actual}"
        )

    taxonomy = mapping(manifest.get("taxonomy"), f"{MANIFEST}: taxonomy", errors)
    for family in ("ai-context-lifecycle", "software-development"):
        record = mapping(taxonomy.get(family), f"{MANIFEST}: taxonomy.{family}", errors)
        target = string_list(
            record.get("target_members"),
            f"{MANIFEST}: taxonomy.{family}.target_members",
            errors,
        )
        compatibility = string_list(
            record.get("compatibility_members"),
            f"{MANIFEST}: taxonomy.{family}.compatibility_members",
            errors,
        )
        expected_candidates = {
            candidate
            for candidate, candidate_family in EXPECTED_TRANSITIONS.values()
            if candidate_family == family
        }
        expected_current = {
            current
            for current, (_, current_family) in EXPECTED_TRANSITIONS.items()
            if current_family == family
        }
        if not expected_candidates <= set(target):
            errors.append(f"{MANIFEST}: taxonomy.{family} misses candidate identifiers")
        if set(compatibility) != expected_current:
            errors.append(
                f"{MANIFEST}: taxonomy.{family}.compatibility_members drifted"
            )

    gate = mapping(
        manifest.get("activation_gate"), f"{MANIFEST}: activation_gate", errors
    )
    deterministic = mapping(
        gate.get("deterministic_evaluation"),
        f"{MANIFEST}: activation_gate.deterministic_evaluation",
        errors,
    )
    if deterministic.get("status") != "passed":
        errors.append(f"{MANIFEST}: deterministic evaluation must be passed")
    for field in ("corpus", "baseline", "compatibility_fixture"):
        value = deterministic.get(field)
        if not isinstance(value, str) or not (root / value).is_file():
            errors.append(
                f"{MANIFEST}: deterministic_evaluation.{field} must resolve"
            )
    model = mapping(
        gate.get("model_in_loop_evaluation"),
        f"{MANIFEST}: activation_gate.model_in_loop_evaluation",
        errors,
    )
    if model.get("status") != "pending-owner-approval":
        errors.append(f"{MANIFEST}: model evaluation must remain pending approval")
    decisions = set(
        string_list(
            model.get("required_decisions"),
            f"{MANIFEST}: model_in_loop_evaluation.required_decisions",
            errors,
        )
    )
    if decisions != REQUIRED_DECISIONS:
        errors.append(f"{MANIFEST}: model evaluation decisions are incomplete")

    current = set(EXPECTED_TRANSITIONS)
    candidates = {candidate for candidate, _ in EXPECTED_TRANSITIONS.values()}
    for identifier in current:
        if not (root / ".ai/assets/skills" / identifier / "skill.yaml").is_file():
            errors.append(f"active canonical skill is missing: {identifier}")
        for runtime_root in RUNTIME_ROOTS:
            if not (root / runtime_root / identifier / "SKILL.md").is_file():
                errors.append(
                    f"active runtime wrapper is missing: {runtime_root}/{identifier}"
                )
    for identifier in candidates:
        if (root / ".ai/assets/skills" / identifier).exists():
            errors.append(
                f"inactive candidate canonical directory already exists: {identifier}"
            )
        for runtime_root in RUNTIME_ROOTS:
            if (root / runtime_root / identifier).exists():
                errors.append(
                    f"inactive candidate runtime directory already exists: "
                    f"{runtime_root}/{identifier}"
                )

    fixture = load_yaml(root, FIXTURE, errors)
    expected_aliases = {
        current_identifier: candidate
        for current_identifier, (candidate, _) in EXPECTED_TRANSITIONS.items()
    }
    if set(fixture.get("active_identifiers", [])) != candidates:
        errors.append(f"{FIXTURE}: active identifier candidate set drifted")
    if fixture.get("compatibility_entries") != expected_aliases:
        errors.append(f"{FIXTURE}: compatibility entry mapping drifted")
    if set(fixture.get("historical_identifiers", [])) != current:
        errors.append(f"{FIXTURE}: historical identifier set drifted")

    for registry in (CANONICAL_REGISTRY, AGENTS_REGISTRY, CLAUDE_REGISTRY):
        validate_registry(root, registry, current, candidates, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        print("Skill transition validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Skill transition validation passed: two inactive candidates, two active "
        "identifiers, atomic deprecated compatibility, and pending model approval."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
