# AI Context Remediation Report

## Report Metadata

- `report_id`: `remediation-report-2026-07-10-ai-context-self-audit`
- `workflow_id`: `2026-07-10-ai-context-self-audit`
- `owner_skill`: `ai-context-governance`
- `status`: `draft`
- `created_at`: `2026-07-11T08:18:07+08:00`
- `updated_at`: `2026-07-11T13:36:00+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-remediation-report-template.md`
- `template_version`: `1.0.0`
- `baseline_report`: `.dev/workflows/2026-07-10-ai-context-self-audit/reports/01-audit-report.md`
- `post_remediation_report`: `.dev/workflows/2026-07-10-ai-context-self-audit/reports/03-post-remediation-audit-report.md`

## Remediation Summary

- Authorized scope: triage and begin correcting AIC-001 through AIC-009 without scanning product `src/` or `tests/` trees.
- Completed scope: current-evidence triage; Batch 1 corrections for AIC-003, AIC-006, AIC-008, and the objective portion of AIC-009; user-decided testing contract for AIC-002.
- Active batch: prepare machine-governance corrections for AIC-001, AIC-004, and AIC-005.
- Closure decision: `not-ready`.

## Finding Resolution Matrix

| Finding | Before Severity | Current Status | Evidence Summary | Planned Action | Owner / Decision |
| --- | --- | --- | --- | --- | --- |
| AIC-001 | HIGH | `partially-resolved` | Boundary policy exists, but `.ai` tech-stack rules and `.dev/standards` still overlap as normative testing/architecture surfaces. | Add a per-rule ownership matrix; convert secondary copies to references or target-adoption guidance. | Governance plus architecture/testing owner. |
| AIC-002 | HIGH | `resolved` | Canonical and human guidance now define BDDfy as the default with explicit opt-out, mandatory GWT without 3A fallback, and conditionally supported `.feature` artifacts. | Request independent verification across testing consumers. | User decision implemented; auditor verifies. |
| AIC-003 | HIGH | `resolved` | Stale onboarding is now explicitly legacy/profile-conditional, current initialization routes to `repo-structure-sync`, and missing `CLAUDE.md` links were removed. | Request independent verification; retained profile examples must remain conditional. | Governance completed; auditor verifies. |
| AIC-004 | HIGH | `not-addressed` | Canonical schema requires `id`; 13 skill specs and 17 sub-agent manifests use `asset_id`; duplicate template families and no schema validator remain. | Version schema, adopt one identifier/type contract, migrate metadata/templates, add PyYAML validation. | Governance; record schema choices before migration. |
| AIC-005 | HIGH | `partially-resolved` | Auditor declares `context-audit`, but other skills lack slots and the capability profile still ambiguously maps `local-change-implementer`. | Define slot vocabulary, add skill metadata and deterministic profile validation. | Dev-workflow contract coordinated by governance. |
| AIC-006 | HIGH | `resolved` | Workflow/commit policies and auditor contracts now distinguish transient conversational analysis, durable report-only audit, and governance remediation. | Request independent verification of authorization and persistence boundaries. | Governance completed; auditor verifies. |
| AIC-007 | HIGH | `deferred` | Required shell checks remain mode `100644`; `check-all.sh` can exit zero after required checks are skipped as warnings. | Create tooling/validation workflow for fail-closed gates and executable-mode enforcement. | Tooling workflow; outside this documentation-governance batch. |
| AIC-008 | MEDIUM | `resolved` | Current catalogs list Agents/Codex and Claude; Gemini paths, targets, branch prefixes, and descriptions were removed; Copilot alone remains planned/optional. | Request independent runtime-truth verification. | Governance completed; auditor verifies. |
| AIC-009 | MEDIUM | `partially-resolved` | Index/runtime/workflow lint is active; root bilingual parity and translation waves 1-4 corrected 39 agent-facing execution documents, including core architecture and standards entry surfaces. Remaining configuration/template guides and policy-aware lint remain. | Finish the bounded active standards backlog, then add language/parity lint with explicit exceptions. | Governance translation migration in progress. |

## Remediation Batches

### Batch 1 — Stop Active Wrong Guidance

- AIC-003: downgrade or rewrite stale onboarding and missing entry references.
- AIC-006: define transient read-only and durable report-only audit modes.
- AIC-008: correct the supported runtime matrix.
- AIC-009: repair active index corruption and add narrow objective context validation.

### Batch 2 — Machine Governance

- AIC-001: establish per-rule ownership.
- AIC-004: version and migrate the canonical asset schema.
- AIC-005: align capability slots and profile-to-skill discovery.

### Decision / Reroute

- AIC-002: decision received and implemented: BDDfy default with explicit opt-out, mandatory GWT, no 3A substitution, conditional `.feature` support.
- AIC-007: defer to a dedicated tooling/validation workflow.

## Validation Plan

- Structured YAML/JSON parse with PyYAML and Python JSON tooling.
- Active path and wrapper/runtime declaration checks.
- Workflow artifact validation and `git diff --check`.
- Repository `check-all.sh --quick`, while retaining AIC-007 because its current warning/exit semantics are under review.
- Independent `ai-context-auditor` post-remediation report before closure.

## Changes And Evidence

### AIC-003

- Changes: downgraded `coding-guide.md` and `NEW-PROJECT-GUIDE.md` to legacy/retired examples; made fixed stack choices conditional; routed current initialization to `repo-structure-sync`; repaired root-entry references and indexes.
- Evidence: `.dev/standards/coding-guide.md`, `.dev/guides/learning-guides/NEW-PROJECT-GUIDE.md`, `.dev/guides/learning-guides/LEARNING-PATH.md`, their README/INDEX owners.
- Validation: targeted searches found no stale `CLAUDE.md` link or active Todo application identity in the corrected entries; repository diff check passed.
- Remaining risk: architecture-specific examples must not be promoted back to target truth without explicit adoption.

### AIC-002

- Decision: BDDfy is the default profile, but a target team may explicitly decline the package. Unit, use-case, and integration tests must still use recognizable Given-When-Then structure and naming; Arrange-Act-Assert/3A is not an allowed substitute.
- Feature policy: `.feature` is optional and not generated by default. It is supported when supplied directly, explicitly requested for design/generation, or enabled by a target profile that names a runner. The context must not infer a runner or package.
- Evidence: dotnet-backend shared testing rules, code-review references, test sub-agent prompts, `bdd-gwt-test-designer`, `spec-compliance-validator`, `.dev/standards/coding-standards/test-standards.md`, and `.dev/specs/tests/` were synchronized.
- Validation: relevant YAML parsed with PyYAML; `bdd-gwt-test-designer` passed `quick_validate.py`; active non-example search found no remaining BDDfy-only/no-feature prohibition or positive 3A rule.
- Remaining risk: historical/reference examples may still demonstrate a specific runner but must remain non-normative.

### AIC-006

- Changes: added transient read-only direct mode, durable report-only workflow mode, and remediation lifecycle boundaries to workflow/commit policy, auditor canonical assets, runtime wrappers, and human guides.
- Evidence: `.dev/standards/WORKFLOW-GATE-POLICY.md`, `.dev/standards/GIT-COMMIT-POLICY.md`, `.ai/assets/skills/ai-context-auditor/`, `.agents/skills/ai-context-auditor/`, `.claude/skills/ai-context-auditor/`.
- Validation: auditor and governance wrappers passed `quick_validate.py`; changed YAML parsed with PyYAML.
- Remaining risk: post-remediation audit must test that generic multi-pass analysis does not accidentally create repository artifacts.

### AIC-008

- Changes: corrected repository identity and runtime catalogs, then removed Gemini targets, templates, branch prefixes, paths, and descriptions entirely. GitHub Copilot remains a planned/optional adapter.
- Evidence: `README.md`, `README.en.md`, `agents.md`, `agents.zh-tw.md`, `.dev/INDEX.md`, `.dev/guides/ai-collaboration-guides/LOCAL-RUNTIME-WRAPPER-GUIDE.md`.
- Validation: new AI context validator confirmed two current runtime roots and wrapper parity.
- Remaining risk: planned adapters must be deliberately promoted and validated when implemented.

### AIC-009

- Changes: repaired three literal table corruptions; added `.ai/scripts/validate-ai-context.py`; translated six active `.ai` documents, five test-spec documents, and problem-frame semantics; declared canonical/translated ownership for root bilingual entries and synchronized auditor mode descriptions.
- Evidence: translated `.ai` files include the code-review index, pitfalls, building-block index, shared/template READMEs, and canonical schema. Translated `.dev` files include test-spec guidance and `.dev/problem-frames/SEMANTICS.md`.
- Validation: translated execution contracts have no residual Han prose; relative Markdown links resolve; root README/agents pairs pass semantic parity review; context lint and repository quick checks pass.
- Remaining risk: 21 high-priority and several medium-priority `.dev/standards`/`.dev/specs` translation candidates remain. Language lint stays deferred until that backlog is reduced and explicit trigger/domain exceptions are encoded.

## Translation Migration Progress

### Wave 1 — Completed

- Six active `.ai` agent-facing documents translated to English.
- Five `.dev/specs/tests` execution documents translated to English while preserving BDDfy-default, mandatory-GWT, no-3A, and conditional-`.feature` semantics.
- `.dev/problem-frames/SEMANTICS.md` translated to English.
- `README.md` / `README.en.md` and `agents.md` / `agents.zh-tw.md` now declare canonical versus translated ownership; auditor descriptions and root-entry catalogs are synchronized.

### Wave 2 — Completed

- Translated `.dev/standards/coding-standards/test-standards.md` while preserving BDDfy-default, mandatory-GWT, no-3A, optional-`.feature`, and no-`BaseTestClass` rules.
- Translated the repository code-review checklist and ASP.NET Core configuration checklist.
- Translated the primary spec authoring and organization guides.
- Translated the ADR catalog and remaining short standards entry surfaces selected for this wave.
- Corrected one positive Contract Test example that still used Arrange/Act terminology; negative examples retain it only as explicitly incorrect behavior.

### Wave 3 — Completed

- Translated aggregate and use-case standards.
- Translated repository and mapper standards.
- Translated controller, projection, reactor, and archive standards.
- Preserved code, identifiers, architecture boundaries, rule strength, and positive/negative example labels.
- Translation review exposed three pre-existing semantic-governance issues without silently changing their architecture decisions:
  - the one-command/one-aggregate rule versus the multi-aggregate `IUnitOfWork` example;
  - the mapper `ClearDomainEvents()` checklist versus an event-rebuild example that omits it;
  - the soft-delete/hard-delete prohibition versus an EF example that calls `Remove()`.

### Wave 4 — Completed

- Translated the main coding-standards entry and coding-standards registry.
- Translated project-structure, anti-pattern, and best-practice contracts.
- Translated profile-configuration and UseCase/Command/Handler relationship standards.
- Translated the selected rationale catalog and rationale documents while preserving the distinction between normative standards and explanatory rationale.
- No new rule conflicts were identified during this wave.
- Updated `check-coding-standards.sh` section matching from retired Chinese headings to the translated English canonical headings; this is a narrow validator-compatibility correction, not the deferred fail-closed tooling redesign.

### Next Translation Waves

1. Remaining configuration/template/standards-guide surfaces identified by the language inventory.
2. Resolve or explicitly defer the three semantic-governance issues exposed during translation.
3. Add policy-aware language/parity lint with explicit exceptions for trigger phrases, identifiers, and human-facing documents.

Each wave must preserve identifiers, paths, code blocks, normative strength, and explicit language exceptions. Do not create bilingual copies for non-entry execution contracts.

## Deferred Work

| Finding | Reason | Owner | Next Action |
| --- | --- | --- | --- |
| AIC-007 | Requires executable-mode and gate-semantics tooling changes, not only context documentation. | Tooling workflow | Create a dated tooling workflow and make required gates fail closed. |

## Closure Evidence

- Required validations: pending remediation and independent post-audit.
- Commit status: waves 1-3 and prior remediation stages are committed; wave 4 plus its validator-compatibility correction are ready for a checkpoint commit.
- Workflow/task status: AICSA-002 completed; AICSA-003 in progress.
- Final next action: complete the AIC-001/AIC-004/AIC-005 machine-governance batch, then request independent post-remediation audit.
