# Architecture Config (Dotnet)

## Source of Truth
- A generated `.dev/project-config.yaml` may summarize confirmed architecture mode, database libraries, and profile support in a target repository.
- Repository code, project files, and package references remain stronger evidence.

## Supported Patterns
- **inmemory**: In-memory repository + message broker
- **outbox**: Transactional message store using the target repository's selected adapter
- **eventsourcing**: Event store + replay

## Mapping Rules
- Command flows use `IAggregateRepository<TAggregate, TId>` for Aggregate Roots
- Query flows use read-only ports inheriting `IQueryRepository`
- Reactor handlers process event data (not domain entities)
- Persistence libraries and databases are selected by the target repository

## DI Registration Rules
- Register repositories per profile/environment
- Prefer explicit registration over scanning

## Outbox Pattern (WolverineFx)
- Persist event first
- Relay to message broker
- Keep metadata for audit
