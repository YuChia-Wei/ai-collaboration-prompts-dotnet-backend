# AI Context Auditor Skill Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-07-ai-context-auditor-skill`
- `owner_skill`: `dev-workflow`
- `status`: `completed`

## Context

- Problem statement: AI context self-audits are recurring work but do not yet have a dedicated skill, stable scan boundary, or reusable report template.
- Current scope: Add one canonical AI context audit skill, runtime wrappers, routing and guide entries, a report template, and the report for the 2026-07-10 audit.
- Why this workflow now: The user wants AI context self-auditing to become a standard repeatable workflow with durable reports.

## Target Direction

- Create `ai-context-auditor` as a read-only-by-default audit skill.
- Default to AI context and governance surfaces while excluding product code roots such as `src/` and `tests/`.
- Route source-code review requests to `code-reviewer` instead of expanding the audit scope.
- Persist each audit report under `.dev/workflows/<workflow-id>/review-report.md` using a canonical template.
- Keep canonical instructions under `.ai/assets/skills/` and runtime wrappers thin.

## Stages

### Stage 1: Skill and report contract

- Goal: Define scan boundaries, audit phases, severity, evidence, comparison, and report persistence rules.
- Scope: Canonical skill spec, references, template, and initialized runtime wrapper.
- Non-goals: Product code review, production code changes, architecture redesign, or automatic remediation.
- Risks: The auditor could overlap with `ai-context-governance` or `code-reviewer` if boundaries are vague.
- Recommended implementer: `ai-context-governance`

### Stage 2: Runtime and navigation sync

- Goal: Synchronize Codex and Claude wrappers, registries, routing, and the human-facing guide.
- Scope: `.agents/skills/`, `.claude/skills/`, canonical and wrapper indexes, capability profile, and guide index.
- Non-goals: Gemini or Copilot wrapper implementation.
- Risks: Registry or wrapper drift.
- Recommended implementer: `ai-context-governance`

### Stage 3: Initial audit report and validation

- Goal: Save the completed audit using the new report contract and validate all new relationships.
- Scope: Workflow review report, JSON state, skill validation, references, Markdown, and git diff checks.
- Non-goals: Fixing the audit findings in this workflow.
- Risks: The report could overstate checks that were not run.
- Recommended implementer: `ai-context-auditor`

### Stage 4: Post-commit reconciliation

- Goal: Reconcile the manually completed commit with workflow state and correct validation gaps discovered after commit.
- Scope: EOF whitespace normalization, workflow commit status, validation evidence, and a compliant follow-up commit.
- Non-goals: Rewriting the already-pushed `3a11df7` commit or remediating findings from the audit report.
- Risks: Rewriting published history or erasing the original approval-limit context.
- Recommended implementer: `ai-context-governance`

## Validation Strategy

- Run the skill-creator quick validator against the Codex runtime wrapper.
- Parse all changed JSON files.
- Verify canonical, wrapper, guide, template, and report paths.
- Verify default exclusions and the code-review handoff rule by targeted searches.
- Run `git diff --check` and repository context checks that do not scan product code.

## Notes

- Open questions: None. The repository conventions provide enough evidence for naming and placement.
- Dependencies: `skill-creator`, `dev-workflow`, and `ai-context-governance`.

## Completion Summary

- Added the canonical `ai-context-auditor` skill, scope and routing rules, two-pass audit playbook, output contract, and report template.
- Added thin Codex and Claude wrappers, runtime UI metadata, registry entries, root routing, dev-workflow capability routing, and a human-facing guide.
- Saved the 2026-07-10 self-audit as this workflow's `review-report.md`.
- Validated the skill structure, structured files, wrapper parity, required paths, scope boundaries, portability, and forward-test behavior.
- Post-commit reconciliation completed after the user manually created and pushed commit `3a11df7`.
- Removed the eight EOF whitespace defects missed while the files were untracked.
- Reconciled stale commit-pending state and recorded the original commit-body omission as a published-history exception without amending or force-pushing `main`.
