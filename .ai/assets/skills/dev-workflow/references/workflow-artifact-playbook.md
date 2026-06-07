# Workflow Artifact Playbook

Use workflow artifacts when work crosses stages, changes source-of-truth, changes AI context or skill routing, needs sub-agent handoff, or is likely to touch multiple repository boundaries.

## Artifact Layout

```text
.dev/workflows/<workflow-id>/
  workflow-plan.md
  review-report.md
  tasks/
    <task-id>.json
```

`review-report.md` is optional and should be created only when review output is produced.

## Workflow Plan

The workflow plan should capture:

- metadata: plan id, owner skill, status;
- problem statement and current scope;
- target direction and constraints;
- stages, goals, scope, risks, and recommended implementers;
- validation strategy;
- open questions and dependencies;
- completion summary when closed.

## Task JSON

Each task JSON should capture:

- `task_id`;
- `owner_skill`;
- `related_plan_id`;
- `status`;
- scope target, files, dependency radius, constraints, and non-goals;
- inputs and user constraints;
- execution steps, validation, and deferred items;
- results after completion.

Use these statuses:

```text
pending -> in_progress -> completed
```

Use `deferred` only when the work is intentionally postponed and the task or plan explains why.

## Stage Update Rules

- Mark a task `in_progress` before making material edits for that task.
- Mark a task `completed` only after the task output exists and the narrow validation has passed.
- Record skipped validation when it would normally apply.
- Keep task results factual: changed files, commands run, and follow-up state.
- Do not close the workflow plan until final validation has passed.
