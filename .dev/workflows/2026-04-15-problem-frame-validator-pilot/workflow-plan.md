# Workflow Plan

## Metadata

- `plan_id`: `workflow-plan-2026-04-15-problem-frame-validator-pilot`
- `owner_skill`: `ddd-ca-hex-architect`
- `status`: `completed`

## Context

- Problem statement: The repository ships a .NET problem-frame spec compliance validator, but currently has no portable problem-frame artifacts that let the validator demonstrate real value.
- Current scope: Add a minimal workflow plus a validator-ready example for an external-system integration use case.
- Why this workflow now: The repository is intended to be imported into real projects, so the validator needs a concrete, teachable starting point instead of a gate with no input.

## Target Direction

- Target architecture summary: Keep requirement and spec documents as human-facing truth, and add problem-frame documents as a structured verification layer per use case.
- Key constraints:
  - Use the validator's expected directory structure and file names.
  - Keep the example portable and generic enough to copy into another repository.
  - Use an external-system-dependent command use case so the value of frame concerns is obvious.
- Non-goals:
  - No full problem-frame methodology rollout across the entire repository.
  - No production code generation in this workflow.
  - No claim that all teams must adopt problem frames.

## Stages

### Stage 1
- Goal: Define the pilot workflow and the role of problem frames in this repository.
- Scope: Workflow artifacts plus a short problem-frame guide for this repository.
- Non-goals: Deep academic explanation of Problem Frames theory.
- Risks: Over-specifying the process before the team has run a pilot.
- Recommended implementer: `ddd-ca-hex-architect`

### Stage 2
- Goal: Add a validator-ready CBF example for an external payment authorization use case.
- Scope: `frame.yaml`, `machine/machine.yaml`, `machine/use-case.yaml`, `controlled-domain/aggregate.yaml`, `acceptance.yaml`, and a reusable template set.
- Non-goals: Generated .NET code and tests.
- Risks: The example could become too domain-specific to reuse.
- Recommended implementer: `staged-refactor-implementer`

## Validation Strategy

- Reviewer checkpoints:
  - The new files match the validator's expected structure.
  - The example clearly shows how requirements/specs map into problem-frame artifacts.
  - The example highlights external-system constraints, retries, idempotency, and asynchronous confirmation.
- Tests/validation expectations:
  - Structural validation by file presence and content inspection.
  - Manual dry-run against the validator's required inputs.

## Notes

- Open questions:
  - Whether future repos should standardize on CBF first and add SWF later.
  - Whether a separate authoring guide should be added after the pilot is evaluated.
- Dependencies:
  - `.agents/skills/spec-compliance-validator/SKILL.md`
  - `.dev/workflows/templates/*`
