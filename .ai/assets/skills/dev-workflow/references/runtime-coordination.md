# Dev Workflow Runtime Coordination

Use this reference when `dev-workflow` runs inside a runtime that has its own goal, workflow, command, routine, or automation feature.

Runtime features and `dev-workflow` operate at different layers:

- runtime goal or objective tracking keeps the current task durable;
- runtime workflow or command features provide an execution surface;
- `dev-workflow` defines the repository/team software-development lifecycle orchestration policy;
- downstream skills perform specialist work.

## Intent-Based Runtime Activation

A runtime should select this contract from a high-level multi-stage
software-development request even when the user does not write
`$dev-workflow`, `dev-workflow`, or downstream skill names. A named command may
remain a convenience, but the activation signal is the requested outcome,
current lifecycle artifacts, mutation scope, and need for approval or durable
tracking.

After activation:

- map intent to generic capability slots before resolving providers;
- pause before implementation while requirement, design, or specification
  approval is pending;
- use repository and target policy as process truth;
- do not treat runtime completion, a skill invocation, a push, or a merge as
  product closeout.

## Layer Model

| Layer | Responsibility | Typical examples |
| --- | --- | --- |
| Runtime tracker | Preserve the durable objective, session state, or continuation rule. | Codex Goal, thread objective, long-running task tracker. |
| Runtime workflow | Start or automate a repeatable runtime procedure. | Claude workflow, slash command, routine, automation. |
| `dev-workflow` | Decide the development entry point, workflow mode, development capability routing, artifacts, validation, and commit checkpoints. | `.dev/workflows/<workflow-id>/`, development stage routing, handoff packets. |
| Downstream skills | Execute specialist stages. | requirements, specs, architecture, implementation, review, compliance. |

## Codex Goal Pattern

Use a Codex Goal for the durable software-development objective. Put `dev-workflow` inside that goal as the development orchestration policy.

Prompt shape:

```text
Goal:
- <durable software or product development objective>

Use $dev-workflow as the orchestration policy.

Rules:
- Detect the current entry point from existing requirement/spec/workflow artifacts.
- Create or update workflow artifacts when workflow mode applies.
- Route stages through capability slots, local profile, or skill discovery.
- Use fallback-mode only when no downstream skill or reliable standard is available.
- Execute target-owned unit and integration tests by default; run specialized tests only when selected.
- Treat unselected spec compliance as not applicable and selected compliance as a 100% fail-closed gate.
- Commit after a validated durable stage or coherent bounded batch.
- Keep working until the goal is complete or a direction decision is required.
```

## Claude Workflow Pattern

Use a Claude workflow, slash command, or routine as the runtime trigger. Put `dev-workflow` in the workflow prompt as the planning and routing policy.

Prompt shape:

```text
Run the team dev workflow.

Use $dev-workflow as the orchestration policy for this repository.

Inputs:
- Objective: <software or product development objective>
- Existing artifacts: <requirements/specs/workflow/task paths, if any>
- Constraints: <branch, commit, validation, issue number, model/sub-agent constraints>

Execution:
- Detect the entry point.
- Plan stages with capability slots.
- Resolve skills from the active profile or discovery playbook.
- Create or update .dev/workflows/<workflow-id>/ when workflow mode applies.
- Honor approval pauses before implementation.
- Record exact target-owned test outcomes and selected compliance gates.
- Execute stages until done, blocked, or a user direction decision is required.

Return:
- selected mode
- stage plan
- skill routing and confidence
- workflow artifacts
- validation and commit checkpoints
- open decisions
```

## Entry Point Detection

`dev-workflow` should not always restart from requirements.

| Available input | Starting point |
| --- | --- |
| Raw idea only | `requirements` |
| Requirement artifacts exist | `specification` or `architecture` |
| Requirement and spec artifacts exist | `architecture`, `test-design`, or `implementation` |
| Workflow task artifacts exist | current task status |
| Implementation exists | `review` or `compliance-validation` |

An artifact's existence does not prove approval. Before moving from requirement,
design, or specification work into implementation, verify and record the
authorization source.

## Runtime-Agnostic Prompt Contract

When writing prompts for any runtime, include:

1. objective;
2. current artifacts or state;
3. requested runtime behavior;
4. `dev-workflow` orchestration rules;
5. validation expectations;
6. commit or handoff expectations;
7. target-owned test commands, prerequisites, policy, and selected levels;
8. whether spec compliance is selected;
9. when to ask the user for a direction decision.

Do not make runtime workflows the source of truth for repository process rules. Runtime workflows should invoke `dev-workflow`; `dev-workflow` should point to repository policies and downstream skills.
