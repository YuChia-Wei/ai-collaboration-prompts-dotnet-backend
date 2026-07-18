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
- `updated_at`: `2026-07-18T21:43:22+08:00`
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
3. Existing contract-preserving content corrections remain v0.4.1 candidates,
   but cannot displace these two package defects.
4. New policy, schema, CI, or generalized validation contracts remain v0.5.0
   unless the smallest defect correction cannot be expressed within existing
   published contracts.
5. `v0.4.2` remains conditional; it is not a destination for either confirmed
   defect merely because implementation touches packaging code.

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
| `V041-002` | Implement executable governed version-to-version migration metadata and real upgrade validation. | `in_progress` |
| `V041-003` | Separate source-only tests from downstream package documentation and required gates. | `pending` |
| `V041-004` | Run immutable candidate validation, independent verification, and remediation closeout. | `pending` |

## Resume Checkpoint

- Last completed action: retained the downstream upgrade findings, created `PKG-001` and `PKG-002` as HIGH/P0 v0.4.1 items, activated this remediation workflow, and reordered the roadmap so package correctness precedes general content fixes.
- Current task: `V041-002`.
- Exact next action: read `evidence/downstream-v0.4-upgrade-findings.md`, reproduce the clean-install-only metadata from `v0.4.0`, then design the smallest patch-compatible builder input that binds the governed v0.3.0 `files.yaml` and emits deterministic upgrade operations.
- Validation already completed: immutable `v0.4.0` tag behavior compared with current `main`; source guide/builder/apply/profile/runner contracts inspected; downstream workflow and assessment evidence pinned to `dotnet-mq-arch-lab@2eeddf392ca79deb4407c47d13ad53178015ba90`; workflow artifact validation passed for 21 workflows, 41 indexed directories, and 14 backlog items; AI-context, assessment, and five-release version validation passed; six backlog release-contract GWT passed; all four task JSON files parsed; `git diff --check` passed.
- Git state: planning checkpoint `69ac74f5c9eeeb9efe8a9055a812348773127d0b` is committed on `codex/2026-07-18-v0-4-1-downstream-upgrade-remediation` from local `main@728fb73025b834997f8b7818380b9ca28f72f220`; implementation has not started.
- Branch history and checkpoint handoffs: segment 1 is a local session-handoff checkpoint; no source branch push, merge, tag, or publication was requested.
- Blockers or unresolved decisions: none for `PKG-001` or `PKG-002`; if implementation requires a new schema, new required validation contract, or published-path removal, stop and request SemVer/roadmap reclassification before making that expansion.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-18-v0-4-1-downstream-upgrade-remediation` | `main@728fb73025b834997f8b7818380b9ca28f72f220` | local session handoff | `69ac74f5c9eeeb9efe8a9055a812348773127d0b` | local | `2026-07-18T21:43:22+08:00` | Preserve planning and evidence before implementation in a new source-repository session. | Open this repository and resume the same branch at `V041-002`. |
