# Simplification Roadmap Intake Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-20-simplification-roadmap-intake`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-20-simplification-roadmap-intake`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-20-simplification-roadmap-intake`
- `created_at`: `2026-07-20T23:24:59+08:00`
- `updated_at`: `2026-07-20T23:30:28+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: The Fable 5 simplification plan is a valuable independent
  planning source, but corpus word counts do not establish actual prompt cost.
  Historical evidence and core development standards also carry materially
  different risk from always-loaded context.
- Authorized remediation scope: create durable simplification and standards
  deliberation items, record the reason archive work is conditional, establish
  a portable external-AI discussion roundtrip, and update roadmap sequencing.
- Exclusions: do not simplify canonical context, edit standards, move or delete
  history, change schema, assign standards work to a release, or implement
  v0.6.0/v0.7.0 work.
- Completion criteria: `SIMPL-001` and `STD-001` are indexed; archive rationale
  and preconditions are explicit; standards may receive a dedicated release;
  ChatGPT/Fable discussion can return through the external-review intake; and
  repository validators pass.

## Artifact Contract

- Planning source: `.dev/assessments/ASM-20260720-001/evidence/fable5-v0.4.2/06-simplification-plan.md`
- Backlog items: `.dev/backlog/items/SIMPL-001.yaml`, `.dev/backlog/items/STD-001.yaml`
- Human guide: `.dev/guides/ai-collaboration-guides/EXTERNAL-AI-DISCUSSION-ROUNDTRIP-GUIDE.md`
- Task: `.dev/workflows/2026-07-20-simplification-roadmap-intake/tasks/SIMPLPLAN-001.json`
- Report: `.dev/workflows/2026-07-20-simplification-roadmap-intake/reports/remediation-report.md`

## Finding Triage

| Source | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| Fable 5 simplification candidates | planning input | `ai-context-governance` | create measured v0.6 disposition item | `SIMPLPLAN-001` | backlog/workflow validation |
| Historical archive proposal | high-risk decision | `ai-context-governance` | conditional v0.7 successor only | `SIMPLPLAN-001` | rationale and precondition review |
| Standards simplification | core product decision | `ai-context-governance` | unassigned deliberation item | `SIMPLPLAN-001` | roundtrip and version-boundary review |

## Stages And Checkpoints

1. Create the simplification and standards backlog boundaries.
2. Record measured-context and archive evidence requirements.
3. Establish the external discussion roundtrip.
4. Reconcile roadmap and indexes.
5. Validate, report, commit, and close the planning workflow.

## Resume Checkpoint

- Last completed action: Created and validated SIMPL-001, STD-001, archive sequencing, roadmap integration, and the external-AI discussion roundtrip.
- Current task: none
- Exact next action: open the v0.5.0 planning workflow; start a separate STD-001 deliberation workflow when the owner selects its first bounded standards topic.
- Validation already completed: assessment, workflow/backlog, AI-context, version, structured-data, lifecycle, backlog-release, and diff checks passed.
- Git state: closure artifacts are ready for the workflow commit on the dedicated branch.
- Branch history and checkpoint handoffs: `main@97750dd` was pushed before this workflow began.
- Blockers or unresolved decisions: none for this planning intake; standards version and archive execution intentionally remain future owner decisions represented by durable backlog gates.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-20-simplification-roadmap-intake` | `main@97750dd8174138b54710a15eb316fec55d92ade4` | started | `97750dd8174138b54710a15eb316fec55d92ade4` | local | `2026-07-20T23:24:59+08:00` | Plan simplification, archive, and standards discussion boundaries. | Complete `SIMPLPLAN-001`. |
