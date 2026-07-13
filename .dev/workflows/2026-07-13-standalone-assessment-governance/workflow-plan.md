# Standalone Assessment Storage And Search Identity

## Workflow Metadata

- `workflow_id`: `2026-07-13-standalone-assessment-governance`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-13-standalone-assessment-governance`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation`
- `artifact_root`: `.dev/workflows/2026-07-13-standalone-assessment-governance`
- `created_at`: `2026-07-13T22:57:44+08:00`
- `updated_at`: `2026-07-13T23:18:49+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.1.0`

## Objective And Scope

- Problem statement: Durable self-audits and large code-review reports are observations that may never become authorized work. Storing every report as a workflow conflates knowledge with execution, hides reusable findings inside process records, and creates misleading unfinished workflows. Git SHA alone is also insufficient as a durable lookup key because amend, rebase, cherry-pick, or history migration can change it.
- Authorized remediation scope:
  - create `.dev/assessments/` as the canonical durable assessment catalog;
  - define stable `ASM-YYYYMMDD-NNN` identities and commit lookup rules;
  - distinguish transient analysis, standalone durable assessment, and workflow-owned remediation;
  - preserve assessed revision metadata separately from the commit that stores the report;
  - update AI context audit and large code-review skills to emit standalone assessments when persistence is requested;
  - update governance lifecycle handoffs, backlog references, branch policy, indexes, and deterministic validation.
- Exclusions:
  - migrate or rewrite historical workflow reports;
  - perform a new AI-context audit or code review;
  - remediate findings contained in an assessment;
  - change product source or product tests;
  - require any external index, graph, MCP server, or IDE tooling.

## Agreed Design Decisions

1. An assessment records what was observed; a workflow records authorized execution.
2. Durable assessments live under `.dev/assessments/<assessment-id>/` regardless of whether they later become workflow inputs.
3. The stable identifier is `ASM-YYYYMMDD-NNN`, where the date is the local creation date and the sequence is the next unused three-digit value for that date.
4. The assessment ID is the durable lookup key; the assessed Git SHA remains a version-specific evidence pointer.
5. Assessment creation commits include `[ASM-...]` in the subject and `Assessment-Id: ASM-...` as a trailer before the required AI signature trailer.
6. Later workflow, backlog, ADR, remediation, or verification artifacts reference the assessment ID and finding IDs rather than copying the report.
7. Final assessments are immutable snapshots. Corrections use an addendum or successor assessment with `supersedes`; post-remediation verification is a new assessment.
8. Historical workflow reports remain historical and are not silently relocated.

## Target Information Architecture

```text
.dev/assessments/
  README.MD
  INDEX.MD
  templates/
    assessment-locator-template.yaml
  ASM-YYYYMMDD-NNN/
    assessment.yaml
    report.md
    evidence/                  # optional, assessment-owned evidence only
```

The repository owns the locator and identity contract. Each assessment-producing skill owns its report template and finding format.

## Lifecycle And Routing

| Request | Storage / Mode | Branch | Follow-up |
| --- | --- | --- | --- |
| Read-only analysis, no persistence requested | Conversation only | none | no artifact |
| Persisted audit or large code review, no remediation authorized | Standalone assessment | dedicated assessment branch | merge report independently |
| Audit/review plus remediation authorized from the start | Assessment stored under `.dev/assessments/`; execution stored in owning workflow | workflow branch | workflow references assessment |
| Existing standalone assessment selected for action later | New workflow | new workflow branch | link assessment and selected finding IDs |
| Post-remediation verification | New assessment | active workflow branch when part of that lifecycle | relate to baseline assessment and workflow |

## Metadata Contract

The locator must distinguish the reviewed subject from the artifact commit:

- `assessment_id`, `schema_version`, `assessment_type`, `title`, `owner_skill`, `status`;
- `report`, `created_at`, `updated_at`, `template_source`, `template_version`;
- `subject_ref.repository`, `subject_ref.branch`, and `subject_ref.commit` for the revision assessed;
- `scope.included` and `scope.excluded`;
- `relations.supersedes`, `relations.related_assessments`, `relations.workflow_refs`, `relations.backlog_refs`, and `relations.adr_refs`;
- `commit_search_id`, equal to `assessment_id`.

The storing commit SHA is intentionally not required inside the initial locator because that would create a circular write requirement. It is discovered through the stable ID in Git history.

## Commit Search Contract

Assessment creation or material assessment-update subject:

```text
docs(assessment): [ASM-20260713-001] add AI context health assessment
```

Required trailers:

```text
Assessment-Id: ASM-20260713-001
Co-Authored-By: <AI runtime/model> <noreply@provider-domain>
```

Lookup:

```text
git log --all --grep='ASM-20260713-001'
```

## Task Plan

| Task | Purpose | Status | Primary validation |
| --- | --- | --- | --- |
| `ASMG-001` | Define assessment storage, identity, lifecycle, branch, backlog, and commit policies. | `completed` | Policy cross-reference and structured metadata review passed. |
| `ASMG-002` | Create assessment locator template, indexes, validator, and fail-closed GWT tests. | `completed` | Nine positive and fail-closed GWT scenarios passed; quick gate selected both checks. |
| `ASMG-003` | Move AI-context auditor and governance lifecycle contracts to standalone assessments. | `completed` | Canonical specs, references, templates, guides, and four wrappers validated. |
| `ASMG-004` | Add transient and durable assessment output modes to code-reviewer. | `in_progress` | Canonical spec/reference/template and wrapper validation. |
| `ASMG-005` | Run full validation, reconcile indexes, close tasks, and commit. | `pending` | `check-all.sh --quick`, assessment/context/workflow validators, and Git checks. |

## Validation Strategy

- Parse all new YAML with PyYAML through repository validators.
- Validate assessment directory name and `assessment_id` equality.
- Validate full-date ID and per-date sequence uniqueness.
- Validate required timestamps, report target, template metadata, subject commit shape, scopes, and relationship lists.
- Validate `INDEX.MD` contains exactly one row per assessment locator and no dangling row.
- Validate `commit_search_id == assessment_id`.
- Use GWT-named positive and fail-closed tests for missing fields, bad IDs, path mismatch, dangling report, duplicate index state, and invalid relationships.
- Keep assessment validation independent of Codebase Memory, Code Graph, IDE, or other optional indexes.

## Legacy And Migration Boundary

- Existing reports under `.dev/workflows/**` remain where they are.
- New assessment rules apply prospectively after this workflow lands.
- A historical report may receive a standalone assessment successor, but must not be moved merely for normalization.
- Existing backlog and workflow links remain valid; new items may add assessment references without duplicating findings.

## Resume Checkpoint

- Last completed action: Migrated AI-context auditor and governance contracts from workflow-owned audit reports to standalone baseline and verification assessments while retaining legacy template paths for historical references.
- Current task: `ASMG-004`
- Exact next action: Add transient and durable assessment modes, report template, and stable handoff references to code-reviewer.
- Validation already completed: Four auditor/governance runtime wrappers passed skill validation; assessment, AI-context, and workflow validators passed; `git diff --check` passed.
- Git state: ASMG-003 skill migration is ready for a stage commit.
- Branch history and checkpoint handoffs: segment 1 started from `main` merge commit `69c2850`.
- Blockers or unresolved decisions: none; historical report migration is explicitly excluded.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-13-standalone-assessment-governance` | `main` | started | `69c2850` | local | `2026-07-13T22:57:44+08:00` | Establish standalone assessment governance and skill support. | Continue `ASMG-001`. |
