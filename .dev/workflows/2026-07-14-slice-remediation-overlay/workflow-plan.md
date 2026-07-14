# Slice Remediation Intent And Overlay Contract

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-14-slice-remediation-overlay`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-14-slice-remediation-overlay`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `current_phase`: `closed`
- `artifact_root`: `.dev/workflows/2026-07-14-slice-remediation-overlay`
- `created_at`: `2026-07-14T20:56:16+08:00`
- `updated_at`: `2026-07-14T21:19:12+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: `slice-implementer` lists remediation and refactor as modes while exposing only command, query, reactor, and generic mode references. Runtime agents therefore search for a nonexistent `remediation.md`, fall back implicitly, and may treat workflow findings as undifferentiated source truth.
- Authorized remediation scope: separate task intent from execution mode; add a remediation overlay; define layered authority, finding evidence, and normative truth; synchronize canonical skill assets, runtime wrappers, development capability routing, task generation, fail-closed validation, and human guidance.
- Exclusions: product source or tests, implementation of a real remediation slice, changes to architecture standards, creation of a new top-level implementer skill, and historical workflow normalization.
- Completion criteria: no active contract describes remediation or refactor as an execution mode; both runtimes can discover the overlay; remediation tasks retain architecture-specific mode rules; source authority and finding evidence are unambiguous; all targeted and repository AI-context validators pass.

## Design Decision

Use two composable axes:

```yaml
intent: review-remediation
execution_mode: command
overlays:
  - remediation
```

- `execution_mode`: `command | query | reactor | generic`.
- `intent`: `feature | bug-fix | review-remediation | validation-failure-remediation | behavior-correction | refactor | cleanup`.
- `remediation` is an overlay because a remediation slice may still be command, query, reactor, or generic.
- A workflow task owns authorized scope, acceptance criteria, non-goals, and required validation.
- A finding reference owns the observed defect and supporting evidence.
- Requirements, specs, standards, and ADRs remain normative truth.
- Do not create a standalone `remediation` execution mode or silently treat a workflow task as the only semantic truth.

## Artifact Contract

- Baseline assessment: not created; the user-provided runtime message and current canonical files are sufficient workflow intake evidence.
- Remediation report: task results and this plan; no separate report is required for this bounded taxonomy correction.
- Verification assessment: not requested; targeted wrapper and context validation provide closeout evidence.
- Tasks: `.dev/workflows/2026-07-14-slice-remediation-overlay/tasks/`.

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `SRO-MODE-001` | medium | `ai-context-governance` | separate intent and execution mode | `SRO-001` | canonical contract review and reference scan |
| `SRO-OVERLAY-001` | medium | `skill-creator` | add remediation overlay and source-layer rules | `SRO-002` | overlay content and skill validation |
| `SRO-SYNC-001` | medium | `ai-context-governance` | synchronize wrappers, profile, task template, validator, and guides | `SRO-003` | runtime parity, seven GWT scenarios, and AI-context validation |
| `SRO-CLOSE-001` | low | `ai-context-governance` | run fail-closed closeout and commit | `SRO-004` | quick gate, workflow validator, Git checks |

## Task Plan

| Task | Purpose | Status | Primary validation |
| --- | --- | --- | --- |
| `SRO-001` | Normalize the canonical input model to intent plus execution mode. | `completed` | No canonical mode list claims remediation/refactor references exist. |
| `SRO-002` | Add remediation overlay rules and layered source contracts. | `completed` | Overlay is directly discoverable and preserves architecture-specific mode rules. |
| `SRO-003` | Synchronize wrappers, capability profile, task generation, validation, and human guidance. | `completed` | Codex/Claude wrappers, new development tasks, and repository routing agree with canonical spec. |
| `SRO-004` | Run full validation, reconcile artifacts, and close the workflow. | `completed` | 9/9 required quick checks, 7 implementation-contract GWT tests, 9 assessment GWT tests, 49 .NET tests, wrappers, and structural/Git checks passed. |

## Validation Strategy

- Quick-validate Codex and Claude `slice-implementer` wrappers.
- Run seven GWT scenarios for valid, invalid, deprecated, and historical implementation task contracts.
- Search active canonical and runtime surfaces for obsolete remediation/refactor mode wording and nonexistent mode references.
- Validate workflow artifacts and AI-context relationships.
- Run `check-all.sh --quick` and `git diff --check` before closure.
- Verify every workflow commit has the required body sections and final AI co-author trailer.

## Resume Checkpoint

- Last completed action: Completed all tasks, committed the contract change, and passed the full repository closeout gate.
- Current task: none; workflow completed.
- Exact next action: await explicit merge or push authorization.
- Validation already completed: 9/9 required quick checks, 7/7 implementation-contract GWT tests, 9/9 assessment GWT tests, 47 analyzer tests, 2 configuration tests, both wrapper validations, workflow/AI-context/shell/YAML/JSON/whitespace checks, and independent forward-test passed.
- Git state: bootstrap and SRO-001 through SRO-003 are committed; final workflow closure is ready to commit.
- Branch history and checkpoint handoffs: segment 1 started from `main` commit `8af858e`.
- Blockers or unresolved decisions: none. Dependency/version validation remains deferred; historical workflow tasks are intentionally not migrated.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-14-slice-remediation-overlay` | `main` | started | `8af858e` | local | `2026-07-14T20:56:16+08:00` | Correct slice implementation taxonomy and remediation handoff semantics. | Continue `SRO-001`. |
