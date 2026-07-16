# BuildingBlocks And Examples MVP Plan

## Purpose

Prove that the v0.4.0 architecture can be reconstructed from stable, contract-only BuildingBlocks without turning this AI context repository into a product implementation or prematurely publishing a template/NuGet package.

## Architecture Decision

BuildingBlocks is the portable framework contract surface closest to the role EzDDD played, but it does not own target persistence, message-broker, ORM, observability, or other adapter implementations.

- BuildingBlocks Domain contracts define domain identity/event/aggregate/value semantics.
- BuildingBlocks Application contracts define Aggregate Repository, Query Repository marker, time, dispatch, result, and other portable ports selected for the MVP.
- BuildingBlocks Integration contracts define integration event and publisher/request-reply contract boundaries without Wolverine/RabbitMQ/Kafka implementations.
- Sample Product Domain and Application consume the contracts.
- Sample Product Infrastructure owns concrete in-memory or test-only adapter implementations used to prove the ports.
- Future product Infrastructure may use EF Core, Dapper, event stores, Wolverine, or another target-selected adapter without editing BuildingBlocks.

This is Hexagonal Architecture aligned: BuildingBlocks owns reusable port vocabulary; products own business semantics and adapters. It is conceptually aligned with EzDDD's reusable abstractions while deliberately avoiding EzDDD-specific runtime implementations.

## Proposed MVP Projects

The final names remain reviewable. The logical split is the contract:

```text
tools/DotnetBackendArchitectureFixture/
├── BuildingBlocks.Domain.Contracts/
├── BuildingBlocks.Application.Contracts/
├── BuildingBlocks.Integration.Contracts/
├── SampleProduct.Domain/
├── SampleProduct.Application/
├── SampleProduct.Infrastructure/
└── SampleProduct.ArchitectureTests/
```

### Contract-Only BuildingBlocks Surface

Start with the smallest coherent set:

- `IDomainEntity<TId>`
- `IAggregateRoot<TId>`
- `IDomainEvent`
- value-object marker/equality contract only if it can be expressed without product behavior
- `IAggregateRepository<TAggregate,TId>` with `FindByIdAsync` and `SaveAsync`
- `IQueryRepository` marker
- `IIntegrationEvent`
- `IIntegrationEventPublisher`

Do not include:

- EF Core/Dapper repositories or DbContexts;
- Wolverine/RabbitMQ/Kafka publishers or consumers;
- generic writable CRUD repositories;
- physical purge in the shared Aggregate Repository;
- application-specific query methods;
- product-specific Aggregate base behavior.

If an abstract base class is later desired, evaluate it separately from this interface-first MVP so reusable behavior does not enter the contract by accident.

## Sample Product Proof

Use one intentionally small Aggregate and one Use Case:

1. `WorkItem` implements `IAggregateRoot<WorkItemId>` and supports standard soft deletion.
2. `DeleteWorkItemUseCase` invokes Aggregate deletion and calls `SaveAsync`.
3. `PurgeWorkItemUseCase` uses a product-owned restricted `IWorkItemPurgePort`; it is not part of `IAggregateRepository`.
4. `SampleProduct.Infrastructure` provides in-memory/test adapters only for fixture verification.
5. An optional integration event demonstrates the contract boundary without a broker implementation.

This proves the legal/privacy distinction: normal deletion preserves an auditable Aggregate state; explicit purge is separately authorized and implemented.

## Example And Test Contract

| Tier | Contains implementation | Test requirement | Allowed claim |
| --- | --- | --- | --- |
| `executable-tested` | yes | build plus focused tests required | verified executable reference |
| `structure-validated` | partial/configuration | deterministic structural validator required | structure validated only |
| `illustrative` | optional snippets | no test required | illustrative; not copy-ready |
| `reference-only` | no required implementation | no test required | conceptual/reference guidance |
| `historical` | legacy provenance | no test required | history/migration only |

Only the MVP fixture starts as `executable-tested`. Existing examples remain unpromoted until individually migrated and tested.

## MVP Tests

- BuildingBlocks projects have no forbidden EF/Dapper/Wolverine/ASP.NET/AspectInjector dependencies.
- Product Domain depends only on approved BuildingBlocks Domain contracts.
- Product Application depends on Product Domain and BuildingBlocks Application/Integration contracts.
- Product Infrastructure implements repository/purge/event-publisher ports.
- Standard deletion calls Aggregate behavior plus `SaveAsync`.
- Physical purge is unreachable through `IAggregateRepository` and requires the dedicated port/use case.
- NSubstitute is used for application-layer test doubles under the default profile.
- Executable example inventory contains no item without a matching build/test validation route.

## Review Gates Before Full Implementation

1. Approve project names and exact interface list.
2. Confirm whether value-object equality remains entirely product-owned in the interface-first MVP.
3. Approve the sample Aggregate/use-case choice.
4. Approve the five example verification tiers.
5. Only then implement the fixture and migrate the first examples.

## Deferred

- `dotnet new` template packaging;
- NuGet packaging/versioning;
- production-ready EF Core, Dapper, Wolverine, or broker adapters;
- full example portfolio conversion;
- analyzer package extraction.
