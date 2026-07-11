# .NET CA + WolverineFx Project Structure Guide

This project uses a **multi-Bounded Context (BC)** architecture. Each Domain has independent DomainCore and Presentation layers.

## Project Directory Structure

```
project-root/
├── src/
│   ├── BC-Contracts/                    # Cross-BC communication contracts (Published Language)
│   │   └── Lab.BoundedContextContracts.<Domain>/ # Integration Events / Interactions / DTOs for each Domain
│   ├── BuildingBlocks/                  # Shared building blocks (architectural infrastructure)
│   │   ├── Lab.BuildingBlocks.Domain/   # Shared Domain-layer components
│   │   ├── Lab.BuildingBlocks.Application/
│   │   └── Lab.BuildingBlocks.Infrastructure/
│   ├── Shared/                          # Shared domain core (Shared Kernel)
│   │   └── Lab.SharedKernel/            # Domain concepts shared across BCs, such as Value Objects and Enums
│   └── <DomainName>/                    # Specific Domain (for example, Order or Product)
│       ├── DomainCore/                  # Domain core layer
│       │   ├── <DomainName>.Domains/        # Domain Model
│       │   ├── <DomainName>.Applications/   # Application layer
│       │   └── <DomainName>.Infrastructure/ # Technical infrastructure
│       └── Presentation/                # Presentation layer
│           ├── <DomainName>.WebApi/         # REST API
│           └── <DomainName>.Consumer/       # MQ Consumer (Console App)
├── tests/
│   └── <TargetProject>.Tests/           # Tests for the corresponding project
├── docker-compose/                      # Docker Compose configuration
├── docs/                                # Documentation and design notes
├── https/                               # HTTP test files
│   └── <Context>/                       # HTTP tests for a specific BC
├── sql-script/                          # Database scripts
├── .ai/                                 # Reusable prompts, shared rules, and scripts for agents
├── .dev/                                # Human-facing specs, ADRs, requirements, and guides
├── .github/                             # GitHub repository resources; the Copilot adapter is optional
└── *.slnx                               # .NET Solution
```

## Project Layer Rules

| Layer | Responsibility | Naming Convention | Location |
|------|------|---------|------|
| Domain | Domain Model | `<DomainName>.Domains` | `./src/<DomainName>/DomainCore` |
| Application | Use Cases and ports | `<DomainName>.Applications` | `./src/<DomainName>/DomainCore` |
| Infrastructure | Technical infrastructure | `<DomainName>.Infrastructure` | `./src/<DomainName>/DomainCore` |
| Presentation | Web API | `<DomainName>.WebApi` | `./src/<DomainName>/Presentation` |
| Presentation | Queue Consumer | `<DomainName>.Consumer` | `./src/<DomainName>/Presentation` |
| Cross-BC | Cross-BC communication contracts | `Lab.BoundedContextContracts.<Domain>` | `./src/BC-Contracts` |
| BuildingBlocks | Architectural infrastructure | `Lab.BuildingBlocks.<Layer>` | `./src/BuildingBlocks` |
| SharedKernel | Shared domain core | `Lab.SharedKernel` | `./src/Shared` |
| Tests | Test project | `<TargetProject>.Tests` | `./tests` |

## Documentation and AI Asset Responsibilities

| Path | Primary Audience | Purpose |
|------|---------|------|
| `./.dev/guides/ai-collaboration-guides` | Human | AI collaboration guides, workflows, and prompt templates |
| `./.dev/guides` | Human | General development and design guides (AI collaboration / design / implementation / learning) |
| `./ai` | Agent | Prompt components, shared rules, and scripts |
| `./.claude/skills` | Agent | Skill definitions and skill-local references |

## Solution File (.slnx) Rules

- Solution Folders in `.slnx` use logical grouping and do not need to match the physical directory structure.
- Solution Folder names must use leading and trailing slashes: `/{Group}/`, `/{Group}/{SubGroup}/` (for example, `/Order/DomainCore/`).
- Logical grouping should primarily reflect Bounded Context and layer semantics (such as `<ContextA>/DomainCore` and `<ContextB>/Presentation`).
- `tests` may remain a single top-level group: `/tests/`.

## Application-Layer Directory Structure

```
<DomainName>.Applications/
├── UseCases/                    # Application inbound ports + implementations
│   ├── Create<Entity>/
│   │   ├── ICreate<Entity>UseCase.cs
│   │   ├── Create<Entity>UseCase.cs
│   │   ├── Create<Entity>Input.cs
│   │   └── Create<Entity>Output.cs
│   └── Get<Entity>/
│       ├── IGet<Entity>UseCase.cs
│       ├── Get<Entity>UseCase.cs
│       └── Get<Entity>Output.cs
├── Ports/                       # Outbound port interface definitions
│   ├── Queries/
│   │   └── I<Feature>QueryRepository.cs
│   ├── Persistence/             # Include only domain-specific capabilities
│   │   └── I<Capability>Port.cs
│   ├── Messaging/
│   │   └── I<Feature>EventPublisher.cs
│   └── I<Feature>QueryService.cs # optional composition port
├── QueryServices/               # Optional Application query composition
│   └── <Domain>QueryService.cs
├── Dispatch/                    # Optional package-neutral dispatch contracts/handlers
│   └── Create<Entity>Command.cs
├── DomainEventHandlers/         # Domain Event handlers
└── Dtos/                        # Application-layer DTOs (Input/Output)
```

The portable Aggregate Repository contract resides in `BuildingBlocks.Application`:

- `IAggregateRepository<TAggregate, TId>`
- compatibility `IDomainRepository<TAggregate, TId>`
- `IQueryRepository` marker

Do not create an empty `I<Aggregate>Repository` for every Aggregate by default. Create a domain-specific port only to maintain compatibility with existing code or to add approved Aggregate lifecycle/capability semantics.

### Application Terminology and Responsibilities

- `Use Case`
  - An explicit inbound port and application orchestration object, such as
    `ICreateProductUseCase` / `CreateProductUseCase`
- `Command` / `Query`
  - A delivery contract needed only for a dispatch entry, not a Use Case input
- `Handler`
  - An inbound adapter for a real dispatch/message entry that maps input and then invokes one Use Case
- `Application Service`
  - Not defined by this standard; if a target repository uses one, its responsibility must be decided explicitly elsewhere

Default rules:

- Controllers directly inject Use Case interfaces.
- Use Case implementations use the `*UseCase` suffix and `ExecuteAsync`.
- A Handler and a Use Case are distinct objects.
- Do not create a Handler without a real dispatch/message entry.
- Place Wolverine/MediatR/MQ-specific Handlers in an inbound adapter or composition
  boundary, not in a portable Use Case.
- Only explicitly approved pure-query endpoints may directly access a Query Repository/Service as an exception.

Recommended relationship chain:

```text
Controller
  -> I<Operation>UseCase
  -> <Operation>UseCase
  -> Aggregate / Domain Service / Repository / Query Service
  -> Use Case Output
```

Actual dispatch/message entry:

```text
Command / Message
  -> Handler
  -> I<Operation>UseCase
```

For additional rules, see [`USECASE-COMMAND-HANDLER-RELATIONSHIP.MD`](./USECASE-COMMAND-HANDLER-RELATIONSHIP.MD).

## Infrastructure-Layer Directory Structure

```
<DomainName>.Infrastructure/
├── Repositories/                # Aggregate Repository adapters
│   └── <Aggregate>Repository.cs
├── QueryRepositories/           # Query Repository implementations
│   └── <Feature>QueryRepository.cs
├── Persistence/                 # Target-selected DB/ORM/event-store configuration
├── Writers/                     # Outbox/Projection/Import/Purge capability adapters
└── Messaging/                   # MQ-related implementations
    └── <Feature>EventPublisher.cs # Application outbound port adapter
```

## Clean Architecture Layers

- **Domain**: Aggregates, Entities, Value Objects, Domain Events
- **Application**: Use Cases, inbound/outbound Ports, Policies
- **Infrastructure**: target-selected persistence, Outbox, Message Bus, Repository/Query/Writer adapters
- **Presentation**: Controllers, DTO mapping, validation, MQ Consumers

## Naming and Dependency Direction

- Domain does not depend on any other layer.
- Application depends on Domain.
- Infrastructure depends on Application/Domain.
- Presentation depends on Application (not directly on Infrastructure; connect it through DI).

### Relationship Between Adapters and the Bus

- By default, a Controller depends on a Use Case interface, not on a Handler, bus, dispatcher,
  write repository, or aggregate.
- Only explicitly approved pure-query endpoints may directly depend on a read-only Query Repository/Service.
- A normal synchronous API within the same BC and process directly invokes a Use Case port.
- A dispatch/message Handler exists only when there is a real delivery entry and invokes one Use Case.
- Only cross-BC communication mandates an MQ/message bus.
- A Use Case depends on a project-owned event publisher port; only Infrastructure depends on
  Wolverine or another broker/framework.

### Persistence Port Rules

- An Aggregate Repository accepts only an Aggregate Root.
- Persist a child Entity through its owning Aggregate Root.
- A Query Repository implements `IQueryRepository` and is read-only.
- Use capability-specific ports for physical purge, Outbox, Projection, Import, and similar capabilities.
- Target-specific batch persistence does not belong in the portable/default project template.

## Cross-BC Communication Rules

> ⚠️ **Important restriction**: Cross-Domain services **must not** communicate through Web APIs; they must use a Message Queue (RabbitMQ/Kafka).
> 💡 **Consistency model**: Cross-Domain data synchronization uses **Eventual Consistency** and does not require strong consistency.

| Communication Type | Mechanism | Definition Location |
|---------|---------|---------|
| Within the same BC | Domain Events | `<Domain>.Domains/DomainEvents` |
| Cross-BC | Integration Events | `./src/BC-Contracts/Lab.BoundedContextContracts.<Domain>` |

## Shared Projects Classification

> For detailed design rationale and DDD explanations, treat this document and the corresponding rationale/guide documents as authoritative.

This project has three cross-domain shared areas, each corresponding to a different DDD concept:

| Project | DDD Concept | Responsibility | Dependency Permission |
|------|---------|------|----------|
| `BuildingBlocks` | Architectural infrastructure | Abstract bases and interfaces without business semantics | May be referenced by all layers |
| `SharedKernel` | Shared Kernel | Shared domain concepts across BCs (VOs, Enums) | May be referenced by the Domain layer |
| `BC-Contracts` | Published Language | Communication contracts between BCs (Integration Events, Request/Reply) | **Must not be referenced by the Domain layer** |

### Dependency Direction Constraints

```
BuildingBlocks ← may be referenced by all layers
SharedKernel   ← Domain / Application / Infrastructure / Presentation
BC-Contracts   ← Application / Infrastructure / Presentation (Domain prohibited)
```

### BC-Contracts Internal Categories

| Subdirectory | Purpose | Example |
|--------|------|------|
| `IntegrationEvents/` | Asynchronous event contracts (MQ Payload) | `OrderPlaced`, `ProductStockDecreased` |
| `Interactions/` | Request/Reply contracts | `ReserveInventoryRequestContract` |
| `DataTransferObjects/` | Cross-BC query response contracts | `OrderDetailsResponse` |

When using these areas, ensure that Bounded Context boundary isolation is not compromised.
