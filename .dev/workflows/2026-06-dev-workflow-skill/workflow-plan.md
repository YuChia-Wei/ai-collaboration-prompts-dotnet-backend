# Dev Workflow Skill Extraction Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-06-dev-workflow-skill`
- `owner_skill`: `skill-creator`
- `status`: `completed`

## Context

- Problem statement:
  - Development process coordination is currently distributed across root agent instructions, workflow gate policy, commit policy, and individual skill descriptions.
  - The repository has clear domain skills, but no dedicated orchestration skill for deciding when to create workflow artifacts, how to route stages to other skills, and when to validate or commit.
  - A `dev-workflow` skill should coordinate development work without taking over implementation, architecture, documentation governance, or review responsibilities from existing skills.
- Current scope:
  - Canonical skill registry, canonical skill spec, runtime wrappers, human-facing skill guide, root routing instructions, and workflow artifacts.
- Why this workflow now:
  - The user wants to evaluate and introduce a separate `dev-workflow` skill that can drive other skills through a development workflow.

## Target Direction

- Target architecture summary:
  - `dev-workflow` owns development workflow orchestration, stage planning, skill routing, validation checkpoints, and commit timing guidance.
  - Existing skills keep their specialized responsibilities.
  - The new skill is available through canonical `.ai` assets, Codex `.agents` wrapper, Claude `.claude` wrapper, and human-facing Traditional Chinese guide.
- Key constraints:
  - Use `skill-creator` to create the new skill.
  - Keep agent-facing skill material in English.
  - Keep human-facing guide material in Traditional Chinese Taiwan usage.
  - Keep wrappers thin and point to canonical specs.
  - Do not duplicate detailed domain rules from downstream skills.
- Non-goals:
  - Do not rewrite every existing skill.
  - Do not implement product code.
  - Do not redesign dotnet backend analyzer or script migration work.

## Stages

### Stage 1: Workflow Bootstrap
- Goal:
  - Create workflow artifacts and task tracking for the skill extraction.
- Scope:
  - `.dev/workflows/2026-06-dev-workflow-skill/`.
- Recommended implementer:
  - `skill-creator`.

### Stage 2: Skill Boundary Design
- Goal:
  - Define what `dev-workflow` owns and what it delegates to existing skills.
- Scope:
  - Canonical skill spec and reference material.
- Recommended implementer:
  - `skill-creator`; consult `ai-context-governance` boundaries when routing touches AI context cleanup.

### Stage 3: Runtime Wrapper Sync
- Goal:
  - Add thin wrappers for Codex and Claude-compatible runtimes.
- Scope:
  - `.agents/skills/dev-workflow/`, `.claude/skills/dev-workflow/`.
- Recommended implementer:
  - `skill-creator`.

### Stage 4: Guide and Index Sync
- Goal:
  - Add human-facing guide and update skill indexes/routing tables.
- Scope:
  - `.dev/guides/ai-collaboration-guides/`, `.ai/assets/skills/README.MD`, wrapper indexes, root agent guides.
- Recommended implementer:
  - `skill-creator` with `ai-context-governance` boundary awareness.

### Stage 5: Final Validation
- Goal:
  - Validate references, JSON tasks, language boundaries, and whitespace before commit.
- Scope:
  - Changed files only, plus routing reference searches.
- Recommended implementer:
  - `skill-creator`.

## Validation Strategy

- Parse workflow task JSON files with `ConvertFrom-Json`.
- Run `rg` for `dev-workflow` references across updated indexes and wrappers.
- Confirm `agents.md` remains English-only.
- Run `git diff --check`.

## Notes

- Open questions:
  - None currently; the initial assumption is that `dev-workflow` is an orchestration skill, not a replacement for domain-specific skills.
- Dependencies:
  - `.dev/standards/WORKFLOW-GATE-POLICY.md`
  - `.dev/standards/GIT-COMMIT-POLICY.md`
  - `.ai/assets/skills/README.MD`
  - `.ai/assets/skills/ai-context-governance/skill.yaml`

## Completion Summary

- Added `dev-workflow` as a universal orchestration skill for workflow mode decisions, workflow artifacts, skill routing, validation checkpoints, and commit checkpoints.
- Added canonical references for routing, workflow artifacts, and output contracts.
- Added thin Codex/current-runtime and Claude-compatible wrappers.
- Added a Traditional Chinese human-facing guide and updated repository, skill, wrapper, workflow, and root agent indexes.
- Validated task JSON parsing, reference discoverability, English-only `agents.md`, and whitespace checks.
