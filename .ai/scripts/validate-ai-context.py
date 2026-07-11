#!/usr/bin/env python3
"""Validate objective, active AI-context navigation and runtime contracts."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TABLE_PATH = re.compile(r"^\|\s*`([^`]+)`\s*\|")
ACTIVE_RUNTIME_ROOTS = (Path(".agents/skills"), Path(".claude/skills"))
PLANNED_RUNTIME_ROOTS = (
    Path(".github/prompts"),
    Path(".github/copilot-instructions.md"),
)
SKIP_PARTS = {"workflows", "archive", "archived", "migrations"}
LANGUAGE_SKIP_PARTS = SKIP_PARTS | {"examples", "example", "generated"}
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
LANGUAGE_ALLOWLIST: dict[Path, tuple[str, ...]] = {
    Path(".ai/assets/skills/ai-context-auditor/skill.yaml"): (
        "自檢 AI context",
        "檢查 AI context 品質",
    ),
    Path(".dev/standards/WORKFLOW-GATE-POLICY.md"): (
        "規劃",
        "整理",
        "重構",
        "標準化",
        "治理",
        "拆分",
    ),
}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return [Path(line) for line in result.stdout.splitlines() if line]


def active_indexes(files: list[Path]) -> list[Path]:
    return [
        path
        for path in files
        if path.name.lower() == "index.md"
        and not any(part.lower() in SKIP_PARTS for part in path.parts)
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
    if path.suffix.lower() not in LANGUAGE_EXTENSIONS:
        return False
    if any(part.lower() in LANGUAGE_SKIP_PARTS for part in path.parts):
        return False
    if path.parts[:2] == (".ai", "scripts"):
        return False
    return any(path == root or root in path.parents for root in LANGUAGE_ROOTS)


def validate_language(path: Path, errors: list[str]) -> None:
    """Reject Han prose except exact, path-scoped routing trigger fragments."""
    allowed = LANGUAGE_ALLOWLIST.get(path, ())
    text = (ROOT / path).read_text(encoding="utf-8")
    for line_number, line in enumerate(text.splitlines(), 1):
        remainder = line
        for fragment in allowed:
            remainder = remainder.replace(fragment, "")
        if HAN.search(remainder):
            errors.append(f"{path}:{line_number}: unexpected Han text in agent-facing context")


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
    for canonical, canonical_link, canonical_marker, translation, translation_link, translation_marker in contracts:
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


def skill_names(root: Path, entry: str) -> set[str]:
    absolute = ROOT / root
    return {
        child.name
        for child in absolute.iterdir()
        if child.is_dir() and (child / entry).is_file()
    }


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
        f"and {len(language_files)} language-policy files."
    )
    print("Root bilingual entry links and ownership markers passed (semantic parity is not asserted).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
