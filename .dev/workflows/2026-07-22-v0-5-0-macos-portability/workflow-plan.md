# v0.5.0 macOS Portability Evidence And Fixture Isolation

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-22T20:35:44+08:00`
- `updated_at`: `2026-07-22T20:54:45+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-22-v0-5-0-macos-portability`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-22-v0-5-0-macos-portability`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `closure`
- `artifact_root`: `.dev/workflows/2026-07-22-v0-5-0-macos-portability`
- `created_at`: `2026-07-22T20:35:44+08:00`
- `updated_at`: `2026-07-22T20:35:44+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: owner-arranged Fable 5 execution verified the v0.5.0
  candidate on macOS but exposed that the documented `AI_CONTEXT_PYTHON`
  route leaks into synthetic runner fixtures and causes eight false failures.
- Authorized remediation scope: preserve and normalize the external report,
  isolate the fixture environment, add a regression, document the exact SDK
  floor, and update active v0.5.0 portability claims before publication.
- Exclusions: do not rewrite final historical assessments or completed workflow
  evidence; do not change release compatibility, upgrade sources, gate sets,
  or provider-native attribution contracts.
- Completion criteria: all three baseline findings are resolved, an independent
  verification assessment passes, focused and critical gates pass, hosted PR
  checks pass, the current-main pre-tag gate passes, and the owner-authorized
  v0.5.0 publication lifecycle completes.

## Artifact Contract

- Baseline assessment: `.dev/assessments/ASM-20260722-003/assessment.yaml`
- Remediation report: `.dev/workflows/2026-07-22-v0-5-0-macos-portability/reports/remediation-report.md`
- Verification assessment: `.dev/assessments/ASM-20260722-004/assessment.yaml`
- Task: `.dev/workflows/2026-07-22-v0-5-0-macos-portability/tasks/MACOS-001.json`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `ASM-20260722-003#AIC-001` | HIGH | `ai-context-governance` | fix before v0.5.0 publication | `MACOS-001` | inherited-override GWT plus focused suite |
| `ASM-20260722-003#AIC-002` | MEDIUM | `ai-context-governance` | document before v0.5.0 publication | `MACOS-001` | prerequisite and version checks |
| `ASM-20260722-003#AIC-003` | LOW | `ai-context-governance` | reconcile active truth | `MACOS-001` | release/backlog/reference scans |

## Stages And Checkpoints

1. Preserve and normalize the Fable 5 report; reproduce material defects.
2. Implement bounded fixture isolation and documentation/release-truth updates.
3. Run focused, structural, critical, and release-candidate validations.
4. Obtain independent post-remediation assessment and reconcile all findings.
5. Merge through hosted gates, rerun pre-tag on current clean `main`, then use
   the owner's explicit authorization to complete tag, publication, and local
   release-registry finalization without moving the immutable tag.

## Resume Checkpoint

- Last completed action: remediated all three `ASM-20260722-003` findings;
  focused suites pass 27/27 normally and with a parent override, critical gate
  passes 33/33, and independent `ASM-20260722-004` reports no blocker.
- Current task: `MACOS-001` in progress.
- Exact next action: persist this verification checkpoint, push and merge after
  hosted checks, rerun pre-tag on current clean `main`, then complete the
  explicitly authorized v0.5.0 publication and registry finalization.
- Validation already completed: raw evidence and subject verified; eight-failure
  reproduction; 27/27 normal and parent-override suites; assessment, workflow,
  AI-context, version, backlog, renderer, and shell validation; candidate state;
  commit range 2/2; critical gate 33/33; independent no-blocker verification.
- Git state: workflow branch at `da70bb5` plus uncommitted verification and
  closure-progress records; no `v0.5.0` tag exists.
- Branch history and checkpoint handoffs: none.
- Blockers or unresolved decisions: none; hosted merge, current-main pre-tag,
  immutable tag, hosted publication, and local finalization remain execution
  steps under the owner's explicit authorization.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-22-v0-5-0-macos-portability` | `main@9ac40bee` | active | pending | local | `2026-07-22T20:35:44+08:00` | Adopt owner-arranged macOS evidence and repair the reproduced fixture leak. | Complete `MACOS-001`, verify, and merge. |
