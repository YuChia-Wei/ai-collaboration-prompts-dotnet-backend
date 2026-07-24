# v0.6.0 Deterministic AI Behavior Evaluation Baseline

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-24-v0-6-eval-deterministic`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-24-v0-6-eval-deterministic`
- `base_branch`: `codex/2026-07-23-v0-6-product-contract-planning`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation`
- `artifact_root`: `.dev/workflows/2026-07-24-v0-6-eval-deterministic`
- `created_at`: `2026-07-24T09:30:25+08:00`
- `updated_at`: `2026-07-24T09:30:25+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: `EVAL-001` requires a complete model-free baseline before
  taxonomy and initialization identifiers can change, but the repository has
  only capability-specific tests rather than one EVAL-owned corpus, result
  schema, runner, and baseline/candidate comparison contract.
- Authorized remediation scope: design and implement the deterministic corpus,
  exact structural and semantic oracle, negative mutations, comparison output,
  and aggregate release gate for empty, existing, copied-template,
  software-development, customization, and compatibility cases.
- Exclusions:
  - Do not call a model or select a model, judge, repetitions, threshold, or
    token budget without owner approval.
  - Do not activate `software-development-orchestrator` or `ai-context-init`.
  - Do not make model evaluation part of routine downstream install or upgrade.
- Completion criteria:
  - Corpus manifest and checked-in expected outputs cover all declared families.
  - A model-free runner produces normalized per-case results and deterministic
    baseline/candidate comparison.
  - Mutants prove missing routes, false authorization, false test success,
    source-truth leakage, dual provenance, and compatibility removal fail closed.
  - The deterministic suite is required by the aggregate gate.
  - Remaining model-in-loop decisions are documented without claiming
    EVAL-001 itself is resolved.

## Artifact Contract

- Baseline assessment: not applicable; EVAL-001 and the completed product
  contract supply the authorized acceptance criteria.
- Remediation report:
  `.dev/workflows/2026-07-24-v0-6-eval-deterministic/reports/remediation-report.md`
- Verification assessment: bounded transient independent verification.
- Tasks: `.dev/workflows/2026-07-24-v0-6-eval-deterministic/tasks/`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| No EVAL-owned deterministic corpus or comparison result | high | governance | implement | `EVALDET-001` | full corpus and exact oracle |
| Model configuration is not approved | high | repository owner | defer at explicit decision boundary | future release-side task | approved plan before calls |

## Stages And Checkpoints

1. Freeze deterministic corpus and result schema.
2. Implement exact model-free runner and negative mutations.
3. Add baseline/candidate comparison and aggregate registration.
4. Run independent verification and close this bounded workflow.
5. Request owner decisions for the release-side model evaluation.

## Resume Checkpoint

- Last completed action: Closed the v0.6.0 product, customization, and
  software-development contract workflow at `9120b21`.
- Current task: `EVALDET-001`.
- Exact next action: implement the EVAL-owned corpus, model-free oracle, result
  schema, comparison runner, and required aggregate tests.
- Validation already completed: final product-contract immutable package matrix
  and independent auditor verification passed.
- Git state: clean stacked branch from the completed product-contract branch;
  no push or merge requested.
- Branch history and checkpoint handoffs: one local stacked branch.
- Blockers or unresolved decisions: model/judge configuration is intentionally
  excluded and does not block deterministic engineering.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-24-v0-6-eval-deterministic` | `codex/2026-07-23-v0-6-product-contract-planning@9120b21` | active bootstrap | containing bootstrap commit | local | `2026-07-24T09:30:25+08:00` | Keep EVAL deterministic work outside the completed product workflow | Continue `EVALDET-001` |
