# Skill Implementer Naming Requirements

## Metadata

- Version: 0.1
- Date: 2026-06-08
- Owner: YuChia-Wei
- Scope: In
  - Rename and clarify generic implementation skills whose current names overemphasize refactoring.
  - Define intent and scope rules for routing code change work.
  - Evaluate whether a dedicated test author / test writer skill is needed.
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
- Preserve architecture-role implementers such as command, query, and reactor implementers.
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

### FR-3: Preserve Architecture-Role Implementer Skills

The following skills should remain architecture-role implementers unless later requirements prove otherwise:

- `command-use-case-implementer`
- `query-use-case-implementer`
- `reactor-implementer`

These skills express architectural roles, not just change size. Generic change skills should not replace them when a task is clearly a command use case, query use case, or reactor implementation.

### FR-4: Update Dev Workflow Routing

The future implementation must update `dev-workflow` capability routing so code changes are not automatically treated as refactoring.

`dev-workflow` should classify:

1. current entry point;
2. work intent;
3. architecture role, if any;
4. change scope;
5. owner skill.

### FR-5: Provide Backward Compatibility For Old Skill Names

The future rename should preserve old skill names as deprecated aliases or compatibility wrappers for a limited migration period.

The migration should:

- keep old wrappers thin;
- point old names to the new canonical skill;
- mark old names as deprecated;
- avoid rewriting historical workflow artifacts unless a migration note is enough.

### FR-6: Evaluate Test Author / Test Writer Before Creating It

The repository should not create a test author or test writer skill until its boundary is decided.

Candidate meanings:

| Candidate | Meaning | Risk |
| --- | --- | --- |
| `test-author` | Authors test plans, test cases, or test specs without necessarily writing code. | May overlap with `bdd-gwt-test-designer` and `spec-author`. |
| `test-writer` | Writes executable test code. | May overlap with implementer skills and require stronger code execution validation. |
| No new skill | Keep BDD scenario design in `bdd-gwt-test-designer`; let implementer skills write tests required for their changes. | Less discoverable for test-only implementation work. |

Recommended initial decision:

- Do not create the skill yet.
- Add it as an open decision for the next `dev-workflow`.
- If created later, prefer `test-author` only if the skill is document/test-design oriented, and `test-writer` only if it writes executable test code.

## Non-Functional Requirements

- Naming must be understandable to humans without reading long descriptions.
- Agent-facing canonical specs should remain English.
- Human-facing guides should use Traditional Chinese Taiwan usage.
- Migration should preserve compatibility for existing runtime users.
- Reference updates must be validated with search.

## Constraints & Assumptions

- This requirement assumes the current repository purpose is clear enough and does not require a root `agents.md` rewrite.
- The rename will affect `.ai/assets/skills/`, `.agents/skills/`, `.claude/skills/`, `.dev/guides/ai-collaboration-guides/`, skill registries, and `dev-workflow` profile references.
- Historical workflow artifacts should not be rewritten solely to replace old skill names.
- The future implementation should be driven by `dev-workflow` and likely executed with `ai-context-governance` for skill registry and wrapper migration.

## Domain / Business Rules

- A skill name should describe either its architectural role or safe change boundary.
- `refactor` is an intent or implementation technique, not the default category for all code changes.
- A generic change implementer must not redefine architecture direction.
- A local change implementer must not expand into a multi-module redesign.
- A change slice implementer must not silently broaden the agreed slice.

## Acceptance Criteria

- The future implementation has a migration plan for replacing `staged-refactor-implementer` and `tactical-refactor-implementer`.
- The new names are based on safe change scope or architectural role, not refactor-only terminology.
- `dev-workflow` routing distinguishes intent, scope, and architecture role.
- Deprecated aliases exist or a deliberate no-alias decision is recorded.
- Test author/writer is either explicitly deferred or defined with a non-overlapping boundary.
- Updated files pass reference search and whitespace validation.

## User Decisions Required

| Decision | Recommended approach | Why |
| --- | --- | --- |
| Final new name for `staged-refactor-implementer` | `change-slice-implementer` | Names the bounded slice without implying pure refactor. |
| Final new name for `tactical-refactor-implementer` | `local-change-implementer` | Names local blast radius clearly and naturally. |
| Keep deprecated aliases? | Yes, for one migration period | Reduces breakage for existing prompts and wrappers. |
| Create test skill now? | No | Boundary overlaps are not resolved yet. |
| If test skill is created later, preferred term? | Use `test-author` for test docs/design; `test-writer` for executable test code | Keeps authoring and implementation separate. |

## Recommended Next Skill

Use `dev-workflow` after user decisions are confirmed.

Expected downstream stages:

1. `ai-context-governance`: skill rename migration plan and wrapper/index sync.
2. `dev-workflow`: route implementation stages and validation checkpoints.
3. Optional `ddd-ca-hex-architect`: only if naming changes reveal deeper architecture-role conflicts.

## References

- `.ai/assets/skills/staged-refactor-implementer/skill.yaml`
- `.ai/assets/skills/tactical-refactor-implementer/skill.yaml`
- `.dev/guides/ai-collaboration-guides/STAGED-REFACTOR-IMPLEMENTER-SKILL-GUIDE.md`
- `.dev/guides/ai-collaboration-guides/TACTICAL-REFACTOR-IMPLEMENTER-SKILL-GUIDE.md`
- `.ai/assets/skills/dev-workflow/references/capability-profile.md`
- `.ai/assets/skills/dev-workflow/references/routing-playbook.md`
