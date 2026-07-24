# v0.6.0 Repository Configuration And Skill Transition

## Workflow Metadata

- `workflow_id`: `2026-07-24-v0-6-config-skill-transition`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-24-v0-6-config-skill-transition`
- `base_branch`: `codex/2026-07-24-v0-6-context-load-simplification`
- `status`: `in_progress`
- `current_phase`: `remediation`
- `artifact_root`: `.dev/workflows/2026-07-24-v0-6-config-skill-transition`
- `created_at`: `2026-07-24T10:52:55+08:00`
- `updated_at`: `2026-07-24T10:52:55+08:00`

## Objective And Scope

- Execute `CFG-001` and prepare `SKILL-001` as one coordinated v0.6.0
  configuration and taxonomy workstream.
- Accept ADR-001 for the already approved v0.6.0 horizon after implementation
  proves source/downstream ownership, cross-platform text behavior, immutable
  evidence handling, package projection, migration, and target preservation.
- Make root `.editorconfig` and `.gitattributes` source-only truth.
- Map dedicated `repo-structure-sync` public-root templates to downstream root
  seed files that become target-owned and are not silently overwritten.
- Define the compatibility metadata and validation needed for
  `ai-context-init` and `software-development-orchestrator`.

## Activation Boundary

The new skill identifiers must not become active until the owner approves and
runs the release-side model evaluation required by `EVAL-001`. This workflow may
prepare aliases, manifests, fixtures, migrations, and validation in an
inactive-candidate state, but it must keep `repo-structure-sync` and
`dev-workflow` as the active identifiers until that gate passes.

Historical `owner_skill`, provenance, workflow, assessment, task, and release
identifiers remain immutable.

## Stages

1. Bootstrap the coordinated workflow and freeze the accepted configuration
   boundary.
2. Implement source-only repository configuration and dedicated downstream
   target templates.
3. Add fail-closed text-policy, evidence, package, migration, and preservation
   validation.
4. Prepare non-active compatible skill transition metadata and evaluation
   candidates.
5. Run independent verification.
6. Close `CFG-001`; pause only the activation portion of `SKILL-001` at the
   model-evaluation decision boundary.

## Resume Checkpoint

- Current task: `CFG-001`.
- Exact next action: implement and verify the configuration ownership split.
- Git state: local stacked branch; no push or merge requested.
- Blocker: only the active identifier transition requires owner-approved
  model-in-loop EVAL; CFG implementation is not blocked.
