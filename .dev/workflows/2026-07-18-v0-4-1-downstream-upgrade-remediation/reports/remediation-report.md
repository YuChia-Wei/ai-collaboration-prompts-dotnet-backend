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
- `status`: `final`
- `created_at`: `2026-07-18T21:39:19+08:00`
- `updated_at`: `2026-07-18T23:15:10+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-remediation-report-template.md`
- `template_version`: `2.0.0`
- `baseline_assessment`: `external dotnet-mq-arch-lab#ASM-20260718-001 plus provenance-bound workflow evidence`
- `verification_assessment`: `ASM-20260718-001`

## Remediation Summary

- Authorized scope: prioritize and remediate the two package defects proven by the first governed downstream v0.4.0 upgrade.
- Completed scope: evidence intake, PKG-001 migration implementation, PKG-002 package-applicability correction, and real extracted-package upgrade/target-gate validation.
- Validation summary: immutable v0.4.0 failed as reported; corrected immutable candidates passed focused GWT, archive parity, a real v0.3.0-to-v0.4.1 dry-run/apply, and a synchronized target quick gate at 19/19.
- Closure decision: `ready-for-separate-release-publication`

## Finding Resolution Matrix

| Finding | Before Severity | Status | Changed Files | Validation | Commit | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `PKG-001` | HIGH / P0 | resolved | builder, release workflows, packaging GWT | 14/14 packaging GWT; real extracted v0.3.0 upgrade; archive parity; `ASM-20260718-001` | `af18803` | Schema 1.0.0 remains intentionally single-source; multi-source upgrades move to v0.5.0. |
| `PKG-002` | HIGH / P0 | resolved | profile, runner, shell registry, README, navigation validator, GWT | source gates retained; source-only payload paths absent; synchronized target quick gate 19/19; `ASM-20260718-001` | `ff9908c`, `3221276` | Target-owned synchronization and provenance finalization remain required after package apply. |

## Changes And Evidence

### `PKG-001`

- Changes: added paired `--previous-files` and `--previous-version` builder inputs, exact previous manifest identity binding, deterministic add/replace/remove/rename/reconcile derivation, and release-workflow projection of the single declared automatic source.
- Evidence: `evidence/downstream-v0.4-upgrade-findings.md`, immutable v0.3.0 files inventory SHA binding, candidate validation evidence, and `ASM-20260718-001`.
- Validation: 14/14 packaging GWT; 13 apply GWT plus one platform skip; real extracted v0.3.0-to-v0.4.1 dry-run and apply; ZIP/tar parity and sidecars.
- Remaining risk: multi-source automatic migration is not part of v0.4.1 and remains assigned to `PKG-003`/v0.5.0.

### `PKG-002`

- Changes: excluded source-only release/builder tests from the target payload, retained them as conditional required checks in the source repository, kept safe-apply coverage required downstream, documented applicability, and aligned active-script reference validation with the same proven source boundary.
- Evidence: `evidence/downstream-v0.4-upgrade-findings.md`, immutable candidate `32212761c8b6e06f895486ca393059645e18d44a`, and the disposable v0.3.0-to-v0.4.1 synchronized target.
- Validation: 19/19 runner fixtures, 5/5 active-script fixtures, payload inventory assertions, and downstream `check-all.sh --quick` 19/19 with zero required failures.
- Remaining risk: target repositories must still reconcile target-owned seeds/catalogs and finalize `.dev/AI-CONTEXT-SOURCE.yaml`; the package tool intentionally does not claim that authority.

## Verification Assessment Reconciliation

- Independent auditor: `ai-context-auditor` in `ASM-20260718-001`.
- Confirmed resolved: `PKG-001`, `PKG-002`.
- Recurring findings: none.
- New or regressed findings: none.

## Deferred Work

| Finding | Reason | Owner | Next Action |
| --- | --- | --- | --- |
| Original v0.4.1 content corrections | User moved the complete pre-existing correction set to v0.4.2 so v0.4.1 remains a focused release-contract patch. | `ai-context-governance` | Activate v0.4.2 after v0.4.1 publication. |
| Multi-source direct upgrades, including v0.4.0 to the newest release | Migration schema 1.0.0 represents one source; expanding it is a new public contract. | roadmap owner | Implement and validate in v0.5.0, including the retained dotnet-mq-arch-lab v0.4.0 target. |
| New enforcement, policy, schema, or CI routes | Existing roadmap assigns contract expansion to v0.5.0. | roadmap owner | Stop for reclassification if the defect cannot be corrected within existing contracts. |

## Closure Evidence

- Required validations: source full gate 21/21; package-applicable downstream gate 19/19; packaging GWT 14/14; package apply 13 passes plus one Windows privilege skip; two byte-identical package builds; archive validation; independent assessment.
- Commit status: implementation and verification checkpoints `af18803`, `ff9908c`, `3221276`, `25c7847`, `962919b`, and `8eeb63c` exist; this final governance reconciliation is the closure commit.
- Workflow/task status: all four tasks completed; workflow closed.
- Final next action: start the separate v0.4.1 release-publication workflow authorized by the user.
