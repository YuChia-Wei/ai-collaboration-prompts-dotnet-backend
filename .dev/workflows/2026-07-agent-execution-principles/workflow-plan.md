# Agent Execution Principles Workflow

- Plan ID: `2026-07-agent-execution-principles`
- Owner skill: `dev-workflow`
- Supporting skill: `ai-context-governance`
- Status: `in_progress`

## Problem

The root collaboration guide defines repository routing and workflow rules but does not state concise default execution principles for assumptions, scope control, speculative work, and completion verification.

## Direction

Add repository-wide execution principles to the English agent guide and keep the Traditional Chinese translation synchronized.

The principles must:

- prohibit invented project truth while allowing disclosed, low-risk assumptions;
- require the smallest coherent change that satisfies defined criteria;
- prevent unrelated edits and cleanup;
- require verifiable completion criteria and explicit blocker reporting.

## Stages

1. Record the governance decision and target wording.
2. Update `agents.md` and `agents.zh-tw.md`.
3. Validate translation alignment, formatting, and references.

## Validation

- Compare the English and Traditional Chinese principle lists.
- Run `git diff --check`.
- Confirm the task result records the changed files and validation.

## Constraints

- Do not create a new skill for universal execution behavior.
- Do not duplicate the detailed workflow or implementation rules already owned by standards and skills.
- Do not change unrelated agent routing or repository identity content.

## Open Questions

None. The user approved adding the recommended principles and merging the completed branch into `main`.

