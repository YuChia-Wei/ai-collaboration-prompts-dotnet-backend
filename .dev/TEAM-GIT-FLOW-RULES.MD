# Team Git Flow Rules

This document defines the current repository git flow.

## Core Rule

`main` is the only long-lived trunk.

All feature, workflow, documentation, and agent work branches start from `main` and merge back to `main` when complete.

## Branch Model

### Long-Lived Branches

| Branch | Role |
| --- | --- |
| `main` | Single trunk and integration branch. Must stay coherent and reviewable. |

Do not create persistent `develop`, `baseline`, `release`, or agent-specific long-lived branches for normal work.

### Short-Lived Branches

Use short-lived branches for bounded work:

| Prefix | Use |
| --- | --- |
| `codex/` | Codex-owned workflow or task branch. |
| `claude/` | Claude-owned workflow or task branch. |
| `gemini/` | Gemini-owned workflow or task branch. |
| `docs/` | Human-authored documentation branch when no agent prefix is appropriate. |
| `fix/` | Small human-authored fix branch when no agent prefix is appropriate. |

Use the agent prefix when an agent performs the work.

## Normal Flow

1. Start from a clean `main`.
2. Create a short-lived branch:

   ```text
   <prefix>/<topic>
   ```

3. Make focused commits following `.dev/standards/GIT-COMMIT-POLICY.md`.
4. Run the narrowest meaningful validation.
5. Merge back to `main` with no fast-forward:

   ```bash
   git checkout main
   git merge --no-ff <branch-name>
   ```

6. Confirm `main` is clean after merge.

## Workflow Branches

When work uses `.dev/workflows/<workflow-id>/`, prefer:

```text
codex/<workflow-id>
claude/<workflow-id>
gemini/<workflow-id>
```

Examples:

```text
codex/2026-05-ai-context-skill-and-doc-cleanup
claude/payment-refactor-stage-1
gemini/spec-cleanup
```

## Merge Rule

Use `--no-ff` for workflow and multi-commit branches so the branch work remains visible as a grouped unit.

Fast-forward merge is acceptable only for tiny direct-mode branches when the user or maintainer explicitly chooses it.

## Commit Rule

Commit formatting and commit timing are defined in:

```text
.dev/standards/GIT-COMMIT-POLICY.md
```

Do not duplicate detailed commit message rules here.

## Workflow Gate

When deciding whether a task needs a workflow branch and workflow artifacts, follow:

```text
.dev/standards/WORKFLOW-GATE-POLICY.md
```

## Cleanup Before Merge

Before merging a short-lived branch back to `main`:

- confirm workflow task statuses are accurate;
- confirm validation was run or skipped with a documented reason;
- remove accidental temporary files;
- keep intentional workflow artifacts when they are part of the decision trail;
- run `git status --short` and confirm only intended changes were committed.

## Outdated Branch Models

The following branch models are not used for current work:

- persistent `baseline/*` integration branches;
- persistent `release/*` cleanup branches;
- `develop` as a second long-lived integration line;
- agent-specific long-lived branches.

Reintroduce any of these only after updating this document and the related workflow policy.
