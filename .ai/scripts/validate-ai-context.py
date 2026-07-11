#!/usr/bin/env python3
"""Validate objective, active AI-context navigation and runtime contracts."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
TABLE_PATH = re.compile(r"^\|\s*`([^`]+)`\s*\|")
ACTIVE_RUNTIME_ROOTS = (Path(".agents/skills"), Path(".claude/skills"))
PLANNED_RUNTIME_ROOTS = (
    Path(".github/prompts"),
    Path(".github/copilot-instructions.md"),
)
SKIP_PARTS = {"workflows", "archive", "archived", "migrations"}
LANGUAGE_SKIP_PARTS = SKIP_PARTS | {"examples", "example", "generated"}
PRODUCT_ROOTS = {"src", "test", "tests"}
LANGUAGE_EXTENSIONS = {".md", ".yaml", ".yml", ".json"}
HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
LANGUAGE_ROOTS = (
    Path(".ai"),
    Path(".agents"),
    Path(".claude"),
    Path(".dev/standards"),
    Path(".dev/specs"),
    Path(".dev/problem-frames"),
)
EXPLICIT_LANGUAGE_FILES = {Path(".dev/ARCHITECTURE.md")}
LANGUAGE_ALLOWLIST: dict[Path, frozenset[str]] = {
    Path(".ai/assets/skills/ai-context-auditor/skill.yaml"): frozenset(
        {'  - "自檢 AI context"', '  - "檢查 AI context 品質"'}
    ),
    Path(".dev/standards/WORKFLOW-GATE-POLICY.md"): frozenset(
        {
            '- the user uses wording such as "workflow", "規劃", "整理", "重構", '
            '"標準化", "治理", or "拆分" for repo-wide documentation or context work.'
        }
    ),
}
OWNERSHIP_REGISTRY = Path(".dev/standards/AI-CONTEXT-OWNERSHIP.yaml")
RULE_STRENGTHS = {"invariant", "profile-default", "conditional", "example", "historical"}
RULE_STATUSES = {"active", "deprecated", "historical"}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line]


def active_indexes(files: list[Path]) -> list[Path]:
    return [
        path
        for path in files
        if path.name.lower() == "index.md"
        and not any(part.lower() in SKIP_PARTS for part in path.parts)
        and (not path.parts or path.parts[0].lower() not in PRODUCT_ROOTS)
    ]


def is_catalog_path(value: str) -> bool:
    return not (
        not value
        or "<" in value
        or ">" in value
        or "*" in value
        or value.startswith(("http://", "https://"))
    )


def validate_index(index: Path, errors: list[str]) -> None:
    text = (ROOT / index).read_text(encoding="utf-8")
    if "|`n|" in text:
        errors.append(f"{index}: contains literal table corruption |`n|")
    for line_number, line in enumerate(text.splitlines(), 1):
        match = TABLE_PATH.match(line)
        if not match or not is_catalog_path(match.group(1)):
            continue
        target = (ROOT / index.parent / match.group(1)).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{index}:{line_number}: catalog path escapes repository: {match.group(1)}")
            continue
        if not target.exists():
            errors.append(f"{index}:{line_number}: missing catalog path: {match.group(1)}")


def is_language_surface(path: Path, indexes: set[Path]) -> bool:
    """Return whether a tracked file is active agent-facing execution context."""
    if path in indexes:
        return True
    if path.parts and path.parts[0].lower() in PRODUCT_ROOTS:
        return False
    if path.suffix.lower() not in LANGUAGE_EXTENSIONS:
        return False
    if any(part.lower() in LANGUAGE_SKIP_PARTS for part in path.parts):
        return False
    return path in EXPLICIT_LANGUAGE_FILES or any(
        path == root or root in path.parents for root in LANGUAGE_ROOTS
    )


def validate_language(path: Path, errors: list[str]) -> None:
    """Reject Han prose except exact, path-scoped routing trigger fragments."""
    allowed_lines = LANGUAGE_ALLOWLIST.get(path, frozenset())
    text = (ROOT / path).read_text(encoding="utf-8")
    for line_number, line in enumerate(text.splitlines(), 1):
        if HAN.search(line) and line not in allowed_lines:
            errors.append(f"{path}:{line_number}: unexpected Han text in agent-facing context")


def markdown_structure(path: Path) -> tuple[list[int], list[str]]:
    """Return heading levels and ordered path-like backtick values in table rows."""
    headings: list[int] = []
    table_paths: list[str] = []
    fenced = False
    for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        heading = re.match(r"^(#{1,6})\s+", line)
        if heading:
            headings.append(len(heading.group(1)))
        if line.lstrip().startswith("|"):
            for value in re.findall(r"`([^`]+)`", line):
                if "/" in value or value.lower().endswith(".md"):
                    table_paths.append(value)
    return headings, table_paths


def validate_bilingual_entries(errors: list[str]) -> None:
    """Validate entry-file ownership and reciprocal links, not semantic parity."""
    contracts = (
        (
            Path("README.md"),
            "[English](README.en.md)",
            "canonical",
            Path("README.en.md"),
            "[繁體中文](README.md)",
            "translation",
        ),
        (
            Path("agents.md"),
            "[Traditional Chinese](agents.zh-tw.md)",
            "canonical English",
            Path("agents.zh-tw.md"),
            "[English](agents.md)",
            "翻譯",
        ),
    )
    for (
        canonical,
        canonical_link,
        canonical_marker,
        translation,
        translation_link,
        translation_marker,
    ) in contracts:
        for path in (canonical, translation):
            if not (ROOT / path).is_file():
                errors.append(f"missing bilingual entry file: {path}")
        if not (ROOT / canonical).is_file() or not (ROOT / translation).is_file():
            continue
        canonical_text = (ROOT / canonical).read_text(encoding="utf-8")
        translation_text = (ROOT / translation).read_text(encoding="utf-8")
        if canonical_link not in canonical_text:
            errors.append(f"{canonical}: missing reciprocal translation link to {translation}")
        if translation_link not in translation_text:
            errors.append(f"{translation}: missing reciprocal canonical link to {canonical}")
        if canonical_marker not in canonical_text:
            errors.append(f"{canonical}: missing canonical ownership marker")
        if translation_marker not in translation_text:
            errors.append(f"{translation}: missing translation ownership marker")
        canonical_headings, canonical_paths = markdown_structure(canonical)
        translation_headings, translation_paths = markdown_structure(translation)
        if canonical_headings != translation_headings:
            errors.append(
                f"{canonical} <-> {translation}: heading-level structural parity mismatch"
            )
        if Counter(canonical_paths) != Counter(translation_paths):
            errors.append(
                f"{canonical} <-> {translation}: backtick table-path multiset parity mismatch"
            )
        elif canonical_paths != translation_paths:
            errors.append(
                f"{canonical} <-> {translation}: backtick table-path order parity mismatch"
            )

    required_agent_rows = {"README.md", "README.en.md", "agents.md", "agents.zh-tw.md"}
    for path in (Path("agents.md"), Path("agents.zh-tw.md")):
        if not (ROOT / path).is_file():
            continue
        _, table_paths = markdown_structure(path)
        missing = sorted(required_agent_rows - set(table_paths))
        if missing:
            errors.append(f"{path}: missing required root entry table rows: {missing}")


def skill_names(root: Path, entry: str) -> set[str]:
    absolute = ROOT / root
    return {
        child.name
        for child in absolute.iterdir()
        if child.is_dir() and (child / entry).is_file()
    }


def validate_rule_ownership(errors: list[str]) -> int:
    """Validate structural ownership contracts without claiming semantic parity."""
    registry_path = ROOT / OWNERSHIP_REGISTRY
    if not registry_path.is_file():
        errors.append(f"missing rule ownership registry: {OWNERSHIP_REGISTRY}")
        return 0
    try:
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"{OWNERSHIP_REGISTRY}: invalid YAML: {exc}")
        return 0
    rules = data.get("rules", []) if isinstance(data, dict) else []
    if not isinstance(rules, list):
        errors.append(f"{OWNERSHIP_REGISTRY}: rules must be a list")
        return 0

    seen: set[str] = set()
    for index, rule in enumerate(rules, 1):
        label = f"{OWNERSHIP_REGISTRY}:rules[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{label}: rule must be a mapping")
            continue
        rule_id = rule.get("rule_id")
        if not isinstance(rule_id, str) or not rule_id:
            errors.append(f"{label}: missing rule_id")
            continue
        if rule_id in seen:
            errors.append(f"{label}: duplicate rule_id {rule_id}")
        seen.add(rule_id)
        strength = rule.get("strength")
        status = rule.get("status")
        override = rule.get("override_policy")
        if strength not in RULE_STRENGTHS:
            errors.append(f"{label}: invalid strength {strength!r}")
        if status not in RULE_STATUSES:
            errors.append(f"{label}: invalid status {status!r}")
        expected_override = {
            "invariant": "forbidden",
            "profile-default": "explicit-target-decision",
            "conditional": "not-applicable",
        }.get(strength)
        if expected_override and override != expected_override:
            errors.append(
                f"{label}: {strength} requires override_policy {expected_override}"
            )
        if strength == "conditional" and not rule.get("applicability"):
            errors.append(f"{label}: conditional rule requires applicability")

        canonical_value = rule.get("canonical_path")
        if not isinstance(canonical_value, str):
            errors.append(f"{label}: missing canonical_path")
            continue
        canonical = Path(canonical_value)
        if Path(".dev/standards") not in canonical.parents:
            errors.append(f"{label}: canonical_path must be under .dev/standards")
        canonical_file = ROOT / canonical
        if not canonical_file.is_file():
            errors.append(f"{label}: missing canonical_path {canonical}")
            continue
        anchor = rule.get("canonical_anchor")
        canonical_text = canonical_file.read_text(encoding="utf-8")
        if not isinstance(anchor, str) or anchor not in canonical_text:
            errors.append(f"{label}: canonical_anchor not found in {canonical}")

        consumers = rule.get("derived_consumers", [])
        if not isinstance(consumers, list):
            errors.append(f"{label}: derived_consumers must be a list")
            continue
        for consumer_value in consumers:
            consumer = Path(consumer_value)
            consumer_file = ROOT / consumer
            if not consumer_file.is_file():
                errors.append(f"{label}: missing derived consumer {consumer}")
            elif rule_id not in consumer_file.read_text(encoding="utf-8"):
                errors.append(f"{label}: derived consumer {consumer} does not cite {rule_id}")
    return len(rules)


def main() -> int:
    errors: list[str] = []
    files = tracked_files()
    indexes = active_indexes(files)

    for index in indexes:
        validate_index(index, errors)

    index_set = set(indexes)
    language_files = [path for path in files if is_language_surface(path, index_set)]
    for path in language_files:
        validate_language(path, errors)

    validate_bilingual_entries(errors)
    ownership_rules = validate_rule_ownership(errors)

    for runtime_root in ACTIVE_RUNTIME_ROOTS:
        if not (ROOT / runtime_root).is_dir():
            errors.append(f"declared current runtime root is missing: {runtime_root}")

    # Future adapters must be deliberately promoted to the current-runtime contract.
    present_planned = [str(path) for path in PLANNED_RUNTIME_ROOTS if (ROOT / path).exists()]
    if present_planned:
        errors.append(
            "planned runtime path exists but is not declared current: " + ", ".join(present_planned)
        )

    canonical = skill_names(Path(".ai/assets/skills"), "skill.yaml")
    agents = skill_names(Path(".agents/skills"), "SKILL.md")
    claude = skill_names(Path(".claude/skills"), "SKILL.md")
    for label, inventory in (("Agents/Codex", agents), ("Claude", claude)):
        if inventory != canonical:
            missing = sorted(canonical - inventory)
            extra = sorted(inventory - canonical)
            errors.append(f"{label} wrapper parity mismatch; missing={missing}, extra={extra}")

    if errors:
        print("AI context validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"AI context validation passed: {len(indexes)} active indexes, "
        f"{len(canonical)} canonical skills, {len(ACTIVE_RUNTIME_ROOTS)} current runtime roots, "
        f"{len(language_files)} language-policy files, and {ownership_rules} owned rules."
    )
    print(
        "Root bilingual entry ownership, links, and structural parity passed "
        "(semantic parity is not asserted)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
