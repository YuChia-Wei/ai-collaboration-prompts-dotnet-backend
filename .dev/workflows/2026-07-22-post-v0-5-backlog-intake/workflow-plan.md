# Post-v0.5 Backlog Intake And Legacy Upgrade Preservation Planning

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-22T21:53:50+08:00`
- `updated_at`: `2026-07-22T22:06:03+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-22-post-v0-5-backlog-intake`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-22-post-v0-5-backlog-intake`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-22-post-v0-5-backlog-intake`
- `created_at`: `2026-07-22T21:53:50+08:00`
- `updated_at`: `2026-07-22T22:06:03+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: v0.5.0 publication exposed Node.js 20 artifact-action
  warnings, while an external WorkService comparison identifies useful issue
  and timeline metadata plus a future legacy customized-target upgrade need.
- Authorized remediation scope: normalize the external evidence, create durable
  backlog items, assign only the urgent CI compatibility work to v0.6.0, retain
  other release decisions as unassigned, and document the existing safe upgrade
  mechanism for future WorkService execution.
- Exclusions: do not edit canonical dev-workflow or upgrader contracts; do not
  inspect or mutate WorkService; do not execute a target upgrade; do not change
  v0.5.0 artifacts or tags.
- Completion criteria: stable assessment findings map one-to-one to backlog,
  roadmap/index discovery is consistent, raw evidence is preserved, validators
  pass, and an independent verification assessment finds no intake blocker.

## Artifact Contract

- Baseline assessment: `.dev/assessments/ASM-20260722-005/assessment.yaml`
- Remediation report: `.dev/workflows/2026-07-22-post-v0-5-backlog-intake/reports/remediation-report.md`
- Verification assessment: `.dev/assessments/ASM-20260722-006/assessment.yaml`
- Task: `.dev/workflows/2026-07-22-post-v0-5-backlog-intake/tasks/INTAKE-001.json`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `ASM-20260722-005#AIC-001` | HIGH | governance | schedule v0.6.0 blocker `CI-001` | `INTAKE-001` | backlog and roadmap validators |
| `ASM-20260722-005#AIC-002` | MEDIUM | dev-workflow/governance | create unassigned `DEVWF-001` | `INTAKE-001` | field and link checks |
| `ASM-20260722-005#AIC-003` | MEDIUM | upgrader/governance | create unassigned `UPG-001` | `INTAKE-001` | migration and provenance checks |

## Stages And Checkpoints

1. Preserve and normalize the external comparison.
2. Verify current-repository and hosted warning claims.
3. Create backlog items and reconcile roadmap discovery.
4. Run structural validation and independent verification.
5. Commit the bounded planning result and close the workflow.

## Resume Checkpoint

- Last completed action: `ASM-20260722-006` verified all three backlog mappings,
  roadmap dispositions, hosted warning evidence, and external-file integrity.
- Current task: none; `INTAKE-001` is completed.
- Exact next action: activate `CI-001` before the next release workflow; discuss
  `DEVWF-001` and activate `UPG-001` in their own authorized workflows.
- Validation completed: assessment, workflow/backlog, backlog contract 6/6, AI
  context, version, JSON, diff, digest, and independent verification checks.
- Git state: closure commit is the commit containing this update.
- Branch history and checkpoint handoffs: checkpoint commits `51b9906` and
  `7714721` preserve the intake and evidence correction respectively.
- Blockers or unresolved decisions: none for intake closure. WorkService remains
  external and its actual upgrade requires target-repository authorization.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-22-post-v0-5-backlog-intake` | `main@79ac24d` | closeout | `51b9906`, `7714721`, and the commit containing this update | local / remote branch | `2026-07-22T22:06:03+08:00` | Normalize evidence, create durable planning records, and verify the intake. | Activate `CI-001` before the next release workflow. |
