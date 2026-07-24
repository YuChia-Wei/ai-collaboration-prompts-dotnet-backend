# v0.6.0 GitHub Workflow And Release Lifecycle Contracts

## Workflow Metadata

- `workflow_id`: `2026-07-24-v0-6-ci-lifecycle`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-24-v0-6-ci-lifecycle`
- `base_branch`: `codex/2026-07-24-v0-6-eval-deterministic`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `awaiting-owner-decision`
- `artifact_root`: `.dev/workflows/2026-07-24-v0-6-ci-lifecycle`
- `created_at`: `2026-07-24T10:00:00+08:00`
- `updated_at`: `2026-07-24T10:15:00+08:00`

## Objective And Scope

- Execute `CI-001` and `CI-002` as one release-engineering workstream.
- Upgrade artifact actions to verified Node.js 24-native majors while preserving
  transfer semantics.
- Enforce the exact trigger, permission, concurrency, responsibility, cost, and
  mutation matrix for every active GitHub workflow.
- Remove stale concrete release literals from general governance.
- Preserve the existing v0.5.0 version-specific phase truth until the owner
  chooses the v0.6 phase-contract storage model.

## Decision Boundary

The singleton release phase contract is fixed to v0.5.0. A v0.6.0 candidate
cannot pass until the owner chooses version-scoped phase contracts, which
preserve historical revalidation, or replacement of the singleton, which is
smaller but destroys historical truth. Version-scoped contracts are
recommended. Hosted warning-free artifact and concurrency evidence also
requires a pushed PR and an authorized publication rehearsal or real release.

## Stages

1. Apply the locally decidable workflow matrix and Node.js 24 action majors.
2. Add fail-closed static lifecycle contract tests and runner registration.
3. Record the release phase-contract and hosted evidence boundary.
4. After owner approval, implement version-scoped phase contracts.
5. After push/publication authorization, collect hosted evidence and close.

## Resume Checkpoint

- Current task: `CIENG-001`.
- Exact next action: obtain the owner phase-contract decision, then implement
  the approved version storage and collect hosted evidence after authorization.
- Blockers: version-specific phase-contract owner decision and hosted execution.
- Git state: local static slice committed at `b18833f`; no push or merge
  requested.
