# Repository Branch And Runtime Entry Policy

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.1.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-11T00:22:30+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-12-repository-runtime-entry-policy`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-12-repository-runtime-entry-policy`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation`
- `artifact_root`: `.dev/workflows/2026-07-12-repository-runtime-entry-policy`
- `created_at`: `2026-07-12T19:23:53+08:00`
- `updated_at`: `2026-07-12T19:23:53+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.1.0`

## Objective And Scope

- Problem statement: the canonical Git policy is active and current but its name can be confused with classic Git Flow, one sentence overstates branch requirements outside workflow mode, and the root collaboration entry uses lowercase `agents.md` without the official uppercase Claude entry.
- Authorized remediation scope: clarify the repository's single-trunk short-lived-branch model in place; normalize the canonical root entry to `AGENTS.md`; add a thin `CLAUDE.md` that imports the canonical guide; synchronize active root links, indexes, bilingual parity, language allowlists, and validators as required.
- Exclusions: product source/tests, changing branch/merge semantics, requiring hosted PRs or CI, duplicating the full collaboration guide, changing runtime skill wrappers, and broad root-document redesign.
- Completion criteria: Git policy naming and mode boundary are unambiguous; Git tracks uppercase `AGENTS.md` and `CLAUDE.md`; Claude entry imports rather than duplicates canonical instructions; active references resolve case-safely; root bilingual/context/workflow validators and targeted searches pass; workflow is committed and closed.

## Evidence And Decisions

- `.dev/TEAM-GIT-FLOW-RULES.MD` is the canonical owner referenced by root instructions, workflow/commit policies, `dev-workflow`, `ai-context-governance`, and `ai-context-auditor`; removal or rename would require broad low-value migration.
- Observed model: one long-lived `main`, short-lived branches, workflow branch-first, checkpoint continuation, and default `--no-ff`. This is GitHub-Flow-like with repository-specific rules, not classic Git Flow and not strict trunk-based development.
- Anthropic documents uppercase root `CLAUDE.md` discovery and `@path` imports. The Claude entry will therefore be a thin adapter containing `@AGENTS.md` plus a canonical-ownership note.
- Codex durable repo guidance uses `AGENTS.md`. The current lowercase file works on this Windows checkout but is not case-safe for Linux/WSL portability.

## Tasks

| Task | Scope | Status | Validation |
| --- | --- | --- | --- |
| `GITP-001` | Clarify Git policy identity and workflow-mode branch boundary without changing semantics or path. | `pending` | active-reference inventory, policy comparison, context validation |
| `RTENT-001` | Normalize `agents.md` to `AGENTS.md`, add thin `CLAUDE.md`, and synchronize active consumers/validators. | `pending` | Git case inventory, link/reference checks, root parity and context validation |

## Execution Order

1. Commit workflow bootstrap on the dedicated branch.
2. Clarify `.dev/TEAM-GIT-FLOW-RULES.MD` in place and update its index description only if needed.
3. Perform a two-step Git case rename for `agents.md` to `AGENTS.md`, add `CLAUDE.md` with `@AGENTS.md`, and update all active exact-case consumers atomically.
4. Run targeted searches, structured validation, and the quick context gate.
5. Complete tasks/workflow, commit final state, and leave merge/push to explicit user direction.

## Resume Checkpoint

- Last completed action: read-only inventories established the canonical Git-policy ownership and official Claude/Codex root-entry conventions.
- Current task: workflow bootstrap.
- Exact next action: commit bootstrap, then execute `GITP-001`.
- Validation already completed: main merge validators passed; active Git-policy reference inventory and Git-tracked root-entry case were inspected.
- Git state: clean dedicated branch created from local `main` merge commit `1bdf508`; no push.
- Branch history and checkpoint handoffs: segment 1, local only.
- Blockers or unresolved decisions: none. Preserve the Git-policy path and one canonical collaboration body.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-12-repository-runtime-entry-policy` | `main` | workflow bootstrap | pending | local branch | `2026-07-12T19:23:53+08:00` | Clarify canonical branch policy and runtime entry portability together | Commit bootstrap, then execute `GITP-001` |
