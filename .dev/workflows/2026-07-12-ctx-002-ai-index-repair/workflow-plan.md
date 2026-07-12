# CTX-002 AI Index Repair

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.1.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-11T00:22:30+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-12-ctx-002-ai-index-repair`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `source_backlog_item`: `CTX-002`
- `branch`: `codex/2026-07-12-ctx-002-ai-index-repair`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation`
- `artifact_root`: `.dev/workflows/2026-07-12-ctx-002-ai-index-repair`
- `created_at`: `2026-07-12T14:25:35+08:00`
- `updated_at`: `2026-07-12T14:25:35+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.1.0`

## Objective And Scope

- Problem statement: `.ai/INDEX.MD` catalogs the retired `.ai/scripts/generated/` path, causing `validate-ai-context.py` to fail after AIC-007 removed generated regex checks.
- Authorized remediation scope: remove the stale active catalog row, verify nearby script navigation, update workflow and backlog lifecycle evidence, and validate the repaired AI context.
- Exclusions: no restoration of retired scripts; no product source or test scan; no unrelated index cleanup; no CTX-001 audit conclusions in this remediation workflow.
- Completion criteria: active script catalog matches the filesystem; AI context, workflow/backlog, and shell asset validators pass; CTX-002 is resolved with commit evidence; an independent read-only verification finds no scope regression.

## Artifact Contract

- Baseline evidence: `.dev/backlog/items/CTX-002.yaml` and the observed validator failure.
- Remediation report: `.dev/workflows/2026-07-12-ctx-002-ai-index-repair/reports/02-remediation-report.md`
- Post-remediation verification: task results plus independent read-only review; the broader durable health audit remains `CTX-001`.
- Tasks: `.dev/workflows/2026-07-12-ctx-002-ai-index-repair/tasks/`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| CTX-002 | HIGH | `ai-context-governance` | remove stale catalog entry | CTX002-001 | AI context validator, workflow validator, shell asset validator, reference search |

## Stages And Checkpoints

1. Bootstrap workflow and freeze the failing evidence.
2. Remove only the retired generated-script catalog entry.
3. Run targeted and aggregate context validation.
4. Request independent read-only scope verification.
5. Reconcile CTX-002, verify commit policy, and close the workflow.

## Resume Checkpoint

- Last completed action: dedicated branch created and CTX-002 evidence confirmed.
- Current task: `CTX002-001`.
- Exact next action: validate workflow bootstrap, then remove the stale `.ai/INDEX.MD` row.
- Validation already completed: baseline `validate-ai-context.py` failed on missing `scripts/generated/`; prior backlog validator passed.
- Git state: branch created from local `main` at `9c0e9c6`; workflow bootstrap edits are uncommitted.
- Branch history and checkpoint handoffs: segment 1 started locally; no push or merge handoff.
- Blockers or unresolved decisions: none.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-12-ctx-002-ai-index-repair` | `main` | workflow bootstrap | pending | local branch | `2026-07-12T14:25:35+08:00` | Repair CTX-002 and restore context validation | Complete `CTX002-001` |

