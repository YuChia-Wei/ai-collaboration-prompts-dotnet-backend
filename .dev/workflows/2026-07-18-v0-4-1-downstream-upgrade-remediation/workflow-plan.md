# v0.4.1 Downstream Upgrade Contract Remediation

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-18-v0-4-1-downstream-upgrade-remediation`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-18-v0-4-1-downstream-upgrade-remediation`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation`
- `artifact_root`: `.dev/workflows/2026-07-18-v0-4-1-downstream-upgrade-remediation`
- `created_at`: `2026-07-18T21:39:19+08:00`
- `updated_at`: `2026-07-18T22:27:21+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: the first governed downstream v0.1.0 to v0.3.0 to v0.4.0 upgrade proved that the published v0.4.0 migration metadata is clean-install-only despite the migration guide requiring a v0.3.0 source manifest, and that the package selects source-release tests whose dependencies are excluded downstream.
- Authorized remediation scope: make both defects the highest-priority v0.4.1 work, implement an executable version-to-version migration contract, correct downstream test applicability, validate an actual extracted-package upgrade, and retain independent verification evidence.
- Exclusions: do not implement fixes during the workflow-bootstrap session; do not publish, tag, merge, or rewrite v0.4.0; do not modify `dotnet-mq-arch-lab`; do not broaden into v0.5.0 policy, CI, taxonomy, or unrelated content cleanup.
- Completion criteria: `PKG-001` and `PKG-002` are resolved; a clean v0.3.0 downstream fixture upgrades using only published-style v0.4.1 assets; downstream required checks are package-applicable; deterministic package parity and source gates pass; an independent verification assessment confirms the fixes; all remaining v0.4.1 candidates are explicitly rescheduled.

## Artifact Contract

- Baseline evidence: `evidence/downstream-v0.4-upgrade-findings.md`
- Remediation report: `reports/remediation-report.md`
- Verification assessment: pending; create a successor `ASM-YYYYMMDD-NNN` with `ai-context-auditor` after implementation
- Tasks: `tasks/`
- Backlog: `.dev/backlog/items/PKG-001.yaml`, `.dev/backlog/items/PKG-002.yaml`

## Roadmap Reordering Decision

The downstream evidence supersedes the earlier execution order without rewriting
the independently authored planning source:

1. `PKG-001` is the v0.4.1 release blocker and executes first.
2. `PKG-002` executes second and must be included in the same extracted-package
   acceptance path.
3. Existing contract-preserving content corrections move to v0.4.2 by user
   decision; v0.4.1 remains a focused package-defect patch.
4. New policy, schema, CI, or generalized validation contracts remain v0.5.0
   unless the smallest defect correction cannot be expressed within existing
   published contracts.
5. Multi-source automatic migration requires a new public contract and is
   assigned to v0.5.0; v0.4.1 binds only the governed v0.3.0 inventory.

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `PKG-001` clean-install-only migration metadata contradicts the declared v0.3.0 upgrade path | HIGH / P0 | `ai-context-governance` | selected for v0.4.1, release blocker | `V041-002` | real extracted v0.3.0 to v0.4.1 upgrade, deterministic archives, planner/apply GWT |
| `PKG-002` source-only tests are packaged and selected as downstream required checks | HIGH / P0 | `ai-context-governance` | selected for v0.4.1, release blocker | `V041-003` | extracted-package required gate and missing-dependency negative fixtures |

## Implementation Boundaries

### PKG-001

- The package builder must receive or derive a governed previous release
  inventory for every declared supported source.
- `metadata/migration.yaml#from` must bind the exact previous version and
  manifest SHA-256.
- Migration operations must be derived from immutable previous and incoming
  inventories; target-local modifications remain reconciliation results, not
  generated overwrite authority.
- Clean install and versioned upgrade may use separate metadata or an explicit
  existing-contract-compatible selection mechanism; do not silently relabel a
  clean-install manifest as an upgrade manifest.

### PKG-002

- Source release-governance and builder tests remain required in the source
  repository.
- A target package must not advertise or require a check whose inputs or modules
  are intentionally excluded from that package.
- Prefer an explicit distribution/applicability boundary over downstream
  repository-specific runner overrides.
- Keep the safe-apply suite and target manifest validation packaged and required.

## Stages And Checkpoints

1. Downstream evidence intake, backlog creation, and roadmap reordering.
2. Implement `PKG-001` and its real-upgrade fixtures.
3. Implement `PKG-002` and extracted-package gate fixtures.
4. Build twice from an immutable candidate ref and run full source plus package validation.
5. Request independent AI-context verification and reconcile both findings.
6. Close remediation, then hand off to a separate release-publication workflow.

## Task Plan

| Task | Purpose | Status |
| --- | --- | --- |
| `V041-001` | Preserve downstream evidence, create P0 backlog items, and reorder the live roadmap. | `completed` |
| `V041-002` | Implement executable governed version-to-version migration metadata and real upgrade validation. | `completed` |
| `V041-003` | Separate source-only tests from downstream package documentation and required gates. | `in_progress` |
| `V041-004` | Run immutable candidate validation, independent verification, and remediation closeout. | `pending` |

## Resume Checkpoint

- Last completed action: reproduced the immutable v0.4.0 failure, added an optional previous-inventory builder input within migration schema 1.0.0, derived deterministic versioned operations, and proved a real extracted v0.3.0-to-v0.4.1 dry-run and apply.
- Current task: `V041-003`.
- Exact next action: classify source-only release/package-builder tests, exclude them from the target payload, and make the packaged runner select only target-applicable version and safe-apply checks.
- Validation already completed: 14/14 package-builder GWT passed including the real v0.3.0-to-v0.4.1 extracted upgrade; 13/14 package-apply GWT passed with the Windows symlink fixture skipped for unavailable privilege; candidate and publish workflows parse and bind their single automatic migration source; ZIP/tar parity and sidecars passed; `git diff --check` passed.
- Git state: V041-002 implementation is ready for its required task commit on `codex/2026-07-18-v0-4-1-downstream-upgrade-remediation`.
- Branch history and checkpoint handoffs: segment 1 is a local session-handoff checkpoint; no source branch push, merge, tag, or publication was requested.
- Blockers or unresolved decisions: none. The user assigned multi-source automatic migration to v0.5.0 and selected a v0.4.0-to-v0.5.0 direct upgrade gate; dotnet-mq-arch-lab remains unchanged on v0.4.0.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-18-v0-4-1-downstream-upgrade-remediation` | `main@728fb73025b834997f8b7818380b9ca28f72f220` | local session handoff | `69ac74f5c9eeeb9efe8a9055a812348773127d0b` | local | `2026-07-18T21:43:22+08:00` | Preserve planning and evidence before implementation in a new source-repository session. | Open this repository and resume the same branch at `V041-002`. |
