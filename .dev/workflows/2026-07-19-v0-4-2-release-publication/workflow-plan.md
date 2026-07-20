# v0.4.2 Release Publication Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-19-v0-4-2-release-publication`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-19-v0-4-2-release-publication-cont-02`
- `base_branch`: `main`
- `branch_segment`: `2`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-19-v0-4-2-release-publication`
- `created_at`: `2026-07-19T15:50:00+08:00`
- `updated_at`: `2026-07-20T22:28:31+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: `REL-v0.4.2` is a validated candidate merged and pushed to `main`; publication requires final immutable-tree evidence, an authorized annotated tag, hosted automation verification, and post-publication registry finalization.
- Authorized scope: validate the final tagged-tree candidate, integrate this publication-preparation workflow, create and push annotated `v0.4.2`, verify the GitHub Actions run and four governed assets, then finalize trusted registry truth without moving the tag.
- Exclusions: do not change package contracts after tag creation; do not move, recreate, or delete any published tag; do not modify `dotnet-mq-arch-lab`; do not implement v0.5.0 or `PKG-003`.
- Completion criteria: final full gate and two-build package parity pass; annotated `v0.4.2` resolves to the validated main commit; hosted publication succeeds; downloaded assets validate; registry/backlog/workflow finalization is merged and pushed.

## Release Boundaries

- Governed automatic source: `v0.3.0`.
- Existing `v0.4.0` targets should wait for the `PKG-003` multi-source contract in v0.5.0 unless they explicitly choose manual reconciliation.
- `v0.0.1` targets must first follow the published manual path to validated v0.3.0 provenance, then use the v0.3.0-to-v0.4.2 package path.
- The complete original v0.4.2 correction set is resolved.

## Task Plan

| Task | Purpose | Status | Validation |
| --- | --- | --- | --- |
| `REL042-001` | Validate and record the immutable tagged-tree candidate. | `completed` | Full gate, version validation, two deterministic package builds and parity. |
| `REL042-002` | Create and push the authorized annotated tag, then verify hosted publication. | `completed` | Annotated tag identity, Actions run, release asset set and checksums. |
| `REL042-003` | Finalize published registry/backlog truth and close the workflow. | `completed` | Published record, tag resolution, context/workflow/version validators. |

## Resume Checkpoint

- Last completed action: Successor hotfix reconciled the published tag identity, local release registry, authored sources, and copied workflow evidence.
- Current task: none; historical workflow is completed with a corrective successor.
- Exact next action: With explicit authorization, regenerate the public GitHub Release body from the corrected authored sources under `R042-005`.
- Validation already completed: final tag peel resolves to `f474c3b058cb9f89f93929e0732fc1f276422dd9`; owner-supplied hosted evidence records failed run `29678934006` and successful run `29679273269`; successor validation is recorded by workflow `2026-07-20-v0-4-2-release-finalization-hotfix`.
- Git state: historical workflow artifacts corrected in a successor workflow; Git history and the immutable final tag are unchanged.
- Blockers or unresolved decisions: public GitHub Release body replacement requires explicit authorization.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-19-v0-4-2-release-publication` | `main@312b0252fbcc9b7475bbeb3b530d3b0ad8bd0b55` | started | `312b0252fbcc9b7475bbeb3b530d3b0ad8bd0b55` | local | `2026-07-19T15:50:00+08:00` | Prepare immutable v0.4.2 publication evidence and authorized tag. | Complete `REL042-001`. |
| 2 | `codex/2026-07-19-v0-4-2-release-publication-cont-02` | `main@1c13d799a8cd0c897304e6f21c14a1874ea76b81` | merge | `f474c3b058cb9f89f93929e0732fc1f276422dd9` | `main` | `2026-07-19T15:58:33+08:00` | Integrate the publication registry after the first tag attempt failed closed. | Corrected by `2026-07-20-v0-4-2-release-finalization-hotfix`; do not resume this branch. |
