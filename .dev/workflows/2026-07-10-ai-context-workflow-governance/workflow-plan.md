# AI Context Workflow Governance Plan

## Metadata

- `workflow_id`: `2026-07-10-ai-context-workflow-governance`
- `workflow_schema_version`: `1.0`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `active_supporting_skills`: `skill-creator`, `ai-context-auditor`
- `historical_or_subject_skill`: `dev-workflow` was used and modified during the boundary migration; it is not the active orchestrator for this AI-context workflow
- `artifact_root`: `.dev/workflows/2026-07-10-ai-context-workflow-governance`
- `created_at`: `2026-07-10T18:17:55+08:00`
- `updated_at`: `2026-07-10T23:41:46+08:00`
- `status`: `completed`
- `template_source`: `none; created before the ai-context-governance lifecycle template was introduced`
- `template_version`: `N/A`

## Context

- At workflow start, the repository used `.dev/workflows/` as a shared artifact store while `dev-workflow` also owned generic workflow templates and broad routing for development, documentation, refactoring, and AI collaboration. That ownership has now been narrowed.
- The target design narrows `dev-workflow` to software-development work and lets every workflow-creating skill own task-specific templates, workflow IDs, task IDs, report structures, and artifact-root selection.
- A small repository-wide discovery and metadata contract is still required so skill-specific workflows remain traceable across time and can be resumed without reconstructing prior context.
- Existing AI-context workflow IDs use month-only prefixes. Three active or recent AI-context workflows are not immediately sortable by creation order from their names alone.
- The morning AI-context self-audit report was initially mixed into `2026-07-ai-context-auditor-skill`, whose primary responsibility is building the recurring auditor skill. It has now been relocated to the distinct `2026-07-10-ai-context-self-audit` workflow so later remediation can proceed independently.

## Decisions Already Accepted

1. Keep `ai-context-auditor` read-only and responsible for baseline and post-remediation audits.
2. Use `ai-context-governance` for AI-context remediation and lifecycle coordination.
3. Narrow `dev-workflow` to software-development orchestration rather than universal repository-work orchestration.
4. Treat `.dev/workflows/` as a shared default artifact location, not as storage owned by `dev-workflow`.
5. Allow workflow-creating skills to own their templates, ID conventions, task structure, report structure, and declared artifact root.
6. Require workflow and task artifacts to record durable timestamps and ownership metadata.
7. Give the 2026-07-10 morning self-audit a separate workflow from the auditor-skill implementation workflow and the earlier relationship-audit workflow.

## Target Direction

### Shared Minimum Contract

The repository-wide contract will define discovery and lifecycle metadata only:

- workflow IDs must begin with `YYYY-MM-DD-` unless a stronger skill-specific convention preserves the same sortable date;
- every workflow root must declare `workflow_id`, `workflow_kind`, `owner_skill`, `artifact_root`, `created_at`, `updated_at`, and `status`;
- every task must declare `task_id`, `workflow_id`, `owner_skill`, `created_at`, `updated_at`, and `status`;
- the owning skill must document its artifact root and provide discovery from a canonical index or the default `.dev/workflows/` location;
- timestamps use ISO 8601 with an explicit UTC offset;
- `created_at` is immutable; `updated_at` changes whenever artifact meaning or status changes.

### Skill-Owned Workflow Frameworks

- `dev-workflow` owns templates for software-development workflows only.
- `ai-context-governance` owns AI-context maintenance workflow, remediation, task, and completion-report templates.
- `ai-context-auditor` owns audit-report templates and emits reports into a declared workflow/artifact root.
- Other workflow-creating skills may own their own templates when their task lifecycle materially differs.
- The repository does not maintain one central template that pretends to fit every workflow kind.

### AI Context Maintenance Lifecycle

1. `ai-context-auditor` creates an immutable baseline audit report.
2. `ai-context-governance` triages findings and creates remediation tasks.
3. Context specialists execute authorized remediation.
4. `ai-context-auditor` performs an independent post-remediation audit.
5. `ai-context-governance` creates a remediation completion report and closes or defers remaining findings.

## Scope

- Update workflow policy and repository instructions to distinguish shared discovery rules from skill-owned templates.
- Add full-date workflow naming and timestamp requirements.
- Narrow `dev-workflow` canonical spec, wrapper metadata, references, and human guide to development work.
- Extend `ai-context-governance` with the AI-context maintenance lifecycle and owned templates.
- Update `ai-context-auditor` output routing and report metadata for baseline/post-remediation use.
- Re-home the morning audit report into a new dated workflow without confusing it with the auditor-skill implementation workflow.
- Record the status and relationship of the three recent AI-context workflows.
- Update indexes, wrappers, examples, and validation surfaces affected by these changes.

## Non-Goals

- Do not scan or review `src/`, `tests/`, or product implementation code.
- Do not rewrite historical workflow IDs solely for cosmetic uniformity.
- Do not merge the earlier relationship audit with the morning self-audit.
- Do not make `ai-context-auditor` perform remediation.
- Do not add a new `ai-context-maintenance` skill unless implementation evidence shows `ai-context-governance` cannot own the lifecycle coherently.

## Stages and Tasks

### Stage 1 — Inventory and Reconciliation

- `AICWG-001`: Inventory current policies, templates, skill routing, workflow references, validation scripts, workflow chronology, and report provenance.

Exit criteria:

- Every affected canonical source and derived wrapper is listed.
- Existing workflows have evidence-backed creation order and responsibility.
- Migration does not rewrite the earlier relationship-audit history.

### Stage 2 — Shared Contract and Skill Boundaries

- `AICWG-002`: Define the minimum workflow discovery and metadata contract, remove central-template ownership, and add validation.
- `AICWG-003`: Narrow `dev-workflow` and establish AI-context governance/audit lifecycle templates and routing.

Exit criteria:

- Shared policy contains no universal task/report template mandate.
- `dev-workflow` no longer claims general AI-context/document-governance orchestration.
- Artifact-root flexibility remains discoverable and auditable.

### Stage 3 — AI Context Audit and Remediation Lifecycle

- Covered by `AICWG-003`, including routing, indexes, wrappers, and human guides.

Exit criteria:

- Audit, remediation, verification, and closure have distinct artifacts.
- Baseline reports remain immutable.
- Finding IDs can be traced into remediation tasks and completion status.

### Stage 4 — Morning Audit Separation

- `AICWG-004`: Create a new dated workflow for the 2026-07-10 morning self-audit, relocate reports with provenance, and correct historical handoff references.

Exit criteria:

- The auditor-skill workflow and audit-result workflow have different responsibilities.
- The morning report has an explicit status and remediation handoff.
- No report is silently overwritten or detached from its originating commit/history.

### Stage 5 — Validation and Closeout

- `AICWG-005`: Validate links, IDs, metadata, wrapper sync, skill schemas, and repository context checks; then close this governance workflow under commit policy.

Exit criteria:

- All validation passes or skipped checks have explicit reasons.
- Task and workflow timestamps/statuses reflect final state.
- Commit-policy requirements are satisfied before completion is claimed.

## Validation Strategy

- Use `rg -uu` for hidden AI-context trees and workflow references.
- Validate canonical skill specs and thin runtime wrappers remain aligned.
- Run skill validation tooling where available.
- Run `C:\Program Files\Git\bin\bash.exe ./.ai/scripts/check-all.sh --quick` after governance changes.
- Check that no active workflow or guide still presents month-only naming as the preferred convention.
- Check that workflow discovery does not depend on knowing a skill-specific artifact root in advance.
- Verify report moves with `git diff --summary`, `git log --follow`, and content hashes where appropriate.

## Resume Packet

If work stops because of quota or interruption:

1. Read this plan and all JSON files under `tasks/`.
2. Read the latest `updated_at` values and task `results` before repeating analysis.
3. Inspect `git status --short` and preserve unrelated user changes.
4. Resume the first `in_progress` task; otherwise resume the first `pending` task whose dependencies are complete.
5. Do not recreate the morning audit report from memory; use the existing report and git history as evidence.

## Open Risks

- Allowing arbitrary artifact roots without a discovery contract would make workflows harder to find than today.
- Renaming historical workflow directories can break links and erase the meaning of old commits; prefer explicit migration only for the still-active morning audit.
- Some existing `dev-workflow` references may embed documentation/context routing and require coordinated updates.
- The translated audit report must remain a derived copy of a clearly identified English canonical report.

## Completion Summary

- Established a repository-wide discovery and metadata contract while leaving plan, task, report, ID suffix, and artifact-root design with each workflow-producing skill.
- Added sortable full-date workflow IDs, ISO 8601 lifecycle timestamps, template provenance, stable `.dev/workflows/<workflow-id>/workflow.yaml` locators, and automated validation.
- Narrowed `dev-workflow` to software/product development and gave it a complete skill-owned locator/plan/task/review template set.
- Assigned AI context audit and post-remediation verification to read-only `ai-context-auditor`; assigned triage, remediation, post-audit coordination, and closure to `ai-context-governance`.
- Relocated the 2026-07-10 baseline and zh-TW report into `2026-07-10-ai-context-self-audit`; its AIC-001 through AIC-009 remediation remains pending and was not conflated with this completed governance workflow.
- Validation passed: workflow artifact validator, 13 JSON parses, 3 locator template contracts, wrapper path/frontmatter checks, stale-reference searches, `git diff --check`, and repository `check-all.sh --quick` with 4/4 checks passed (47 analyzer tests and 2 configuration-validation tests).
- `skill-creator` `quick_validate.py` could not run because the available Python runtimes lack `PyYAML`; equivalent wrapper frontmatter, referenced-path, JSON, locator, and repository checks passed.
- Commit policy: this completion is intended to be recorded by the immediate workflow closeout commit.
