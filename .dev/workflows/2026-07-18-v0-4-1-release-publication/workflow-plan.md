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
- `current_phase`: `validation`
- `artifact_root`: `.dev/workflows/2026-07-18-v0-4-1-release-publication`
- `created_at`: `2026-07-18T23:25:13+08:00`
- `updated_at`: `2026-07-18T23:25:13+08:00`
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
| `REL041-001` | Validate and record the immutable tagged-tree candidate. | `in_progress` | Full gate, version validation, two deterministic package builds and parity. |
| `REL041-002` | Create and push the authorized annotated tag, then verify hosted publication. | `pending` | Annotated tag identity, Actions run, release asset set and checksums. |
| `REL041-003` | Finalize published registry/backlog truth and close the workflow. | `pending` | Published record, tag resolution, context/workflow/version validators. |

## Resume Checkpoint

- Last completed action: merged and pushed the independently verified remediation to `main@f68e85aff5511fcc59b52bcd90b3ee7337da5ee8`.
- Current task: `REL041-001`.
- Exact next action: commit this workflow bootstrap, run the final full source gate, build twice from the immutable publication-preparation commit, and record package digests.
- Validation already completed: remediation candidate source gate 21/21, synchronized target gate 19/19, two candidate builds, and independent verification `ASM-20260718-001`.
- Git state: publication branch created from clean pushed main.
- Blockers or unresolved decisions: none; the user explicitly authorized v0.4.1 publication.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-18-v0-4-1-release-publication` | `main@f68e85aff5511fcc59b52bcd90b3ee7337da5ee8` | started | `f68e85aff5511fcc59b52bcd90b3ee7337da5ee8` | local | `2026-07-18T23:25:13+08:00` | Prepare immutable v0.4.1 publication evidence and authorized tag. | Complete `REL041-001`, integrate, revalidate final main, and publish. |
