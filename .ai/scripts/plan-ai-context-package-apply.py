#!/usr/bin/env python3
"""Plan an extracted AI context package application; apply only with --apply."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from ai_context_package_apply import ApplyError, apply_plan, build_plan


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--target-root", type=Path, required=True)
    parser.add_argument("--previous-files", type=Path)
    parser.add_argument("--acknowledge", action="append", default=[])
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--plan-output", type=Path)
    args = parser.parse_args()
    try:
        plan = build_plan(args.package_root, args.target_root, args.previous_files)
        content = yaml.safe_dump(plan, sort_keys=False, allow_unicode=True)
        if args.plan_output:
            args.plan_output.write_text(content, encoding="utf-8", newline="\n")
        print(content, end="")
        if not args.apply:
            print("Dry run only. Re-run with --apply after reviewing the plan.")
            return 0
        receipt = apply_plan(plan, set(args.acknowledge))
        print(yaml.safe_dump({"apply_receipt": receipt}, sort_keys=False), end="")
        return 0
    except (OSError, ApplyError, ValueError) as exc:
        print(f"AI context package apply failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
