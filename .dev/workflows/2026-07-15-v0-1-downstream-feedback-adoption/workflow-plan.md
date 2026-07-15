# v0.1.0 Downstream Feedback Adoption Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-15-v0-1-downstream-feedback-adoption`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-15-v0-1-downstream-feedback-adoption`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `tool-and-index-freshness`
- `artifact_root`: `.dev/workflows/2026-07-15-v0-1-downstream-feedback-adoption`
- `created_at`: `2026-07-15T08:06:44+08:00`
- `updated_at`: `2026-07-15T08:37:59+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: Real installation and remediation feedback from a `v0.1.0` raw-overlay downstream repository identifies gaps that are only partly covered by the newly merged v0.3 packaging work.
- Authorized remediation scope: retain the downstream feedback as provenance-bound evidence; classify each recommendation against current source truth; implement historical release semantics, payload reference integrity, exact-case validation, commit-policy enforcement, workflow semantic validation, and bounded validator/index improvements.
- Exclusions: product `src/` and `tests/`; mutation of `dotnet-mq-arch-lab`; creation or publication of `v0.3.0`; creation of historical tags; dependence on codebase-memory-mcp or another external index as proof; blind copying of downstream project truth into canonical framework context.
- Completion criteria: every `DSFB-*` finding has an explicit resolved/deferred disposition; required GWT and repository gates pass; copied evidence remains blob-identical; an independent verification pass reviews the remediated surfaces; commits satisfy the repository policy.

## Artifact Contract

- Downstream evidence: `evidence/ai-context-v0.1.0-downstream-feedback.md`
- Evidence provenance: `evidence/README.md`
- Remediation report: `reports/remediation-report.md`
- Tasks: `tasks/`

## Current-State Reconciliation

| Finding | Current disposition | Evidence | Task |
| --- | --- | --- | --- |
| `DSFB-P0-001` Separate source snapshot, distribution package, and installed state | open | `v0.1.0` and `v0.2.0` remain retrospective records without `distribution_kind` or `installable`; the v0.1 guide still says to copy the framework. | `AICFB-002` |
| `DSFB-P0-002 Governed builder and safe application` | mostly resolved | v0.3 deterministic archives, ownership inventory, safe apply, runtime requirements, and provenance handoff are validated; excluded-path backlink validation is not yet a package gate. | `AICFB-003` |
| `DSFB-P0-003 Validator extension and aggregate parity` | resolved | required shell children and literal required commands are compared as declared sets; no fixed expected count is used, and fail-closed parity fixtures cover omitted registrations. | `AICFB-006` |
| `DSFB-P0-004 Executable commit policy` | resolved | machine-readable policy and explicit-range validator enforce subject, final AI trailer, assessment identity, and optional workflow sections/identity; the quick gate activates it only when `COMMIT_RANGE` is supplied. | `AICFB-005` |
| `DSFB-P1-001 Source lifecycle install leaks` | resolved by profile, regression pending | v0.3 profile excludes source requirements, backlog instances, workflows, assessments, releases, and source root truth; regression must prove excluded paths and backlinks stay absent. | `AICFB-003` |
| `DSFB-P1-002 Exact-case active references` | resolved | Git-backed exact-case validation covers root-relative, Markdown-link, and relative-link forms; 28 active source mismatches were repaired and five GWT cases pass. | `AICFB-004` |
| `DSFB-P1-003 Workflow metadata semantics` | resolved prospectively | locator templates opt into lifecycle contract 1.0, enforcing active-task cardinality, completed workflow/task/phase consistency, and completed result evidence while preserving legacy locators. | `AICFB-006` |
| `DSFB-P1-004 Knowledge-graph freshness` | policy-level resolved, automation review pending | tool-neutral evidence policy requires freshness disclosure and file-backed verification; repo must not introduce an MCP dependency. | `AICFB-007` |
| `DSFB-P2-001 Index and generated-inventory drift` | partially resolved | README/INDEX ownership is established; generated inventory provenance and drift signals need a bounded review. | `AICFB-007` |

## Task Plan

| Task | Purpose | Status | Primary validation |
| --- | --- | --- | --- |
| `AICFB-001` | Import the downstream feedback verbatim, bind provenance, and reconcile recommendations against current source truth. | `completed` | Source and copied Git blob IDs match; workflow artifacts validate. |
| `AICFB-002` | Mark v0.1/v0.2 as non-installable historical source snapshots and repair migration guidance/validation. | `completed` | Release validator and GWT tests reject false installability claims. |
| `AICFB-003` | Add package excluded-path/reference-integrity gates and v0.1-style regression fixtures. | `completed` | Built payload contains no excluded lifecycle file or backlink. |
| `AICFB-004` | Add exact-case active-reference validation and repair current reusable context paths. | `completed` | Windows-safe Git-path case tests fail closed; active paths use exact Git case. |
| `AICFB-005` | Implement commit subject/body/trailer validation and workflow closeout commit verification. | `completed` | Positive/negative GWT commit fixtures and quick-gate integration pass. |
| `AICFB-006` | Remove brittle validator-count assumptions and enforce workflow/task semantic state consistency. | `completed` | Registry/set parity and lifecycle contradiction fixtures pass. |
| `AICFB-007` | Reconcile tool freshness and generated-index drift signals without creating an external-tool dependency. | `in_progress` | Tool-neutral validation and documentation checks pass or record a bounded deferral. |
| `AICFB-008` | Run independent verification, reconcile findings, write remediation evidence, and close the workflow. | `pending` | Required quick gate, workflow/version/package gates, Git-policy checks, and independent review pass. |

## Stages And Checkpoints

1. Evidence import and current-state reconciliation.
2. Historical release and installability contract remediation.
3. Package/reference and exact-case regression gates.
4. Commit and workflow governance automation.
5. Tool/index boundary reconciliation.
6. Independent verification, commit evidence, and closure.

## Resume Checkpoint

- Last completed action: added set-based required-command parity, six lifecycle contradiction fixtures, and prospective locator lifecycle contract 1.0 while preserving legacy compatibility.
- Current task: `AICFB-007`.
- Exact next action: reconcile existing optional-tool policy with remaining generated-index freshness signals and either implement a tool-neutral check or record a bounded deferral.
- Validation already completed: runner/registry GWT passed 17/17; lifecycle GWT passed 6/6; shell/workflow/context validators passed; quick gate passed with six commit messages verified.
- Git state: AICFB-006 implementation and task transition are ready for checkpoint commit.
- Branch history and checkpoint handoffs: segment 1 started from merge commit `d3ebfc527d49e30c3dc1cee958054a69e415eeef`.
- Blockers or unresolved decisions: none. Historical `v0.0.1` selection and actual `v0.3.0` publication remain out of scope.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-15-v0-1-downstream-feedback-adoption` | `main` | started | `d3ebfc527d49e30c3dc1cee958054a69e415eeef` | local | `2026-07-15T08:06:44+08:00` | Adopt verified downstream installation feedback into source governance. | Continue `AICFB-002`. |
