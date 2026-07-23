# v0.6.0 Product, Distribution, And Lifecycle Contract Planning

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-23-v0-6-product-contract-planning`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-23-v0-6-product-contract-planning`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation-planning`
- `artifact_root`: `.dev/workflows/2026-07-23-v0-6-product-contract-planning`
- `created_at`: `2026-07-23T22:52:32+08:00`
- `updated_at`: `2026-07-23T22:55:14+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: The repository has mature release and self-governance
  machinery, but v0.6.0 needs an explicit product contract that identifies what
  a downstream user receives, preserves software-delivery workflow capability
  as a primary value, makes backlog tracking optional, and gives customized AI
  context a governed upgrade lifecycle.
- Authorized remediation scope: Preserve the current planning decisions,
  establish the `DIST-001` deliberation frame, and record additional owner
  decisions required before backlog activation or implementation.
- Exclusions:
  - Do not create or assign proposed backlog items before owner approval.
  - Do not change the package profile, provenance schema, canonical skill IDs,
    runtime wrappers, CI workflows, or v0.6.0 roadmap in this planning checkpoint.
  - Do not treat proposed identifiers `DIST-001`, `CUST-001`, or `DEVWF-002` as
    allocated backlog IDs until corresponding items are approved and created.
- Completion criteria:
  - Product layers and distribution boundaries are explicitly approved.
  - The owner decides the target customization record boundary.
  - The owner decides whether the software-delivery end-to-end gate is a new
    backlog item and whether `dev-workflow` enters rename deliberation.
  - Approved decisions are normalized into backlog and roadmap artifacts with
    validation evidence.

## Confirmed Owner Decisions

1. `CI-001` and `CI-002` belong to one release-engineering workstream because
   both affect how the repository builds and publishes a release.
2. `CFG-001` and `SKILL-001` may be planned together because configuration
   ownership, tracked-file behavior, package projection, and skill taxonomy
   need one coherent downstream boundary.
3. `EVAL-001` begins with deterministic fixtures and oracles before any
   budgeted model-in-the-loop release evaluation.
4. Repository backlog storage is an optional work-tracking provider. A target
   may instead use Azure DevOps, Jira, GitHub Issues, GitHub Projects, or another
   system.
5. `.dev/workflows/` remains a core downstream capability. It records the
   execution plan, decisions, stage handoffs, validation, and closure evidence
   for software development; it is not a replacement issue tracker.
6. The core product must retain the software-delivery lifecycle: requirements,
   specifications, problem framing, DDD and architecture design, test design,
   implementation, review, compliance validation, and workflow closeout.
7. Target-facing `ai-context-governance` and `ai-context-auditor` remain core
   lifecycle capabilities. They must support governed customized context so
   upgrades do not rediscover or overwrite target intent.
8. `SIMPL-001` remains measurement and disposition work. It must not remove
   software-delivery or customization-safety capabilities merely because recent
   source-repository activity emphasized self-governance.

## Proposed Product Layers For DIST-001 Deliberation

| Layer | Candidate contents | Current disposition |
| --- | --- | --- |
| Core: software delivery | `dev-workflow`, requirement/spec/problem-frame/architecture/test-design/implementation/review/compliance skills, `.dev/workflows/` governance and target workflow artifacts | Direction agreed; exact package acceptance gate remains open |
| Core: AI context lifecycle | initialization, auditor, target-facing governance, upgrader, provenance, customization reconciliation, post-upgrade verification | Direction agreed; customization record schema remains open |
| Optional providers | repository backlog, GitHub Issues/Projects, Azure DevOps, Jira, and future tracker adapters | Repository backlog confirmed optional; provider contract remains open |
| Source-only operations | package builders, publication/finalization tooling, source release registry, source workflow/assessment/backlog instances, release CI fixtures | Direction agreed; exact projection inventory remains open |

`DIST-001` is a proposed backlog identity for the product and distribution
contract. It should define capability composition and package acceptance before
CI enforces the resulting matrix or `SIMPL-001` measures what can be reduced.

## Software-Delivery Product Evidence

The current framework still declares deterministic capability routing for:

- workflow orchestration;
- requirements;
- specification;
- problem framing;
- DDD, Clean Architecture, CQRS, and hexagonal architecture;
- GWT test design;
- bounded and local implementation;
- code review;
- compliance validation.

The observed gap is not missing skill inventory. The release contract lacks a
downstream end-to-end acceptance fixture that proves a target can move from a
requirement through architecture/specification, implementation, validation, and
workflow closeout. `DEVWF-001` owns optional issue linkage and richer lifecycle
timestamps and does not cover this product-level acceptance gap.

Proposed decision: create a separately scoped product gate, provisionally
called `DEVWF-002`, or explicitly add the same acceptance contract to an
owner-approved existing item without overloading `DEVWF-001`.

## Customized AI Context Contract

The current `.dev/AI-CONTEXT-SOURCE.yaml` contract records installed source
identity, upgrade history, `local_overrides`, and unresolved reconciliation.
Its validated override fields are currently path-oriented: stable ID, paths,
reason, owner, and disposition.

That protects changed bytes but does not fully describe capability semantics.
The v0.6.0 design should decide how to record:

- stable customization identity;
- affected capability, rule, or contract identity;
- affected paths;
- base framework version and evidence;
- whether the target extends, replaces, deviates from, or adds target-only
  behavior;
- owner, reason, dependencies, and requirement/ADR/workflow evidence;
- whether an incoming official capability is absent, partially equivalent,
  equivalent, or conflicting;
- retain, merge, supersede, retire, or unresolved disposition;
- reconciliation and validation evidence.

Recommended lifecycle under deliberation:

1. Governance records an authorized customization.
2. Auditor verifies that the record matches the target's actual active context.
3. Upgrader performs Base/Incoming/Target path comparison plus capability-level
   equivalence analysis.
4. Governance records the accepted reconciliation.
5. Auditor performs independent post-upgrade verification.
6. Upgrader updates provenance only after target validation succeeds.

Recommended storage direction under deliberation:

- Keep `.dev/AI-CONTEXT-SOURCE.yaml` as the compact installation and provenance
  locator.
- Store scalable semantic customization records in a target-owned ledger
  referenced by the provenance manifest.
- Use workflow and assessment artifacts as decision and verification evidence,
  not as the current customization source of truth.

## Why AI-CONTEXT-SOURCE.yaml Is Currently Under .dev

The current folder boundary is ownership-based:

- `.ai/` contains reusable, framework-managed AI assets and runtime context that
  a package may update.
- `.dev/` contains target-repository project truth, governance state, decisions,
  requirements, specifications, workflow records, and other target-owned
  knowledge.

`AI-CONTEXT-SOURCE.yaml` describes one target installation: its installed
framework commit, timestamps, previous source, local overrides, unresolved
reconciliation, and last validated migration. Those facts do not belong to the
source framework and must survive replacement of framework-managed `.ai/`
content. Its current `.dev/` location therefore protects the ownership
boundary, even though agents are its primary reader.

Open compatibility decision: v0.6.0 may keep the published root path, or
introduce a grouped `.dev/ai-context/` target-owned area through an explicit
migration. Moving the file merely because its name contains `AI-CONTEXT` is not
sufficient reason to break the published path.

## dev-workflow Naming Deliberation

The concern is valid: `dev-workflow` is generic and may be confused with native
workflow systems, runtime workflow features, or provider keywords.

Current candidate direction:

- Prefer a name based on responsibility rather than storage mechanism.
- Leading candidate: `software-delivery-orchestrator`.
- Other candidates: `development-lifecycle-orchestrator`,
  `software-delivery-coordinator`.
- Avoid another name whose primary distinguishing word is `workflow`.

If a rename is approved:

- retain `dev-workflow` as a thin deprecated compatibility entry for at least
  one published compatibility window;
- preserve historical `owner_skill`, workflow, assessment, and release
  provenance;
- change canonical identifiers, wrappers, capability profile, routing,
  documentation, package inventory, validators, and migration metadata
  together;
- require `EVAL-001` deterministic routing and representative development
  scenarios before activation;
- do not silently fold removal of the old identifier into v0.6.0.

Open decision: deliberate this rename within the taxonomy scope of `SKILL-001`,
create a separate low-priority backlog item, or record it as deferred naming
input only.

## Proposed v0.6.0 Sequencing

1. Approve the `DIST-001` product layers, package composition, and provider
   model.
2. Approve the customization ledger and four-skill lifecycle contract; keep
   `UPG-001` as a real legacy-target acceptance case rather than the sole owner
   of the cross-lifecycle schema.
3. Establish a software-delivery end-to-end product gate separate from the
   optional metadata work in `DEVWF-001`.
4. Implement `EVAL-001` deterministic fixtures for both software-delivery and
   AI-context lifecycle scenarios.
5. Execute `CFG-001` and `SKILL-001` as one coordinated package/taxonomy
   workstream after their activation decisions pass.
6. Execute `CI-001` and `CI-002` as one release-engineering workstream. Review
   may begin earlier, but the final CI matrix must enforce the approved product
   and package composition.
7. Measure and disposition `SIMPL-001` without broad historical deletion or
   reduction of either core product pillar.
8. Build and validate the v0.6.0 candidate only after all release blockers and
   accepted provider/profile gates are explicit.

## Decisions Required From The Owner

| ID | Decision | Recommendation | Why it matters |
| --- | --- | --- | --- |
| D-001 | Approve `DIST-001` as a new backlog item and v0.6.0 release-definition gate | Approve | CI and simplification need a defined product surface |
| D-002 | Choose package composition: one package with selectable capabilities, multiple profiles, or core plus optional add-ons | Discuss before selection | Determines manifests, install/upgrade behavior, and CI matrix |
| D-003 | Keep `.dev/AI-CONTEXT-SOURCE.yaml` at its published path or migrate to a grouped target-owned area | Keep for v0.6.0 unless grouping produces a concrete benefit | Avoids path churn while preserving target ownership |
| D-004 | Approve a separate semantic customization ledger referenced by provenance | Approve | Path-only overrides cannot express capability equivalence |
| D-005 | Create `DEVWF-002` for software-delivery end-to-end acceptance | Approve | `DEVWF-001` has a different optional-metadata scope |
| D-006 | Route `dev-workflow` rename through `SKILL-001`, a new low-priority item, or defer it | Prefer a separate low-priority item linked to `SKILL-001` | Avoids expanding taxonomy implementation without explicit priority |
| D-007 | Choose the replacement skill name if rename deliberation is activated | Start from `software-delivery-orchestrator` | It describes responsibility and avoids the generic workflow keyword |

## Artifact Contract

- Baseline assessment: not required for the planning checkpoint
- Remediation report: not created until implementation or roadmap normalization
  is authorized
- Verification assessment: not required for the planning checkpoint
- Tasks: `.dev/workflows/2026-07-23-v0-6-product-contract-planning/tasks/`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| Product composition is implicit in one broad package profile | high | repository owner + governance | decision-required | `V060PLAN-001` | owner-approved product layer and package matrix |
| Customized context is protected by paths but lacks a semantic capability ledger | high | governance + auditor + upgrader | decision-required | `V060PLAN-001` | owner-approved schema and lifecycle |
| Software-delivery skills exist but lack a downstream end-to-end release gate | high | dev-workflow + governance | decision-required | `V060PLAN-001` | owner-approved acceptance scenario |
| `dev-workflow` may collide conceptually with native workflow terminology | low | governance | deliberate or defer | `V060PLAN-001` | explicit owner disposition |

## Stages And Checkpoints

1. Preserve current owner decisions and current-state evidence.
2. Deliberate `DIST-001` product layers and package composition.
3. Deliberate provenance/customization storage and lifecycle.
4. Deliberate software-delivery acceptance and skill naming.
5. Create only the owner-approved backlog and roadmap changes.
6. Validate workflow, backlog, package, and AI-context contracts before closure.

## Resume Checkpoint

- Last completed action: Preserved the current v0.6.0 product contract planning,
  confirmed owner decisions, proposed roadmap sequence, and open decisions.
- Current task: `V060PLAN-001`
- Exact next action: Discuss `D-001` and `D-002`, beginning with the detailed
  `DIST-001` product and package composition boundary.
- Validation already completed: Git preflight confirmed clean synchronized
  `main` at `97bcf2f8c657a9af3af7512453c6cac686a9ffab` before branch creation.
- Git state: the validated workflow bootstrap is committed on
  `codex/2026-07-23-v0-6-product-contract-planning`; no push or merge has been
  requested.
- Branch history and checkpoint handoffs: none.
- Blockers or unresolved decisions: `D-001` through `D-007`.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-23-v0-6-product-contract-planning` | `main@97bcf2f` | active bootstrap | current branch bootstrap commit | local | `2026-07-23T22:55:14+08:00` | Preserve planning before further deliberation | Continue `V060PLAN-001` on this branch |
