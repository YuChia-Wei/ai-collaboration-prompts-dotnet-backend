# v0.6.0 Skill Transition Report

## Outcome

`SKILL-001` is complete.

- Active canonical identifiers:
  - `ai-context-init`
  - `software-development-orchestrator`
- Deprecated compatibility identifiers:
  - `repo-structure-sync` → `ai-context-init`
  - `dev-workflow` → `software-development-orchestrator`
- Removal target for either compatibility identifier: none
- Historical identifier rewrite authority: none

## Activation Evidence

The owner selected `gpt-5.6-terra` instead of Sol for the release-side model
evaluation. Two fresh Terra candidates and one independent Terra judge produced
8/8 critical safety passes and 8/8 full-rubric passes. Exact source evidence is
retained under workflow `2026-07-24-v0-6-model-evaluation`; the distributed
transition manifest carries SHA-256 values instead of source-workflow paths.

The activation was committed atomically in `b32f6ca`. The transition validator
fails closed unless both active canonical/runtime surfaces, both deprecated
canonical/runtime aliases, the deterministic gate, and the Terra evidence
hashes all agree.

## Compatibility Boundary

- New workflow, initialization, templates, guides, validators, and runtime
  routing use the active identifiers.
- Existing workflow, task, assessment, release, provenance, `initialized_by`,
  and `generatedBy` values retain their historical identifiers.
- Historical backlog links to moved canonical resources resolve through an
  explicit legacy-prefix compatibility map; source records are not rewritten.
- The legacy schema-1 provenance template retains
  `initialized_by: repo-structure-sync`; schema-2 initialization uses
  `ai-context-init`.
- `software-development-orchestrator` ends at approved development closeout or
  PR-ready handoff. Delivery, deployment, maintenance-window, production
  verification, and rollback orchestration remain out of scope.

## Validation

| Gate | Result |
| --- | --- |
| Terra model evaluation | 8/8 critical; 8/8 full |
| Skill transition fail-closed suite | 7 passed |
| AI context wrapper contract | 16 passed |
| Software-development acceptance | 3 passed |
| Software-development capability contract | 13 passed |
| Workflow optional-backlog contract | 6 passed |
| Semantic customization skill contract | 5 passed |
| Staged v0.6.0 ZIP/tar build and parity | passed |
| Packaging regression on activation commit | 25 passed; 1 environment-gated test skipped |
| Repository configuration contract | 13 passed |
| AI behavior evaluation | 10 passed |
| Deterministic corpus | 6 cases; zero model calls |
| AI context and workflow validators | passed |
| Skill wrapper quick validation | both active wrappers passed |

The one skipped packaging case is the existing retained downstream integration
test that requires `AI_CONTEXT_DOWNSTREAM_REPO`; it was not converted into a
pass.
