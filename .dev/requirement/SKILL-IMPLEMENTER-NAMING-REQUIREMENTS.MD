# Skill Implementer Naming Requirements

## Metadata

- Version: 0.2
- Date: 2026-06-08
- Owner: YuChia-Wei
- Scope: In
  - Rename and clarify generic implementation skills whose current names overemphasize refactoring.
  - Define intent and scope rules for routing code change work.
  - Record the current test implementer discussion without creating a test skill yet.
- Scope: Out
  - Do not implement the rename in this requirement.
  - Do not modify runtime wrappers, canonical skill registry, or dev-workflow profile yet.
  - Do not redesign command/query/reactor implementer responsibilities unless required by the final routing decision.

## Context & Goals

The current `staged-refactor-implementer` and `tactical-refactor-implementer` names can mislead AI agents. In other projects, agents recommended refactor implementer skills for work that started from new requirements, bug fixes, validation failures, or review remediation. The problem is not that the work never includes refactoring. The problem is that `refactor` is a technique or intent, not the safest primary routing category for all code changes.

This repository needs implementation skill names and routing rules that describe the safe change boundary or architectural role, rather than overclassifying work as refactoring.

Goals:

- Reduce incorrect routing of feature, fix, and remediation work into refactor-only skills.
- Keep generic implementation skill count small.
- Describe generic change skills by change scope and blast radius.
- Re-evaluate whether architecture-role implementers such as command, query, and reactor implementers need to remain separate from generic change-slice implementation.
- Decide whether test authoring needs a dedicated skill or should remain part of existing BDD/spec/implementation flows.

Success means a future `dev-workflow` execution can rename and update the affected skills without re-opening the basic naming rationale.

## Personas

- Human maintainer
  - Wants skill names that match how work is actually requested.
  - Needs clear decisions before skill migration changes many files.
- AI agent
  - Needs routing rules that distinguish work intent from change scope.
  - Must not treat every code change as refactoring.
- Downstream project user
  - Wants to use these skills in product repositories without confusing feature work, bug fixes, and pure refactoring.

## Functional Requirements

### FR-1: Rename Generic Refactor Skills By Change Scope

The repository should rename generic refactor implementer skills to neutral change-oriented names.

Recommended naming:

| Current skill | Recommended new name | Meaning |
| --- | --- | --- |
| `staged-refactor-implementer` | `change-slice-implementer` | Implements one bounded change slice that may be feature, fix, remediation, cleanup, or refactor. |
| `tactical-refactor-implementer` | `local-change-implementer` | Implements one local code change around a class, object, method, symbol, or direct call sites. |

The final names must avoid implying that the skill is only for behavior-preserving refactoring.

### FR-2: Separate Work Intent From Change Scope

Generic implementation skills should require explicit intent and scope.

Intent examples:

- `feature`
- `bug-fix`
- `review-remediation`
- `validation-failure-remediation`
- `behavior-correction`
- `refactor`
- `cleanup`

Scope examples:

- `local`
- `slice`
- `architecture-level`

Routing should choose the skill primarily by safe scope and architectural role, then record the intent in the task or prompt.

### FR-3: Re-Evaluate Implementer Classification Consistency

The current implementer skill family mixes different classification axes:

- architecture role: `command-use-case-implementer`, `query-use-case-implementer`, `reactor-implementer`;
- change scope: proposed `change-slice-implementer`, `local-change-implementer`;
- original technique-oriented naming: refactor implementers.

This inconsistency must be resolved before skill rename implementation.

Open classification question:

- If `change-slice-implementer` can handle a bounded cross-role change, can it also handle command, query, or reactor changes?
- If yes, why should command/query/reactor remain separate skills?
- If no, what specialist quality or architecture contract do command/query/reactor skills provide that a generic change-slice skill cannot?

This requirement does not decide the final answer yet.

Recommended analysis direction:

1. compare command/query/reactor implementer outputs against a generic change-slice output contract;
2. identify whether their value is architecture-specific implementation knowledge, prompt convenience, or historical naming;
3. keep only distinctions that can be explained clearly to a team.

### FR-4: Update Dev Workflow Routing

The future implementation must update `dev-workflow` capability routing so code changes are not automatically treated as refactoring.

`dev-workflow` should classify:

1. current entry point;
2. work intent;
3. architecture role, if any;
4. change scope;
5. owner skill.

### FR-5: Remove Old Skill Names Without Alias

The future rename should remove old skill names instead of keeping deprecated aliases.

The migration should:

- delete old canonical skill directories and runtime wrappers as part of the rename;
- update active registries, wrappers, guides, and `dev-workflow` profile references;
- leave historical workflow artifacts unchanged unless a short migration note is useful;
- rely on git history for recovery if a deleted skill name needs to be inspected later.

### FR-6: Defer Test Implementer Skill

The repository should not create a test author, test writer, or test implementer skill in this workflow.

Current decision:

- test documentation and design should remain covered by `bdd-gwt-test-designer` and related spec workflows;
- a future executable test skill, if needed, should likely be named `test-implementer`;
- the likely responsibility would be analyzing classes or behaviors without adequate tests and creating executable tests;
- details are not mature enough to include in the current implementation rename workflow.

Deferred candidate:

| Candidate | Meaning | Current status |
| --- | --- | --- |
| `test-implementer` | Finds missing executable test coverage and adds tests for existing behavior or changed behavior. | Deferred; needs separate requirement. |

## Non-Functional Requirements

- Naming must be understandable to humans without reading long descriptions.
- Agent-facing canonical specs should remain English.
- Human-facing guides should use Traditional Chinese Taiwan usage.
- Migration may remove old runtime skill names directly; compatibility aliases are not required.
- Reference updates must be validated with search.

## Constraints & Assumptions

- This requirement assumes the current repository purpose is clear enough and does not require a root `agents.md` rewrite.
- The rename will affect `.ai/assets/skills/`, `.agents/skills/`, `.claude/skills/`, `.dev/guides/ai-collaboration-guides/`, skill registries, and `dev-workflow` profile references.
- Historical workflow artifacts should not be rewritten solely to replace old skill names.
- The future implementation should be driven by `dev-workflow` and likely executed with `ai-context-governance` for skill registry and wrapper migration.
- Implementer classification must remain an open decision until the architecture-role versus change-scope distinction can be explained clearly.

## Domain / Business Rules

- A skill name should use one consistent classification model within the implementer family, or explicitly document why a different axis is used.
- `refactor` is an intent or implementation technique, not the default category for all code changes.
- A generic change implementer must not redefine architecture direction.
- A local change implementer must not expand into a multi-module redesign.
- A change slice implementer must not silently broaden the agreed slice.
- If local change work requires extracting a class, extracting an interface, changing dependency direction, or changing domain language, it must stop and escalate to architecture review or a larger change-slice workflow.

## Acceptance Criteria

- The future implementation has a migration plan for replacing `staged-refactor-implementer` and `tactical-refactor-implementer`.
- The new names are based on safe change scope or architectural role, not refactor-only terminology.
- `dev-workflow` routing distinguishes intent, scope, and architecture role.
- Old skill names are removed directly, or any retained alias is justified against the current no-alias decision.
- Test implementer is explicitly deferred and not mixed into the rename workflow.
- The implementer family classification model is documented before any rename is implemented.
- Updated files pass reference search and whitespace validation.

## User Decisions Required

| Decision | Recommended approach | Why |
| --- | --- | --- |
| Final new name for `staged-refactor-implementer` | `change-slice-implementer` | Names the bounded slice without implying pure refactor. |
| Final new name for `tactical-refactor-implementer` | `local-change-implementer` | Names local blast radius clearly and naturally. |
| Keep deprecated aliases? | No | The repository is still being actively organized and git history is enough for recovery. |
| Create test skill now? | No | Boundary overlaps are not resolved yet. |
| If test skill is created later, preferred term? | `test-implementer` | The possible gap is executable test creation, while BDD/test design is already covered. |

## Open Decisions

| Decision | Current concern | Suggested next step |
| --- | --- | --- |
| Should command/query/reactor implementers remain separate from `change-slice-implementer`? | The current taxonomy mixes architecture role and change scope, making it hard to explain to a team. | Compare their actual input/output contracts and decide whether the architecture-specific skills provide unique value. |
| Should `change-slice-implementer` become the single bounded implementation skill? | It may be able to handle command/query/reactor work if given clear requirements/specs. | Evaluate whether specialist skills mainly encode architecture knowledge or just convenience prompts. |
| Where should local change escalate? | Local changes can discover new class/interface/dependency needs. | Require escalation to architect or change-slice planning when new abstraction or architecture boundary appears. |

## Recommended Next Skill

Use `dev-workflow` after user decisions are confirmed.

Expected downstream stages:

1. `dev-workflow`: plan the implementer taxonomy decision workflow before renaming.
2. `ai-context-governance`: execute confirmed skill rename migration and wrapper/index sync.
3. Optional `ddd-ca-hex-architect`: evaluate whether command/query/reactor skills encode architecture-specific contracts that should remain separate.

## References

- `.ai/assets/skills/staged-refactor-implementer/skill.yaml`
- `.ai/assets/skills/tactical-refactor-implementer/skill.yaml`
- `.dev/guides/ai-collaboration-guides/STAGED-REFACTOR-IMPLEMENTER-SKILL-GUIDE.md`
- `.dev/guides/ai-collaboration-guides/TACTICAL-REFACTOR-IMPLEMENTER-SKILL-GUIDE.md`
- `.ai/assets/skills/dev-workflow/references/capability-profile.md`
- `.ai/assets/skills/dev-workflow/references/routing-playbook.md`
