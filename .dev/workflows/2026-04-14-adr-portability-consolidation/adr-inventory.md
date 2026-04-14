# ADR Inventory

## Purpose

This inventory is the Stage 1 artifact for `workflow-plan-2026-04-14-adr-portability-consolidation`.
It maps every current ADR to a landing bucket and a primary canonical target so later migration work can proceed without re-deciding ownership.

## Bucket Legend

- `A`
  - portable agent-facing rule in `.ai/`
- `B`
  - framework standard or hard constraint in `.dev/standards/`, `.dev/ARCHITECTURE.MD`, `.dev/requirement/`, or `AGENTS.md`
- `C`
  - pattern usage guide in `.dev/guides/` or `.dev/standards/rationale/`
- `D`
  - retire/delete after landing or because the value is only historical

## Inventory Table

| ADR | Focus | Current Status | Bucket | Primary Landing Target | Notes |
| --- | --- | --- | --- | --- | --- |
| ADR-001 | Use case package and namespace structure | Landed in Standards | B | `.dev/standards/project-structure.md` | Keep as standard only; ADR can retire after reference cleanup. |
| ADR-002 | ORM configuration location | Landed in Standards | C | `.dev/guides/implementation-guides/PERSISTENCE-CONFIGURATION-GUIDE.md` | Usage/application guidance, not a top-level portable AI asset. |
| ADR-003 | DI and configuration structure | Landed in Standards | B | `.dev/standards/ASPNET-CORE-CONFIGURATION-CHECKLIST.md` | Historical Spring naming should be normalized when references are cleaned. |
| ADR-005 | AI task execution SOP | Landed in Standards | C | `.dev/guides/ai-collaboration-guides/AI-COLLABORATION-WORKFLOW-GUIDE.md` | Keep workflow rules in guide form; repo-entry minimum may stay in `AGENTS.md`. |
| ADR-009 | Command/query sub-agent separation | Landed in Standards | A | `.ai/SUB-AGENT-SYSTEM.MD` | Agent-facing routing rule. |
| ADR-010 | Explicit service registration | Landed in Standards | B | `.dev/guides/implementation-guides/DOTNET-DI-TEST-GUIDE.md` | Likely needs a stronger normative home in standards/checklist form. |
| ADR-019 | Outbox pattern implementation | Landed in Standards | B+C | `.dev/standards/coding-standards.md` | Split normative rules to standards; keep implementation walkthrough in a guide. |
| ADR-020 | Archive/query model implementation | Landed in Standards | B | `.dev/standards/coding-standards/archive-standards.md` | Standardized pattern rules. |
| ADR-021 | Aggregate field initialization pattern | Landed in Standards | B | `.dev/standards/coding-standards/aggregate-standards.md` | Hard modeling rule. |
| ADR-023 | Outbox mapper completeness requirement | Landed in Standards | B+C | `.dev/guides/design-guides/FRAMEWORK-API-INTEGRATION-GUIDE.md` | Split mapper requirements into standards if not already explicit enough. |
| ADR-024 | Test isolation and domain event mapper | Landed in Standards | B | `.dev/standards/coding-standards/test-standards.md` | Test constraint. |
| ADR-025 | Mutation testing exclusion policy | Landed in Standards | B | `.dev/standards/coding-standards.md` | Constraint/policy. |
| ADR-031 | Reactor interface definition | Landed in Standards | B | `.dev/standards/coding-standards/reactor-standards.md` | Hard architectural interface rule. |
| ADR-035 | Transaction outbox pattern | Landed in Standards | B | `.dev/standards/coding-standards.md` | Rule-level source. |
| ADR-040 | Profile/environment configuration loading | Landed in Standards | B | `.dev/standards/ASPNET-CORE-CONFIGURATION-CHECKLIST.md` | Hard environment/config rule. |
| ADR-041 | Mapper serialization requirements | Landed in Standards | B | `.dev/standards/coding-standards/mapper-standards.md` | Hard mapper rule. |
| ADR-043 | Audit fields in event metadata | Landed in Standards | B | `AGENTS.md` | Repo-entry baseline constraint. |
| ADR-044 | Profile-based dependency injection | Landed in Standards | C | `.dev/guides/implementation-guides/PROFILE-CONFIGURATION-COMPLEXITY-SOLUTION.md` | How-to and usage guidance. |
| ADR-045 | Sub-agent prompt modularization | Landed in Standards | A | `.ai/SUB-AGENT-SYSTEM.MD` | Agent-facing asset structure rule. |
| ADR-047 | Shared project classification | Landed in Standards | B | `.dev/standards/project-structure.md` | Structural rule. |
| ADR-048 | Solution folder structure | Landed in Standards | B | `.dev/standards/project-structure.md` | Structural rule. |
| ADR-049 | Docker restore-cache csproj copy rule | Landed in Standards | C | `.dev/guides/implementation-guides/DOCKER-RESTORE-CACHE-GUIDE.md` | Pattern usage guide. |
| ADR-052 | Script generation from markdown documentation | Landed in Standards | A | `.ai/scripts/MD-SCRIPT-GENERATION-GUIDE.md` | Portable agent-facing script workflow. |

## Multi-Bucket ADRs That Must Be Split

These ADRs should not migrate as one-to-one copies because they contain both rules and usage/tutorial content:

| ADR | Split Strategy |
| --- | --- |
| ADR-019 | Put must-follow outbox constraints in standards; keep implementation steps and testing walkthrough in a design/implementation guide. |
| ADR-023 | Put mapper completeness requirements in standards if missing; keep framework-specific integration flow in guide form. |

## Early Normalization Findings

### 1. `.ai` vs `.dev/standards/prompts`

- Prompt architecture and reusable agent instructions should keep converging on `.ai/assets/`.
- Human-facing prompt catalogs can remain in `.dev/standards/prompts/` only if clearly marked as wrapper or usage examples, not canonical prompt source.

### 2. Historical naming still leaks into current docs

- ADR-003 and ADR-040 still use `spring` naming in file names.
- These should be treated as historical filenames or renamed when reference cleanup is safe.

### 3. Some guide targets currently hold normative rules

- ADR-010 and ADR-044 both land in implementation guides.
- During Stage 2, decide whether these need a companion standards/checklist file so hard rules are not buried only in prose guides.

## Recommended Retirement Order

1. Retire AI-asset ADRs after `.ai` references are confirmed.
2. Retire pure standards ADRs after standards docs are cross-linked and complete.
3. Retire guide-oriented ADRs after guide/checklist split is normalized.
4. Keep only governance files in `.dev/adr/` unless a genuinely active architecture decision remains uncaptured elsewhere.
