# .NET Validator Phase 3 Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-07-dotnet-validator-phase-3`
- `owner_skill`: `dev-workflow`
- `status`: `in_progress`

## Goal

Replace the remaining Mapper, Aggregate, UseCase, and Projection grep-based checks with reliable dotnet-native validation while preserving software-design rules that belong to AI review.

## Scope

- Classify each existing rule as `.editorconfig`, Roslyn Analyzer, architecture/configuration test, or AI review responsibility.
- Resolve and implement Mapper validation after its policy decision.
- Distinguish `EsAggregateRoot` validation from normal `AggregateRoot` validation.
- Complete deterministic UseCase validation not already covered by `DBA1002`.
- Identify projections through an interface and validate EF Core registration through a configuration test.
- Remove each transitional script only after equivalent reliable coverage exists.

## Deferred

- Repository interface and remaining Repository validation are excluded until the repository standard is revised in a separate worktree and conversation.
- Dependencies and version validation remain outside Phase 3.
- Product-specific aggregate, mapper, use-case, or projection conventions are not introduced.

## Stages

1. Normalize Phase 3 requirements and validator ownership.
2. Resolve the Mapper policy decision.
3. Implement Mapper validation.
4. Implement Aggregate and UseCase validation.
5. Add the Projection marker-interface and EF Core configuration-test template.
6. Retire replaced scripts and update orchestration and documentation.
7. Run final validation and close the workflow.

## Routing

| Stage | Capability | Owner |
| --- | --- | --- |
| Requirements and rule ownership | requirements | `requirement-author` |
| Aggregate profile semantics | architecture | `ddd-ca-hex-architect` |
| Analyzer and test implementation | implementation | `slice-implementer` |
| Local analyzer changes | local-change | `local-change-implementer` |
| Script and AI context cleanup | context-governance | `ai-context-governance` |
| Stage and commit coordination | workflow-orchestration | `dev-workflow` |

## Validation Strategy

- Analyzer positive and negative tests for each deterministic diagnostic.
- EF Core model/configuration tests for projection registration.
- JSON parsing and reference searches for workflow and script migration.
- `dotnet test` for the analyzer and configuration-test templates.
- `git diff --check`.

## Open Decision

- Mapper policy: require static mappers only, or allow both static mappers and sealed stateless mapper services.

## Progress

- Stage 1 completed: Phase 3 requirements and enforcement ownership are documented.
- Stage 2 pending: Mapper policy decision.
- Aggregate/UseCase and Projection streams are ready for implementation after the requirement commit.

## Constraints

- Do not create custom analyzers for formatting or coding-style preferences already supported by `.editorconfig` and standard .NET analyzers.
- An `.editorconfig` preference becomes a gate only when its diagnostic severity and CI command enforce it.
- Do not encode `Apply/When` requirements for normal `AggregateRoot` implementations.
- Do not convert design-intent review heuristics into syntax-based build gates.

