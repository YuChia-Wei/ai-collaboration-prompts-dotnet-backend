# Native Attribution Handoff Planning Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-20-native-attribution-handoff-planning`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-20-native-attribution-handoff-planning`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-20-native-attribution-handoff-planning`
- `created_at`: `2026-07-20T23:55:02+08:00`
- `updated_at`: `2026-07-21T00:00:29+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: HANDOFF-001 needs execution provenance, but one
  repository-mandated `Co-Authored-By` shape can conflict with provider-native
  authorship, signature, human co-author, and session-log behavior.
- Authorized remediation scope: add provider-native attribution preservation,
  provenance-source labels, real-provider fixture requirements, and the known
  current-validator compatibility gap to HANDOFF-001.
- Exclusions: do not change Git commit policy or its validator, do not add or
  modify Copilot or Claude settings, do not rewrite existing commits, and do
  not claim undocumented Claude attribution behavior.
- Completion criteria: HANDOFF-001 treats native attribution as preserved
  evidence, separates execution provenance from authorship, requires golden
  fixtures before implementation, and records the current policy gap.

## Artifact Contract

- Backlog item: `.dev/backlog/items/HANDOFF-001.yaml`
- Research evidence: `.dev/workflows/2026-07-20-native-attribution-handoff-planning/evidence/provider-native-attribution-research.md`
- Task: `.dev/workflows/2026-07-20-native-attribution-handoff-planning/tasks/HANDOFFPLAN-001.json`
- Report: `.dev/workflows/2026-07-20-native-attribution-handoff-planning/reports/remediation-report.md`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| Current validator requires a final AI co-author trailer for every selected commit | compatibility gap | `ai-context-governance` | implement under HANDOFF-001 after fixtures | `HANDOFFPLAN-001` | policy GWT fixtures |
| Copilot CLI repository settings can override its native trailer default | high-risk configuration boundary | repository owner | forbid implicit override; require approval and fixture | `HANDOFFPLAN-001` | settings inventory |
| Copilot cloud-agent authorship is not the same as Copilot CLI trailers | provider contract | `ai-context-governance` | accept evidence union without rewriting | `HANDOFFPLAN-001` | signed commit fixture |
| Claude native attribution is not established by current official docs research | unresolved evidence | `ai-context-governance` | require captured real fixture | `HANDOFFPLAN-001` | provider-generated commit |
| Runtime model and reasoning identity may be available from session metadata | provenance | receiving agent | record source and exact observed values | `HANDOFFPLAN-001` | machine-readable checkpoint |

## Stages And Checkpoints

1. Inspect current policy, validator, settings surfaces, and official provider
   documentation.
2. Distinguish native Git attribution from supplemental execution provenance.
3. Add preservation, source-label, and golden-fixture gates to HANDOFF-001.
4. Validate the backlog and workflow artifacts without changing runtime
   behavior.
5. Commit the planning checkpoint and leave implementation to the v0.5.0
   HANDOFF-001 workflow.

## Resume Checkpoint

- Last completed action: Added native-attribution preservation and real-fixture requirements to HANDOFF-001.
- Current task: none
- Exact next action: during v0.5.0 planning, capture provider-generated fixtures before revising GIT-COMMIT-POLICY or validate-git-commits.py.
- Validation already completed: provider documentation research, repository policy and settings inventory, structured artifact validation, focused governance checks, and the Git for Windows quick gate with all 21 required checks passing.
- Git state: closure artifacts are ready for the workflow commit on the dedicated branch.
- Branch history and checkpoint handoffs: this continuation branch started from local `main@b3eb2af31fbeffe773967ca805fd78600901c03b`, which was two commits ahead of `origin/main`.
- Blockers or unresolved decisions: Claude native attribution remains unasserted until a real provider-generated fixture is captured; the exact HANDOFF-001 schema remains a v0.5.0 owner decision. A bare `bash` command routed to unconfigured WSL and exited before checks; the explicit Git for Windows Bash rerun is the recorded validation result.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-20-native-attribution-handoff-planning` | `main@b3eb2af31fbeffe773967ca805fd78600901c03b` | started | `b3eb2af31fbeffe773967ca805fd78600901c03b` | local | `2026-07-20T23:55:02+08:00` | Plan provider-native attribution compatibility under HANDOFF-001. | Complete `HANDOFFPLAN-001`; leave implementation to v0.5.0. |
