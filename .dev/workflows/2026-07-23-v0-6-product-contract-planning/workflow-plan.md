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
- `updated_at`: `2026-07-23T23:38:18+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: The repository has mature release and self-governance
  machinery, but v0.6.0 needs an explicit product contract that identifies what
  a downstream user receives, preserves software-development workflow capability
  as a primary value, makes backlog tracking optional, and gives customized AI
  context a governed upgrade lifecycle.
- Authorized remediation scope: Preserve the current planning decisions,
  create and schedule the approved `DIST-001` release-definition gate, normalize
  approved v0.6.0 workstream pairings, and record additional owner decisions
  required before implementation.
- Exclusions:
  - Do not create or assign additional proposed backlog items before owner approval.
  - Do not change the package profile, provenance schema, canonical skill IDs,
    runtime wrappers, CI workflows, or v0.6.0 roadmap in this planning checkpoint.
  - Do not treat proposed identifiers `CUST-001` or `DEVWF-002` as allocated
    backlog IDs until their detailed scopes are approved and created.
- Completion criteria:
  - Product layers and distribution boundaries are explicitly approved.
  - The owner decides the target customization record boundary.
  - The owner decides whether the software-development end-to-end gate is a new
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
6. The core product must retain the software-development lifecycle: requirements,
   specifications, problem framing, DDD and architecture design, test design,
   implementation, review, compliance validation, and workflow closeout.
7. Target-facing `ai-context-governance` and `ai-context-auditor` remain core
   lifecycle capabilities. They must support governed customized context so
   upgrades do not rediscover or overwrite target intent.
8. `SIMPL-001` remains measurement and disposition work. It must not remove
   software-development or customization-safety capabilities merely because recent
   source-repository activity emphasized self-governance.
9. `DIST-001` is an allocated v0.6.0 release blocker and release-definition
   gate.
10. Target provenance moves from `.dev/AI-CONTEXT-SOURCE.yaml` into the
    `.dev/ai-context/` target-owned area in v0.6.0; the exact destination
    filename remains an owner decision.
11. The `dev-workflow` transition executes in `SKILL-001` together with
    `repo-structure-sync` to `ai-context-init`, sharing one compatibility and
    validation campaign while retaining separate lifecycle responsibilities.
12. Package-registry or installable CLI distribution is a future exploration,
    not a v0.6.0 release blocker.
13. The provenance destination is `.dev/ai-context/provenance.yaml`.
14. `dev-workflow` transitions to `software-development-orchestrator`.
15. `DIST-001` uses one versioned componentized release. New installations
    default the repository-backlog provider off; existing targets preserve it
    and record the selection.
16. A future software-delivery capability remains separate from the current
    software-development orchestrator and requires evidence from real
    development, PR, runbook, maintenance-window, deployment-approval,
    production-verification, and rollback usage.

## Approved Product Layers And Remaining DIST-001 Deliberation

| Layer | Candidate contents | Current disposition |
| --- | --- | --- |
| Core: software development | `dev-workflow`, requirement/spec/problem-frame/architecture/test-design/implementation/review/compliance skills, `.dev/workflows/` governance and target workflow artifacts | Direction agreed; exact package acceptance gate remains open |
| Core: AI context lifecycle | initialization, auditor, target-facing governance, upgrader, provenance, customization reconciliation, post-upgrade verification | Direction agreed; customization record schema remains open |
| Optional providers | repository backlog, GitHub Issues/Projects, Azure DevOps, Jira, and future tracker adapters | Repository backlog confirmed optional; provider contract remains open |
| Source-only operations | package builders, publication/finalization tooling, source release registry, source workflow/assessment/backlog instances, release CI fixtures | Direction agreed; exact projection inventory remains open |

`DIST-001` is now the allocated v0.6.0 product and distribution contract. It
defines capability composition and package acceptance before CI enforces the
resulting matrix or `SIMPL-001` measures what can be reduced.

## Software-Development Product Evidence

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

Approved storage direction with one remaining naming decision:

- Move the compact installation and provenance locator from
  `.dev/AI-CONTEXT-SOURCE.yaml` into `.dev/ai-context/` in v0.6.0.
- Store scalable semantic customization records in a target-owned ledger
  beside and referenced by the provenance manifest.
- Use workflow and assessment artifacts as decision and verification evidence,
  not as the current customization source of truth.
- Use `.dev/ai-context/provenance.yaml` as the single authoritative destination.

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

Owner decision: v0.6.0 introduces
`.dev/ai-context/provenance.yaml` through an explicit migration. Low current
adoption makes the one-time path transition materially cheaper than leaving a
permanent organization debt. The migration must preserve target data, support
exact v0.5.0 input, update all readers and validators atomically, and leave only
one authoritative manifest.

## dev-workflow Naming Deliberation

The concern is valid: `dev-workflow` is generic and may be confused with native
workflow systems, runtime workflow features, or provider keywords.

The original `software-delivery-orchestrator` suggestion used "delivery"
because the skill coordinates an outcome across requirements, design,
implementation, validation, and closeout rather than only writing code.
However, the current skill does not own deployment or release publication, so
"delivery" may overstate its boundary and collide with release engineering.

Approved direction:

- Prefer a name based on responsibility rather than storage mechanism.
- Active v0.6.0 name: `software-development-orchestrator`.
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

Owner decision: perform the `dev-workflow` to
`software-development-orchestrator` rename inside the `SKILL-001` taxonomy and
compatibility workstream together with `repo-structure-sync` to
`ai-context-init`.

## Software Development And Future Delivery Boundary

`software-development-orchestrator` owns the deliberative software-development
lifecycle. Requirements, architecture, design, and specifications may remain
in long-running discussion and approval states before implementation tasks are
created. The orchestrator must not assume a request authorizes uninterrupted
execution from idea through deployment.

Its current terminal boundary is an approved development closeout or PR-ready
handoff. Whether it should later author a PR description or create a PR remains
an evidence-driven extension decision.

Potential supporting capabilities have different ownership:

- a user-story writer belongs to requirement or optional work-tracking
  authoring rather than production delivery;
- a PR-description writer may be a development-closeout specialist;
- GitHub or on-premises Azure DevOps PR creation is a provider adapter with an
  explicit external-mutation approval boundary;
- runbooks, maintenance windows, deployment approval, production verification,
  and rollback belong to a future software-delivery lifecycle.

If repeated target usage proves the need, a future
`software-delivery-orchestrator` may begin from an approved development
handoff and coordinate those operational stages. It is not created or assigned
to v0.6.0 by this plan.

## Future Package-Registry Distribution Wish

The repository may later expose a CLI that installs, initializes, plans,
upgrades, and validates the AI-context package through a package manager.
Current implementation affinity favors a Python CLI because package planning,
application, and validators are already Python-based.

Potential future sequence:

1. Stabilize the v0.6.0 component, provenance, and migration contracts.
2. Extract a Python CLI with commands such as `init`, `plan`, `apply`,
   `upgrade`, and `validate`.
3. Support source or PyPI installation through `uv tool install` and ephemeral
   execution through `uvx`.
4. Evaluate npm or a .NET global tool only as wrappers or ecosystem-specific
   entry points after the canonical CLI contract is stable.

This remains a recorded wish. It has no allocated backlog ID, release target,
or v0.6.0 acceptance requirement.

## Proposed v0.6.0 Sequencing

1. Complete the remaining `DIST-001` package composition, default selection,
   installed-component provenance, and validation-matrix decisions.
2. Approve the customization ledger and four-skill lifecycle contract; keep
   `UPG-001` as a real legacy-target acceptance case rather than the sole owner
   of the cross-lifecycle schema.
3. Establish a software-development end-to-end product gate separate from the
   optional metadata work in `DEVWF-001`.
4. Implement `EVAL-001` deterministic fixtures for both software-development and
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
| D-001 | Approve `DIST-001` as a new backlog item and v0.6.0 release-definition gate | Approved and normalized | CI and simplification need a defined product surface |
| D-002 | Choose package composition: one package with selectable capabilities, multiple profiles, or core plus optional add-ons | Approved: one versioned componentized release; repo backlog off by default for new installs and preserved for existing targets | Determines manifests, install/upgrade behavior, and CI matrix |
| D-003 | Keep `.dev/AI-CONTEXT-SOURCE.yaml` at its published path or migrate to a grouped target-owned area | Approved: migrate to `.dev/ai-context/provenance.yaml` | Accept one low-adoption migration now instead of permanent organization debt |
| D-004 | Approve a separate semantic customization ledger referenced by provenance | Approve | Path-only overrides cannot express capability equivalence |
| D-005 | Create `DEVWF-002` for software-development end-to-end acceptance | Approve | `DEVWF-001` has a different optional-metadata scope |
| D-006 | Route `dev-workflow` rename through `SKILL-001`, a new low-priority item, or defer it | Approved: execute in `SKILL-001` with the init rename | One compatibility campaign lowers downstream transition overhead |
| D-007 | Choose the replacement skill name | Approved: `software-development-orchestrator` | It keeps the development boundary and avoids generic workflow terminology |
| D-008 | Allocate package-registry CLI distribution to a release | Deferred wish only | Stabilize component and migration contracts before choosing PyPI, npm, or NuGet distribution |
| D-009 | Extend development closeout into PR authoring/creation or create a delivery orchestrator | Defer pending real team usage | External mutation and operational delivery require distinct approval evidence |

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
4. Deliberate software-development acceptance and skill naming.
5. Create only the owner-approved backlog and roadmap changes.
6. Validate workflow, backlog, package, and AI-context contracts before closure.

## Resume Checkpoint

- Last completed action: Approved the `DIST-001` component model,
  `.dev/ai-context/provenance.yaml`, and
  `software-development-orchestrator`, and recorded the future
  development-to-delivery boundary.
- Current task: `V060PLAN-001`
- Exact next action: Deliberate the semantic customization ledger (`D-004`) and
  software-development end-to-end acceptance gate (`D-005`) before allocating
  their detailed backlog items.
- Validation already completed: Git preflight confirmed clean synchronized
  `main` at `97bcf2f8c657a9af3af7512453c6cac686a9ffab` before branch creation.
- Git state: the validated workflow bootstrap is committed on
  `codex/2026-07-23-v0-6-product-contract-planning`; no push or merge has been
  requested.
- Branch history and checkpoint handoffs: none.
- Blockers or unresolved decisions: detailed allocation for `D-004` and
  `D-005`; `D-008` and `D-009` remain explicitly deferred.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-23-v0-6-product-contract-planning` | `main@97bcf2f` | active bootstrap | current branch bootstrap commit | local | `2026-07-23T22:55:14+08:00` | Preserve planning before further deliberation | Continue `V060PLAN-001` on this branch |
