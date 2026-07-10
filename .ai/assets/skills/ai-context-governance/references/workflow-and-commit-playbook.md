# Workflow and Commit Playbook

Use this playbook when AI context cleanup is large enough to need workflow tracking or commits.

## Workflow Gate

Check `.dev/standards/WORKFLOW-GATE-POLICY.md`.

Create a workflow when cleanup:

- changes source-of-truth rules;
- reorganizes `.ai`, `.dev`, `.agents`, or `.claude`;
- affects future agent behavior;
- crosses skill boundaries;
- needs multiple stages or task status.

## Skill-Owned Workflow Contract

Use the workflow templates owned by this skill for AI context maintenance. Do not depend on a universal workflow body template.

- Workflow id: `YYYY-MM-DD-topic[-NN]`.
- Stable locator: `.dev/workflows/<workflow-id>/workflow.yaml`.
- `artifact_root` may be the locator directory or another repository path selected for the task.
- Timestamps: ISO 8601 with an explicit offset, for example `2026-07-10T18:22:49+08:00`.
- Preserve `created_at`; update `updated_at` whenever an artifact changes.
- Generated artifacts must record `template_source` and `template_version`.

If the base id already exists, append `-02`, `-03`, and so on. Do not infer sequence from an ambiguous month-only directory name.

## Commit Policy

Check `.dev/standards/GIT-COMMIT-POLICY.md`.

For workflow-stage commits, use:

```text
<type>(<scope>): <summary>
```

or with issue number:

```text
<type>(#<issue-number>|<scope>): <summary>
```

Include body sections:

- `Why`
- `What`
- `Validation`
- `Workflow`

## Task Updates

When completing a task:

- set `status` to `completed`;
- summarize changed files in `results.files_changed`;
- list validation in `results.tests_run`;
- leave `follow_up_needed` true only when another explicit task remains outside the current workflow.
- update the task's `updated_at` while preserving `created_at`.
