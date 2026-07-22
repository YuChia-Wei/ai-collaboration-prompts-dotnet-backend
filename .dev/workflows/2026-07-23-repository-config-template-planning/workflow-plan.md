# Source Configuration And Downstream Template Separation Planning

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-23T00:29:56+08:00`
- `updated_at`: `2026-07-23T00:29:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-23-repository-config-template-planning`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-22-post-v0-5-backlog-intake`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-23-repository-config-template-planning`
- `created_at`: `2026-07-23T00:29:56+08:00`
- `updated_at`: `2026-07-23T00:29:56+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: source-root `.editorconfig` and `.gitattributes` currently
  serve both this repository and downstream packaging, while external original
  evidence has no accepted centralized preservation policy.
- Authorized remediation scope: preserve the tradeoff in a Proposed ADR, create
  one durable backlog item, and record the v0.5.1-versus-v0.6.0 gate without
  implementing package changes.
- Exclusions: do not accept ADR-001, edit package profiles or templates, change
  source line endings, relocate evidence, publish v0.5.1, or assign CFG-001.
- Completion criteria: ADR-001 and CFG-001 are indexed and cross-linked; roadmap
  records both candidate horizons; repository validators pass.

## Artifact Contract

- Proposed decision: `.dev/adr/ADR-001-separate-source-config-from-downstream-templates.md`
- Backlog item: `.dev/backlog/items/CFG-001.yaml`
- Task: `.dev/workflows/2026-07-23-repository-config-template-planning/tasks/CFGPLAN-001.json`
- Report: `.dev/workflows/2026-07-23-repository-config-template-planning/reports/remediation-report.md`

## Finding Triage

| Source | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| source/package config ownership | structural | governance | Proposed ADR and backlog | `CFGPLAN-001` | profile/template review |
| cross-platform line endings | portability risk | governance | require implementation evidence | `CFGPLAN-001` | Git/editor policy checks |
| immutable external evidence | decision required | owner | retain tactical fix | `CFGPLAN-001` | digest boundary review |

## Stages And Checkpoints

1. Verify current source and package ownership.
2. Record alternatives and tradeoffs in Proposed ADR-001.
3. Create CFG-001 with patch/minor classification criteria.
4. Reconcile roadmap and discovery indexes.
5. Validate and close planning without implementation.

## Resume Checkpoint

- Last completed action: created Proposed ADR-001 and unassigned CFG-001.
- Current task: none; `CFGPLAN-001` is completed.
- Exact next action: after the intake merges, review ADR-001 and reproduce
  downstream impact before assigning CFG-001 to v0.5.1 or v0.6.0.
- Validation already completed: direct package-profile, public-template,
  EditorConfig, Git attributes, and assessment-evidence boundary review.
- Git state: planning changes use the owner-approved existing backlog branch.
- Branch history and checkpoint handoffs: this workflow intentionally shares
  the unmerged backlog-intake branch by explicit owner direction.
- Blockers or unresolved decisions: ADR acceptance and release assignment remain
  owner decisions; implementation is not authorized here.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-22-post-v0-5-backlog-intake` | `main@79ac24d` | planning addendum | commit containing this workflow | current intake branch | `2026-07-23T00:29:56+08:00` | Owner approved related backlog planning before merge. | Merge intake; activate CFG-001 after ADR and release classification. |
