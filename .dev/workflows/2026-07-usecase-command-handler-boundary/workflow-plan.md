# Use Case and Command Handler Boundary Workflow

## Metadata

- Plan ID: `workflow-plan-2026-07-usecase-command-handler-boundary`
- Workflow ID: `2026-07-usecase-command-handler-boundary`
- Owner skill: `dev-workflow`
- Status: `in-progress`
- Created: `2026-07-06`
- Branch: `codex/usecase-command-handler-alignment`
- Base: `main` at merge commit `343ab29`
- Issue: not provided

## Problem Statement

Active standards currently define two incompatible synchronous application entry
models:

1. `Controller -> Command/Query -> Handler`, where the Handler normally is the Use
   Case implementation.
2. `Controller -> IUseCase -> UseCase implementation`, where a Handler is a
   separate delivery/dispatch object.

The user-approved target from the repository-pattern workflow is the second model:

- Use Case and Handler are separate objects;
- an API Controller injects a Use Case interface;
- normal synchronous API behavior does not publish a Command through a bus;
- message/event Handler responsibilities remain distinct from Use Case
  orchestration.

The current guidance, examples, prompts, project structure, tests, and analyzers do
not consistently implement that target.

The evidence baseline is recorded in [review-report.md](./review-report.md).

## Scope

### In scope

- define `Use Case`, `Input`, `Command`, `Query`, `Handler`, `Application Service`,
  `Controller`, `Consumer`, and `Reactor` responsibilities;
- define the default synchronous API invocation chain;
- define when command/query/message handlers exist and what they may delegate;
- define whether query flows use the same explicit Use Case boundary;
- align DI, naming, project structure, prompts, examples, tests, and analyzers;
- keep Wolverine and other dispatch packages conditional on target-repository
  evidence.

### Non-goals

- no production application implementation;
- no message broker or transport redesign;
- no repository-pattern redesign;
- no broad standards translation;
- no target-specific Wolverine API configuration;
- no sub-agent work unless explicitly requested later.

## Governing Constraints

- DDD + Clean Architecture + CQRS remains the base architecture.
- A Use Case is the application orchestration boundary.
- Presentation adapters do not depend directly on repositories or Domain objects.
- Cross-bounded-context communication remains MQ-only.
- In-process synchronous API behavior does not require message publication.
- Eventual consistency remains the default across Aggregates.
- Exceptional strong consistency is declared by an explicit `IUnitOfWork`
  dependency on the Use Case, not hidden in a Handler.
- Runtime packages such as Wolverine are conditional target-repository choices.

## Preliminary Target Direction

This direction is a proposal pending the decisions below:

```text
HTTP Request
  -> Controller
  -> I<CreateOperation>UseCase
  -> <CreateOperation>UseCase
  -> Aggregate / Domain Service / outbound ports
  -> Use Case Output
  -> HTTP Response
```

When a dispatch or message entry is actually required:

```text
Command / Message / Scheduled Trigger
  -> Handler (inbound adapter)
  -> I<CreateOperation>UseCase
  -> Use Case implementation
```

Proposed responsibility split:

- `Use Case interface`: stable inbound Application port;
- `Use Case implementation`: application orchestration, transaction requirement,
  Aggregate/query collaboration, and output contract;
- `Input` / `Output`: transport-neutral Use Case contract;
- `Command`: intent message used only where command dispatch is intentionally
  selected;
- `Handler`: adapter for a selected delivery mechanism; maps its input and invokes
  a Use Case, without becoming the default Use Case implementation;
- `Controller`: HTTP adapter that maps HTTP DTOs to Use Case input and injects only
  Use Case interfaces;
- `Consumer` / event Handler / Reactor: message adapters or eventual-consistency
  workers, kept distinct from synchronous API Use Cases.

## Open Decisions

### D1 — Use Case interface shape

Decide the canonical operation signature and cancellation policy.

Proposed default:

```csharp
public interface ICreateProductUseCase
{
    Task<CreateProductOutput> ExecuteAsync(
        CreateProductInput input,
        CancellationToken cancellationToken = default);
}
```

Questions:

- Is `ExecuteAsync` the mandatory method name?
- Does every Use Case accept a dedicated input object, including parameterless
  operations?
- Is `CancellationToken` mandatory for asynchronous Use Cases?

### D2 — Input versus Command

Decide whether a Use Case accepts a transport-neutral `Input` or directly accepts
an `ICommand<T>` object.

Recommended direction:

- Controller maps HTTP request to `CreateProductInput`;
- `CreateProductInput` does not implement a dispatcher/package marker;
- a message/command Handler maps `CreateProductCommand` to the same input when a
  dispatch entry is needed.

This prevents Application ports from becoming coupled to a selected dispatcher.

### D3 — Command Handler existence and role

Decide whether a Command Handler:

1. exists only when an actual command/message dispatch entry is configured; or
2. is mandatory for every command Use Case even though Controllers do not use it.

Recommended direction: option 1. A mandatory one-line Handler for every Use Case
would add an unused layer and recreate the ambiguity under a new name.

### D4 — Controller dependency rule

Confirm whether Controllers are strictly prohibited from injecting:

- concrete Handlers;
- `IMessageBus`;
- mediator/dispatcher abstractions;
- repositories or Domain services.

Recommended default: Controller injects one or more explicit Use Case interfaces
only. Framework-specific endpoint models require a separately approved profile.

### D5 — Query-side symmetry

Decide whether synchronous queries also require:

```text
Controller -> I<GetProduct>UseCase -> GetProductUseCase -> IProductQueryRepository
```

or whether direct Controller-to-query-handler dispatch remains allowed.

Using one inbound-port rule for both commands and queries is more consistent, but
must not force unnecessary QueryService layers.

### D6 — Handler placement

Decide placement by handler type:

- package-neutral in-process command Handler;
- Wolverine/MediatR-specific Handler;
- MQ Consumer Handler;
- Domain Event Handler / Reactor.

Recommended rule: package-neutral Use Cases remain in Application; transport- or
framework-specific handlers belong to the inbound adapter/composition boundary.
A convention-only Handler may remain in Application only when it has no package or
transport dependency.

### D7 — Result and error ownership

Decide whether Use Case Output owns typed success/failure semantics and whether
Handlers may translate them.

Recommended direction:

- Use Case returns a transport-neutral typed Output/Result;
- Controller maps it to HTTP;
- message Handler maps failures to retry/dead-letter behavior;
- Use Case does not return `IActionResult`, broker acknowledgements, or
  framework-specific envelopes.

### D8 — Transaction and event lifecycle ownership

Confirm that repository, `IUnitOfWork`, outbox coordination, and pending Domain
Event acknowledgement dependencies belong to the Use Case implementation.

Recommended direction: Handler never introduces hidden strong consistency and
does not independently commit after invoking a Use Case.

### D9 — Concrete implementation naming

Choose one default:

- `CreateProductUseCase`;
- `CreateProductService`;
- another explicit suffix.

Recommended direction: `CreateProductUseCase` makes the concrete role visible and
removes the ambiguous optional `Application Service` terminology.

### D10 — Compatibility and migration

Decide how existing products that register
`ICreateProductUseCase -> CreateProductHandler` migrate.

Recommended staged rule:

- flag the shape as legacy/deprecated, not silently valid;
- introduce a concrete Use Case and move orchestration first;
- retain the Handler only if a dispatch entry actually consumes it;
- remove unused Handler registrations after callers migrate.

### D11 — Analyzer enforcement

Decide mandatory severity and coverage for:

- Controller dependencies on Handler, dispatcher, or message bus;
- Use Case interface and implementation shape;
- Handler-to-UseCase dependency direction;
- transport/package dependencies in Use Cases;
- legacy classes that implement both Use Case and Handler entry points.

Recommended default: deterministic boundary violations are errors; naming-only or
migration advisories remain warnings until target-repository markers exist.

### D12 — Wolverine and dispatcher policy

Confirm that Wolverine is:

- valid conditional guidance for messaging, outbox, consumers, and intentionally
  selected dispatch;
- not a portable requirement for normal synchronous API Use Cases;
- not automatically introduced by command/query implementation prompts.

## Skill Routing

| Stage | Capability | Skill | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| S0 | workflow orchestration | `dev-workflow` | High | Mandatory workflow gate and existing deferred task |
| S0-S2 | architecture | `ddd-ca-hex-architect` | High | Use Case/Handler/Controller/adapter boundary design |
| S3 | context governance | `ai-context-governance` | High | Prompts, reusable AI assets, guides, and examples |
| S4 | implementation | `slice-implementer` | High | Bounded analyzer and validation changes |
| S5 | workflow validation | `dev-workflow` | High | Cross-file consistency and closure |

## Stages

### S0 — Workflow bootstrap and pre-analysis

- Status: completed
- Outputs:
  - `workflow-plan.md`;
  - `review-report.md`;
  - `tasks/bootstrap-usecase-command-handler-workflow.json`.
- Validation:
  - branch starts from merged `main`;
  - workflow artifacts parse and links resolve;
  - findings cite active repository evidence.

### S1 — Resolve architecture decisions

- Status: pending
- Owner: `ddd-ca-hex-architect`
- Output:
  - approved D1-D12 decisions;
  - `tasks/resolve-usecase-command-handler-decisions.json`.
- Gate:
  - no canonical standards rewrite before user decisions are recorded.

### S2 — Align canonical standards

- Status: pending
- Owner: `ddd-ca-hex-architect`
- Primary scope:
  - `.dev/ARCHITECTURE.md`;
  - `.dev/standards/USECASE-COMMAND-HANDLER-RELATIONSHIP.MD`;
  - usecase/controller/test/project-structure standards;
  - DI and technology-profile rules.

### S3 — Synchronize context, prompts, guides, and examples

- Status: pending
- Owner: `ai-context-governance`
- Primary scope:
  - command/query/controller sub-agent prompts;
  - slice-implementer modes;
  - .NET backend templates and checklists;
  - controller/usecase/testing/DI examples and guides.

### S4 — Align analyzers and executable validation

- Status: pending
- Owner: `slice-implementer`
- Primary scope:
  - Controller and Use Case analyzer rules;
  - positive, negative, migration, and false-positive tests;
  - analyzer documentation and severity template.

### S5 — Final validation and closure

- Status: pending
- Owner: `dev-workflow`
- Validation:
  - all task JSON parses;
  - analyzer tests pass;
  - changed Markdown links resolve;
  - targeted role and invocation searches match approved decisions;
  - `git diff --check`;
  - deferred migration risks are recorded.

## Commit Checkpoints

1. `workflow(workflow): bootstrap use case handler alignment`
2. `workflow(workflow): record use case handler decisions`
3. `docs(architecture): align use case handler boundaries`
4. `docs(ai-context): synchronize use case handler guidance`
5. `feat(dotnet-backend): enforce use case handler boundaries`
6. `workflow(workflow): close use case handler alignment`

Each workflow-stage commit includes `Why`, `What`, `Validation`, and `Workflow`
sections.

## Completion Criteria

- Controller, Use Case, Input/Output, Command/Query, and Handler each have one
  canonical role.
- Synchronous API invocation has one default dependency chain.
- Framework-specific dispatch is conditional and cannot silently replace the
  Application port.
- Transaction and event lifecycle ownership is explicit.
- Prompts, examples, tests, DI guidance, and analyzers agree with the approved
  model.
- Migration guidance distinguishes legacy compatibility from the new default.
