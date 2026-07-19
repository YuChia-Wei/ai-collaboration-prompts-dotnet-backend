# AI Context Release Roadmap

## Roadmap Metadata

- `roadmap_id`: `post-v0.4.0`
- `status`: `active`
- `current_target`: `v0.4.2`
- `created_at`: `2026-07-18T14:19:06+08:00`
- `updated_at`: `2026-07-19T12:41:16+08:00`
- `source_assessment`: `.dev/assessments/ASM-20260717-004/assessment.yaml`
- `source_plan`: `.dev/backlog/plans/post-v0.4.0-improvement-plan.md`
- `planning_workflow`: `.dev/workflows/2026-07-18-post-v0-4-roadmap-planning/workflow.yaml`
- `gate_revision_workflow`: `.dev/workflows/2026-07-19-roadmap-gate-revision/workflow.yaml`

## Usage Contract

Read this file before planning or resuming a post-v0.4.0 release.

- This roadmap owns release horizons, release-level state, activation gates, and workflow handoffs.
- Individual backlog items own candidate work and their target/completed/published release metadata.
- Execution workflows own task progress, validation evidence, commits, and publication checkpoints.
- Open the planning workflow only when decision rationale or evidence details are needed.

## Release Horizons

| Version | State | Required | Objective | Activation Gate | Workflow |
| --- | --- | --- | --- | --- | --- |
| `v0.4.1` | `published` | yes | Restore only the published package upgrade and downstream-validation contracts through `PKG-001` and `PKG-002`. | Completed at immutable tag `v0.4.1`; hosted run `29650583394` and downloaded assets passed validation. | [`2026-07-18-v0-4-1-release-publication`](../workflows/2026-07-18-v0-4-1-release-publication/workflow.yaml) |
| `v0.4.2` | `ready_for_publication` | yes | `R042-001` through `R042-004` are resolved and independently verified; publish the governed patch candidate. | Windows Git Bash and GitHub Codespaces Ubuntu 24.04 passed 21/21 required quick checks; macOS remains explicitly unverified; publication and immutable tag evidence remain. | [`2026-07-19-v0-4-2-remediation`](../workflows/2026-07-19-v0-4-2-remediation/workflow.yaml) |
| `v0.5.0` | `blocked_by_v0.4.2` | yes | Complete `PKG-003`, `SAG-001`, `ENF-001`, `TOOL-001`, and `LANG-001` as release blockers; explicitly disposition `GOV-001`, `CAP-001`, and `VAL-001`. | Do not create the v0.5.0 implementation workflow until v0.4.2 is completed. Then approve policy, CI, validator, adapter, migration-schema, runner, language, and published-path decisions. | not created |
| `v0.6.0` | `planned` | yes | Establish `EVAL-001`, then introduce skill-family taxonomy and transition `repo-structure-sync` to `ai-context-init` with a deprecated compatibility entry through `SKILL-001`. | Stabilize v0.5.0 governance and adapter contracts; pass deterministic regression fixtures and the approved budgeted release-side model evaluation before taxonomy implementation. | not created |
| `v0.7.0` | `conditional` | no | Retire legacy skill identifiers only when downstream migration evidence supports removal. | Demonstrate adoption of `ai-context-init` and no remaining dependency on old prompts, wrappers, provenance values, or template paths. | not created |

## Release Gate Semantics

- A `release-blocker` is required implementation and evidence. The release
  cannot enter publication while the item is unresolved.
- A `disposition-gate` requires an explicit retained decision before release
  closure. The result may be implement, retain, defer to a named horizon, or
  reject; an unreviewed or silently dropped item fails the gate.
- An `activation-gate` must be satisfied before the named implementation work
  begins.
- These gates control completeness and decision visibility. They do not impose
  a deadline, force a version split, or create artificial time pressure.

| Version | Release Blockers | Disposition Gates | Activation Dependencies |
| --- | --- | --- | --- |
| `v0.4.2` | `R042-001`, `R042-002`, `R042-003`, `R042-004` | Any selected correction that would add a schema, required validation or CI route, remove a published path, or intentionally change pass/fail semantics must stop and move to an explicit v0.5.0 item. | v0.4.1 publication and registry closeout are complete. |
| `v0.5.0` | `PKG-003`, `SAG-001`, `ENF-001`, `TOOL-001`, `LANG-001` | `GOV-001`, `CAP-001`, `VAL-001` | v0.4.2 is completed; its workflow, independent verification, release evidence, and final version state are reconciled. |
| `v0.6.0` | `SKILL-001` | Any legacy identifier retirement remains conditional and cannot be silently included. | `EVAL-001` and v0.5.0 completion. |

`OBS-001` remains an independent unassigned architecture decision. It is not a
hidden v0.5.0 blocker or disposition gate.

## Current Release Evidence

The first governed downstream v0.4.0 upgrade supplied newer and more direct
release evidence than the earlier planning source:

1. `dotnet-mq-arch-lab@2eeddf392ca79deb4407c47d13ad53178015ba90`
   completed the progressive v0.1.0 to v0.3.0 to v0.4.0 upgrade and retained
   workflow plus assessment evidence.
2. `PKG-001` proves that the published guide requires the v0.3.0 manifest while
   the tagged builder emits a clean-install-only `migration.yaml`; this blocks
   the advertised upgrade path.
3. `PKG-002` proves that the package includes and selects source-release tests
   whose Git history, release registry, or builder module is excluded
   downstream.
4. Both are patch-compatible defect corrections unless implementation requires
   a new schema, new required validation contract, or published-path removal.
   Such expansion must stop for v0.5.0 reclassification.
5. The historical assessment and independent Fable 5 plan remain valid planning
   inputs, but their general content corrections no longer precede these
   observed release failures.
6. By user decision, every correction originally targeted to v0.4.1 moves to
   required v0.4.2 work; the independently authored source plan is retained
   unchanged as historical planning input.
7. Migration schema 1.0.0 remains single-source in v0.4.1. `PKG-003` owns the
   v0.5.0 multi-source contract, including direct v0.4.0-to-v0.5.0 validation
   against the retained `dotnet-mq-arch-lab` consumer.

## Approved 2026-07-19 Gate Revision

1. v0.5.0 may not start before v0.4.2 is complete.
2. v0.4.2 contains only patch-compatible corrections. Its release workflow must
   stop and reclassify work when the smallest coherent change needs a new
   schema, required validator or CI route, published-path removal, or intentional
   pass/fail semantic change.
3. The minimum portability evidence for v0.4.2 is Windows Git Bash plus hosted
   Ubuntu. macOS requires a separately arranged environment and remains
   explicitly unverified; no artifact may imply macOS execution.
4. `TOOL-001` and `LANG-001` are v0.5.0 release blockers, not optional cleanup
   or disposition-only work.
5. Model-in-the-loop evaluation is a v0.6.0 release-side activation gate.
   Routine downstream installs and upgrades remain deterministic and model-free
   by default.

## Backlog Release Targets

The backlog index is the quick catalog for target, completion, and publication
versions. Current assignments:

- `v0.4.1`: `PKG-001` and `PKG-002` were completed and published in
  `REL-v0.4.1`.
- `v0.4.2`: all corrections originally assigned to v0.4.1 by the retained
  source plan, bounded by `R042-001` through `R042-004`.
- `v0.5.0` release blockers: `PKG-003`, `SAG-001`, `ENF-001`, `TOOL-001`,
  and `LANG-001`.
- `v0.5.0` disposition gates: `GOV-001`, `CAP-001`, and `VAL-001`.
- `v0.6.0`: `EVAL-001` is the activation gate for `SKILL-001`, which owns the
  taxonomy and compatible `repo-structure-sync` to `ai-context-init`
  transition.
- `unassigned`: `OBS-001`, which remains an independent architecture workflow
  and is not a mandatory v0.5.0 closeout gate.
- Resolved `AIC-007` and `CTX-001` through `CTX-003` were first completed and
  published in `v0.1.0`, verified by Git tag ancestry.

## Sub-Agent Runtime Integration Timing

- `v0.4.2`: correct only the existing `context-translator` routing/catalog
  omission. This is a contract-preserving documentation patch and does not
  authorize new adapter semantics or bulk wrapper generation.
- `v0.5.0`: execute `SAG-001` to define dynamic versus runtime-native role
  integration, add exact adapter metadata and parity validation, verify package
  coverage, and record explicit role-by-role promotion decisions.
- `v0.6.0`: consume the stabilized contract during skill-family taxonomy work.
  Taxonomy grouping or renaming does not automatically promote a role to a
  runtime-native adapter.

## AI Behavior Evaluation And Token Cost Boundary

- Deterministic structure and contract checks are the mandatory complete
  baseline and require no model call.
- Model-in-the-loop evaluation runs on release candidates or explicitly
  requested full evaluations. It does not run during a normal downstream
  upgrade.
- The release workflow must approve the model, judge, repetitions, fixture
  sampling, maximum token budget, acceptance threshold, and result retention
  before executing model calls.
- Empty, existing, and copied-template repositories form the minimum fixture
  families. Deterministic coverage applies to the complete declared corpus;
  model evaluation may use an approved representative sample to bound cost.
- Stochastic results are comparative evidence, not a sole oracle. A single
  model pass cannot override deterministic regression failure.

## Next Action

Execute `V042-001` in the active v0.4.2 remediation workflow: reproduce every
selected observation against `main@9b03668f`, freeze patch-impact dispositions,
then complete `R042-001` through `R042-004`. Retain Windows Git Bash and hosted
Ubuntu evidence, and do not activate v0.5.0 until v0.4.2 is complete. Keep
v0.4.0 consumers on their current version until v0.5.0 unless they explicitly
choose a manual reconciliation; `PKG-003` must prove their direct v0.5.0 path.
