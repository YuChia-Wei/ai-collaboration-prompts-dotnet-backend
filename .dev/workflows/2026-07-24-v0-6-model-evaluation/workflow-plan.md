# v0.6.0 Terra Model-In-The-Loop Evaluation

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-24-v0-6-model-evaluation`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-24-v0-6-model-eval-terra`
- `base_branch`: `codex/2026-07-24-v0-6-ci-phase-contract`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-24-v0-6-model-evaluation`
- `created_at`: `2026-07-24T12:25:22+08:00`
- `updated_at`: `2026-07-24T12:36:47+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: the deterministic EVAL-001 corpus passes, but it cannot
  prove that a model interprets natural-language requests, routes the planned
  identifiers, preserves approval pauses, and reconciles target-owned
  customization.
- Authorized scope: run a bounded release-side evaluation with
  `gpt-5.6-terra`, retain the complete prompt plan and outputs, apply an
  independent Terra judgment, and decide whether the SKILL-001 activation gate
  passes.
- Exclusions:
  - Do not use Sol as candidate or judge.
  - Do not activate or create candidate skill directories before the judgment
    passes.
  - Candidate and judge agents remain read-only.
  - Do not add model calls to downstream install, upgrade, or normal CI.
- Completion criteria:
  - Two fresh Terra runs answer four representative natural-language cases
    without access to deterministic expected outputs or each other's results.
  - One fresh Terra judge compares all eight case results against repository
    truth and records critical and full-rubric outcomes.
  - All eight critical safety outcomes pass and at least seven of eight full
    case outcomes pass.
  - Complete retained output stays within the approved generated-output ceiling
    and any unavailable provider token telemetry is explicit.
  - EVAL-001 and SKILL-001 states are updated only from the retained judgment.

## Approved Evaluation Configuration

- Candidate model: `gpt-5.6-terra`, default medium reasoning, two fresh runs.
- Judge model: `gpt-5.6-terra`, high reasoning, one fresh independent run.
- Sampling: four representative deterministic families—empty initialization,
  customization-aware upgrade, software-development orchestration, and
  identifier compatibility.
- Prompt/context: only the plan's natural-language cases and declared
  `allowed_context`; deterministic expected outputs, baselines, mutants, and
  other candidate results are forbidden to candidates.
- Generated-output ceiling: 4,000 tokens per model call; three calls and 12,000
  generated tokens maximum in aggregate. Provider-reported total prompt-token
  usage is recorded when available and otherwise remains unavailable.
- Pass threshold: 8/8 critical safety outcomes and at least 7/8 full-rubric
  outcomes.
- Retention: exact candidate outputs, exact judge output, prompt plan, hashes,
  and normalized summary under this workflow's `evidence/` directory.
- Failure disposition: keep both candidate identifiers inactive, leave
  EVAL-001 planned and SKILL-001 in progress, and record the failed cases for a
  later approved rerun.

## Artifact Contract

- Baseline: `.dev/workflows/2026-07-24-v0-6-eval-deterministic/workflow.yaml`
- Evaluation plan: `model-evaluation-plan.yaml`
- Model evidence: `evidence/`
- Result report: `reports/model-evaluation-report.md`
- Task: `tasks/EVALMODEL-001.json`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| Natural-language routing and pause behavior remain unverified | high | governance | evaluate | `EVALMODEL-001` | two candidates plus independent judge |
| Terra result may be stochastic | high | governance | bound with repetitions and threshold | `EVALMODEL-001` | 8/8 critical and 7/8 full |

## Stages And Checkpoints

1. Commit the approved evaluation configuration and prompt packet.
2. Run two independent fresh Terra candidate evaluations.
3. Run one independent Terra judge over retained candidate outputs.
4. Normalize evidence, apply the deterministic threshold, and update gates.
5. Validate and commit the result without activating skills unless the gate
   passes.

All five stages completed. The retained Terra judgment records 8/8 critical
safety outcomes and 8/8 full-rubric outcomes, so the model-in-the-loop gate
passes and the separate atomic skill activation may proceed.

## Resume Checkpoint

- Last completed action: retained two independent Terra candidate outputs and
  one independent Terra judgment, then applied the approved threshold.
- Current task: none; `EVALMODEL-001` is completed.
- Exact next action: resume SKILL-001 and activate both compatible transitions
  atomically.
- Validation already completed: deterministic six-family EVAL baseline; 8/8
  critical safety outcomes; 8/8 full-rubric outcomes; evidence YAML parsing;
  retained SHA-256 hashes.
- Git state: new dedicated branch from pushed CI phase-contract checkpoint.
- Branch history and checkpoint handoffs: one local segment; no push requested.
- Blockers or unresolved decisions: none for EVAL-001. Luna was unavailable in
  this runtime, so the owner-selected Terra configuration was used.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-24-v0-6-model-eval-terra` | `codex/2026-07-24-v0-6-ci-phase-contract@9ba1865` | active bootstrap | containing plan commit | local | `2026-07-24T12:25:22+08:00` | Run owner-approved model EVAL without changing the pushed CI branch | Start two fresh Terra candidate runs |
| 1 | `codex/2026-07-24-v0-6-model-eval-terra` | `codex/2026-07-24-v0-6-ci-phase-contract@9ba1865` | completed local checkpoint | containing result commit | local | `2026-07-24T12:36:47+08:00` | Terra threshold passed and retained evidence is complete | Resume SKILL-001 atomic activation on this branch |
