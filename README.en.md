# Distributed Architecture Lab

[繁體中文](README.md)

`dotnet distributed architecture lab` is a sample backend project built with **.NET 10**, **C# 14**, containerization, and modern architecture practices such as **Clean Architecture**, **DDD**, and **CQRS**.

It is meant to show how a distributed system can be organized with DDD, CA, CQRS, and message-driven integration. The repo also demonstrates spec-driven collaboration with AI agents and Spec-Kit.

The current solution centers on two business domains:

- **SaleOrders**
- **SaleProducts**

These services communicate asynchronously through **RabbitMQ** or **Kafka**.

## Architecture

- **Clean Architecture** for dependency and responsibility separation
- **Domain-Driven Design** for core domain modeling
- **CQRS** for splitting write and read flows
- **WolverineFx** for command, query, and message handling
- **PostgreSQL** as the main database
- **Docker** for runtime and deployment

## Tech Stack

- **Runtime:** .NET 10
- **Language:** C# 14
- **Messaging / handlers:** WolverineFx
- **Database:** PostgreSQL
- **Broker:** RabbitMQ / Kafka
- **Containerization:** Docker

## Package Snapshot

Version numbers below reflect the current `*.csproj` files:

- `WolverineFx` `5.16.2` with `WolverineFx.Kafka` and `WolverineFx.RabbitMQ`
- `Dapper` `2.1.66`
- `Npgsql` `10.0.1`
- `xunit` `2.9.3`
- `xunit.runner.visualstudio` `3.1.5`
- `Microsoft.NET.Test.Sdk` `18.0.1`

## Run the Project

The project is fully containerized. You only need Docker and Docker Compose on your machine.

1. Choose the message broker in `docker-compose/docker-compose.yml` by setting `QUEUE_SERVICE`:
   - `Kafka` is the default
   - change it to `RabbitMQ` to use RabbitMQ instead

2. Start the full stack from the repository root:

   ```bash
   docker-compose -f ./docker-compose/docker-compose.yml up -d
   ```

3. The compose setup brings up:
   - `orders-api`
   - `orders-consumer`
   - `product-api`
   - `product-consumer`
   - `postgres`
   - `rabbitmq` when RabbitMQ is selected
   - `kafka` and `kafka-ui` when Kafka is selected

## API Endpoints

Both web APIs expose interactive documentation through Scalar.

### Orders API

- API docs: http://localhost:8080/scalar/v1
- OpenAPI spec: http://localhost:8080/openapi/v1

### Products API

- API docs: http://localhost:8090/scalar/v1
- OpenAPI spec: http://localhost:8090/openapi/v1

## Service UIs

- **Kafka UI:** http://localhost:8088
- **RabbitMQ Management UI:** http://localhost:15672
  - Username: `guest`
  - Password: `guest`

## Repository Layout

| Path | Purpose |
| --- | --- |
| `./.codex` | Codex CLI assets |
| `./.gemini` | Gemini CLI assets |
| `./.github` | GitHub and GitHub Copilot assets |
| `./.ai/assets` | Canonical reusable AI assets, including skills, commands, and shared packages |
| `./.specify` | Spec-Kit scripts and prompt templates |
| `./docker-compose` | Docker Compose files, deployment settings, and related data |
| `./docs` | Documentation and working notes |
| `./https` | HTTP request files for quick API testing |
| `./specs` | Feature specifications generated through spec-driven development |
| `./sql-script` | Database scripts |
| `./src` | .NET source code |
| `./src/BC-Contracts` | Cross-boundary communication contracts, including integration events and request/reply DTOs |
| `./src/BuildingBlocks` | Shared architectural building blocks such as `AggregateRoot` and `ValueObject` |
| `./src/Shared` | Shared kernel concepts used across bounded contexts |
| `./src/<DomainName>` | A business domain |
| `./src/<DomainName>/DomainCore` | Domain core projects, including domain, application, and infrastructure concerns as needed |
| `./src/<DomainName>/Presentation` | Presentation projects such as Web API and consumer hosts |
| `./tests` | Test projects, including xUnit tests and k6 E2E scripts |

## AI Collaboration Context

This repository keeps its AI collaboration rules and reusable prompts in dedicated folders:

- `agents.md` and `.github/copilot-instructions.md` provide default context for supported AI tools
- `.agents/skills/` and `.claude/skills/` are thin runtime wrappers
- `.ai/assets/` is the canonical source for reusable AI assets

The repo also includes translated Spec-Kit prompt material so the workflow can be studied and reused across Codex, Gemini CLI, and GitHub Copilot.

## Spec-Driven Development

- [Spec-Kit](https://github.com/github/spec-kit)

The repo is set up to support spec-driven collaboration with AI agents, including constitutions, plans, tasks, and implementation flows.
