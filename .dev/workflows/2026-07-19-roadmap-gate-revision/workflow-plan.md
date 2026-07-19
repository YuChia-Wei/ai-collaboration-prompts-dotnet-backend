# Post-v0.4 Roadmap Release Gate Revision

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-19-roadmap-gate-revision`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-19-roadmap-gate-revision`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `closure`
- `artifact_root`: `.dev/workflows/2026-07-19-roadmap-gate-revision`
- `created_at`: `2026-07-19T12:25:11+08:00`
- `updated_at`: `2026-07-19T12:36:28+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: the active roadmap makes v0.4.2 required but does not yet express the repository owner's strict v0.4.2-to-v0.5.0 sequencing, patch-only disposition rules, minimum portability evidence, v0.5.0 blocker classification, or model-in-the-loop evaluation boundary.
- Authorized remediation scope: revise the active roadmap and backlog planning records to capture the user's approved release blockers, disposition gates, environment evidence boundary, and v0.6.0 evaluation prerequisite.
- Exclusions: do not alter the historical source plan; do not implement v0.4.2 corrections; do not add validation routes, schemas, CI, published-path removals, release tags, or publication actions.
- Completion criteria: the roadmap defines strict release sequencing and gate semantics; v0.4.2 has bounded patch-compatible backlog items; v0.5.0 identifies `TOOL-001` and `LANG-001` as release blockers; v0.6.0 has a deterministic-first model-in-the-loop evaluation backlog item; all artifacts validate and the workflow is merged to `main`.

## Decision Authority

The repository owner approved these decisions on 2026-07-19:

1. v0.5.0 must not start until v0.4.2 is complete.
2. v0.4.2 contains only patch-compatible corrections.
3. v0.4.2 portability evidence requires Windows Git Bash and hosted Ubuntu at minimum; macOS evidence is deferred to a separately arranged environment.
4. `TOOL-001` and `LANG-001` are v0.5.0 release blockers.
5. Model-in-the-loop evaluation belongs to the release-side evaluation contract; downstream upgrades remain deterministic by default so routine upgrades do not inherit model token cost.

These decisions supersede only the active roadmap timing and gate classification.
The completed predecessor workflow and
`.dev/backlog/plans/post-v0.4.0-improvement-plan.md` remain immutable historical
planning records.

## Decision Register Addendum

| Decision | Outcome | Relationship To Prior Plan |
| --- | --- | --- |
| `ROADMAP-REV-001` strict release sequence | v0.4.2 is required and v0.5.0 remains blocked until v0.4.2 completion. | Supersedes the predecessor's conditional-v0.4.2 timing; does not rewrite its historical rationale. |
| `ROADMAP-REV-002` patch boundary | v0.4.2 contains only `R042-001` through `R042-004` patch-compatible corrections. | Retains the predecessor SemVer boundary and applies it to the now-required patch release. |
| `ROADMAP-REV-003` portability evidence | Windows Git Bash and hosted Ubuntu are required minimum evidence; macOS is explicitly deferred to a separately arranged environment. | Replaces any broad cross-platform implication with executed-environment claims. |
| `ROADMAP-REV-004` v0.5.0 blockers | `PKG-003`, `SAG-001`, `ENF-001`, `TOOL-001`, and `LANG-001` require completed implementation and evidence. | Elevates TOOL-001 and LANG-001 from disposition candidates; preserves governance, adapter, and migration institutionalization. |
| `ROADMAP-REV-005` v0.5.0 dispositions | `GOV-001`, `CAP-001`, and `VAL-001` require explicit disposition but not necessarily implementation. | Prevents low-priority decisions from silently disappearing without turning every valid deferral into release implementation. |
| `ROADMAP-REV-006` AI behavior evaluation | `EVAL-001` is a deterministic-first, budgeted release-side activation gate for v0.6.0; normal downstream upgrades remain model-free. | Adds the regression strategy required before the taxonomy and `ai-context-init` transition. |

## Gate Semantics

- `release blocker`: required release scope; the release cannot enter publication until the item is resolved and its acceptance evidence is recorded.
- `disposition gate`: a required explicit decision before release closure; implementation may be accepted, deferred, rejected, or moved, but silence is not an acceptable outcome.
- No schedule-pressure exception is implied. These gates prevent incomplete or undecided work from being hidden by version cutting; they do not introduce a timebox or force artificial version splits.

## Artifact Contract

- Active roadmap: `.dev/backlog/ROADMAP.md`
- Backlog index and items: `.dev/backlog/INDEX.MD`, `.dev/backlog/items/`
- Historical planning predecessor: `.dev/workflows/2026-07-18-post-v0-4-roadmap-planning/workflow-plan.md`
- Historical source plan: `.dev/backlog/plans/post-v0.4.0-improvement-plan.md`
- Tasks: `.dev/workflows/2026-07-19-roadmap-gate-revision/tasks/`

## Stages And Checkpoints

1. Create the roadmap-revision workflow and freeze user-approved decisions.
2. Add bounded v0.4.2 and v0.6.0 backlog items.
3. Revise release horizons, blockers, disposition gates, and environment evidence.
4. Validate artifacts and commit history.
5. Close the workflow and merge it to `main` with `--no-ff`.

## Task Plan

| Task | Purpose | Status |
| --- | --- | --- |
| `RGR-001` | Persist the approved roadmap and backlog gate revisions. | `completed` |
| `RGR-002` | Validate, close, commit, and merge the revision workflow. | `in_progress` |

## Resume Checkpoint

- Last completed action: persisted the approved gate semantics, four v0.4.2 blockers, five v0.5.0 blockers, three v0.5.0 disposition gates, and the deterministic-first v0.6.0 evaluation contract.
- Current task: `RGR-002`.
- Exact next action: commit the roadmap revision, validate the workflow commit range, close lifecycle records, and merge to `main` with `--no-ff`.
- Validation already completed: workflow artifact validation passed for 23 workflows and 21 backlog items; six backlog release-contract tests passed; AI-context and version validation passed; Git Bash quick gate passed 21/21 required checks with one declared deferred dependency/version check and two not-applicable checks; task JSON, backlog YAML, and `git diff --check` passed.
- Git state: branch `codex/2026-07-19-roadmap-gate-revision` is based on `main@e83d6ba8aba60263e49fa214db9df3ec8e8f8932`.
- Branch history and checkpoint handoffs: segment 1 started locally for the approved roadmap revision.
- Blockers or unresolved decisions: none for the approved planning revision; release tagging and publication remain outside this workflow.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-19-roadmap-gate-revision` | `main@e83d6ba8aba60263e49fa214db9df3ec8e8f8932` | workflow start | `e83d6ba8aba60263e49fa214db9df3ec8e8f8932` | local | `2026-07-19T12:25:11+08:00` | Persist the approved gate revision without rewriting historical planning records. | Complete `RGR-001`, validate `RGR-002`, then merge to `main`. |
