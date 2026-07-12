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
- `status`: `completed`
- `current_phase`: `closure`
- `artifact_root`: `.dev/workflows/2026-07-12-repository-runtime-entry-policy`
- `created_at`: `2026-07-12T19:23:53+08:00`
- `updated_at`: `2026-07-12T19:42:59+08:00`
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
| `GITP-001` | Clarify Git policy identity and workflow-mode branch boundary without changing semantics or path. | `completed` | active-reference inventory, policy comparison, context validation |
| `RTENT-001` | Normalize `agents.md` to `AGENTS.md`, add thin `CLAUDE.md`, and synchronize active consumers/validators. | `completed` | Git case inventory, link/reference checks, root parity and context validation |
| `GITP-002` | Remove obsolete branch-model examples and require AI identity trailers on AI-assisted commits. | `completed` | targeted policy searches, context/workflow validation, signed commit/merge evidence |

## Execution Order

1. Commit workflow bootstrap on the dedicated branch.
2. Clarify `.dev/TEAM-GIT-FLOW-RULES.MD` in place and update its index description only if needed.
3. Perform a two-step Git case rename for `agents.md` to `AGENTS.md`, add `CLAUDE.md` with `@AGENTS.md`, and update all active exact-case consumers atomically.
4. Run targeted searches, structured validation, and the quick context gate.
5. Complete tasks/workflow, commit final state, and leave merge/push to explicit user direction.

## Resume Checkpoint

- Last completed action: the user explicitly reopened the completed workflow for `GITP-002`; obsolete baseline/release branch examples were removed and the AI model signature trailer contract was added.
- Current task: all tasks and the workflow are completed.
- Exact next action: commit the correction using the new AI signature trailer, then merge with `--no-ff` using an AI-signed merge commit.
- Validation already completed: 6/6 root-entry GWT fixtures, Python compilation, AI context/workflow validators, quick gate 6/6 required checks, independent re-review, and `git diff --check` pass.
- Git state: bootstrap `4a3e323`; GITP-001 `a81951a`; RTENT-001/closure `5946e9b`; GITP-002 correction changes pending this commit; no push.
- Branch history and checkpoint handoffs: segment 1, local only.
- Blockers or unresolved decisions: none. The canonical body remains `AGENTS.md`; `CLAUDE.md` is enforced as an exact thin import adapter.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-12-repository-runtime-entry-policy` | `main` | workflow bootstrap | `4a3e323` | local branch | `2026-07-12T19:23:53+08:00` | Clarify canonical branch policy and runtime entry portability together | Execute `GITP-001` |
| 1 | `codex/2026-07-12-repository-runtime-entry-policy` | `main` | branch policy checkpoint | `a81951a` | local branch | `2026-07-12T19:26:17+08:00` | GITP-001 resolved and validated | Execute `RTENT-001` |
| 1 | `codex/2026-07-12-repository-runtime-entry-policy` | `main` | runtime entry and closure checkpoint | `5946e9b` | local branch | `2026-07-12T19:34:28+08:00` | RTENT-001 resolved, independently reviewed, and workflow closed | Merge with `--no-ff` when requested |
| 1 | `codex/2026-07-12-repository-runtime-entry-policy` | `main` | explicit correction reopen | pending | local branch | `2026-07-12T19:42:59+08:00` | User requested GITP-002 before merge; workflow reopened and reclosed in the correction commit | Commit with AI trailer, then merge with `--no-ff` |
