# v0.4.1 Release Publication Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-18-v0-4-1-release-publication`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-18-v0-4-1-release-publication`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `publication`
- `artifact_root`: `.dev/workflows/2026-07-18-v0-4-1-release-publication`
- `created_at`: `2026-07-18T23:25:13+08:00`
- `updated_at`: `2026-07-18T23:34:24+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: `REL-v0.4.1` is a validated candidate merged and pushed to `main`; publication requires final immutable-tree evidence, an authorized annotated tag, hosted automation verification, and post-publication registry finalization.
- Authorized scope: validate the final tagged-tree candidate, integrate this publication-preparation workflow, create and push annotated `v0.4.1`, verify the GitHub Actions run and four governed assets, then finalize trusted registry truth without moving the tag.
- Exclusions: do not change package contracts after tag creation; do not move, recreate, or delete any published tag; do not modify `dotnet-mq-arch-lab`; do not implement v0.4.2 or `PKG-003`.
- Completion criteria: final full gate and two-build package parity pass; annotated `v0.4.1` resolves to the validated main commit; hosted publication succeeds; downloaded assets validate; registry/backlog/workflow finalization is merged and pushed.

## Release Boundaries

- Governed automatic source: `v0.3.0`.
- Existing `v0.4.0` targets should wait for the `PKG-003` multi-source contract in v0.5.0 unless they explicitly choose manual reconciliation.
- `v0.0.1` targets must first follow the published manual path to validated v0.3.0 provenance, then use the v0.3.0-to-v0.4.1 package path.
- The complete original v0.4.1 correction set remains required v0.4.2 work.

## Task Plan

| Task | Purpose | Status | Validation |
| --- | --- | --- | --- |
| `REL041-001` | Validate and record the immutable tagged-tree candidate. | `completed` | Full gate, version validation, two deterministic package builds and parity. |
| `REL041-002` | Create and push the authorized annotated tag, then verify hosted publication. | `in_progress` | Annotated tag identity, Actions run, release asset set and checksums. |
| `REL041-003` | Finalize published registry/backlog truth and close the workflow. | `pending` | Published record, tag resolution, context/workflow/version validators. |

## Resume Checkpoint

- Last completed action: validated publication-preparation commit `bc99a795e9d6f23e1dd1e70ff3da83c9a9de1161` with the full 21/21 gate and two byte-identical v0.4.1 builds.
- Current task: `REL041-002`.
- Exact next action: commit readiness evidence, merge this branch to `main`, revalidate the final main commit, then create and push annotated `v0.4.1`.
- Validation already completed: full source gate 21/21; archive validation; deterministic ZIP `030a94df60c923917e265c0f90d7921d830d8d1bb2f487c3c5d345128a03703f`; deterministic tar.gz `c8d0cdda3a08c89df546aefa34ac47d658379a3473926320e819690f80352cfe`.
- Git state: publication branch contains immutable readiness evidence and remains untagged.
- Blockers or unresolved decisions: none; the user explicitly authorized v0.4.1 publication.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-18-v0-4-1-release-publication` | `main@f68e85aff5511fcc59b52bcd90b3ee7337da5ee8` | started | `f68e85aff5511fcc59b52bcd90b3ee7337da5ee8` | local | `2026-07-18T23:25:13+08:00` | Prepare immutable v0.4.1 publication evidence and authorized tag. | Complete `REL041-001`, integrate, revalidate final main, and publish. |
| 1 | `codex/2026-07-18-v0-4-1-release-publication` | `main@f68e85aff5511fcc59b52bcd90b3ee7337da5ee8` | readiness-validated | `bc99a795e9d6f23e1dd1e70ff3da83c9a9de1161` | local | `2026-07-18T23:34:24+08:00` | Full gate and two immutable-tree builds passed. | Integrate to main, revalidate the final commit, then publish the annotated tag. |
