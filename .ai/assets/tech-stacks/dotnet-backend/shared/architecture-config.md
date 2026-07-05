# Architecture Config (Dotnet)

## Source of Truth
- A generated `.dev/project-config.yaml` may summarize confirmed architecture mode, database libraries, and profile support in a target repository.
- Repository code, project files, and package references remain stronger evidence.

## Supported Patterns
- **inmemory**: In-memory repository + message broker
- **outbox**: EF Core + Outbox message store
- **eventsourcing**: Event store + replay

## Mapping Rules
- Command handlers use write model repositories
- Query handlers use read model projections
- Reactor handlers process event data (not domain entities)

## DI Registration Rules
- Register repositories per profile/environment
- Prefer explicit registration over scanning

## Outbox Pattern (WolverineFx)
- Persist event first
- Relay to message broker
- Keep metadata for audit
