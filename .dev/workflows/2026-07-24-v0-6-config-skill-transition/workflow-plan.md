# v0.6.0 Repository Configuration And Skill Transition

## Workflow Metadata

- `workflow_id`: `2026-07-24-v0-6-config-skill-transition`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-24-v0-6-model-eval-terra`
- `base_branch`: `codex/2026-07-24-v0-6-ci-phase-contract`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-24-v0-6-config-skill-transition`
- `created_at`: `2026-07-24T10:52:55+08:00`
- `updated_at`: `2026-07-24T13:08:39+08:00`

## Objective And Scope

- Execute `CFG-001` and prepare `SKILL-001` as one coordinated v0.6.0
  configuration and taxonomy workstream.
- Accept ADR-001 for the already approved v0.6.0 horizon after implementation
  proves source/downstream ownership, cross-platform text behavior, immutable
  evidence handling, package projection, migration, and target preservation.
- Make root `.editorconfig` and `.gitattributes` source-only truth.
- Map dedicated `ai-context-init` public-root templates to downstream root
  seed files that become target-owned and are not silently overwritten.
- Define the compatibility metadata and validation needed for
  `ai-context-init` and `software-development-orchestrator`.

## Activation Boundary

The owner selected `gpt-5.6-terra` for two fresh candidate runs and one
independent judge. EVAL-001 passed 8/8 critical safety outcomes and 8/8
full-rubric outcomes. `ai-context-init` and
`software-development-orchestrator` therefore activated atomically, while
`repo-structure-sync` and `dev-workflow` remain thin deprecated compatibility
entries with no scheduled removal release.

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
7. Resume after the Terra gate, activate both identifiers atomically, run the
   complete compatibility and package regression, and close `SKILL-001`.

## Resume Checkpoint

- Completed tasks: `CFG-001` and `SKILL-001`.
- Current task: none.
- Last completed action: committed the atomic skill activation and verified the
  actual commit with the 25-case package regression, 13-case repository
  configuration suite, and 10-case deterministic behavior suite.
- Exact next action: include this local branch in the v0.6.0 integration and
  release-definition review.
- Git state: local continuation branch; no push requested for this branch.
- Blocker: none for CFG-001 or SKILL-001.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint | Commit | Recorded At | Resume |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-24-v0-6-config-skill-transition` | `codex/2026-07-24-v0-6-context-load-simplification` | configuration and inactive transition preparation | pre-activation checkpoint | `2026-07-24T11:22:45+08:00` | Await approved model EVAL |
| 2 | `codex/2026-07-24-v0-6-model-eval-terra` | `codex/2026-07-24-v0-6-ci-phase-contract@9ba1865` | Terra evidence and atomic activation | `ab913ae`, `b32f6ca` | `2026-07-24T13:08:39+08:00` | Close workflow after full package regression |
