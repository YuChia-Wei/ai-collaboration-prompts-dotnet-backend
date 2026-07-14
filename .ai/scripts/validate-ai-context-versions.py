#!/usr/bin/env python3
"""Validate AI context release records and optional target provenance."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml


VERSION_RE = re.compile(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def load_mapping(path: Path, errors: list[str]) -> dict | None:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        errors.append(f"{path}: cannot parse YAML: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path}: root must be a mapping")
        return None
    return value


def iso_with_offset(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def resolve_tag(root: Path, tag: str) -> str | None:
    result = subprocess.run(
        ["git", "rev-list", "-n", "1", tag],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def validate_release(path: Path, root: Path, errors: list[str], verify_git: bool) -> None:
    data = load_mapping(path, errors)
    if data is None:
        return
    version = data.get("version")
    status = data.get("status")
    if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
        errors.append(f"{path}: version must be vMAJOR.MINOR.PATCH")
        return
    if path.parent.name != version:
        errors.append(f"{path}: directory must equal version {version}")
    if data.get("release_id") != f"REL-{version}":
        errors.append(f"{path}: release_id must be REL-{version}")
    if status not in {"planned", "validated", "published", "superseded"}:
        errors.append(f"{path}: unsupported status {status!r}")
    for artifact in ("release-notes.md", "migration-guide.md"):
        if not (path.parent / artifact).is_file():
            errors.append(f"{path}: missing {artifact}")
    compatibility = data.get("compatibility")
    if not isinstance(compatibility, dict) or not isinstance(compatibility.get("breaking_changes"), bool):
        errors.append(f"{path}: compatibility.breaking_changes must be boolean")
    if status == "published":
        tag, commit = data.get("tag"), data.get("commit")
        if tag != version:
            errors.append(f"{path}: published tag must equal version")
        if not isinstance(commit, str) or not SHA_RE.fullmatch(commit):
            errors.append(f"{path}: published commit must be a full lowercase Git SHA")
        elif verify_git:
            resolved = resolve_tag(root, tag)
            if resolved != commit:
                errors.append(f"{path}: tag {tag} resolves to {resolved!r}, expected {commit}")


def validate_manifest(path: Path, errors: list[str]) -> None:
    data = load_mapping(path, errors)
    if data is None:
        return
    source = data.get("source")
    installation = data.get("installation")
    migration = data.get("last_migration")
    if not isinstance(source, dict):
        errors.append(f"{path}: source must be a mapping")
        return
    version = source.get("version")
    if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
        errors.append(f"{path}: source.version must be vMAJOR.MINOR.PATCH")
    else:
        if source.get("release_id") != f"REL-{version}":
            errors.append(f"{path}: source.release_id must be REL-{version}")
        if source.get("tag") != version:
            errors.append(f"{path}: source.tag must equal source.version")
    if not isinstance(source.get("repository"), str) or not source["repository"].strip():
        errors.append(f"{path}: source.repository is required")
    if not isinstance(source.get("commit"), str) or not SHA_RE.fullmatch(source["commit"]):
        errors.append(f"{path}: source.commit must be a full lowercase Git SHA")
    if not isinstance(installation, dict) or not iso_with_offset(installation.get("imported_at")):
        errors.append(f"{path}: installation.imported_at must use ISO 8601 with an offset")
    if not isinstance(migration, dict) or migration.get("status") != "completed" or migration.get("to_version") != version:
        errors.append(f"{path}: completed last_migration.to_version must equal source.version")
    overrides = data.get("local_overrides")
    if not isinstance(overrides, list):
        errors.append(f"{path}: local_overrides must be a list")
    else:
        ids: set[str] = set()
        for index, item in enumerate(overrides):
            if not isinstance(item, dict):
                errors.append(f"{path}: local_overrides[{index}] must be a mapping")
                continue
            override_id = item.get("id")
            if not isinstance(override_id, str) or not override_id or override_id in ids:
                errors.append(f"{path}: local_overrides[{index}].id must be unique and non-empty")
            else:
                ids.add(override_id)
            if not isinstance(item.get("paths"), list) or not item["paths"]:
                errors.append(f"{path}: local_overrides[{index}].paths must be non-empty")
            for field in ("reason", "owner", "disposition"):
                if not isinstance(item.get(field), str) or not item[field].strip():
                    errors.append(f"{path}: local_overrides[{index}].{field} is required")


def validate(root: Path, manifest: Path | None = None, verify_git: bool = True) -> list[str]:
    errors: list[str] = []
    release_files = sorted((root / ".dev" / "releases").glob("v*/release.yaml"))
    for path in release_files:
        validate_release(path, root, errors, verify_git)
    effective_manifest = manifest
    default_manifest = root / ".dev" / "AI-CONTEXT-SOURCE.yaml"
    if effective_manifest is None and default_manifest.is_file():
        effective_manifest = default_manifest
    if effective_manifest is not None:
        validate_manifest(effective_manifest, errors)
    if not release_files and effective_manifest is None:
        errors.append(f"{root}: expected source release records or target .dev/AI-CONTEXT-SOURCE.yaml")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--no-git", action="store_true")
    args = parser.parse_args()
    errors = validate(args.root.resolve(), args.manifest, not args.no_git)
    if errors:
        print("AI context version validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    count = len(list((args.root / ".dev" / "releases").glob("v*/release.yaml")))
    manifest = args.manifest or (args.root / ".dev" / "AI-CONTEXT-SOURCE.yaml")
    suffix = f" and target manifest {manifest}" if manifest.is_file() else ""
    print(f"AI context version validation passed for {count} release record(s){suffix}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
