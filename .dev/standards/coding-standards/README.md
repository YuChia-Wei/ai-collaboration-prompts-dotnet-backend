# .NET Coding Standards

This directory contains all .NET coding-standard documents. Each document focuses on standards and best practices for a specific area.

---

## Navigation

Use [INDEX.MD](INDEX.MD) for the complete focused-standard catalog. This README
summarizes the shared rules and common navigation choices.

---

## 🔴 Key Principle Summary

### Mandatory Core Rules

#### 1. Repository Rules
- ✅ New code uses `IAggregateRepository<Aggregate, AggregateId>`
- ✅ Existing `IDomainRepository<Aggregate, AggregateId>` remains a compatibility contract
- ✅ The shared Aggregate Repository exposes only `FindByIdAsync()` and `SaveAsync()`
- ❌ Child Entity repositories and public generic CRUD repositories are prohibited
- ✅ Query ports implement `IQueryRepository` and remain read-only
- ✅ Physical purge and target-specific batch persistence use separate capabilities

#### 2. Aggregate Design
- ✅ Aggregate Repository profiles use soft deletion by default; targets may record an explicit opt-out
- ✅ Use public constructors rather than static factory methods
- ✅ Command methods must include `Contract.Ensure` postcondition checks

#### 3. Handler Design (CQRS)
- ✅ Commands and Queries must be separated
- ✅ Define Commands/Queries with `sealed record`
- ✅ Use Constructor Injection; `[FromServices]` is prohibited
- ✅ Use cases, services, mappers, and projections must be registered explicitly through `IServiceCollection`; attribute-based auto registration is prohibited
- ✅ Return `Result<T>` for error handling

#### 4. Testing Requirements
- ✅ Use xUnit + BDDfy by default; when the target team disables BDDfy, C# tests must still use GWT style
- ✅ Resolve the target mocking selection; default to NSubstitute
- ✅ Do not inherit from BaseTestClass
- ✅ Use `Guid.NewGuid().ToString()` for Aggregate Root IDs
- ✅ See [profile-configuration-standards.md](./profile-configuration-standards.md) for profile and environment rules

---

## 📋 Quick Navigation

### When you need to...
- **Create a new Aggregate** → See [aggregate-standards.md](./aggregate-standards.md)
- **Implement a Handler/Use Case** → See [usecase-standards.md](./usecase-standards.md)
- **Design a REST API** → See [controller-standards.md](./controller-standards.md)
- **Write tests** → See [test-standards.md](./test-standards.md)
- **Handle profile/environment/DI branches** → See [profile-configuration-standards.md](./profile-configuration-standards.md)
- **Handle queries** → See [projection-standards.md](./projection-standards.md)
- **Manage a Read Model** → See [archive-standards.md](./archive-standards.md)

---

## 🛠️ Technology Choices

Database, ORM, event store, message broker, and package versions are determined by target-repository evidence.

This framework may retain conditional/reference guidance for EF Core, Dapper, Npgsql, WolverineFx, RabbitMQ, Kafka, xUnit, NSubstitute, and similar technologies. Resolve target choices through [Target Technology Selection Policy](../TECHNOLOGY-SELECTION-POLICY.md); a reference or default selection must not overwrite an evidenced target choice.

---

## 📚 Related Documents

- [Architecture Document](../../ARCHITECTURE.md) - Overall architecture design
- [Technology Stack Requirements](../../requirement/TECH-STACK-REQUIREMENTS.MD) - Detailed technology-stack requirements
- [ADR Index](../../adr/INDEX.md) - Architecture decision records
- [Code Review Checklist](../CODE-REVIEW-CHECKLIST.md) - Code review checklist
