# Dev Workflow Routing Playbook

Use this playbook after the workflow gate confirms the work needs stage planning, skill orchestration, or durable task tracking.

## Routing Model

Route in two steps:

1. Map each stage to a generic capability slot.
2. Resolve the slot through the active capability profile.

If the active profile has no matching downstream skill, use `fallback-playbooks.md` and clearly mark the stage as fallback-mode.

## Generic Capability Slots

| Work intent | Capability slot | Expected specialist output |
| --- | --- | --- |
| Workflow planning, stage sequencing, task tracking, validation and commit checkpoints | `workflow-orchestration` | Stage plan, artifact decision, checkpoint plan, final evidence summary. |
| AI context cleanup, language policy, prompt boundaries, wrapper sync, skill registry cleanup | `context-governance` | Context classification, source-of-truth decision, migration or wrapper sync plan. |
| First sync after copying a framework or template into a target repo | `repo-initialization` | Repo inventory, stale template fact classification, entry document refresh plan. |
| Requirement drafting or normalization | `requirements` | Requirement draft, assumptions, gaps, source-truth notes. |
| Spec drafting or normalization | `specification` | Behavior or component spec, source references, handoff notes. |
| First problem-frame extraction | `problem-framing` | Validator-ready problem frame draft and source evidence. |
| Architecture design or architecture refactoring direction | `architecture` | Bounded design decision, tradeoffs, target structure, non-goals. |
| GWT scenario and assertion design | `test-design` | Scenarios, assertion points, test level recommendation. |
| Bounded implementation | `implementation` | Code or document changes for a bounded task, narrow validation. |
| Refactoring execution | `refactoring` | Scoped refactor changes and regression validation. |
| Code or artifact review | `review` | Findings, severity, evidence, residual risk. |
| Compliance or coverage gate | `compliance-validation` | Coverage result, missing evidence, pass/fail gate. |

## Local Profile Resolution

For this repository, resolve slots through `capability-profile.md`.

The current local profile maps slots to these concrete skills:

| Capability slot | Local skill |
| --- | --- | --- |
| `context-governance` | `ai-context-governance` |
| `repo-initialization` | `repo-structure-sync` |
| `requirements` | `requirement-author` |
| `specification` | `spec-author` |
| `problem-framing` | `problem-frame-author` |
| `architecture` | `ddd-ca-hex-architect` |
| `test-design` | `bdd-gwt-test-designer` |
| `implementation` | `command-use-case-implementer`, `query-use-case-implementer`, or `reactor-implementer` |
| `refactoring` | `staged-refactor-implementer` or `tactical-refactor-implementer` |
| `review` | `code-reviewer` |
| `compliance-validation` | `spec-compliance-validator` |

## Orchestration Boundaries

- `dev-workflow` may decide the stage sequence, update workflow task status, and request the next skill.
- `dev-workflow` must not invent downstream skill findings or claim a domain result without running or applying the downstream workflow.
- When two capability slots could apply, route by the source of truth being changed:
  - process, context, language, wrapper, or registry truth: `context-governance`
  - repo template or initialization truth: `repo-initialization`
  - product or code architecture truth: `architecture`
  - requirement truth: `requirements`
  - behavior specification truth: `specification`
  - test scenario truth: `test-design`
  - implementation truth: `implementation`
  - review truth: `review` or `compliance-validation`
- If no matching local skill exists, call out fallback-mode explicitly and use `fallback-playbooks.md`.

## Handoff Packet

When handing a stage to another skill or sub-agent, include:

1. workflow id and task id;
2. stage goal and non-goals;
3. source files and policies already read;
4. user constraints and open decisions;
5. expected output files or output sections;
6. validation expected before returning.
