# v0.4.0 AI Context Standards And Reference Architecture Remediation

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-16-v0-4-0-ai-context-remediation`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-16-v0-4-0-ai-context-remediation`
- `base_branch`: `codex/assessment/asm-20260715-002`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `verification-reconciliation`
- `artifact_root`: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation`
- `created_at`: `2026-07-16T07:22:13+08:00`
- `updated_at`: `2026-07-16T23:40:51+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: v0.4.0 needs one coherent .NET backend context that separates invariants, defaults, target choices, examples, and historical Java/EzDDD provenance while supporting both multi-BC micro-system mono repos and mono-system repositories.
- Authorized remediation scope: plan and later remediate findings from `ASM-20260715-002`; use `ASM-20260715-001` only as superseded comparison evidence; incorporate the user's confirmed NSubstitute direction, repository lineage, and read-only downstream architecture observations; coordinate standards, examples, routing, validators, BuildingBlocks reconstruction knowledge, and independent verification.
- Current authorization boundary: the review gates and first remediation slice are approved. Execute `AIC-004` and `AIC-012` first, maintain the file-disposition manifest, and do not create a reference product. Later tasks remain bounded by this plan.
- Exclusions: product code remediation in either lab; publishing packages; creating NuGet packages or a distributable `dotnet new` template; moving tags; GitHub Release work; remote branch deletion; merge without explicit authorization. Pushes of this active workflow branch are authorized for cross-machine review.
- Completion criteria: all 14 authoritative findings and supplemental architecture decisions have explicit outcomes; selected standards and projections agree; examples have declared verification tiers; the BuildingBlocks and project-structure knowledge supports architectural reconstruction without depending on a committed reference product; validators describe and enforce their real scope; an independent successor assessment verifies the result; commits and closure evidence pass policy.

## Artifact Contract

- Historical assessment: `.dev/assessments/ASM-20260715-001/assessment.yaml`
- Authoritative baseline: `.dev/assessments/ASM-20260715-002/assessment.yaml`
- Remediation report: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation/reports/remediation-report.md`
- Verification assessment: `.dev/assessments/ASM-20260716-001/assessment.yaml`
- Tasks: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation/tasks/`
- BuildingBlocks/examples MVP plan: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation/plans/building-blocks-examples-mvp.md`
- File-disposition manifest: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation/plans/file-disposition-manifest.yaml`

## Decision Register

| Decision | State | Current direction | Evidence / consequence |
| --- | --- | --- | --- |
| `V040-DEC-001` Mocking framework | confirmed by user | NSubstitute is the framework profile default and is mandatory within that profile. A target may replace it through one explicit technology-selection override instead of editing scattered rules. | Create one target-owned selection slot and make derived testing guidance consume it; GWT remains invariant. |
| `V040-DEC-002` Deletion semantics | confirmed by user | Soft deletion is a default-profile Aggregate Repository behavior with explicit target opt-out: the Aggregate changes deletion state and `SaveAsync` persists it. Physical deletion is a separately authorized command/use case and restricted repository/capability. | Change `DELETE-SOFT-001` ownership strength and projections consistently; do not make existing targets without global soft deletion violations by default. |
| `V040-DEC-003` Repository profiles | approved minimal core | Use one logical solution-folder grammar: shared foundations plus `<workload>/DomainCore` and `<workload>/Presentation`; workload means BC for micro-system and system for mono-system. | Do not expand this workflow into detailed naming or cross-profile migration design; physical layouts remain target-owned. |
| `V040-DEC-004` Observability | moved out of workflow | Runtime AOP/attribute observability is CrossCutting and Domain must not depend on it; full design is not assessment remediation. | Retain only this bounded candidate if needed for context, and create a separate design workflow for a full standard/reference. |
| `V040-DEC-005` BuildingBlocks realization | approved | BuildingBlocks defaults to contracts/interfaces. Retain one optional `EsAggregateRoot<TId>` abstraction under three conditions: executable-tested pure behavior, an independent behavior contract, and source-copy ownership managed by upgrader three-way reconciliation until packaging exists. | Unify standards/examples and `DBA1009` recognition around the same ES shape; no other default base classes and no reference product. |
| `V040-DEC-006` Examples contract | approved | Executable examples require tests; structure-validated items name their validator; evidence tiers are machine-readable; unclassified legacy defaults downward to historical or illustrative. | Add schema/validator coverage and never infer upward promotion. |
| `V040-DEC-007` Technology selection | approved mechanism | Mocking, ORM, broker, and similar target choices use one generic technology-selection override shape. | NSubstitute remains the default mocking selection without creating a mocking-only override mechanism. |
| `V040-DEC-008` Migration contract | approved prerequisite | Every remediated framework path receives `kept`, `moved-to`, `merged-into`, or `retired` disposition in an upgrader-consumable manifest. | Maintain the manifest during remediation and project it into v0.4.0 migration guidance before `ROUTE-001` and release closure. |

## Repository Lineage And Evidence Consequences

The user supplied this provenance chain: the earliest Java source is `ai-coding-exercise` at `f7ed0b9b5b23822ec012c375261df44f6f03a97f`; initial .NET standards were applied to `dotnet-mq-arch-lab`; that lab was then used to refine the desired architecture and standards; this repository was created after removing the .NET implementation and has evolved as the standalone AI context product.

This history explains why Java, EzDDD, and `Lab.*` material can coexist. It does not make those literals current truth. Remediation must classify each occurrence as an active portable concept, target-owned example, or historical/reference artifact; active canonical guidance must be understandable without either source repository. `dotnet-mq-arch-lab` and `dotnet-webapi-lab` remain read-only adoption evidence rather than canonical implementation sources.

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `ASM-20260715-002#AIC-001` | HIGH | governance + architecture | rewrite profile truth | `RULE-001` | relationship checks and profile fixture |
| `#AIC-002` | HIGH | governance + architecture | make soft delete standard Aggregate Repository behavior; keep purge explicit | `RULE-001` | ownership/projection parity |
| `#AIC-003` | HIGH | governance | define verification tiers; replace stale sync claims | `EXAMPLE-001` | tier inventory and evidence-route checks |
| `#AIC-004` | HIGH | governance + validator owner | replace removed command route | `TRUTH-001` | command existence and analyzer route |
| `#AIC-005` | HIGH | architecture + governance | extract portable concepts; replace placeholders with reconstruction contracts or archive | `BUILD-001` | provenance/concept/reconstruction matrix |
| `#AIC-006` | MEDIUM | governance | consolidate catalogs and shared fixtures while preserving deliberate test modes | `EXAMPLE-001` | duplicate and link scan |
| `#AIC-007` | MEDIUM | governance | move/re-route by audience and ownership | `ROUTE-001` | context and link validators |
| `#AIC-008` | MEDIUM | validator owner | state structural scope and add selected relationship checks | `VALIDATE-001` | fail-closed tests |
| `#AIC-009` | MEDIUM | governance + validator owner | split shell lifecycle taxonomy | `VALIDATE-001` | registry/runner parity |
| `#AIC-010` | MEDIUM | architecture | replace synchronous controller example | `TRUTH-001` | compile-tested async slice |
| `#AIC-011` | LOW | governance | link, archive, or remove after comparison | `ROUTE-001` | inbound route inventory |
| `#AIC-012` | MEDIUM | governance | remove target-specific namespace from canonical guidance | `TRUTH-001` | literal target-name scan |
| `#AIC-013` | HIGH | governance + testing | define NSubstitute profile default with one explicit target override slot | `RULE-001` | package/rule/projection scans |
| `#AIC-014` | MEDIUM | architecture + governance | add a compact reconstruction blueprint and evidence matrix or narrow the portfolio claim | `BUILD-001`, `ARCH-001` | navigation, profile, and downstream comparison checks |

## Task Plan

| Task | Purpose | Status | Depends on |
| --- | --- | --- | --- |
| `PLAN-001` | Freeze user decisions, evidence boundaries, finding mapping, and execution order. | `completed` | none |
| `RULE-001` | Align generic technology selection, soft-delete profile ownership, and projections. | `completed` | `PLAN-001`, `TRUTH-001` |
| `TRUTH-001` | Repair the broken DBA1001 route and target namespace leakage as the first remediation slice. | `completed` | `PLAN-001` |
| `TRUTH-002` | Repair or downgrade the synchronous Java-shaped controller guidance. | `completed` | `TRUTH-001`, `EXAMPLE-001` |
| `EXAMPLE-001` | Define machine-readable example verification tiers and default-downward legacy classification. | `completed` | `PLAN-001`, `RULE-001` |
| `EXAMPLE-002` | Consolidate duplicate example catalogs and fixtures after the retained portfolio stabilizes. | `completed` | `BUILD-001`, `TRUTH-002` |
| `BUILD-001` | Produce the lineage-to-BuildingBlocks concept matrix, minimize base classes, and establish the documentation-first reconstruction contract. | `completed` | `RULE-001`, `EXAMPLE-001` |
| `ARCH-001` | Add only the minimal shared logical grammar for micro-system/mono-system repository profiles. | `completed` | `PLAN-001`, `RULE-001` |
| `MIGRATE-001` | Maintain the file-disposition manifest and integrate it with upgrader/release migration guidance. | `completed` | all changed-path tasks; must complete before `ROUTE-001` |
| `ROUTE-001` | Correct audience placement and weak routing; archive only after replacement evidence. | `completed` | `EXAMPLE-001`, `ARCH-001` |
| `VALIDATE-001` | Correct validator claims and shell lifecycle taxonomy; add required fail-closed coverage. | `completed` | `TRUTH-001`, `BUILD-001`, `ROUTE-001` |
| `VERIFY-001` | Run independent verification assessment, reconcile all findings, and close or defer explicitly. | `in_progress` | all remediation tasks |
| `PROFILE-002` | Close the verified active profile-selector and naming residual. | `completed` | `VERIFY-001` assessment intake |
| `DOC-002` | Align routed mocking-default and async use-case documentation. | `completed` | `PROFILE-002` |
| `GATE-002` | Add BuildingBlocks behavior tests to the required aggregate gate. | `completed` | `DOC-002` |

## Stages And Checkpoints

1. Completed: decision confirmation, evidence freeze, and file-disposition contract.
2. First slice: `AIC-004` and `AIC-012` active truth repair.
3. Canonical profile ownership and generic technology-selection repair.
4. Machine-readable example contract, optional ES abstraction, and minimal repository-profile work.
5. Complete migration-manifest/upgrader/release projection before routing changes.
6. Placement, routing, validator, and script-lifecycle remediation.
7. Independent verification assessment, including clean navigation/reconstruction without copying either lab.
8. Finding reconciliation, commit verification, and workflow closure.

## Task Detail: TRUTH-001

The original task was split so the first slice can close without waiting for profile or example-tier design:

1. `AIC-004`: the active spec-compliance skill still routes to removed `check-repository-compliance.sh`; replace it with the current analyzer/tool contract and test command existence.
2. `AIC-012`: broad canonical guidance contains `Lab.MessageSchemas.<Domain>`; replace it with the portable canonical namespace placeholder or a link to the canonical project-structure owner.

`AIC-010` is now `TRUTH-002` and follows the evidence-tier contract. `TRUTH-001` deliberately excludes profile ownership, example portfolio consolidation, and analyzer redesign. Its success criterion is that every active command/path it touches can be followed literally without reaching a missing command or target-specific namespace.

## BuildingBlocks And Examples MVP

The approved MVP is defined in [the dedicated reconstruction-contract plan](plans/building-blocks-examples-mvp.md). It removes the complete BuildingBlocks/SampleProduct fixture proposal, keeps the repository focused on reconstructable knowledge, and approves `EsAggregateRoot<TId>` option B under executable-test, behavior-contract, and upgrader-ownership conditions.

## Validation Strategy

- Parse all task JSON and validate workflow artifacts after every task status change.
- Run `validate-ai-context.py`, `validate-shell-assets.py`, and focused fail-closed tests for changed validators.
- Build and test only retained executable examples with real validation routes; use focused inline analyzer/validator inputs rather than a committed reference product.
- Scan exact-case links, target-specific names, Moq/NSubstitute projections, profile selectors, and soft-delete applicability.
- Run the repository quick gate and validate the full workflow commit range before closure.
- Require `ai-context-auditor` to create a new verification assessment; governance must not author its conclusions.

## Resume Checkpoint

- Last completed action: completed `GATE-002` and re-ran final candidate validation.
- Current task: `VERIFY-001`.
- Exact next action: obtain decisions for `VFY-005` and `VFY-006`, execute the selected dispositions, then repeat final full and commit-range validation.
- Validation already completed: quick gate passes 20/20; full gate passes all 20 required checks with one advisory from the stale transitional test helper; commit-range validation fails fourteen historical trailer violations plus the merged assessment commit's missing workflow sections.
- Git state: GATE-002 commit `a3a816d` is pushed and the worktree is clean before this resume-evidence update.
- Branch history and checkpoint handoffs: branch segment 1 starts from `codex/assessment/asm-20260715-002` because both unmerged assessment reports are required inputs.
- Blockers or unresolved decisions: `ASM-20260716-001#VFY-005` requires repair-versus-retire direction for transitional test helpers; the recommended low-maintenance disposition is to remove the automatic full-gate route and mark the helper `retirement-candidate` while retaining one release of packaged compatibility. `#VFY-006` requires a decision on already-pushed commit-history handling; the recommended strict disposition is a coordinated rewrite and force-push because a permanent validator exception would add governance debt. Full Observability design remains in backlog item `OBS-001` and outside the current verification scope.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | started | `443093bae351c8474beaaf08a553c32d3eb3c068` | local | `2026-07-16T07:22:13+08:00` | Preserve both assessment artifacts without merging or rewriting them. | Continue `PLAN-001`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `9853cb89797d99d782bafdc32b5d1fc66cc9a0e4` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T08:15:44+08:00` | User manually pushed the planning checkpoint for cross-machine review and authorized later workflow pushes. | Resume and push future coherent workflow checkpoints on the same branch. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `77e54de5ebe1e8ef4bf0adf362d987b5adf8661e` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T08:20:40+08:00` | Publish the confirmed decisions, `TRUTH-001` explanation, and reviewable BuildingBlocks/examples MVP plan. | Await user review before starting the first remediation slice. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `cbd467e82cff31e325719b28d07187c27824bb74` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T09:07:19+08:00` | Publish the documentation-first reconstruction contract, base-class minimization proposal, and repository-lineage provenance. | Await user review; do not start standards remediation. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `4b6ea2811c53eb892693c6e1b648a5965f4ffe24` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T21:12:11+08:00` | Publish the approved gate decisions, migration manifest prerequisite, and completed `AIC-004`/`AIC-012` first slice. | Continue with `RULE-001` on the same branch. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `9ae97035954d52e1ac1aa34dac05ccd2e60249ad` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T21:24:37+08:00` | Publish generic target technology selection, overridable NSubstitute default, and soft-delete profile-default/opt-out alignment. | Continue with `EXAMPLE-001` on the same branch. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `ba3af7fc74acad987a4d02b5cb2cb0fd61288255` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T21:39:12+08:00` | Publish machine-readable example evidence tiers, stale metadata retirement, and durable Observability backlog item `OBS-001`. | Continue with `BUILD-001` on the same branch. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | checkpoint-commit | `5926b26960ad41faeb3b331f06c2ef23699e9e1b` | local, pending push with checkpoint metadata | `2026-07-16T22:06:05+08:00` | Record interface-first BuildingBlocks truth, executable-tested optional ES mechanics, and BUILD-001 dispositions. | Commit checkpoint metadata, push both commits, then continue `TRUTH-002`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | checkpoint-commit | `1d683ea457c013e8be197eb0f9c1815c32d037c8` | local, pending push with checkpoint metadata | `2026-07-16T22:09:43+08:00` | Resolve AIC-010 by aligning Controller examples and delegated guidance to the async Use Case contract. | Commit checkpoint metadata, push both commits, then continue `EXAMPLE-002`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | checkpoint-commit | `16595ea257be5dc1af7d765a453472d6ed3bc87b` | local, pending push with checkpoint metadata | `2026-07-16T22:24:16+08:00` | Resolve placeholder and duplicate example routing without creating a reference product. | Commit checkpoint metadata, push both commits, then continue `ARCH-001`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | checkpoint-commit | `b68e82d518a22a9b0cda52a9e800013d8fdbd48c` | local, pending push with checkpoint metadata | `2026-07-16T22:28:33+08:00` | Record the shared micro-system/mono-system logical workload grammar. | Commit checkpoint metadata, push both commits, then continue `MIGRATE-001`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | checkpoint-commit | `68086ded0b24ffa59858b6027f461268e5200d87` | local, pending push with checkpoint metadata | `2026-07-16T22:38:59+08:00` | Record complete file dispositions, target-safe upgrader semantics, and the planned v0.4.0 migration/release contract. | Commit checkpoint metadata, push both commits, then continue `ROUTE-001`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | checkpoint-commit | `48619abe0640daa4417b4c6f6632a9ecf0212c73` | local, pending push with checkpoint metadata | `2026-07-16T22:52:49+08:00` | Normalize human-guide placement, retire replaced prompts, and separate README purpose from complete INDEX catalogs. | Commit checkpoint metadata, push both commits, then continue `VALIDATE-001`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | checkpoint-commit | `36fe0b9c6172ae474c2ca0c8c7e15119d8a3e2a7` | local, pending push with checkpoint metadata | `2026-07-16T23:02:25+08:00` | Make structural validation claims truthful and classify every shell asset without equating packaging with endorsement. | Commit checkpoint metadata, push both commits, then create the independent verification assessment. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | assessment-merge-push | `002d415` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T23:17:21+08:00` | Integrate independent verification `ASM-20260716-001` and expose release-blocking residuals. | Execute `PROFILE-002`, `DOC-002`, and `GATE-002`; preserve decision-required findings. |
