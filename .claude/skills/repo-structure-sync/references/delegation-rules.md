# Delegation Rules

Use these rules after the low-cost inventory pass decides whether to stay local or escalate.

## Update Directly on the Current Pass

These are usually safe for the low-cost pass to update directly when the facts are clear:

- file and directory index tables
- stack-version tables sourced from project files
- quick-start links and doc-entry references
- wording that replaces stale repo names with current file-backed names
- simple architecture bullets that mirror confirmed project layout

## Prefer Stronger Model or Sub-Agent

Delegate these when the rewrite needs synthesis instead of substitution:

- `.dev/ARCHITECTURE.MD` full narrative rewrite
- `agents.md` rule sections that need architectural reinterpretation
- cross-document conflict resolution where one change affects several docs
- module or bounded-context naming normalization
- mixed-stack partitioning or multi-solution ownership explanation

## Recommended Split

If delegating, split the work into the smallest useful packets:

- inventory agent:
  - solution list
  - project classification
  - package/stack summary
- conflict agent:
  - README versus codebase comparison
  - stale copied names and paths
- rewrite agent:
  - one high-impact target document at a time

## Source Packet Requirements

Every delegated task should receive:

- confirmed repo facts only
- exact files inspected
- `P0` and `P1` hits
- target files to rewrite
- explicit out-of-scope files

Do not ask a stronger model or sub-agent to rediscover the repo from scratch unless the first pass was clearly incomplete.
