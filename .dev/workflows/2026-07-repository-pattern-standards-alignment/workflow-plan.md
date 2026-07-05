# Repository Pattern Standards Alignment Workflow

## Metadata

- Plan ID: `workflow-plan-2026-07-repository-pattern-standards-alignment`
- Workflow ID: `2026-07-repository-pattern-standards-alignment`
- Owner skill: `dev-workflow`
- Status: `awaiting-user-decisions`
- Created: `2026-07-05`
- Branch state at bootstrap: detached HEAD
- Issue: not provided

## Problem Statement

The repository pattern guidance does not currently provide one reliable execution contract. Active standards, architecture references, prompts, examples, and generated checks disagree on:

- repository abstraction name;
- allowed operation set;
- command-side persistence technology;
- query-side layering;
- custom repository interface policy;
- soft-delete behavior;
- transaction and domain-event lifecycle;
- automated enforcement.

These conflicts can cause generated code, reviews, tests, and future context synchronization to enforce incompatible designs.

The baseline findings are retained in [review-report.md](./review-report.md).

## Scope

### In scope

- Establish the canonical command-side repository contract.
- Establish query-side port and adapter placement.
- Align Dapper, Npgsql, EF Core, Unit of Work, and outbox responsibilities.
- Resolve aggregate deletion and domain-event lifecycle rules.
- Update canonical `.dev` standards and architecture references.
- Synchronize dependent `.ai` context, prompts, guides, examples, and checks.
- Replace or constrain checks that cannot safely validate semantic architecture rules.

### Non-goals

- No product application implementation.
- No target-repository migration.
- No unrelated standards cleanup.
- No broad documentation translation unless explicitly approved.
- No runtime wrapper redesign unless a canonical skill contract is affected.
- No cross-bounded-context communication redesign.

## Governing Constraints

- DDD + Clean Architecture + CQRS remains the base architecture.
- Hexagonal Architecture defines application ports and infrastructure adapters.
- Cross-bounded-context communication remains MQ-only.
- Domain objects remain independent of ORM, broker, and transport concerns.
- Write-side technology is currently declared as Dapper + Npgsql.
- Read/projection technology is currently declared as EF Core or Dapper.
- Runtime wrappers must remain thin.
- `.dev/standards/**` is agent-facing execution context; new normative text should follow the language policy.
- User decisions must be recorded before canonical standards are rewritten.

## Target Direction

The following direction is recommended but is not approved until the open decisions are answered:

1. Use `IDomainRepository<TAggregate, TId>` as the command-side outbound port name.
2. Keep the generic contract limited to aggregate lifecycle operations.
3. Exclude bulk operations from the generic contract.
4. Model soft deletion as aggregate behavior followed by `SaveAsync`; reserve physical purge for a separate maintenance port.
5. Use Dapper + Npgsql for command-side adapters and EF Core or Dapper for query adapters.
6. Let the transaction coordinator own connection, transaction, commit, rollback, and atomic outbox persistence.
7. Clear recorded domain events only after successful atomic persistence.
8. Use direct query ports for simple reads; introduce an application query service only for composition or query-side policy.
9. Prevent empty custom repository wrappers, while allowing explicitly justified aggregate-lifecycle ports.
10. Move semantic enforcement from broad regex checks to architecture tests, analyzers, or focused executable tests.

## Open Decisions

### D1 — Canonical abstraction name

- Recommended: `IDomainRepository<TAggregate, TId>`.
- Alternative: retain `IRepository<TAggregate, TId>`.
- Impact: at least 24 documentation/context files currently reference `IRepository<`, while two primary standards reference `IDomainRepository<`.

### D2 — Generic operation set and deletion semantics

- Recommended: `FindByIdAsync` and `SaveAsync`; soft delete is an aggregate behavior; physical purge uses a separate maintenance port.
- Alternative: retain `DeleteAsync` in the generic contract with one explicitly defined semantic.
- Must not proceed with both physical delete and mandatory soft delete as simultaneous defaults.

### D3 — Bulk aggregate operations

- Recommended: remove `FindByIdsAsync` and `SaveAllAsync` from the generic contract; use independent commands, messaging, or an explicitly bounded batch port.
- Alternative: retain bulk methods and define transaction, partial-failure, concurrency, and aggregate-consistency rules.

### D4 — Custom repository interfaces

- Recommended: prohibit empty wrappers and read-model query methods; permit an exception only for stable aggregate-lifecycle semantics that cannot be represented by the generic port.
- Alternative: absolute prohibition with no exception.

### D5 — Command-side persistence technology

- Recommended: confirm Dapper + Npgsql as canonical and rewrite EF Core command-side examples.
- Alternative: change the tech-stack requirement to EF Core or allow per-target selection.
- This decision also determines the Unit of Work and concurrency examples.

### D6 — Unit of Work and outbox integration depth

- Recommended: define the framework-neutral atomicity contract first, then run a technical verification task against the selected Wolverine + Dapper/Npgsql integration before publishing concrete APIs.
- Alternative: retain EF Core-specific transaction examples.
- Concrete library APIs must not be invented without verification.

### D7 — Query-side layering

- Recommended: a simple query handler depends on an application query port implemented by Infrastructure; add an application Query Service only for multi-source composition or query-side policy.
- Alternative: require Query Repository + Query Service for every query.

### D8 — Remediation breadth

- Recommended: update canonical standards and active agent context first, then examples/guides, then generated checks in separate validated stages.
- Alternative: one atomic rewrite of all references.

### D9 — Language migration

- Recommended: keep this workflow focused on behavior and boundary consistency; schedule standards-language normalization separately.
- Alternative: convert every touched normative standard to English during this workflow.

## Skill Routing

| Stage | Capability | Skill | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| S0 | workflow orchestration | `dev-workflow` | High | Repository capability profile |
| S0-S2 | architecture | `ddd-ca-hex-architect` | High | Repository capability profile |
| S0, S3-S5 | context governance | `ai-context-governance` | High | Repository capability profile |
| S4 | local tooling change | `local-change-implementer` | High | Repository capability profile |

No sub-agent work is planned. Specialist skills are applied sequentially in the current thread.

## Stages

### S0 — Baseline analysis and decision frame

- Status: completed
- Goal: retain evidence-backed findings and create the decision boundary.
- Outputs:
  - `review-report.md`
  - `tasks/repository-pattern-analysis-and-decision-frame.json`
- Validation:
  - workflow Markdown exists;
  - task JSON parses;
  - findings include source evidence and do not claim user approval.

### S1 — Resolve architecture decisions

- Status: pending
- Owner: `ddd-ca-hex-architect`
- Goal: obtain and record D1-D9 decisions.
- Output:
  - updated decision section in this plan;
  - `tasks/resolve-repository-pattern-decisions.json`
- Validation:
  - every decision is approved, rejected, or explicitly deferred;
  - no unresolved decision is silently inferred.

### S2 — Align canonical standards

- Status: pending
- Owner: `ddd-ca-hex-architect`
- Goal: rewrite the normative repository, query, transaction, deletion, and persistence rules.
- Primary targets:
  - `.dev/ARCHITECTURE.MD`
  - `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`
  - `.dev/standards/coding-standards.md`
  - `.dev/standards/coding-standards/repository-standards.md`
  - `.dev/standards/coding-standards/projection-standards.md`
  - `.dev/standards/coding-standards/usecase-standards.md`
  - `.dev/standards/project-structure.md`
  - matching rationale documents
- Validation:
  - one abstraction name;
  - one operation set;
  - one command-side persistence policy;
  - one query-layer placement model;
  - explicit transaction, event, concurrency, and deletion semantics.

### S3 — Synchronize dependent context

- Status: pending
- Owner: `ai-context-governance`
- Goal: propagate approved rules without duplicating canonical ownership.
- Scope:
  - `.ai/assets/tech-stacks/dotnet-backend/`
  - relevant skill and sub-agent references;
  - active prompts;
  - human-facing guides;
  - examples and checklists.
- Validation:
  - canonical rules remain in standards or canonical AI assets;
  - runtime wrappers remain thin;
  - reference searches find no active contradictory contract;
  - deferred historical examples are explicitly labeled.

### S4 — Align validation tooling

- Status: pending
- Owner: `local-change-implementer`
- Goal: correct or retire repository regex checks and regenerate derived files.
- Scope:
  - `.ai/scripts/check-repository-compliance.sh`
  - `.ai/scripts/generated/check-repository.sh`
  - generator source or pattern metadata where applicable
- Validation:
  - no rule rejects the allowed identity lookup;
  - query repository files are not checked as domain repositories;
  - source and generated checks agree;
  - shell syntax validation passes;
  - semantic rules are assigned to an appropriate executable validation layer.

### S5 — Final consistency validation and closure

- Status: pending
- Owner: `dev-workflow`
- Goal: verify the complete rule family and close the workflow.
- Validation:
  - parse all changed JSON;
  - `git diff --check`;
  - targeted reference searches;
  - Markdown link validation for changed documents;
  - shell syntax checks for changed scripts;
  - relevant repository validation commands;
  - residual risks and deferred work documented.

## Commit Checkpoints

No commit is authorized by the current request. If commits are requested later, use these coherent boundaries:

1. `workflow(workflow): bootstrap repository pattern alignment`
2. `docs(architecture): align repository pattern standards`
3. `docs(ai-context): synchronize repository guidance`
4. `chore(dotnet-backend): align repository validation checks`
5. `workflow(workflow): close repository pattern alignment`

Each workflow-stage commit must include `Why`, `What`, `Validation`, and `Workflow` sections.

## Completion Criteria

- D1-D9 are resolved or explicitly deferred.
- Canonical standards contain no internal contradiction for the repository rule family.
- Active prompts, guides, examples, and checks do not override the canonical contract.
- Transaction/outbox examples match the approved command-side technology.
- Generated validation agrees with its source.
- Final validation evidence is recorded.

