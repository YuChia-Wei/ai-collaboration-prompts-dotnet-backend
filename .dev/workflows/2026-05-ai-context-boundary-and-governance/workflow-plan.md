# AI Context Boundary and Governance Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-05-ai-context-boundary-and-governance`
- `owner_skill`: `ddd-ca-hex-architect`
- `status`: `completed`

## Context

- Problem statement:
  - Current AI collaboration context mixes reusable agent rules, .NET backend-specific rules, repo-specific truth, human-facing guidance, and runtime wrapper instructions.
  - Git commit format and commit timing are not standardized for autonomous agent work or workflow-stage work.
  - Workflow creation is mostly user-triggered instead of governed by a shared gate.
  - AI-only documentation refactoring lacks a dedicated skill and can be routed to unrelated skills.
- Current scope:
  - `.ai/`, `.agents/`, `.claude/`, `.dev/`, `agents.md`, README and index files.
  - Documentation and AI context governance only; no production code changes.
- Why this workflow now:
  - The repo is moving from a single .NET backend prompt baseline toward separated universal AI context and .NET backend-only context.
  - The current task itself should exercise the new git commit and workflow governance rules.

## Target Direction

- Target architecture summary:
  - Universal agent context lives under `.ai/assets/shared/`.
  - .NET backend-only agent context lives under `.ai/assets/tech-stacks/dotnet-backend/`.
  - Runtime wrappers under `.agents/` and `.claude/` stay thin and English-only.
  - Human-facing guides and requirements use Traditional Chinese Taiwan wording unless they are agent execution contracts.
  - Agent-facing execution contracts use English to reduce token cost and ambiguity.
  - AI context cleanup is handled by a dedicated `ai-context-governance` skill.
- Key constraints:
  - Do not use `bdd-gwt-test-designer` for AI context cleanup.
  - Dotnet backend context excludes Razor, Blazor, MAUI, and other .NET frontend frameworks.
  - Folder placement is the primary classification mechanism; metadata is reserved for machine-readable canonical assets.
  - Commit titles use `<type>(#<issue-number>|<scope>): <summary>` when an issue exists and `<type>(<scope>): <summary>` when none exists.
  - Commit bodies include `Why`, `What`, `Validation`, and `Workflow` sections for workflow-stage commits.
- Non-goals:
  - Do not redesign the production architecture.
  - Do not migrate this repo into a full-stack or mono-system template.
  - Do not translate every document in this workflow.

## Stages

### Stage 1: Context Inventory
- Goal:
  - Inventory AI context files and classify their intended audience, scope, language, and action.
- Scope:
  - `.ai/`, `.agents/`, `.claude/`, `.dev/`, root README, and `agents.md`.
- Non-goals:
  - Do not move files yet.
- Risks:
  - Classification can become stale if not summarized into durable policy.
- Recommended implementer:
  - `ai-context-governance` once created; `ddd-ca-hex-architect` for this bootstrap run.

### Stage 2: Context Boundary Policy
- Goal:
  - Define universal, tech-stack-specific, and repo-specific context placement rules.
- Scope:
  - Add policy under `.dev/standards/` and update entry docs.
- Non-goals:
  - Do not create a second template repo in this workflow.
- Risks:
  - Over-classification can make the repo hard to navigate.
- Recommended implementer:
  - `ai-context-governance`.

### Stage 3: Language Policy
- Goal:
  - Define English, Traditional Chinese Taiwan, and bilingual documentation rules.
- Scope:
  - Agent-facing, human-facing, README, AGENTS, index, specs, requirements, and standards.
- Non-goals:
  - Do not perform full translation pass yet.
- Risks:
  - Bilingual file sprawl if every document requires translations.
- Recommended implementer:
  - `ai-context-governance`.

### Stage 4: Git Commit Policy
- Goal:
  - Standardize commit title, body, issue-number syntax, and autonomous commit timing.
- Scope:
  - Add `.dev/standards/GIT-COMMIT-POLICY.md` and update `agents.md`.
- Non-goals:
  - Do not rewrite historical commits.
- Risks:
  - Commit automation can create noisy commits if stage boundaries are too small.
- Recommended implementer:
  - `ai-context-governance`.

### Stage 5: Workflow Gate Policy
- Goal:
  - Define when agents must create workflow artifacts without waiting for explicit user instruction.
- Scope:
  - Add `.dev/standards/WORKFLOW-GATE-POLICY.md`, update `.dev/workflows/README.MD`, and update `agents.md`.
- Non-goals:
  - Do not require workflow artifacts for every small change.
- Risks:
  - Over-triggering workflows can slow down simple tasks.
- Recommended implementer:
  - `ai-context-governance`.

### Stage 6: AI Context Governance Skill
- Goal:
  - Create a dedicated skill for AI context cleanup, language policy, skill routing, wrapper sync, and context migration.
- Scope:
  - Add canonical skill spec, references, Codex wrapper, Claude wrapper, and human guide.
- Non-goals:
  - Do not merge this responsibility into BDD or code review skills.
- Risks:
  - Skill scope can become too broad unless it excludes code implementation, BDD design, and domain architecture.
- Recommended implementer:
  - `skill-creator` plus `ddd-ca-hex-architect`.

### Stage 7: Dotnet Backend Context Extraction
- Goal:
  - Create the folder structure for .NET backend-only context and move or reference backend-specific agent materials there.
- Scope:
  - `.ai/assets/tech-stacks/dotnet-backend/` and related indexes.
- Non-goals:
  - Do not convert this repo into a mono-system template.
- Risks:
  - Moving files before policy is stable can create churn.
- Recommended implementer:
  - `ai-context-governance`.

### Stage 8: Wrapper and Index Sync
- Goal:
  - Align registry, README, AGENTS, and runtime wrapper indexes with the new context and skill boundaries.
- Scope:
  - `.ai/assets/skills/README.MD`, `.agents/skills/README.md`, `.claude/skills/README.md`, `.ai/INDEX.MD`, `.dev/README.MD`, `agents.md`.
- Non-goals:
  - Do not duplicate canonical rule bodies into wrappers.
- Risks:
  - Broken links or stale wrapper descriptions.
- Recommended implementer:
  - `ai-context-governance`.

## Validation Strategy

- Reviewer checkpoints:
  - Universal context and .NET backend-only context have distinct folders and rule ownership.
  - Human-facing and agent-facing language rules are explicit.
  - Git commit policy supports issue-number and no-issue workflows.
  - Workflow gate rules are actionable without forcing workflows for small tasks.
  - The new skill has a narrow enough purpose to avoid overlap with BDD, code review, and production implementation skills.
- Tests/validation expectations:
  - Run reference searches for stale paths and banned responsibility overlaps.
  - Validate JSON workflow tasks with `ConvertFrom-Json`.
  - Use `git diff --check` before commits.

## Notes

- Open questions:
  - None remaining.
- Dependencies:
  - `.dev/workflows/README.MD`
  - `.ai/assets/skills/README.MD`
  - `.dev/guides/ai-collaboration-guides/SKILL-AND-SUB-AGENT-TAXONOMY-GUIDE.md`

## Completion Summary

- Created context inventory and classification.
- Added AI context boundary, language, git commit, and workflow gate policies.
- Created the dedicated `ai-context-governance` skill with canonical spec, references, Codex wrapper, Claude wrapper, and human guide.
- Extracted .NET backend-only shared context into `.ai/assets/tech-stacks/dotnet-backend/`.
- Synced key indexes and wrapper README files.
- Validated all workflow task JSON files and checked for stale moved shared paths.
