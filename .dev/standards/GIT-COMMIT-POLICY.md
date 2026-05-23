# Git Commit Policy

This policy defines commit title format, commit body structure, and commit timing for agent-assisted work.

## Title Format

When an issue number exists:

```text
<type>(#<issue-number>|<scope>): <summary>
```

When there is no issue number:

```text
<type>(<scope>): <summary>
```

For multiple issue numbers:

```text
<type>(#<issue-number>,#<issue-number>|<scope>): <summary>
```

Examples:

```text
docs(#123|ai-context): define language policy
workflow(#124|governance): add workflow gate
refactor(#125,#128|dotnet-backend): split backend-specific prompt rules
docs(ai-context): inventory context boundaries
```

## Types

Use these commit types:

| Type | Use |
| --- | --- |
| `docs` | Documentation, policy, standards, guides, specs, requirements. |
| `workflow` | Workflow artifacts, task status, review reports, process tracking. |
| `feat` | User-facing or externally visible behavior. |
| `fix` | Bug fixes. |
| `refactor` | Structure changes without intended behavior change. |
| `test` | Test additions or corrections. |
| `chore` | Tooling, housekeeping, generated metadata, or repository maintenance. |

## Scope

The scope should name the affected boundary, not the file extension. Prefer:

- `ai-context`
- `governance`
- `dotnet-backend`
- `repo-structure-sync`
- `skills`
- `workflow`
- `testing`
- `architecture`

## Body Format

Workflow-stage commits should include this body:

```text
Why:
- <why this change exists>

What:
- <main change>
- <main change>

Validation:
- <command or check>
- <skipped validation and reason, if any>

Workflow:
- <workflow-id>
- Stage: <stage-id>
- Task: <task-id>
```

Small direct-mode commits may omit the body when the title is sufficient and the user did not ask for detailed traceability.

## Commit Timing

Create a commit when:

- a workflow stage is completed and validated;
- a task JSON status is updated to `completed`;
- a policy or source-of-truth document is introduced;
- a file move or large rename is completed and references are checked;
- the user explicitly asks for a commit.

Do not commit when:

- the working tree includes unrelated user changes;
- validation is still running or unresolved;
- a task is halfway through a file move;
- the next immediate step may invalidate the current diff;
- the user asked not to commit.

## Workflow Commit Rule

For workflow mode, commit at these boundaries:

1. workflow bootstrap;
2. inventory completed;
3. each policy completed;
4. each skill or wrapper sync completed;
5. each file move batch completed;
6. final validation completed.

If several small policy tasks are completed together and validated together, they may share one commit.

## Validation Notes

Before commit, run the narrowest meaningful validation:

- Markdown or documentation-only changes: `git diff --check` and reference search when links changed.
- JSON task changes: parse changed JSON files.
- Code changes: run the relevant test command or state why tests were not run.

The commit body must mention skipped validation when the skipped check would normally apply.
