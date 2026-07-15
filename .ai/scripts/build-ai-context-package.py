#!/usr/bin/env python3
"""Build deterministic ZIP and tar.gz AI context release packages."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ai_context_package import PackageError, build_package


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--version", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--profile", default=".ai/distribution/profiles/dotnet-backend.yaml"
    )
    args = parser.parse_args()
    try:
        result = build_package(args.repo, args.ref, args.version, args.output, args.profile)
    except (OSError, PackageError) as exc:
        print(f"AI context package build failed: {exc}", file=sys.stderr)
        return 1
    print(f"Built {result['package_id']} from {result['commit']}")
    print(result["zip"])
    print(result["tar_gz"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
