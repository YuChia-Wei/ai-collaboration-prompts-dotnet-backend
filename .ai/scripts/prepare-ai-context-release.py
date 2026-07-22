#!/usr/bin/env python3
"""Run read-only pre-tag release gates and print the user-owned tag command."""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml


STATE_PATH = Path(__file__).with_name("validate-ai-context-release-state.py")
STATE_SPEC = importlib.util.spec_from_file_location("ai_context_release_state", STATE_PATH)
assert STATE_SPEC and STATE_SPEC.loader
release_state = importlib.util.module_from_spec(STATE_SPEC)
STATE_SPEC.loader.exec_module(release_state)


def run(root: Path, args: list[str]) -> str:
    if args != ["bash", ".ai/scripts/check-all.sh", "--critical"]:
        raise RuntimeError("pre-tag preparation may execute only the critical gate")
    result = subprocess.run(args, cwd=root, check=False, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError((result.stderr or result.stdout).strip())
    return result.stdout


def single_line_tag_value(value: str, label: str) -> str:
    if (
        not isinstance(value, str)
        or not value.strip()
        or any(character in value for character in ('\r', '\n', '"', "\\"))
    ):
        raise RuntimeError(f"{label} must be a non-empty safe single-line value")
    return value.strip()


def checkpoint_ai_model(root: Path) -> str:
    registry_path = root / ".dev/workflows/handoff-checkpoints.yaml"
    try:
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        checkpoint_paths = registry["checkpoints"]
        checkpoint_path = root / checkpoint_paths[-1]
        checkpoint = yaml.safe_load(checkpoint_path.read_text(encoding="utf-8"))
        provenance = checkpoint["execution_provenance"]
    except (
        OSError,
        UnicodeDecodeError,
        yaml.YAMLError,
        KeyError,
        IndexError,
        TypeError,
    ) as exc:
        raise RuntimeError(
            "a registered handoff checkpoint with execution provenance is required"
        ) from exc
    if provenance.get("model_source") == "unavailable":
        raise RuntimeError(
            "the latest handoff checkpoint does not identify an AI model"
        )
    runtime = single_line_tag_value(provenance.get("runtime"), "checkpoint runtime")
    model = single_line_tag_value(provenance.get("model"), "checkpoint model")
    effort = single_line_tag_value(
        provenance.get("reasoning_effort"), "checkpoint reasoning effort"
    )
    source = single_line_tag_value(
        provenance.get("model_source"), "checkpoint model source"
    )
    return f"{runtime} / {model} / reasoning {effort} ({source})"


def compatibility_summary(data: dict) -> str:
    compatibility = data.get("compatibility")
    if not isinstance(compatibility, dict):
        raise RuntimeError("release compatibility must be a mapping")
    sources = compatibility.get("automatic_upgrade_sources")
    if not isinstance(sources, list) or not sources:
        raise RuntimeError(
            "release compatibility must declare automatic upgrade sources"
        )
    change = (
        "pre-1.0 breaking release"
        if compatibility.get("breaking_changes") is True
        else "backward-compatible release"
    )
    return single_line_tag_value(
        f"Compatibility: {change}; automatic sources {', '.join(sources)}.",
        "compatibility summary",
    )


def prepare(
    root: Path,
    version: str,
    commit: str | None = None,
    branch: str | None = None,
    ai_model: str | None = None,
    command_runner=run,
    state_runner=subprocess.run,
) -> str:
    """Run only read-only gates and return, but never execute, the tag command."""
    identity = release_state.validate(
        root,
        "candidate",
        version,
        commit,
        branch,
        runner=state_runner,
    )
    if identity["branch"] != "main":
        raise RuntimeError(
            "pre-tag preparation must run from the merged main branch"
        )
    _, data, _, _ = release_state.release_record(root, version)
    model = single_line_tag_value(
        ai_model if ai_model is not None else checkpoint_ai_model(root),
        "AI model",
    )
    summary = compatibility_summary(data)
    command_runner(root, ["bash", ".ai/scripts/check-all.sh", "--critical"])
    release_state.assert_clean_worktree(root, state_runner)
    return (
        f"git tag -a {version} {identity['commit']} "
        f"-m \"REL-{version} - Governed AI Context Release\" "
        f"-m \"{summary}\" "
        f"-m \"AI-Model: {model}\""
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--version", required=True)
    parser.add_argument("--commit", help="optional assertion; must equal current HEAD")
    parser.add_argument("--branch", help="optional assertion; must equal current branch")
    parser.add_argument(
        "--ai-model",
        help="optional safe single-line override; otherwise use the latest handoff checkpoint",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        tag_command = prepare(
            root,
            args.version,
            args.commit,
            args.branch,
            args.ai_model,
        )
    except (OSError, RuntimeError, release_state.ReleaseStateError) as exc:
        print(f"AI context release preparation failed: {exc}", file=sys.stderr)
        return 1
    print("Pre-tag gates passed. Tag creation remains user-owned.")
    print(tag_command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
