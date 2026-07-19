# v0.4.2 Patch-Compatible AI Context Remediation

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-19-v0-4-2-remediation`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-19-v0-4-2-remediation`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation-planning`
- `artifact_root`: `.dev/workflows/2026-07-19-v0-4-2-remediation`
- `created_at`: `2026-07-19T12:41:16+08:00`
- `updated_at`: `2026-07-19T12:41:16+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: the retained post-v0.4.0 assessment and planning source identify wrapper, routing, doctrine, navigation, lifecycle, and portability defects that remain after v0.4.1 focused on the package upgrade contract.
- Authorized remediation scope: complete `R042-001` through `R042-004` using only patch-compatible corrections, validate Windows Git Bash and hosted Ubuntu, independently verify the selected findings, and prepare the governed v0.4.2 candidate.
- Exclusions: no new schema, required validator or CI route, runtime-adapter semantics, runner redesign, intentional pass/fail semantic change, published-path removal, v0.5.0 implementation, tag, or publication.
- Completion criteria: all four blockers are resolved or stopped and explicitly reclassified; selected findings are independently reconciled; Windows Git Bash and hosted Ubuntu evidence is retained; source and candidate gates pass; the remediation workflow closes with an exact release-publication handoff.

## Artifact Contract

- Baseline assessment: `.dev/assessments/ASM-20260717-004/assessment.yaml`
- Current candidate inventory: `evidence/current-candidate-inventory.md`
- Remediation report: `reports/remediation-report.md`
- Verification assessment: `.dev/assessments/<verification-assessment-id>/assessment.yaml`
- Tasks: `.dev/workflows/2026-07-19-v0-4-2-remediation/tasks/`
- Backlog: `.dev/backlog/items/R042-001.yaml` through `.dev/backlog/items/R042-004.yaml`

## Evidence Freshness And Authority

- Immutable workflow base: `main@9b03668f14af7e69e283b4caf30d25fe41d2b460`.
- Historical finding source: `ASM-20260717-004`; its findings remain triage inputs, not automatic proof that every observation is current.
- Independent source plan: `.dev/backlog/plans/post-v0.4.0-improvement-plan.md`; it remains unchanged.
- Current truth: every selected observation must be reproduced against the workflow base before modification. Stale or already-resolved observations are closed with evidence, not edited speculatively.
- Governance authority: the repository owner's 2026-07-19 roadmap decisions and `.dev/backlog/ROADMAP.md`.

## Patch Impact Gate

For every candidate, stop implementation and move the work to a named v0.5.0
backlog item when the smallest coherent correction requires any of:

- a new public schema or runtime-adapter contract;
- a new required validator or CI route;
- published-path or template removal;
- runner redesign or an intentional required-gate pass/fail semantic change;
- a new universal technology or architecture decision.

Content wording, existing routing/catalog completion, path calculation defects,
interpreter discovery for an existing Python contract, dependency/bootstrap
declaration, and explicit historical/deprecated labeling remain patch candidates
when they preserve current public behavior.

## Environment Evidence Contract

- Windows Git Bash is the local source environment.
- Hosted Ubuntu is the minimum independent hosted environment.
- macOS is explicitly unverified until the repository owner arranges a separate
  environment. No report or release note may imply macOS execution.
- A platform claim records the exact command, revision, and result. Passing on
  one platform is not transitive evidence for another.

## Finding Triage

| Backlog / Findings | Severity | Owner | Initial Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `R042-001`; `AIC-001`, `AIC-010`, `SAG-F-002` | HIGH / MEDIUM | `ai-context-governance` | selected; wrapper text and existing routing only | `V042-002` | runtime wrapper quick validation, routing inventory, independent audit |
| `R042-002`; `AIC-002`, `AIC-008`, `AIC-011` | HIGH / MEDIUM | `ai-context-governance` | selected where current canonical doctrine supplies the correction | `V042-003` | focused content assertions, structural checks, independent audit |
| `R042-003`; `AIC-004`, `AIC-006`, `AIC-014`, `AIC-015`, `AIC-018` | HIGH / MEDIUM / LOW | `ai-context-governance` | selected; retain published paths and historical evidence | `V042-004` | link/index/status/outcome checks, independent audit |
| `R042-004`; `AIC-003`, `AIC-005`, `AIC-013` | HIGH / MEDIUM | `ai-context-governance` | selected after current-environment freshness and patch-impact review | `V042-005` | focused shell fixtures, Windows Git Bash, hosted Ubuntu |

`AIC-007` governance PR CI and new semantic wrapper validation are explicitly
excluded and owned by `ENF-001` in v0.5.0. Physical retirement of obsolete
templates and runner redesign are also v0.5.0 scope.

## Stages And Checkpoints

1. Reproduce selected findings and freeze current candidate inventory.
2. Remediate runtime wrapper and routing correctness.
3. Remediate doctrine and standards consistency.
4. Remediate navigation and lifecycle hygiene.
5. Remediate patch-safe tooling portability.
6. Run complete local gates and hosted Ubuntu evidence.
7. Request independent `ai-context-auditor` verification and reconcile findings.
8. Close the remediation workflow and hand off to a separate release-publication workflow.

## Task Plan

| Task | Purpose | Status |
| --- | --- | --- |
| `V042-001` | Reproduce findings, classify patch impact, and freeze the candidate inventory. | `in_progress` |
| `V042-002` | Resolve `R042-001` wrapper and routing correctness. | `pending` |
| `V042-003` | Resolve `R042-002` doctrine and standards consistency. | `pending` |
| `V042-004` | Resolve `R042-003` navigation and lifecycle hygiene. | `pending` |
| `V042-005` | Resolve `R042-004` patch-safe tooling portability. | `pending` |
| `V042-006` | Run candidate gates, hosted evidence, independent verification, and closeout. | `pending` |

## Resume Checkpoint

- Last completed action: created the dedicated v0.4.2 branch from the roadmap-revised `main`.
- Current task: `V042-001`.
- Exact next action: reproduce every selected finding against the immutable workflow base and write `evidence/current-candidate-inventory.md` with patch or v0.5.0 disposition.
- Validation already completed: the roadmap revision and merge commit passed workflow, backlog, AI-context, version, commit, and Git Bash quick-gate validation.
- Git state: `codex/2026-07-19-v0-4-2-remediation` at `main@9b03668f14af7e69e283b4caf30d25fe41d2b460`.
- Branch history and checkpoint handoffs: segment 1 begins after the completed roadmap workflow was merged to `main`.
- Blockers or unresolved decisions: hosted Ubuntu evidence may require a remote branch/run checkpoint; tag and publication remain user-owned and excluded.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-19-v0-4-2-remediation` | `main@9b03668f14af7e69e283b4caf30d25fe41d2b460` | workflow start | `9b03668f14af7e69e283b4caf30d25fe41d2b460` | local | `2026-07-19T12:41:16+08:00` | Execute the required patch-only v0.4.2 blockers after roadmap approval. | Complete V042-001, then execute the four bounded remediation tasks. |

