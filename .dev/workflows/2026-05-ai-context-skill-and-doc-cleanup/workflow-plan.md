# AI Context Skill and Documentation Cleanup Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-05-ai-context-skill-and-doc-cleanup`
- `owner_skill`: `ai-context-governance`
- `status`: `active`

## Context

- Problem statement:
  - Existing skills may have overlapping responsibilities, unclear routing boundaries, or names that do not fully match their contents.
  - `.ai/` and `.dev/` still contain files whose universal, .NET backend-specific, or repo-specific status is unclear.
  - README translation handling needs a bounded rule and implementation pass.
  - `.dev/TEAM-GIT-FLOW-RULES.MD` is outdated and should reflect the current single-mainline flow.
- Current scope:
  - Skill registry, skill specs, runtime wrappers, human-facing skill guides, `.ai` / `.dev` context files, README entry files, and git flow documentation.
- Why this workflow now:
  - The previous governance workflow created the policies and `ai-context-governance` skill. This workflow applies those rules to skills, context files, README translations, and git flow.

## Target Direction

- Target architecture summary:
  - Skill responsibilities are explicit, non-overlapping, and aligned across canonical specs, wrappers, and guides.
  - Universal concept material stays reusable; implementation and code-planning material moves to the .NET backend profile or project-specific docs.
  - README translation is limited to stable entry points, not every README.
  - Team git flow uses a simple `main` trunk plus short-lived branches and no-ff merge.
- Key constraints:
  - Use `ai-context-governance` for AI documentation cleanup.
  - Do not use `bdd-gwt-test-designer` unless designing BDD scenarios.
  - Use sub-agents for low-risk translation or pure file movement when useful and non-blocking.
  - Do not ask the user for direction unless a classification or routing decision is ambiguous and has meaningful long-term impact.
- Non-goals:
  - Do not redesign production architecture.
  - Do not create a mono-system or full-stack template.
  - Do not translate every file in the repository.

## Stages

### Stage 1: Skill Responsibility Audit
- Goal:
  - Audit existing skills for duplicated responsibilities, unclear names, mismatched contents, or wrapper/spec drift.
- Scope:
  - `.ai/assets/skills/`, `.agents/skills/`, `.claude/skills/`, `.dev/guides/ai-collaboration-guides/`.
- Non-goals:
  - Do not rewrite every skill immediately.
- Risks:
  - Over-tightening skill descriptions can make triggering too narrow.
- Recommended implementer:
  - `ai-context-governance`; sub-agent explorer may collect initial findings.

### Stage 2: Skill Boundary Corrections
- Goal:
  - Apply low-risk skill naming, description, routing, and index fixes from the audit.
- Scope:
  - Canonical skill specs, wrappers, and human-facing guide indexes.
- Non-goals:
  - Do not merge or delete skills unless the audit clearly proves redundancy.
- Risks:
  - Wrapper and canonical spec drift.
- Recommended implementer:
  - `ai-context-governance`.

### Stage 3: Non-Generic Context Classification and Relocation
- Goal:
  - Classify `.ai` and `.dev` files as universal concept, .NET backend implementation, repo-specific truth, or archive/deferred.
- Scope:
  - `.ai/`, `.dev/standards/`, `.dev/guides/`, `.dev/operations/`, `.dev/requirement/`, `.dev/specs/`.
- Non-goals:
  - Do not move high-link-count files without a reference check.
- Risks:
  - Moving files can break references in guides and scripts.
- Recommended implementer:
  - `ai-context-governance`; sub-agent worker may handle pure file move batches.

### Stage 4: README Translation Handling
- Goal:
  - Apply README language policy to stable entry README files only.
- Scope:
  - Root README and key `.ai`, `.dev`, `.agents`, `.claude` README files.
- Non-goals:
  - Do not create bilingual variants for every subdirectory README.
- Risks:
  - Translation sprawl and source-of-truth drift.
- Recommended implementer:
  - `ai-context-governance`; sub-agent worker may draft or normalize translation files.

### Stage 5: Mainline Git Flow Simplification
- Goal:
  - Rewrite `.dev/TEAM-GIT-FLOW-RULES.MD` to current single-mainline rules.
- Scope:
  - `.dev/TEAM-GIT-FLOW-RULES.MD`, related indexes if needed.
- Non-goals:
  - Do not redefine commit title/body policy already covered by `.dev/standards/GIT-COMMIT-POLICY.md`.
- Risks:
  - Conflicting branch guidance between files.
- Recommended implementer:
  - `ai-context-governance`.

### Stage 6: Index Sync and Final Validation
- Goal:
  - Sync affected indexes and validate references, task statuses, and workflow completion.
- Scope:
  - `agents.md`, `.ai/INDEX.MD`, `.dev/README.MD`, `.dev/INDEX.md`, skill/wrapper indexes as changed.
- Non-goals:
  - Do not do unrelated cleanup.
- Risks:
  - Stale references after relocations or README variants.
- Recommended implementer:
  - `ai-context-governance`.

## Validation Strategy

- Reviewer checkpoints:
  - No skill is assigned AI documentation cleanup unless that is its purpose.
  - BDD skill remains focused on scenario and assertion design.
  - Universal concept files are separated from .NET backend implementation files.
  - README translation does not create uncontrolled bilingual duplicates.
  - Git flow docs point to a single-mainline model and commit policy.
- Tests/validation expectations:
  - Parse workflow task JSON files with `ConvertFrom-Json`.
  - Run `rg` for stale references after file moves.
  - Run `git diff --check` before commits.

## Notes

- Open questions:
  - None at workflow start. Ambiguous classification decisions should be documented in audit artifacts or deferred if they need user direction.
- Dependencies:
  - `.dev/standards/AI-CONTEXT-BOUNDARY.md`
  - `.dev/standards/AI-CONTEXT-LANGUAGE-POLICY.md`
  - `.dev/standards/GIT-COMMIT-POLICY.md`
  - `.dev/standards/WORKFLOW-GATE-POLICY.md`
  - `.ai/assets/skills/ai-context-governance/skill.yaml`
