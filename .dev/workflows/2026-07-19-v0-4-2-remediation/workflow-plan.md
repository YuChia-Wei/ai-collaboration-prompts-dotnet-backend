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
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-19-v0-4-2-remediation`
- `created_at`: `2026-07-19T12:41:16+08:00`
- `updated_at`: `2026-07-19T15:50:00+08:00`
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
- Verification assessment: `.dev/assessments/ASM-20260719-001/assessment.yaml` (`final`)
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
| `V042-001` | Reproduce findings, classify patch impact, and freeze the candidate inventory. | `completed` |
| `V042-002` | Resolve `R042-001` wrapper and routing correctness. | `completed` |
| `V042-003` | Resolve `R042-002` doctrine and standards consistency. | `completed` |
| `V042-004` | Resolve `R042-003` navigation and lifecycle hygiene. | `completed` |
| `V042-005` | Resolve `R042-004` patch-safe tooling portability. | `completed` |
| `V042-006` | Run candidate gates, hosted evidence, independent verification, and closeout. | `completed` |

## Resume Checkpoint

- Last completed action: finalized `ASM-20260719-001`, reconciled the
  GitHub Codespaces Ubuntu 24.04 21/21 gate at superseding candidate
  `51be197`, and resolved all four v0.4.2 blockers.
- Current task: none.
- Exact next action: merge this completed remediation workflow to `main` with
  `--no-ff`, then start the separately authorized v0.4.2 release-publication
  workflow.
- Validation already completed: 22 portability/fail-closed GWT tests and shell
  asset parity; Windows Git Bash quick gate 21/21 at `e76d89c`; GitHub
  Codespaces Ubuntu 24.04 quick gate 21/21 at `51be197`; final
  `ASM-20260719-001`; assessment, workflow, AI-context, version, shell, and
  segmented commit validators.
- Git state: completed workflow branch prepared for its governance closeout
  commit; local untracked `tmp/` evidence is not part of the candidate tree.
- Branch history and checkpoint handoffs: segment 1 begins after the completed roadmap workflow was merged to `main`.
- Blockers or unresolved decisions: none for remediation closure. macOS remains
  explicitly unverified; tag and publication belong to the separately
  authorized release-publication workflow.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-19-v0-4-2-remediation` | `main@9b03668f14af7e69e283b4caf30d25fe41d2b460` | workflow start | `9b03668f14af7e69e283b4caf30d25fe41d2b460` | local | `2026-07-19T12:41:16+08:00` | Execute the required patch-only v0.4.2 blockers after roadmap approval. | Complete V042-001, then execute the four bounded remediation tasks. |
| 1 | `codex/2026-07-19-v0-4-2-remediation` | `main@9b03668f14af7e69e283b4caf30d25fe41d2b460` | owner intervention | `51be197a9a46caf23438c98065fcca58c723ce99` | `origin/codex/2026-07-19-v0-4-2-remediation` | `2026-07-19T15:24:25+08:00` | Preserve repository-owner test and Codespaces setup commits without fabricated AI trailers or pushed-history rewriting. | Validate the owner changes directly and continue with a separately validated AI closeout segment. |
| 1 | `codex/2026-07-19-v0-4-2-remediation` | `main@9b03668f14af7e69e283b4caf30d25fe41d2b460` | completed | pending | `main` | `2026-07-19T15:50:00+08:00` | All remediation blockers and platform evidence are resolved. | Commit closeout, merge with `--no-ff`, and start release publication. |
