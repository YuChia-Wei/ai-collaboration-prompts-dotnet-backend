# Repository Pattern Standards Baseline Review

## Review Metadata

- Workflow: `2026-07-repository-pattern-standards-alignment`
- Review type: architecture and context consistency baseline
- Review date: `2026-07-05`
- Revalidated after rebase: `2026-07-05`
- Rebase target: local `main` at `2d4130c`
- Review skills:
  - `ddd-ca-hex-architect`
  - `ai-context-governance`
- Scope: active repository pattern standards, architecture references, dependent prompts/guides, and validation scripts
- Product source-code review: not applicable; this repository is a reusable AI collaboration and .NET backend context framework

## Executive Assessment

The repository pattern guidance has a coherent architectural intent but does not currently form a reliable execution contract.

The intended model is:

- command-side repositories load aggregates by identity;
- read-model queries do not expand the domain repository;
- application code depends on ports;
- infrastructure provides persistence adapters;
- write and read persistence may use different technologies;
- outbox persistence must align with the aggregate transaction.

The active material contradicts that intent in naming, method surface, ORM selection, query layering, deletion behavior, event lifecycle, and enforcement. Canonical standards must be aligned before prompts, examples, or checks are mechanically updated.

## Evidence Used

- `.dev/ARCHITECTURE.MD`
- `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`
- `.dev/standards/coding-standards.md`
- `.dev/standards/coding-standards/repository-standards.md`
- `.dev/standards/coding-standards/projection-standards.md`
- `.dev/standards/coding-standards/usecase-standards.md`
- `.dev/standards/coding-standards/README.md`
- `.dev/standards/project-structure.md`
- `.dev/standards/rationale/generic-repository-only-rationale.MD`
- `.dev/standards/rationale/query-side-layering-rationale.MD`
- `.dev/guides/design-guides/FRAMEWORK-API-INTEGRATION-GUIDE.md`
- `.ai/assets/skills/ddd-ca-hex-architect/references/architecture-playbook.md`
- `.ai/scripts/check-repository-compliance.sh`
- `.ai/scripts/generated/check-repository.sh`
- `.dev/requirement/DOTNET-VALIDATOR-PHASE-3-REQUIREMENTS.MD`
- `.dev/workflows/2026-07-dotnet-validator-phase-3/workflow-plan.md`
- `.dev/workflows/2026-05-dotnet-script-to-analyzer-transition/dotnet-validation-strategy.md`
- `.dev/workflows/2026-05-dotnet-script-to-analyzer-transition/script-to-validator-mapping.md`
- `tools/DotnetBackendAnalyzers/RepositoryQueryMethodAnalyzer.cs`
- `tools/DotnetBackendAnalyzers.Tests/RepositoryQueryMethodAnalyzerTests.cs`

## Findings

### F1 — Command-side persistence technology has two incompatible defaults

Severity: critical

Evidence:

- `.dev/requirement/TECH-STACK-REQUIREMENTS.MD` selects Dapper + Npgsql for command writes.
- `.ai/assets/skills/ddd-ca-hex-architect/references/architecture-playbook.md` repeats Dapper + Npgsql for the write side.
- `.dev/standards/coding-standards/repository-standards.md` presents EF Core as the correct repository implementation and requires EF Core in its checklist.
- `.dev/guides/design-guides/FRAMEWORK-API-INTEGRATION-GUIDE.md` couples the outbox transaction explanation to EF Core.

Risk:

- generated command-side adapters can violate the tech-stack requirement;
- Unit of Work and outbox examples cannot be trusted;
- code review can accept and reject the same implementation depending on the entry document used.

Required resolution:

- approve one command-side persistence policy before rewriting examples;
- verify concrete Wolverine transaction APIs instead of inferring them.

### F2 — Repository abstraction name is inconsistent

Severity: high

Evidence:

- the normative interface example and pattern marker use `IDomainRepository<TAggregate, TId>`;
- implementation, DI, use-case, test, profile, guide, prompt, and generated-check material commonly uses `IRepository<TAggregate, TId>`;
- the baseline search found 24 Markdown/YAML files referencing `IRepository<` and two referencing `IDomainRepository<`.

Risk:

- dependency injection registrations and generated handlers use incompatible types;
- regex checks enforce the older name;
- the distinction between domain repository and query repository is weakened.

Required resolution:

- approve D1 and migrate active references by stage.

### F3 — The allowed method surface is internally contradictory

Severity: high

Evidence:

- the repository standard overview defines five methods;
- the coding standards index and checklists state three methods;
- the generic repository rationale describes load, save, and delete as the stable core;
- batch methods are used in an example that also warns about violating the one-aggregate transaction boundary.

Risk:

- reviewers cannot determine whether batch methods are allowed;
- generic bulk operations obscure transaction, concurrency, partial failure, and aggregate consistency semantics.

Required resolution:

- resolve D2 and D3 separately;
- do not treat performance motivation alone as sufficient aggregate-lifecycle semantics.

### F4 — Mandatory soft delete conflicts with physical repository deletion

Severity: high

Evidence:

- active aggregate guidance requires soft-delete support;
- the repository example uses `DbSet.Remove`;
- a global query filter hides soft-deleted data, but the delete example removes the row physically.

Risk:

- audit history and domain deletion invariants can be bypassed;
- `DeleteAsync` has no stable meaning across adapters;
- InMemory and database profiles may behave differently.

Required resolution:

- model soft delete as aggregate behavior plus save, or define a single explicit `DeleteAsync` semantic;
- keep physical purge outside normal application behavior.

### F5 — Domain events are cleared before persistence success

Severity: critical

Evidence:

- repository and in-memory examples call `ClearDomainEvents()` during `SaveAsync` or `DeleteAsync`;
- the handler calls Unit of Work commit afterward;
- the outbox flow requires aggregate persistence and message persistence to succeed atomically.

Risk:

- a failed commit can lose recorded events in memory;
- retry behavior and outbox mapping become ambiguous;
- repositories acquire responsibility for event publication lifecycle.

Required resolution:

- the transaction/outbox coordinator must define event capture and clear timing;
- repositories must not clear events before successful atomic persistence.

### F6 — Query-side layer placement has two competing models

Severity: high

Evidence:

- `coding-standards.md`, `repository-standards.md`, `project-structure.md`, and the rationale place Query Repository adapters in Infrastructure and Query Service implementation in Application;
- `projection-standards.md` places Query Service implementation directly in Infrastructure and lets it access `DbContext`;
- the rationale requires two layers for every query, regardless of whether the application layer adds behavior.

Risk:

- generated project structures disagree;
- simple queries receive mandatory pass-through abstraction;
- the term `QueryService` can mean either an application service or an infrastructure adapter.

Required resolution:

- approve D7;
- define terms by responsibility, not only by suffix.

### F7 — Custom repository interface policy contradicts project structure

Severity: medium

Evidence:

- standards say never create custom repository interfaces;
- the rationale allows a possible exception for stable non-query semantics;
- project structure requires `I<Domain>DomainRepository.cs` under the Application project.

Risk:

- generated projects create interfaces that review rules reject;
- an absolute rule prevents legitimate aggregate-lifecycle ports, while a permissive rule invites read queries into the write repository.

Required resolution:

- approve D4;
- remove the mandatory custom-interface folder if generic-only remains the default.

### F8 — Repository validation has a sound migration direction but still encodes the unresolved policy

Severity: high

Evidence:

- the standard marker requires `IDomainRepository<`, while scripts search for `IRepository<`;
- scripts target all `*Repository*.cs`, including query repositories;
- the forbidden expression `FindBy|GetBy|QueryBy|SearchBy` rejects the allowed `FindByIdAsync`;
- source and generated script locations use the same relative base calculation even though their directory depth differs;
- `main` now explicitly marks the grep script as non-gating and pending replacement;
- `DBA1001` already allows identity lookup and excludes query/read repository names;
- `DBA1001` still hard-codes the unresolved five-method contract and classifies repositories primarily by interface name;
- Validator Phase 3 intentionally deferred repository policy and validation to this workflow.

Risk:

- the legacy script remains misleading if invoked directly;
- changing D2-D4 without updating `DBA1001` would make analyzer behavior disagree with the standards;
- broad name-based detection can report false positives or miss repository ports that use a different approved name.

Required resolution:

- do not use the current scripts as a completion gate;
- approve D10 after D1-D4;
- evolve `DBA1001` with semantic tests and retire the grep artifacts only after replacement coverage passes.

### F9 — Technology and language drift increases migration risk

Severity: medium

Evidence:

- some coding-standard entry material still states .NET 8 / EF Core 8 while current requirements state .NET 10 / EF Core 10;
- `.dev/standards/**` is expected to be English, while many active normative files remain Traditional Chinese;
- active examples mix historical ezDDD vocabulary with current .NET port/adapter terms.

Risk:

- behavioral remediation can accidentally expand into a broad translation or historical-context rewrite;
- version-specific examples may be copied as current truth.

Required resolution:

- approve D8 and D9;
- keep behavior correction and language migration independently reviewable.

## Boundary Classification

| Material | Audience | Scope | Action |
| --- | --- | --- | --- |
| `.dev/standards/**` repository rules | agent/both | dotnet-backend project truth | rewrite as canonical contract |
| `.dev/requirement/TECH-STACK-REQUIREMENTS.MD` | human/both | dotnet-backend project truth | confirm or update selected stack |
| `.ai/assets/skills/ddd-ca-hex-architect/**` | agent | canonical skill context | sync only after standards decision |
| `.ai/assets/tech-stacks/dotnet-backend/**` | agent | dotnet-backend reusable context | sync approved stable rules |
| `.agents/**`, `.claude/**` | agent | runtime-wrapper | keep thin; update only if pointers change |
| `.dev/guides/**` | human | dotnet-backend guidance | explain approved contract, do not own it |
| `.dev/standards/examples/**` | human/agent | dotnet-backend examples | update or label historical/deferred |
| `.ai/scripts/**` | agent/tooling | transitional validation | correct, narrow, regenerate, or retire |

## Recommended Remediation Sequence

1. Resolve D1-D10.
2. Rewrite canonical architecture and coding standards.
3. Update rationale documents to explain approved tradeoffs.
4. Synchronize active agent context and prompts.
5. Synchronize human guides and examples.
6. Align `DBA1001`, add regression coverage, and retire repository grep validation.
7. Run reference, JSON, Markdown, shell, and repository consistency checks.

## Rebase Revalidation Result

The rebase changes the validation-tooling plan but does not invalidate the architecture findings F1-F7 or the technology/language drift finding F9.

Material changes from `main`:

- Validator Phase 3 replaced Mapper, Aggregate, UseCase, and Projection grep checks with dotnet-native validation.
- Projection standards now assign deterministic write-operation validation to `DBA1013` and EF model registration to `DotnetBackendValidation`.
- Repository validation was explicitly excluded from Phase 3 and assigned to a separate repository-policy workflow.
- `check-all.sh` no longer executes repository grep validation as a gate.
- `DBA1001` is the existing repository analyzer bootstrap and must be treated as an implementation dependency of this workflow.

Planning consequence:

- S4 changes from repairing/regenerating grep scripts to extending `DBA1001`, adding semantic regression tests, and retiring the repository scripts.
- A new user decision, D10, is required for enforcement ownership and default severity.
- No previously listed architecture decision can be removed after the rebase.

## Validation Baseline

The working tree was clean when the workflow was opened. No product tests apply to this bootstrap stage.

The current repository compliance scripts were inspected but intentionally not used as an architecture gate. Rebase-updated `main` confirms this is the intended transitional state.

## Residual Risk

The largest unresolved risk is the concrete Dapper/Npgsql/Wolverine atomic outbox integration. The standards can define the required transaction semantics now, but concrete configuration and API examples require a focused verification step before publication.

