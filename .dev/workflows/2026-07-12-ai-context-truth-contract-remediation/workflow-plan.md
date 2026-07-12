# AI Context Truth And Contract Remediation

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.1.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-11T00:22:30+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-12-ai-context-truth-contract-remediation`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `source_backlog_item`: `CTX-003`
- `branch`: `codex/2026-07-12-ai-context-truth-contract-remediation`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `closure`
- `artifact_root`: `.dev/workflows/2026-07-12-ai-context-truth-contract-remediation`
- `created_at`: `2026-07-12T18:26:13+08:00`
- `updated_at`: `2026-07-12T18:55:41+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.1.0`

## Objective And Scope

- Problem statement: the final CTX-001 audit found two active historical-product-truth leaks, an unvalidated wrapper metadata split, an inconsistent transient sub-agent routing rule, and one backlog format typo.
- Authorized remediation scope: resolve `CTX-H-001`, `CTX-H-002`, `CTX-M-001`, `CTX-M-002`, and `CTX-L-001`; update only their direct context consumers, schemas, templates, validation, indexes, and owned workflow artifacts.
- Exclusions: `src/**`, `tests/**`, product implementation, architecture redesign, broad guide modernization, translation expansion, legacy workflow reconciliation, hosted Linux work, and unrelated backlog items.
- Completion criteria: every finding has an explicit outcome; targeted and aggregate context gates pass; `02-remediation-report.md` records change and commit evidence; an independent `ai-context-auditor` pass creates `03-post-remediation-audit-report.md`; workflow and CTX-003 lifecycle close only after reconciliation.

## Artifact Contract

- Immutable baseline audit: `.dev/workflows/2026-07-12-post-aic-007-ai-context-audit/reports/01-audit-report.md`
- Remediation report: `.dev/workflows/2026-07-12-ai-context-truth-contract-remediation/reports/02-remediation-report.md`
- Post-remediation audit: `.dev/workflows/2026-07-12-ai-context-truth-contract-remediation/reports/03-post-remediation-audit-report.md`
- Tasks: `.dev/workflows/2026-07-12-ai-context-truth-contract-remediation/tasks/`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `CTX-H-001` | HIGH | `ai-context-governance` coordinating `ddd-ca-hex-architect` | remediate; classify architecture statements as invariant, profile default, conditional, or example | `AICR-001` | active-truth searches, references, context validators |
| `CTX-H-002` | HIGH | `ai-context-governance` | remediate portable guide wording and unsafe credential defaults | `AICR-002` | targeted source-fact/credential searches, links, context validators |
| `CTX-M-001` | MEDIUM | `ai-context-governance` | standardize `wrapper_path`, document schema/template, migrate manifests, add fail-closed validation | `AICR-003` | manifest parse, negative fixtures or equivalent validator proof, context gate |
| `CTX-M-002` | MEDIUM | `ai-context-governance` | align sub-agent routing with persistence/mutation workflow boundary | `AICR-004` | targeted policy comparison and context gate |
| `CTX-L-001` | LOW | `ai-context-governance` | correct `.md` to `.yaml` opportunistically | `AICR-004` | backlog/workflow validator |
| all | inherited | `ai-context-auditor` then governance | independently verify and reconcile | `AICR-005` | post-remediation report and full closure gates |

## Execution Order And Dependencies

1. `AICR-001` repairs active project-structure truth and its current consumers.
2. `AICR-002` removes or parameterizes retained source-project facts and unsafe defaults in active guides.
3. `AICR-003` establishes one wrapper metadata contract and proves validation fails closed for drift.
4. `AICR-004` aligns routing and backlog documentation; it may share a small governance commit.
5. Governance publishes draft `02-remediation-report.md`; `AICR-005` requests an independent read-only post-audit, reconciles all findings, and closes the workflow.

Tasks 1 and 2 may be analyzed in parallel but are committed separately because each resolves a HIGH finding. Task 3 is kept atomic across schema, template, manifests, and validator to avoid an intermediate undocumented or fail-open contract. Product code remains excluded throughout.

## Validation Strategy

- Targeted `rg -n -uu` searches for historical product assertions, fixed names, unsafe credential recommendations, wrapper metadata key drift, and routing contradictions.
- Parse all changed JSON/YAML files with repository-supported Python/PyYAML.
- `python .ai/scripts/validate-ai-context.py`.
- `python .ai/scripts/validate-workflow-artifacts.py`.
- `python .ai/scripts/validate-shell-assets.py` when aggregate closure is reached.
- `C:\Program Files\Git\bin\bash.exe ./.ai/scripts/check-all.sh --quick` before post-audit/closure.
- `git diff --check` and staged diff verification at each commit boundary.

## Resume Checkpoint

- Last completed action: `AICR-005` reconciled the final governance ledger with an independent `ai-context-auditor` report that confirmed all five findings resolved with no regression.
- Current task: all tasks are completed; workflow and `CTX-003` are closed.
- Exact next action: commit these closure artifacts; merge the clean workflow branch with `--no-ff` when requested.
- Validation already completed: nine wrapper metadata GWT fixtures, all three context validators, and `check-all.sh --quick` passed; quick mode executed 6/6 required checks with zero failures. Independent audit decision is `healthy-with-followups`, bounded score `9.3/10`.
- Git state: bootstrap `63d9b71`; remediation commits `3c6479b`, `af68027`, `3be4f14`, and `97ec656`; final lifecycle reports and closure state are pending this closure commit.
- Branch history and checkpoint handoffs: segment 1, local only; no push or merge.
- Blockers or unresolved decisions: none. Pre-existing coding-standard warnings and deferred dependency/version validation remain separately owned follow-ups and do not block this workflow.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-12-ai-context-truth-contract-remediation` | `main` | workflow bootstrap | `63d9b71` | local branch | `2026-07-12T18:26:13+08:00` | Start authorized CTX-001 remediation on a dedicated branch | Execute bounded remediation tasks |
| 1 | `codex/2026-07-12-ai-context-truth-contract-remediation` | `main` | HIGH finding checkpoint | `3c6479b` | local branch | `2026-07-12T18:32:40+08:00` | AICR-001 resolved and validated | Execute AICR-002 |
| 1 | `codex/2026-07-12-ai-context-truth-contract-remediation` | `main` | HIGH finding checkpoint | `af68027` | local branch | `2026-07-12T18:36:58+08:00` | AICR-002 resolved and validated | Execute AICR-003 |
| 1 | `codex/2026-07-12-ai-context-truth-contract-remediation` | `main` | wrapper contract checkpoint | `3be4f14` | local branch | `2026-07-12T18:45:21+08:00` | AICR-003 resolved and validated | Execute AICR-004 |
| 1 | `codex/2026-07-12-ai-context-truth-contract-remediation` | `main` | routing documentation checkpoint | `97ec656` | local branch | `2026-07-12T18:48:37+08:00` | AICR-004 resolved and validated | Execute AICR-005 |
| 1 | `codex/2026-07-12-ai-context-truth-contract-remediation` | `main` | lifecycle closure | this closure commit | local branch | `2026-07-12T18:55:41+08:00` | Independent audit confirmed all five findings resolved; workflow and backlog closed | Merge with `--no-ff` when requested |
