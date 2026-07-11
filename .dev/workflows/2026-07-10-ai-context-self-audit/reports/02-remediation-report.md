# AI Context Remediation Report

## Report Metadata

- `report_id`: `remediation-report-2026-07-10-ai-context-self-audit`
- `workflow_id`: `2026-07-10-ai-context-self-audit`
- `owner_skill`: `ai-context-governance`
- `status`: `draft`
- `created_at`: `2026-07-11T08:18:07+08:00`
- `updated_at`: `2026-07-11T08:25:12+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-remediation-report-template.md`
- `template_version`: `1.0.0`
- `baseline_report`: `.dev/workflows/2026-07-10-ai-context-self-audit/reports/01-audit-report.md`
- `post_remediation_report`: `.dev/workflows/2026-07-10-ai-context-self-audit/reports/03-post-remediation-audit-report.md`

## Remediation Summary

- Authorized scope: triage and begin correcting AIC-001 through AIC-009 without scanning product `src/` or `tests/` trees.
- Completed scope: current-evidence triage plus Batch 1 corrections for AIC-003, AIC-006, AIC-008, and the objective index/runtime/lifecycle portion of AIC-009.
- Active batch: prepare machine-governance corrections for AIC-001, AIC-004, and AIC-005.
- Closure decision: `not-ready`.

## Finding Resolution Matrix

| Finding | Before Severity | Current Status | Evidence Summary | Planned Action | Owner / Decision |
| --- | --- | --- | --- | --- | --- |
| AIC-001 | HIGH | `partially-resolved` | Boundary policy exists, but `.ai` tech-stack rules and `.dev/standards` still overlap as normative testing/architecture surfaces. | Add a per-rule ownership matrix; convert secondary copies to references or target-adoption guidance. | Governance plus architecture/testing owner. |
| AIC-002 | HIGH | `not-addressed` | BDDfy-only/no-`.feature` rules still conflict with formal `tests/Features` guidance. | Select forbidden, profile-optional, or formally-supported `.feature` policy, then synchronize consumers. | User/testing decision required; profile-optional is recommended. |
| AIC-003 | HIGH | `resolved` | Stale onboarding is now explicitly legacy/profile-conditional, current initialization routes to `repo-structure-sync`, and missing `CLAUDE.md` links were removed. | Request independent verification; retained profile examples must remain conditional. | Governance completed; auditor verifies. |
| AIC-004 | HIGH | `not-addressed` | Canonical schema requires `id`; 13 skill specs and 17 sub-agent manifests use `asset_id`; duplicate template families and no schema validator remain. | Version schema, adopt one identifier/type contract, migrate metadata/templates, add PyYAML validation. | Governance; record schema choices before migration. |
| AIC-005 | HIGH | `partially-resolved` | Auditor declares `context-audit`, but other skills lack slots and the capability profile still ambiguously maps `local-change-implementer`. | Define slot vocabulary, add skill metadata and deterministic profile validation. | Dev-workflow contract coordinated by governance. |
| AIC-006 | HIGH | `resolved` | Workflow/commit policies and auditor contracts now distinguish transient conversational analysis, durable report-only audit, and governance remediation. | Request independent verification of authorization and persistence boundaries. | Governance completed; auditor verifies. |
| AIC-007 | HIGH | `deferred` | Required shell checks remain mode `100644`; `check-all.sh` can exit zero after required checks are skipped as warnings. | Create tooling/validation workflow for fail-closed gates and executable-mode enforcement. | Tooling workflow; outside this documentation-governance batch. |
| AIC-008 | MEDIUM | `resolved` | Current catalogs now list only Agents/Codex and Claude roots; Gemini/Copilot are explicitly planned/optional and absent paths are no longer cataloged as current. | Request independent runtime-truth verification. | Governance completed; auditor verifies. |
| AIC-009 | MEDIUM | `partially-resolved` | Index corruption is repaired and `validate-ai-context.py` checks active paths, runtime status, and wrapper parity; language and bilingual parity lint remain deferred. | Retain narrow lint in quick checks and define a safe language/parity policy later. | Governance partial; auditor verifies implemented scope. |

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

- AIC-002: wait for the `.feature` policy decision before changing testing truth.
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

### AIC-006

- Changes: added transient read-only direct mode, durable report-only workflow mode, and remediation lifecycle boundaries to workflow/commit policy, auditor canonical assets, runtime wrappers, and human guides.
- Evidence: `.dev/standards/WORKFLOW-GATE-POLICY.md`, `.dev/standards/GIT-COMMIT-POLICY.md`, `.ai/assets/skills/ai-context-auditor/`, `.agents/skills/ai-context-auditor/`, `.claude/skills/ai-context-auditor/`.
- Validation: auditor and governance wrappers passed `quick_validate.py`; changed YAML parsed with PyYAML.
- Remaining risk: post-remediation audit must test that generic multi-pass analysis does not accidentally create repository artifacts.

### AIC-008

- Changes: corrected repository identity, root agent indexes, runtime guide, location strategy, and project structure to separate current Agents/Codex and Claude support from planned Gemini/Copilot adapters.
- Evidence: `README.md`, `README.en.md`, `agents.md`, `agents.zh-tw.md`, `.dev/INDEX.md`, `.dev/guides/ai-collaboration-guides/LOCAL-RUNTIME-WRAPPER-GUIDE.md`.
- Validation: new AI context validator confirmed two current runtime roots and wrapper parity.
- Remaining risk: planned adapters must be deliberately promoted and validated when implemented.

### AIC-009

- Changes: repaired three literal table corruptions in `.dev/INDEX.md`; added `.ai/scripts/validate-ai-context.py`; wired it into `check-all.sh --quick`.
- Evidence: validator covers seven active indexes, current/planned runtime status, and 13-skill canonical/Agents/Claude parity.
- Validation: context lint and Python compile passed; repository quick check passed 5/5 including 49 .NET tests.
- Remaining risk: language-policy and bilingual-parity lint are intentionally deferred to avoid unsafe broad character matching.

## Deferred Work

| Finding | Reason | Owner | Next Action |
| --- | --- | --- | --- |
| AIC-002 | Testing artifact strategy changes repository-wide contracts. | User/testing owner | Choose forbidden, profile-optional, or formally-supported `.feature` behavior. |
| AIC-007 | Requires executable-mode and gate-semantics tooling changes, not only context documentation. | Tooling workflow | Create a dated tooling workflow and make required gates fail closed. |

## Closure Evidence

- Required validations: pending remediation and independent post-audit.
- Commit status: continuation branch is dirty; no remediation commit yet.
- Workflow/task status: AICSA-002 completed; AICSA-003 in progress.
- Final next action: complete Batch 1, update finding evidence, then start the machine-governance batch.
