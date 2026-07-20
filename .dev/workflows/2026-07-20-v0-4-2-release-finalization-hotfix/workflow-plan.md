# v0.4.2 Release Finalization Hotfix Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-20-v0-4-2-release-finalization-hotfix`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-20-v0-4-2-release-finalization-hotfix`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `closure`
- `artifact_root`: `.dev/workflows/2026-07-20-v0-4-2-release-finalization-hotfix`
- `created_at`: `2026-07-20T22:23:02+08:00`
- `updated_at`: `2026-07-20T22:43:57+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: The published v0.4.2 package points at the correct immutable
  commit, but repository release finalization, workflow evidence, release
  authoring sources, and roadmap state are inconsistent. The incident also
  exposed missing cold-start release and cross-model handoff controls.
- Authorized remediation scope: preserve the external Fable 5 review, create a
  repo-native intake assessment, repair local v0.4.2 finalization evidence,
  reconcile roadmap and backlog state, and plan mechanical release and handoff
  safeguards.
- Exclusions: do not move, recreate, delete, or retag `v0.4.2`; do not modify
  published package bytes or migration schemas; do not implement v0.5.0
  release automation in this hotfix; do not edit the public GitHub Release body
  without explicit authorization.
- Completion criteria: every `ASM-20260720-001` finding has an explicit
  disposition; local v0.4.2 release and workflow records are consistent;
  `R042-005`, `REL-001`, and `HANDOFF-001` are represented in the live roadmap;
  required repository validators and the full gate pass; the public Release
  body correction remains explicit until authorized and verified.

## Artifact Contract

- Baseline assessment: `.dev/assessments/ASM-20260720-001/assessment.yaml`
- External review input: `.dev/assessments/ASM-20260720-001/evidence/fable5-v0.4.2/README.md`
- Remediation report: `.dev/workflows/2026-07-20-v0-4-2-release-finalization-hotfix/reports/remediation-report.md`
- Verification assessment: `.dev/assessments/ASM-20260720-002/assessment.yaml`
- Tasks: `.dev/workflows/2026-07-20-v0-4-2-release-finalization-hotfix/tasks/`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `ASM-20260720-001#AIC-001` | CRITICAL | `ai-context-governance` | repair now | `R042005-002` | workflow validator |
| `ASM-20260720-001#AIC-002` | CRITICAL | `ai-context-governance` | repair now | `R042005-002` | version and candidate discovery checks |
| `ASM-20260720-001#AIC-003` | HIGH | `ai-context-governance` | repair local source now; public body pending authorization | `R042005-002` | render and marker checks |
| `ASM-20260720-001#AIC-004` | HIGH | `ai-context-governance` | repair now | `R042005-002` | non-empty migration content |
| `ASM-20260720-001#AIC-005` | HIGH | `ai-context-governance` | correct evidence; preserve incident history | `R042005-002` | tag, object, and run identity checks |
| `ASM-20260720-001#AIC-006` | MEDIUM | `ai-context-governance` | reconcile now | `R042005-003` | backlog and roadmap checks |
| `ASM-20260720-001#AIC-007` | HIGH | `ai-context-governance` | plan v0.5.0 hardening | `R042005-003` | backlog and policy relationship checks |

## Stages And Checkpoints

1. Preserve the raw external review and publish the repo-native intake
   assessment (`R042005-001`).
2. Repair local v0.4.2 release finalization and historical workflow evidence
   without rewriting Git history or the immutable tag (`R042005-002`).
3. Reconcile roadmap/backlog truth and define cold-start release, handoff, and
   external-review intake work (`R042005-003`).
4. Run independent post-remediation verification, full validation, and commit
   checks (`R042005-004`).
5. After explicit authorization, replace and verify the public Release body,
   then close R042-005 and the workflow (`R042005-005`).

## Resume Checkpoint

- Last completed action: Committed local remediation at `895ce060b2287e6c6be6a5327496f6e763145891`, completed independent verification `ASM-20260720-002`, and passed the full gate 21/21.
- Current task: `R042005-005`
- Exact next action: obtain explicit authorization to replace the public GitHub Release body, then read it back and close R042-005.
- Validation already completed: all focused validators pass; full gate passed 21/21 required with 0 failures; rendered-body dry-run passed; tag peel is correct; read-only GitHub API reports one invalid SHA, one final SHA, and four assets.
- Git state: verification and closure-checkpoint artifacts are uncommitted on the dedicated branch.
- Branch history and checkpoint handoffs: none.
- Blockers or unresolved decisions: explicit authorization for public GitHub Release body replacement.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-20-v0-4-2-release-finalization-hotfix` | `main@71c41dbd9c4f2b65105a616d15b7f1cc9db2a338` | started | `71c41dbd9c4f2b65105a616d15b7f1cc9db2a338` | local | `2026-07-20T22:23:02+08:00` | Repair release finalization and encode cold-start safeguards. | Complete `R042005-002`. |
