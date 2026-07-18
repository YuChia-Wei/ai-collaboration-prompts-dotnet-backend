# AI Context Release Roadmap

## Roadmap Metadata

- `roadmap_id`: `post-v0.4.0`
- `status`: `active`
- `current_target`: `v0.4.1`
- `created_at`: `2026-07-18T14:19:06+08:00`
- `updated_at`: `2026-07-18T14:53:16+08:00`
- `source_assessment`: `.dev/assessments/ASM-20260717-004/assessment.yaml`
- `source_plan`: `.dev/backlog/plans/post-v0.4.0-improvement-plan.md`
- `planning_workflow`: `.dev/workflows/2026-07-18-post-v0-4-roadmap-planning/workflow.yaml`

## Usage Contract

Read this file before planning or resuming a post-v0.4.0 release.

- This roadmap owns release horizons, release-level state, activation gates, and workflow handoffs.
- Individual backlog items own candidate work and their target/completed/published release metadata.
- Execution workflows own task progress, validation evidence, commits, and publication checkpoints.
- Open the planning workflow only when decision rationale or evidence details are needed.

## Release Horizons

| Version | State | Required | Objective | Activation Gate | Workflow |
| --- | --- | --- | --- | --- | --- |
| `v0.4.1` | `planned` | yes | Correct published-context defects and reproducibility gaps without changing public contracts or removing published paths. | Confirm the exact v0.4.0 commit analyzed by Claude Fable 5, establish a governed successor assessment from the independent plan and reproducible evidence, and pass patch-impact classification. | not created |
| `v0.4.2` | `conditional` | no | Ship a remaining contract-preserving portability defect only if v0.5.0 is materially delayed. | A qualifying defect remains after v0.4.1 and adds no validation route, schema, removal, or required-gate semantic change. | not created |
| `v0.5.0` | `planned` | yes | Institutionalize governance enforcement, CI, validation contracts, policy decisions, and published-path retirement with migration evidence. | Complete v0.4.1 and approve policy, template, CI, and migration decisions. | not created |
| `v0.6.0` | `planned` | yes | Introduce skill-family taxonomy and transition `repo-structure-sync` to `ai-context-init` with a deprecated compatibility entry. | Stabilize v0.5.0 governance contracts and design deprecated-replacement validation. | not created |
| `v0.7.0` | `conditional` | no | Retire legacy skill identifiers only when downstream migration evidence supports removal. | Demonstrate adoption of `ai-context-init` and no remaining dependency on old prompts, wrappers, provenance values, or template paths. | not created |

## Current Gate

The historical assessment and the independently authored Fable 5 plan are two
different inputs:

1. `ASM-20260717-004/assessment.yaml` and `report.md` identify the earlier
   `82b88b7287deb7a64e0311fde6b1b53ea0d194b1` subject and remain a historical
   assessment.
2. `.dev/backlog/plans/post-v0.4.0-improvement-plan.md` was authored separately
   by Claude Fable 5 against the v0.4.0-era repository and was only later placed
   manually in the assessment directory. It is a planning source, not an
   assessment artifact.
3. Confirm whether the analyzed tree was the annotated `v0.4.0` tag commit
   `5af1db672928f9d51f55fee04183ad27b79fb9f8` or a later `main` commit.
4. Use the plan as primary input to a successor assessment, but first record an
   immutable subject, explicit scope and method, and reproducible evidence.
   Recheck only claims that cannot be pinned to the subject or have become
   stale; a full audit is not required by default.

## Backlog Release Targets

The backlog index is the quick catalog for target, completion, and publication
versions. Current assignments:

- `v0.5.0`: `TOOL-001`, `LANG-001`, `GOV-001`, `CAP-001`, and `VAL-001`
  for their declared decision, inventory, or remediation scope.
- `v0.6.0`: `SKILL-001` for the taxonomy and compatible
  `repo-structure-sync` to `ai-context-init` transition.
- `unassigned`: `OBS-001`, which remains an independent architecture workflow
  and is not a mandatory v0.5.0 closeout gate.
- Resolved `AIC-007` and `CTX-001` through `CTX-003` were first completed and
  published in `v0.1.0`, verified by Git tag ancestry.

## Next Action

Confirm the exact v0.4.0 subject commit used by Claude Fable 5, establish a
governed successor assessment using the independent plan and reproducible
evidence, then create the bounded v0.4.1 remediation workflow.
