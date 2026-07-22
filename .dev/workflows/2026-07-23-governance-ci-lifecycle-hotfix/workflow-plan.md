# General Governance Release Lifecycle Hotfix

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-23T00:53:22+08:00`
- `updated_at`: `2026-07-23T00:53:22+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-23-governance-ci-lifecycle-hotfix`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-22-post-v0-5-backlog-intake`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-23-governance-ci-lifecycle-hotfix`
- `created_at`: `2026-07-23T00:53:22+08:00`
- `updated_at`: `2026-07-23T00:53:22+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: PR #6 correctly triggered general governance for backlog
  changes, but the job invoked the v0.5.0 candidate phase after publication and
  failed because the registry correctly reports `published`. After that repair,
  a changed governance contract test also triggered Package Candidate, which
  failed because no planned or validated release exists.
- Authorized remediation scope: create CI-002 for comprehensive review and make
  the smallest tested change that removes concrete release-phase execution from
  the general governance workflow while retaining release-tooling unit tests;
  make the exact no-candidate PR state non-applicable without masking other
  candidate rendering failures.
- Exclusions: do not narrow `.dev/backlog/**`, redesign all workflows, change
  release records, run publication, or claim CI-002 is resolved.
- Completion criteria: the hosted failure is reproduced locally; governance no
  longer invokes candidate/finalization phases; a contract test prevents
  regression; structural and local governance checks pass; PR #6 becomes green.

## Artifact Contract

- Backlog: `.dev/backlog/items/CI-002.yaml`
- Task: `.dev/workflows/2026-07-23-governance-ci-lifecycle-hotfix/tasks/CIHOTFIX-001.json`
- Report: `.dev/workflows/2026-07-23-governance-ci-lifecycle-hotfix/reports/remediation-report.md`

## Finding Triage

| Evidence | Severity | Disposition | Task | Validation |
| --- | --- | --- | --- | --- |
| run `29939246189` candidate-phase failure | HIGH | short-term fix now | `CIHOTFIX-001` | local contract plus hosted rerun |
| run `29940380505` no-candidate failure | HIGH | short-term fix now | `CIHOTFIX-001` | packaging contract plus hosted rerun |
| all-workflow responsibility review | follow-up | defer to `CI-002` | `CIHOTFIX-001` | backlog/workflow validation |

## Stages And Checkpoints

1. Inspect hosted failure and Git history.
2. Create CI-002 with comprehensive review acceptance criteria.
3. Remove phase-specific invocation from general governance.
4. Add regression coverage and run local checks.
5. Push, obtain green hosted checks, and merge PR #6.

## Resume Checkpoint

- Last completed action: implemented and locally validated the short-term
  lifecycle ownership correction and recorded CI-002.
- Current task: none; `CIHOTFIX-001` is completed locally.
- Exact next action: push, wait for PR #6 hosted checks, then merge to main.
- Validation already completed: workflow/backlog, governance contract, release
  tooling tests, AI context, versions, JSON, diff, and commit checks.
- Git state: hotfix commit is the commit containing this workflow.
- Branch history and checkpoint handoffs: owner requested the short-term fix on
  the existing PR branch before immediate merge.
- Blockers or unresolved decisions: comprehensive review ownership and release
  assignment remain deferred to CI-002.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-22-post-v0-5-backlog-intake` | `main@79ac24d` | PR hotfix | commit containing this workflow | PR #6 | `2026-07-23T00:53:22+08:00` | Repair deterministic hosted governance failure before merge. | Merge after green hosted checks; activate CI-002 separately. |
