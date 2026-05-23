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
