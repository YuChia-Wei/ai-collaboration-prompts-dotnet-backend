# Workflow Gate Policy

This policy defines when an agent should create workflow artifacts proactively instead of using direct mode.

## Default Modes

| Mode | Use |
| --- | --- |
| Direct mode | Small, single-pass work that does not need long-lived context. |
| Workflow mode | Multi-stage work that changes source-of-truth, crosses skill boundaries, or needs task status tracking. |

## Must Create a Workflow

Create `.dev/workflows/<workflow-id>/` when any of these are true:

- the task needs two or more stages;
- the task needs cross-skill or sub-agent handoff;
- the task changes canonical source-of-truth rules;
- the task reorganizes `.ai/`, `.dev/`, `.agents/`, `.claude/`, or wrapper routing;
- the task affects future agent behavior;
- the task needs plan, review, or task status artifacts;
- the task involves document governance, source-of-truth cleanup, or context boundary changes;
- the task will likely touch five or more files;
- the user uses wording such as "workflow", "規劃", "整理", "重構", "標準化", "治理", or "拆分" for repo-wide documentation or context work.

## Direct Mode Is Enough

Direct mode is acceptable when all of these are true:

- the change is small and local;
- only one skill is needed;
- no durable decision trail is required;
- no canonical rule or source-of-truth boundary changes;
- no task status needs to be preserved;
- validation can be completed in the same turn.

## Workflow Artifacts

When workflow mode is used, create:

```text
.dev/workflows/<workflow-id>/
  workflow-plan.md
  tasks/
    <task-id>.json
```

Add `review-report.md` when the workflow includes formal review findings or a review gate.

## Task Status Rule

Each task JSON should move through:

```text
pending -> in_progress -> completed
```

Use `deferred` only when the task is intentionally postponed and the workflow plan or task results explain why.

## Commit Rule

Workflow stages should follow `.dev/standards/GIT-COMMIT-POLICY.md`. Commit after a stage or coherent task batch completes and validation has passed.

## Workflow Closing Checklist

Before sending a final response in workflow mode, the agent must verify all of the following:

- workflow plan and task artifacts reflect the completed or deferred state;
- required validation has passed, or skipped validation is explicitly recorded with a reason;
- `.dev/standards/GIT-COMMIT-POLICY.md` has been checked for commit requirements;
- when the commit policy requires a commit, the commit has been created before claiming completion;
- when no commit is created, the final response cites the exact policy exception that applies.
