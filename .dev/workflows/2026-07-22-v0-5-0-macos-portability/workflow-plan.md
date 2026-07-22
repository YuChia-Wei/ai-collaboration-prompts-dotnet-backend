# v0.5.0 macOS Portability Evidence And Fixture Isolation

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-22T20:35:44+08:00`
- `updated_at`: `2026-07-22T21:13:53+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-22-v0-5-0-macos-portability`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-22-v0-5-0-macos-portability-closeout`
- `base_branch`: `main`
- `branch_segment`: `2`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-22-v0-5-0-macos-portability`
- `created_at`: `2026-07-22T20:35:44+08:00`
- `updated_at`: `2026-07-22T21:13:53+08:00`
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

- Last completed action: reconciled the published release registry, backlog,
  roadmap, and workflow closure after successful hosted publication.
- Current task: none; `MACOS-001` is completed.
- Exact next action: begin a separately governed v0.6.0 activation workflow for
  `EVAL-001`, `SIMPL-001`, and then `SKILL-001`.
- Validation completed: the raw report digest and subject were verified; the
  eight-failure defect was reproduced; focused suites pass 27/27 normally and
  with a parent override; critical gate passes 33/33 with 56 .NET tests;
  assessments, workflow, AI-context, versions, backlog, renderer, shell, and
  commit-range validators pass; `ASM-20260722-004` reports no blocker; PR #5
  hosted package, governance, and Ubuntu checks pass; final pre-tag and tag
  phases pass; publication run `29922585651` and hosted publication validation
  pass with a stable four-asset Release. Post-publication dispatch
  `29924453340` passed its initial hosted governance checks but correctly could
  not apply the candidate-only release contract to a published registry; the
  closeout therefore uses the policy-compliant no-fast-forward branch merge.
- Git state: closeout branch based on published `main@1477181f`; immutable tag
  `v0.5.0` peels to that commit. The registry-closeout commit is the commit
  containing this update.
- Branch history and checkpoint handoffs: segment 1 merged by PR #5; segment 2
  records post-publication finalization without moving the tag.
- Blockers or unresolved decisions: none for v0.5.0.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-22-v0-5-0-macos-portability` | `main@9ac40bee` | merge | `ad962f2` | PR #5 / `main@1477181f` | `2026-07-22T21:01:22+08:00` | Adopt owner-arranged macOS evidence, repair the reproduced fixture leak, and verify it independently. | Continue on a fresh closeout branch after publication. |
| 2 | `codex/2026-07-22-v0-5-0-macos-portability-closeout` | `main@1477181f` | closeout | commits containing these updates | `main` | `2026-07-22T21:13:53+08:00` | Reconcile the published registry, roadmap, backlog, and workflow after immutable-tag publication. | Begin governed v0.6.0 activation planning. |
