# Landing Zone Normalization

## Purpose

This Stage 2 artifact fixes canonical ownership before ADR content is moved.
The goal is to prevent the same rule family from remaining duplicated across `.ai/`, `.dev/standards/`, and `.dev/guides/`.

## Decisions

### 1. Prompt content ownership

- Decision:
  - `.ai/` is the only canonical home for reusable prompt content, prompt packages, shared prompt rules, sub-agent prompt assets, and agent-facing prompt templates.
- Rationale:
  - `.ai/INDEX.MD` and `.ai/README.MD` already define `.ai/` as the agent-facing portable baseline.
  - Keeping prompt bodies under `.dev/standards/prompts/` creates duplicate ownership and weakens portability.
- Result:
  - `.dev/standards/prompts/` should be reduced to either:
    - a thin human-facing pointer/index, or
    - removed after references are migrated

### 2. Human-facing prompt documentation

- Decision:
  - Human-facing instructions about how to use prompts belong in `.dev/guides/ai-collaboration-guides/`, not in `.dev/standards/prompts/`.
- Rationale:
  - Standards should hold rules and constraints.
  - Guides should explain invocation, workflow, and examples for humans.

### 3. Hard rules must not live only inside guides

- Decision:
  - When an ADR contains mandatory constraints that are currently discoverable only in a guide, the rule must be elevated into `.dev/standards/` before the ADR is retired.
- Known gaps:
  - ADR-010 explicit registration rule
  - ADR-040 environment/profile loading rule
  - ADR-044 profile-specific DI constraints

### 4. Split rule docs from usage docs

- Decision:
  - A pattern with both mandatory rules and implementation walkthroughs must be split:
    - mandatory constraints to `.dev/standards/`
    - walkthrough/how-to to `.dev/guides/`
- Immediate candidates:
  - ADR-019 outbox pattern
  - ADR-023 outbox mapper completeness and integration guidance

### 5. Historical naming cleanup is part of migration quality

- Decision:
  - Historical Java/Spring naming can remain temporarily for traceability, but any surviving canonical file after ADR retirement should use .NET-first naming and wording when safe.
- Immediate candidates:
  - ADR-003 and ADR-040 references
  - any standards/checklists that still describe .NET rules through Spring terminology

## Canonical Ownership Matrix

| Content Type | Canonical Location | Non-Canonical Locations |
| --- | --- | --- |
| reusable prompt body | `.ai/` | `.dev/standards/prompts/` |
| reusable sub-agent routing rule | `.ai/` | guides or ADRs |
| hard engineering constraint | `.dev/standards/` or `AGENTS.md` | guides only |
| pattern application tutorial | `.dev/guides/` | ADRs as day-to-day source |
| historical rationale only | retired ADR or rationale doc if still useful | `.ai/` |

## Stage 3 Preconditions

Before migrating ADR content:

1. Each targeted ADR must have one primary canonical destination.
2. If a guide is currently the only place holding hard rules, add or choose the standards target first.
3. If a standards prompt file still owns actual prompt text, move that content into `.ai/` before ADR retirement.

## Recommended Stage 3 Work Order

1. `.ai` ownership cleanup
   - reduce `.dev/standards/prompts/` to pointer-only or deprecate it
2. standards gap filling
   - add missing hard rules for ADR-010, ADR-040, ADR-044
3. split mixed ADR families
   - ADR-019 and ADR-023
4. only then retire duplicate ADR guidance
