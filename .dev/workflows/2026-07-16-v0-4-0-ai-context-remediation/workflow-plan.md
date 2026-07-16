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
- `current_phase`: `remediation-planning`
- `artifact_root`: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation`
- `created_at`: `2026-07-16T07:22:13+08:00`
- `updated_at`: `2026-07-16T08:20:40+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: v0.4.0 needs one coherent .NET backend context that separates invariants, defaults, target choices, examples, and historical Java/EzDDD provenance while supporting both multi-BC micro-system mono repos and mono-system repositories.
- Authorized remediation scope: plan and later remediate findings from `ASM-20260715-002`; use `ASM-20260715-001` only as superseded comparison evidence; incorporate the user's confirmed NSubstitute direction and the read-only `dotnet-webapi-lab` architecture observations; coordinate standards, examples, routing, validators, BuildingBlocks reference realization, and independent verification.
- Current authorization boundary: workflow and task planning plus a reviewable MVP/change plan. Do not execute standards remediation or create the fixture implementation until the user reviews the MVP plan.
- Exclusions: product code remediation in either lab; publishing packages; creating NuGet packages or a distributable `dotnet new` template; moving tags; GitHub Release work; remote branch deletion; merge without explicit authorization. Pushes of this active workflow branch are authorized for cross-machine review.
- Completion criteria: all 14 authoritative findings and supplemental architecture decisions have explicit outcomes; selected standards and projections agree; examples have declared verification tiers; BuildingBlocks reconstruction has executable proof or a recorded deferral; validators describe and enforce their real scope; an independent successor assessment verifies the result; commits and closure evidence pass policy.

## Artifact Contract

- Historical assessment: `.dev/assessments/ASM-20260715-001/assessment.yaml`
- Authoritative baseline: `.dev/assessments/ASM-20260715-002/assessment.yaml`
- Remediation report: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation/reports/remediation-report.md`
- Verification assessment: `.dev/assessments/<future-assessment-id>/assessment.yaml`
- Tasks: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation/tasks/`
- BuildingBlocks/examples MVP plan: `.dev/workflows/2026-07-16-v0-4-0-ai-context-remediation/plans/building-blocks-examples-mvp.md`

## Decision Register

| Decision | State | Current direction | Evidence / consequence |
| --- | --- | --- | --- |
| `V040-DEC-001` Mocking framework | confirmed by user | NSubstitute is the framework profile default and is mandatory within that profile. A target may replace it through one explicit technology-selection override instead of editing scattered rules. | Create one target-owned selection slot and make derived testing guidance consume it; GWT remains invariant. |
| `V040-DEC-002` Deletion semantics | confirmed by user | Soft deletion is standard Aggregate Repository behavior: the Aggregate changes deletion state and `SaveAsync` persists it. Physical deletion is a separately authorized command/use case and restricted repository/capability. | Make soft delete the default Aggregate Repository profile and keep purge explicit for legal/privacy/retention needs. |
| `V040-DEC-003` Repository profiles | proposed | Use one logical solution-folder grammar: shared foundations plus `<workload>/DomainCore` and `<workload>/Presentation`; workload means BC for micro-system and system for mono-system | Extend the conditional project-structure profile without forcing identical physical layouts. |
| `V040-DEC-004` Observability | proposed | Treat attribute/AOP observability as runtime CrossCutting infrastructure, separate from build-time Tooling and prohibited from Domain dependencies by default | Add a bounded canonical standard/reference and validation strategy. |
| `V040-DEC-005` BuildingBlocks realization | confirmed by user | BuildingBlocks owns contracts/interfaces and no product persistence, broker, or other concrete adapter implementation. Product Infrastructure implements the outbound ports. | The MVP fixture proves the contracts with a separate sample product implementation; no implementation is placed in BuildingBlocks. |
| `V040-DEC-006` Examples contract | confirmed by user | Executable examples require tests. Documentation-only illustrative/reference examples do not require tests but must not claim executable verification. | Start with a minimal tested MVP and defer full portfolio conversion until review. |

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `ASM-20260715-002#AIC-001` | HIGH | governance + architecture | rewrite profile truth | `RULE-001` | relationship checks and profile fixture |
| `#AIC-002` | HIGH | governance + architecture | make soft delete standard Aggregate Repository behavior; keep purge explicit | `RULE-001` | ownership/projection parity |
| `#AIC-003` | HIGH | governance | define verification tiers; replace stale sync claims | `EXAMPLE-001` | fixture/tier validator |
| `#AIC-004` | HIGH | governance + validator owner | replace removed command route | `TRUTH-001` | command existence and analyzer route |
| `#AIC-005` | HIGH | architecture + governance | extract portable concepts; replace placeholders with executable proof or archive | `BUILD-001` | compile/tests/concept matrix |
| `#AIC-006` | MEDIUM | governance | consolidate catalogs and shared fixtures while preserving deliberate test modes | `EXAMPLE-001` | duplicate and link scan |
| `#AIC-007` | MEDIUM | governance | move/re-route by audience and ownership | `ROUTE-001` | context and link validators |
| `#AIC-008` | MEDIUM | validator owner | state structural scope and add selected relationship checks | `VALIDATE-001` | fail-closed tests |
| `#AIC-009` | MEDIUM | governance + validator owner | split shell lifecycle taxonomy | `VALIDATE-001` | registry/runner parity |
| `#AIC-010` | MEDIUM | architecture | replace synchronous controller example | `TRUTH-001` | compile-tested async slice |
| `#AIC-011` | LOW | governance | link, archive, or remove after comparison | `ROUTE-001` | inbound route inventory |
| `#AIC-012` | MEDIUM | governance | remove target-specific namespace from canonical guidance | `TRUTH-001` | literal target-name scan |
| `#AIC-013` | HIGH | governance + testing | define NSubstitute profile default with one explicit target override slot | `RULE-001` | package/rule/projection scans |
| `#AIC-014` | MEDIUM | architecture + governance | add minimal verified multi-BC/system reference or narrow portfolio claim | `BUILD-001`, `ARCH-001` | reference fixture and profile checks |

## Task Plan

| Task | Purpose | Status | Depends on |
| --- | --- | --- | --- |
| `PLAN-001` | Freeze user decisions, evidence boundaries, finding mapping, and execution order. | `in_progress` | none |
| `RULE-001` | Align profile, soft-delete, and NSubstitute ownership and projections. | `pending` | `PLAN-001` |
| `TRUTH-001` | Repair broken validator routing, async controller example, and target namespace leakage. | `pending` | `RULE-001` |
| `EXAMPLE-001` | Define example verification tiers and consolidate duplicate discovery/fixtures. | `pending` | `PLAN-001` |
| `BUILD-001` | Produce the EzDDD-to-BuildingBlocks concept matrix and compile-tested reference fixture plan/implementation. | `pending` | `RULE-001`, `EXAMPLE-001` |
| `ARCH-001` | Extend repository profiles for micro-system/mono-system parity and add CrossCutting Observability boundaries. | `pending` | `PLAN-001`, `RULE-001` |
| `ROUTE-001` | Correct audience placement and weak routing; archive only after replacement evidence. | `pending` | `EXAMPLE-001`, `ARCH-001` |
| `VALIDATE-001` | Correct validator claims and shell lifecycle taxonomy; add required fail-closed coverage. | `pending` | `TRUTH-001`, `BUILD-001`, `ROUTE-001` |
| `VERIFY-001` | Run independent verification assessment, reconcile all findings, and close or defer explicitly. | `pending` | all remediation tasks |

## Stages And Checkpoints

1. Decision confirmation and evidence freeze.
2. Canonical ownership and active truth repair.
3. Example contract, BuildingBlocks reference, and repository-profile work.
4. Placement, routing, validator, and script-lifecycle remediation.
5. Independent verification assessment.
6. Finding reconciliation, commit verification, and workflow closure.

## Task Detail: TRUTH-001

`TRUTH-001` groups three bounded active-truth defects that can mislead direct agent execution without requiring a broad policy redesign:

1. `AIC-004`: the active spec-compliance skill still routes to removed `check-repository-compliance.sh`; replace it with the current analyzer/tool contract and test command existence.
2. `AIC-010`: the controller example still calls a synchronous Java-shaped `Execute`; rewrite it to the current async Use Case port and include it in the executable MVP or downgrade it from executable guidance.
3. `AIC-012`: broad canonical guidance contains `Lab.MessageSchemas.<Domain>`; replace it with the portable canonical namespace placeholder or a link to the canonical project-structure owner.

The task deliberately excludes profile ownership, example portfolio consolidation, and analyzer redesign. Its success criterion is that every active command/path/example it touches can be followed literally without reaching a missing command, obsolete synchronous contract, or target-specific namespace.

## BuildingBlocks And Examples MVP

The reviewable MVP is defined in [the dedicated MVP plan](plans/building-blocks-examples-mvp.md). It keeps BuildingBlocks contract-only, puts concrete adapters in a sample product Infrastructure project, and tests only executable artifacts. No fixture code is authorized until the user approves that plan.

## Validation Strategy

- Parse all task JSON and validate workflow artifacts after every task status change.
- Run `validate-ai-context.py`, `validate-shell-assets.py`, and focused fail-closed tests for changed validators.
- Compile and test any BuildingBlocks/reference fixture; do not label it verified otherwise.
- Scan exact-case links, target-specific names, Moq/NSubstitute projections, profile selectors, and soft-delete applicability.
- Run the repository quick gate and validate the full workflow commit range before closure.
- Require `ai-context-auditor` to create a new verification assessment; governance must not author its conclusions.

## Resume Checkpoint

- Last completed action: created the workflow branch and drafted the remediation plan from both assessments and supplemental cross-repository evidence.
- Current task: `PLAN-001`.
- Exact next action: user reviews the BuildingBlocks/examples MVP plan and `TRUTH-001` explanation, then authorizes or adjusts the first remediation slice.
- Validation already completed: 9 task JSON files parse; workflow validator passes for 17 post-adoption workflows and 37 indexed workflow directories; assessment and AI-context validators pass; `git diff --check` passes.
- Git state: active workflow branch tracks origin at planning checkpoint `77e54de`; the checkpoint is available for cross-machine review.
- Branch history and checkpoint handoffs: branch segment 1 starts from `codex/assessment/asm-20260715-002` because both unmerged assessment reports are required inputs.
- Blockers or unresolved decisions: MVP plan review; final approval of the first remediation slice. Repository-profile and Observability proposals remain reviewable rather than final.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | started | `443093bae351c8474beaaf08a553c32d3eb3c068` | local | `2026-07-16T07:22:13+08:00` | Preserve both assessment artifacts without merging or rewriting them. | Continue `PLAN-001`. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `9853cb89797d99d782bafdc32b5d1fc66cc9a0e4` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T08:15:44+08:00` | User manually pushed the planning checkpoint for cross-machine review and authorized later workflow pushes. | Resume and push future coherent workflow checkpoints on the same branch. |
| 1 | `codex/2026-07-16-v0-4-0-ai-context-remediation` | `codex/assessment/asm-20260715-002` | push | `77e54de5ebe1e8ef4bf0adf362d987b5adf8661e` | `origin/codex/2026-07-16-v0-4-0-ai-context-remediation` | `2026-07-16T08:20:40+08:00` | Publish the confirmed decisions, `TRUTH-001` explanation, and reviewable BuildingBlocks/examples MVP plan. | Await user review before starting the first remediation slice. |
