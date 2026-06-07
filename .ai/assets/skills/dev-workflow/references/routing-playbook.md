# Dev Workflow Routing Playbook

Use this playbook after the workflow gate confirms the work needs stage planning, skill orchestration, or durable task tracking.

## Routing Rules

| Work intent | Route to | Notes |
| --- | --- | --- |
| AI context cleanup, language policy, prompt boundary, wrapper sync, skill registry cleanup | `ai-context-governance` | Use this for `.ai`, `.dev`, `.agents`, `.claude`, and context migration governance. |
| First sync after copying this framework into another repo | `repo-structure-sync` | Use before requirement, spec, or architecture authoring in the target repo. |
| Requirement drafting or normalization | `requirement-author` | Stop at requirement quality; do not jump into specs unless explicitly staged. |
| Spec drafting or normalization | `spec-author` | Use after requirement truth is clear. |
| First problem frame extraction | `problem-frame-author` | Use when a validator-ready problem frame is needed. |
| .NET backend architecture design | `ddd-ca-hex-architect` | Use for bounded contexts, aggregates, ports/adapters, CQRS, messaging, or architecture refactoring direction. |
| GWT scenario and assertion design | `bdd-gwt-test-designer` | Use for test intent and scenario design only. |
| Command use case implementation | `command-use-case-implementer` | Use after requirement/spec/architecture direction is stable. |
| Query use case implementation | `query-use-case-implementer` | Use after read-model/query behavior is clear. |
| Reactor implementation | `reactor-implementer` | Use for event-driven consistency or projection reactions. |
| Staged refactoring execution | `staged-refactor-implementer` | Use when the refactor stage is already decided. |
| Local tactical refactor | `tactical-refactor-implementer` | Use for one object or symbol with bounded local change. |
| .NET backend code review | `code-reviewer` | Use for code quality review; do not use it as a planning skill. |
| Problem-frame compliance gate | `spec-compliance-validator` | Use when problem-frame coverage must be validated. |

## Orchestration Boundaries

- `dev-workflow` may decide the stage sequence, update workflow task status, and request the next skill.
- `dev-workflow` must not invent downstream skill findings or claim a domain result without running or applying the downstream workflow.
- When two skills could apply, route by the source of truth being changed:
  - process, context, language, wrapper, or registry truth: `ai-context-governance`
  - product or code architecture truth: `ddd-ca-hex-architect`
  - requirement truth: `requirement-author`
  - behavior specification truth: `spec-author`
  - test scenario truth: `bdd-gwt-test-designer`
  - implementation truth: an implementer skill
  - review truth: `code-reviewer` or `spec-compliance-validator`

## Handoff Packet

When handing a stage to another skill or sub-agent, include:

1. workflow id and task id;
2. stage goal and non-goals;
3. source files and policies already read;
4. user constraints and open decisions;
5. expected output files or output sections;
6. validation expected before returning.
