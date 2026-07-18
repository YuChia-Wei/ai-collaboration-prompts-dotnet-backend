# Post-v0.4.0 Version And Skill Taxonomy Roadmap

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-18-post-v0-4-roadmap-planning`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-18-post-v0-4-roadmap-planning`
- `base_branch`: `claude/assessment/asm-20260717-004`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-18-post-v0-4-roadmap-planning`
- `created_at`: `2026-07-18T14:19:06+08:00`
- `updated_at`: `2026-07-18T14:22:41+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: the supplemental `post-v0.4.0-improvement-plan.md` under durable predecessor assessment `ASM-20260717-004` proposes a fixed `v0.4.1 -> v0.4.2 -> v0.5.0` sequence, while the user also wants a decision on assessment-template ownership and a later skill-family reorganization.
- Authorized scope: evaluate and persist the release sequence, template ownership, skill-family horizon, compatibility boundaries, and decomposition into future bounded workflows.
- Exclusions: do not remediate assessment findings, edit the final assessment, rename skills, create release candidates, publish versions, retire published paths, or modify product code.
- Completion criteria: record evidence status; classify patch versus minor work; decide whether `v0.4.2` is mandatory; decide template ownership; place the skill taxonomy work on a version horizon; and define activation gates for follow-up workflows.

## Evidence And Freshness

- Current planning branch base: `claude/assessment/asm-20260717-004@2a31313ff2f3397fcb61af8b47f4e94de31f08f2`.
- Published baseline: `REL-v0.4.0` at `5af1db672928f9d51f55fee04183ad27b79fb9f8`.
- Durable planning input: `.dev/assessments/ASM-20260717-004/post-v0.4.0-improvement-plan.md`, committed before this workflow.
- Freshness limitation: `ASM-20260717-004/assessment.yaml` and `report.md` identify `82b88b7287deb7a64e0311fde6b1b53ea0d194b1`, not a post-v0.4.0 revision. Treat the supplemental plan as the roadmap predecessor and candidate intake rather than an authoritative post-v0.4.0 remediation baseline.
- Required execution gate: create a successor assessment pinned to the intended post-v0.4.0 `main` revision, or durably re-verify every selected finding before remediation begins.
- Codebase Memory MCP: a session index was created in moderate mode with 8,762 nodes and 8,914 edges. It excluded `.ai/assets`, `.claude`, and other material governance paths. A graph search found 41 files containing `repo-structure-sync`; direct inspection found 87 tracked files plus the local untracked planning input. The graph is an accelerator only under `AICTX-EVIDENCE-001`; its untracked persisted cache was removed after use rather than retained without the generated-inventory provenance contract.

## Decision Register

| Decision | Outcome | Rationale |
| --- | --- | --- |
| `ROADMAP-DEC-001` release sequence | Use `v0.4.1 -> v0.5.0`; keep `v0.4.2` conditional, not mandatory. | Governed release publication is expensive, and repository policy does not require two patches before a minor. Split by contract impact, not by content-versus-tooling labels. |
| `ROADMAP-DEC-002` patch boundary | `v0.4.1` contains only corrections that preserve published contracts and paths. | Wording, examples, metadata, dependency declaration, interpreter detection, and path defects qualify as patch work only when no new public rule, required route, schema, or removal is introduced. |
| `ROADMAP-DEC-003` minor boundary | `v0.5.0` owns new enforcement, policy, validator contracts, CI routes, and published-path retirement. | `AI-CONTEXT-VERSION-POLICY.md` classifies backward-compatible rule and validation additions as minor; pre-1.0 breaking changes also require a minor release with migration guidance. |
| `ROADMAP-DEC-004` assessment templates | Keep the shared locator repository-owned and skill report templates skill-owned. | The locator is consumed by both `ai-context-auditor` and `code-reviewer`; the auditor report template is already inside its skill. Moving the shared locator into the auditor would reverse the dependency and create duplicate ownership. |
| `ROADMAP-DEC-005` forced locator move | If ownership is deliberately redesigned, schedule it no earlier than `v0.5.0` and use a neutral owner plus legacy compatibility. | This would change policy, distribution, validator, provenance, and cross-skill contracts. Existing final assessment `template_source` values must remain valid. |
| `ROADMAP-DEC-006` skill taxonomy | Use `v0.6.0` for additive taxonomy and the `ai-context-init` transition; reserve `v0.7.0` for evidence-backed removal of old identifiers or broader breaking renames. | The family model is useful now, but runtime and external references need an alias/deprecation interval. Development skills should first be grouped by lifecycle role rather than renamed for cosmetic symmetry. |

## Release Train

### v0.4.1 — Correctness And Reproducibility Patch

Include only contract-preserving fixes:

- correct cross-runtime wrapper wording without adding a new required routing contract;
- align Handler / Use Case positive examples with existing canonical doctrine;
- remove bare time API use by applying an already-accepted abstraction without selecting a new universal contract;
- correct naming facts, stale status text, requirement outcomes, workflow index entries, and obsolete install paths;
- repair interpreter discovery, declare the existing Python/PyYAML requirements and Python floor, and correct the advisory script repository-root defect;
- mark obsolete auditor workflow templates as deprecated or historical, but do not remove their published paths.

Patch exclusion gate:

- no published path removal;
- no schema change;
- no new required validation or CI route;
- no intentional change to pass/fail semantics;
- no new universal technology decision.

### v0.4.2 — Conditional Portability Patch

Do not schedule by default. Create it only when all conditions hold:

1. `v0.5.0` is materially delayed;
2. a reproducibility defect could not safely land in `v0.4.1`;
3. the candidate contains no added validation route, published-path removal, schema change, or required-gate semantic change.

If these conditions do not arise, record `v0.4.2` as not needed rather than creating a release for numbering continuity.

### v0.5.0 — Governance Enforcement And Contract Institutionalization

Candidate scope:

- add semantic wrapper validation and its GWT contract;
- add governance validation CI for AI-context paths;
- formally retire or relocate obsolete published templates and scripts with file dispositions and migration guidance;
- decide runner redesign and SDK absence semantics;
- institutionalize the disposition manifest, full pre-minor audit baseline, filename convention, and release evidence rules;
- modernize spec-compliance contracts and target-relative layout guidance;
- clarify assessment locator/report ownership in metadata and validators;
- disposition `GOV-001`, `VAL-001`, `LANG-001`, `CAP-001`, and `TOOL-001` without requiring every valid deferral to be implemented;
- keep `OBS-001` in a separate `ddd-ca-hex-architect` workflow so an architecture design does not become an unrelated governance-release blocker.

### v0.6.0 — Skill Family Taxonomy And Compatibility Transition

Introduce a first-class registry taxonomy:

- `ai-context-lifecycle`: `ai-context-init`, `ai-context-auditor`, `ai-context-governance`, `ai-context-upgrader`;
- `development-orchestration`: `dev-workflow`;
- `development-definition`: `requirement-author`, `problem-frame-author`, `spec-author`, `bdd-gwt-test-designer`;
- `development-architecture`: `ddd-ca-hex-architect`;
- `development-execution`: `slice-implementer`, `local-change-implementer`;
- `development-assurance`: `code-reviewer`, `spec-compliance-validator`.

Transition `repo-structure-sync` to `ai-context-init` because its canonical purpose is initialization after framework copy. The transition must:

- define canonical alias/deprecation metadata before changing identifiers;
- do not assume runtimes support native aliases: model `repo-structure-sync` as one deprecated canonical compatibility entry with thin forwarding wrappers and a declared active replacement;
- update canonical registry, runtime wrappers, human guides, routing tables, distribution manifests, validators, tests, source provenance, and upgrader migration behavior;
- preserve historical workflow and assessment prose;
- publish a disposition manifest and migration guide;
- retain an explicit compatibility route for `$repo-structure-sync` during the transition.

New installations write `ai-context-init` into provenance and generated metadata. Existing `repo-structure-sync` values remain valid historical facts and must not be rewritten solely because of the rename.

Do not bulk-prefix or rename all development skills in `v0.6.0`. Their current action-role names are discoverable; grouping provides most of the coherence with far less migration risk.

### v0.7.0 — Conditional Legacy Identifier Retirement

Use this release only after `v0.6.0` compatibility evidence exists. Candidate work:

- remove the deprecated `repo-structure-sync` compatibility route if runtime behavior and downstream migration evidence are satisfactory;
- consider additional development-skill renames only where user intent, routing collisions, or ownership ambiguity provide evidence beyond visual consistency;
- otherwise leave the names stable and use `v0.7.0` for a different capability release.

## Assessment Template Ownership

The current two-layer model is intentional:

| Artifact | Canonical owner | Current path |
| --- | --- | --- |
| Assessment locator and lifecycle schema | repository assessment governance | `.dev/assessments/templates/assessment-locator-template.yaml` |
| AI context audit report format | `ai-context-auditor` | `.ai/assets/skills/ai-context-auditor/templates/ai-context-audit-report-template.md` |
| Code review assessment report format | `code-reviewer` | `.ai/assets/skills/code-reviewer/templates/code-review-assessment-report-template.md` |

No move is recommended. If discoverability is the concern, improve metadata and documentation without duplicating the locator. If the owner/path is intentionally changed in `v0.5.0`, keep the old locator as a frozen compatibility artifact, do not rewrite final assessment provenance, and allow validators to recognize declared legacy and current template source/version pairs.

## Follow-Up Workflow Map

| Order | Proposed workflow | Owner | Activation gate | Scope boundary |
| --- | --- | --- | --- | --- |
| 1 | `post-v0-4-baseline-verification` | `ai-context-auditor` | Select and pin the intended post-v0.4.0 `main` commit. | Read-only successor assessment; no remediation. |
| 2 | `v0-4-1-correctness-remediation` | `ai-context-governance` | Fresh baseline identifies the selected defects and patch-impact review passes. | Contract-preserving fixes only; independent verification required. |
| 3 | `v0-4-1-release-publication` | `ai-context-governance` | Remediation workflow closes and candidate/post-merge gates pass. | Release lifecycle only; user owns tag timing. |
| 4 | `v0-5-0-governance-enforcement` | `ai-context-governance` | Policy/template/CI decisions and SemVer impact are approved. | New governance contracts and migration; separate verification and publication. |
| 5 | `observability-architecture-standard` | `ddd-ca-hex-architect` | `OBS-001` is explicitly prioritized. | Independent architecture workflow; not a mandatory `v0.5.0` closeout gate. |
| 6 | `v0-6-0-skill-family-taxonomy` | `ai-context-governance` | `v0.5.0` governance contracts are stable and alias support is designed. | Taxonomy, `ai-context-init` transition, compatibility, migration, and verification. |
| 7 | `v0-7-0-legacy-skill-id-retirement` | `ai-context-governance` | Downstream evidence shows the deprecated identifier can be removed safely. | Conditional removal only; do not reserve the release if the gate is unmet. |

Each execution and publication workflow receives its own creation-date ID and dedicated branch when activated. The proposed names above are topics, not pre-created workflow identities.

## Durable Roadmap Contract

- Compact roadmap source: `.dev/backlog/items/AIC-ROADMAP-001.yaml`.
- Discovery entry: `.dev/backlog/INDEX.MD#active-release-roadmap`.
- The backlog item owns release horizons, release-level state, activation gates, and workflow handoffs.
- This workflow owns the evidence review, decision rationale, decomposition detail, and validation history.
- Future execution workflows own task progress, validation evidence, commits, and release publication state.
- Agents should read the backlog item first and open this plan only when they need the decision record.

## Validation And Release Gates

- Freshness: selected findings are pinned to the revision being remediated.
- SemVer: classify every candidate change as defect correction, added contract, removed contract, or migration-only evidence.
- Patch: no removals, schemas, new required routes, or intentional behavior changes.
- Environment: claim only platforms actually executed; Linux CI does not prove macOS.
- Compatibility: keep legacy template and skill identifiers resolvable for the declared transition.
- Verification: use `ai-context-auditor` for an independent successor assessment after remediation.
- Publication: planned -> validated -> `--no-ff` merge -> post-merge validation -> user-created annotated tag -> hosted publication -> registry finalization.

## Task Plan

| Task | Purpose | Status |
| --- | --- | --- |
| `ROADMAP-001` | Intake the durable assessment plan, establish evidence freshness, and classify SemVer boundaries. | `completed` |
| `ROADMAP-002` | Decide release sequencing and assessment-template ownership. | `completed` |
| `ROADMAP-003` | Define the skill-family horizon, compatibility strategy, and follow-up workflow map. | `completed` |
| `ROADMAP-004` | Persist the compact active roadmap in the backlog and repair assessment-to-workflow Git history and references. | `completed` |

## Resume Checkpoint

- Last completed action: committed ASM-20260717-004 first, rebased the planning workflow onto that durable predecessor, and promoted the compact active roadmap to backlog item `AIC-ROADMAP-001`.
- Current task: none; planning workflow completed.
- Exact next action: read `AIC-ROADMAP-001`, choose and pin the post-v0.4.0 baseline revision, then authorize a read-only successor assessment before creating the `v0.4.1` remediation workflow.
- Validation already completed: direct file-backed policy/template/reference inspection; version-impact comparison; three bounded sub-agent reviews with main-agent verification; Codebase Memory exclusion comparison; assessment artifact validation passed for 7 assessments; all four task JSON files parsed; workflow artifact validation passed for 19 post-adoption workflows, 39 indexed workflow directories, and 11 backlog items; AI-context validation passed; Git commit validation and diff checks passed.
- Git state: assessment predecessor commit `2a31313ff2f3397fcb61af8b47f4e94de31f08f2` is the base of the planning branch. The earlier local planning commit was unpushed and was safely rebased so durable history now records assessment before planning.
- Branch history and checkpoint handoffs: segment 1 created locally for this planning artifact; no merge, push, release, or tag action authorized.
- Blockers or unresolved decisions: release execution is gated on a fresh pinned baseline. The user may later override the recommended shared locator ownership, but that would activate a `v0.5.0` contract-migration decision.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-18-post-v0-4-roadmap-planning` | `claude/assessment/asm-20260717-004` | started-after-assessment | `2a31313ff2f3397fcb61af8b47f4e94de31f08f2` | local | `2026-07-18T14:19:06+08:00` | Reinitialize the unpushed planning workflow after committing its durable assessment predecessor. | Planning completed; read `AIC-ROADMAP-001` before activating the next workflow. |
