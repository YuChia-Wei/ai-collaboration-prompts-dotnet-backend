#!/usr/bin/env python3
"""Validate the shared locator and minimum metadata for new workflows."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path


ADOPTION_DATE = date(2026, 7, 10)
ID_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-[a-z0-9][a-z0-9-]*$")
TASK_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
REQUIRED_LOCATOR = {
    "schema_version",
    "workflow_id",
    "workflow_kind",
    "title",
    "owner_skill",
    "status",
    "artifact_root",
    "entrypoint",
    "created_at",
    "updated_at",
}
REQUIRED_TASK = {
    "task_id",
    "workflow_id",
    "owner_skill",
    "status",
    "created_at",
    "updated_at",
}


def parse_flat_yaml(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def timestamp(value: str, label: str, errors: list[str]) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid ISO 8601 timestamp: {value}")
        return None
    if parsed.tzinfo is None:
        errors.append(f"{label}: timestamp must include UTC offset: {value}")
        return None
    return parsed


def main() -> int:
    repo = Path(__file__).resolve().parents[2]
    discovery_root = repo / ".dev" / "workflows"
    errors: list[str] = []
    checked = 0
    roots: dict[Path, str] = {}

    for directory in sorted(path for path in discovery_root.iterdir() if path.is_dir()):
        match = ID_RE.match(directory.name)
        if not match:
            continue
        workflow_date = date.fromisoformat(match.group(1))
        if workflow_date < ADOPTION_DATE:
            continue
        checked += 1
        locator_path = directory / "workflow.yaml"
        if not locator_path.is_file():
            errors.append(f"{directory.relative_to(repo)}: missing workflow.yaml")
            continue
        locator = parse_flat_yaml(locator_path)
        missing = sorted(REQUIRED_LOCATOR - locator.keys())
        if missing:
            errors.append(f"{locator_path.relative_to(repo)}: missing fields {', '.join(missing)}")
            continue
        if locator["workflow_id"] != directory.name:
            errors.append(f"{locator_path.relative_to(repo)}: workflow_id must match directory name")
        created = timestamp(locator["created_at"], f"{locator_path.relative_to(repo)} created_at", errors)
        updated = timestamp(locator["updated_at"], f"{locator_path.relative_to(repo)} updated_at", errors)
        if created and updated and updated < created:
            errors.append(f"{locator_path.relative_to(repo)}: updated_at is earlier than created_at")
        root = (repo / locator["artifact_root"]).resolve()
        try:
            root.relative_to(repo.resolve())
        except ValueError:
            errors.append(f"{locator_path.relative_to(repo)}: artifact_root is outside the repository")
            continue
        if not root.is_dir():
            errors.append(f"{locator_path.relative_to(repo)}: artifact_root does not exist")
            continue
        ignored = subprocess.run(
            ["git", "check-ignore", "-q", str(root)],
            cwd=repo,
            check=False,
            capture_output=True,
        )
        if ignored.returncode == 0:
            errors.append(f"{locator_path.relative_to(repo)}: artifact_root is ignored by Git")
        if root in roots and roots[root] != directory.name:
            errors.append(f"{locator_path.relative_to(repo)}: artifact_root also owned by {roots[root]}")
        roots[root] = directory.name
        entrypoint = (root / locator["entrypoint"]).resolve()
        try:
            entrypoint.relative_to(root)
        except ValueError:
            errors.append(f"{locator_path.relative_to(repo)}: entrypoint escapes artifact_root")
            continue
        if not entrypoint.is_file():
            errors.append(f"{locator_path.relative_to(repo)}: entrypoint does not exist in artifact_root")
        task_root = root / "tasks"
        if task_root.is_dir():
            seen: set[str] = set()
            for task_path in sorted(task_root.glob("*.json")):
                try:
                    task = json.loads(task_path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                    errors.append(f"{task_path.relative_to(repo)}: invalid JSON: {exc}")
                    continue
                missing_task = sorted(REQUIRED_TASK - task.keys())
                if missing_task:
                    errors.append(f"{task_path.relative_to(repo)}: missing fields {', '.join(missing_task)}")
                    continue
                if task["workflow_id"] != directory.name:
                    errors.append(f"{task_path.relative_to(repo)}: workflow_id does not match locator")
                if task["task_id"] in seen:
                    errors.append(f"{task_path.relative_to(repo)}: duplicate task_id {task['task_id']}")
                seen.add(task["task_id"])
                if not TASK_ID_RE.match(str(task["task_id"])):
                    errors.append(f"{task_path.relative_to(repo)}: task_id is not path-safe")
                task_created = timestamp(task["created_at"], f"{task_path.relative_to(repo)} created_at", errors)
                task_updated = timestamp(task["updated_at"], f"{task_path.relative_to(repo)} updated_at", errors)
                if task_created and task_updated and task_updated < task_created:
                    errors.append(f"{task_path.relative_to(repo)}: updated_at is earlier than created_at")

    if errors:
        print("Workflow artifact validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Workflow artifact validation passed for {checked} post-adoption workflow(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
