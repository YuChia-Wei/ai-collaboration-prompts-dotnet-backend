# AI Context Release Roadmap

## Roadmap Metadata

- `roadmap_id`: `post-v0.4.0`
- `status`: `active`
- `current_target`: `v0.4.1`
- `created_at`: `2026-07-18T14:19:06+08:00`
- `updated_at`: `2026-07-18T21:39:19+08:00`
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
| `v0.4.1` | `in_progress` | yes | First restore the published package upgrade and downstream-validation contracts, then complete remaining contract-preserving correctness fixes without removing published paths. | Resolve and independently verify `PKG-001` and `PKG-002`; stop for reclassification if either requires a new schema, required contract, or published-path removal. | [`2026-07-18-v0-4-1-downstream-upgrade-remediation`](../workflows/2026-07-18-v0-4-1-downstream-upgrade-remediation/workflow.yaml) |
| `v0.4.2` | `conditional` | no | Ship a remaining contract-preserving portability defect only if v0.5.0 is materially delayed. | A qualifying defect remains after v0.4.1 and adds no validation route, schema, removal, or required-gate semantic change. | not created |
| `v0.5.0` | `planned` | yes | Institutionalize governance enforcement, CI, validation contracts, selective sub-agent adapter promotion, policy decisions, and published-path retirement with migration evidence. | Complete v0.4.1 and approve policy, template, CI, sub-agent adapter, and migration decisions. | not created |
| `v0.6.0` | `planned` | yes | Introduce skill-family taxonomy and transition `repo-structure-sync` to `ai-context-init` with a deprecated compatibility entry. | Stabilize v0.5.0 governance and sub-agent adapter contracts, then design deprecated-replacement validation. | not created |
| `v0.7.0` | `conditional` | no | Retire legacy skill identifiers only when downstream migration evidence supports removal. | Demonstrate adoption of `ai-context-init` and no remaining dependency on old prompts, wrappers, provenance values, or template paths. | not created |

## Current Gate

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

## Backlog Release Targets

The backlog index is the quick catalog for target, completion, and publication
versions. Current assignments:

- `v0.4.1`: `PKG-001` and `PKG-002` are HIGH/P0 release blockers in the active
  downstream-upgrade remediation workflow.
- `v0.5.0`: `SAG-001`, `TOOL-001`, `LANG-001`, `GOV-001`, `CAP-001`, and `VAL-001`
  for their declared decision, inventory, or remediation scope.
- `v0.6.0`: `SKILL-001` for the taxonomy and compatible
  `repo-structure-sync` to `ai-context-init` transition.
- `unassigned`: `OBS-001`, which remains an independent architecture workflow
  and is not a mandatory v0.5.0 closeout gate.
- Resolved `AIC-007` and `CTX-001` through `CTX-003` were first completed and
  published in `v0.1.0`, verified by Git tag ancestry.

## Sub-Agent Runtime Integration Timing

- `v0.4.1`: correct only the existing `context-translator` routing/catalog
  omission. This is a contract-preserving documentation patch and does not
  authorize new adapter semantics or bulk wrapper generation.
- `v0.5.0`: execute `SAG-001` to define dynamic versus runtime-native role
  integration, add exact adapter metadata and parity validation, verify package
  coverage, and record explicit role-by-role promotion decisions.
- `v0.6.0`: consume the stabilized contract during skill-family taxonomy work.
  Taxonomy grouping or renaming does not automatically promote a role to a
  runtime-native adapter.

## Next Action

Resume
[`2026-07-18-v0-4-1-downstream-upgrade-remediation`](../workflows/2026-07-18-v0-4-1-downstream-upgrade-remediation/workflow.yaml)
on its recorded branch. Implement `PKG-001` first, validate a real extracted
v0.3.0-to-v0.4.1 package upgrade, then implement `PKG-002` and prove that the
downstream required gate contains only package-applicable checks. Reassess the
remaining v0.4.1 content candidates only after both release blockers pass
independent verification.
