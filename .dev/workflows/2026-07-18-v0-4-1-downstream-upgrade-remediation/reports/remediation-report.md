# v0.4.1 Downstream Upgrade Contract Remediation Report

## Template Metadata

- `template_id`: `ai-context-governance-remediation-report`
- `template_version`: `2.0.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Report Metadata

- `report_id`: `remediation-report-2026-07-18-v0-4-1-downstream-upgrade-remediation`
- `workflow_id`: `2026-07-18-v0-4-1-downstream-upgrade-remediation`
- `owner_skill`: `ai-context-governance`
- `status`: `draft`
- `created_at`: `2026-07-18T21:39:19+08:00`
- `updated_at`: `2026-07-18T21:39:19+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-remediation-report-template.md`
- `template_version`: `2.0.0`
- `baseline_assessment`: `external dotnet-mq-arch-lab#ASM-20260718-001 plus provenance-bound workflow evidence`
- `verification_assessment`: `pending after V041-002 and V041-003`

## Remediation Summary

- Authorized scope: prioritize and remediate the two package defects proven by the first governed downstream v0.4.0 upgrade.
- Completed scope: evidence intake, backlog registration, roadmap reordering, task decomposition, and implementation handoff only.
- Validation summary: source contracts and immutable v0.4.0 behavior were inspected; workflow, backlog, roadmap, JSON, context, and diff checks are recorded in `V041-001`.
- Closure decision: `not-ready`

## Finding Resolution Matrix

| Finding | Before Severity | Status | Changed Files | Validation | Commit | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `PKG-001` | HIGH / P0 | not-addressed | planning artifacts only | downstream reproduction preserved; source implementation pending | pending | Published version-to-version upgrade remains unusable without locally derived metadata. |
| `PKG-002` | HIGH / P0 | not-addressed | planning artifacts only | downstream failure and target override preserved; source implementation pending | pending | Packaged users can still invoke or inherit required tests whose source-only dependencies are absent. |

## Changes And Evidence

### `PKG-001`

- Changes: registered the defect as the first v0.4.1 release blocker and defined immutable inventory, planner, real-upgrade, and deterministic-package acceptance.
- Evidence: `evidence/downstream-v0.4-upgrade-findings.md` and the source guide/builder/apply contract.
- Validation: planning validation only.
- Remaining risk: full; implementation has intentionally not started in this session.

### `PKG-002`

- Changes: registered the distribution/applicability mismatch as the second v0.4.1 release blocker and defined source-versus-package gate acceptance.
- Evidence: `evidence/downstream-v0.4-upgrade-findings.md` and the source profile/runner/README contract.
- Validation: planning validation only.
- Remaining risk: full; implementation has intentionally not started in this session.

## Verification Assessment Reconciliation

- Independent auditor: pending.
- Confirmed resolved: none.
- Recurring findings: pending.
- New or regressed findings: pending.

## Deferred Work

| Finding | Reason | Owner | Next Action |
| --- | --- | --- | --- |
| Existing v0.4.1 content corrections | Lower impact than confirmed published upgrade failures. | `ai-context-governance` | Re-evaluate after `PKG-001` and `PKG-002` pass extracted-package acceptance. |
| New enforcement, policy, schema, or CI routes | Existing roadmap assigns contract expansion to v0.5.0. | roadmap owner | Stop for reclassification if the defect cannot be corrected within existing contracts. |

## Closure Evidence

- Required validations: pending implementation, immutable candidate package parity, real extracted-package upgrade, source full gate, package-applicable downstream gate, and independent verification.
- Commit status: planning checkpoint pending.
- Workflow/task status: workflow in progress; `V041-001` completed, `V041-002` in progress, `V041-003` and `V041-004` pending.
- Final next action: resume `V041-002` on the workflow branch in a new source-repository session.
