# Architecture

本文件提供可重用的 .NET backend architecture context 入口。詳細技術選型見 [TECH-STACK-REQUIREMENTS.MD](./requirement/TECH-STACK-REQUIREMENTS.MD)，專案結構見 [project-structure.md](./standards/project-structure.md)。

## Architecture Overview

### Core Architecture
- **Style**: Clean Architecture + DDD + CQRS
- **Patterns**: Outbox / InMemory / Event Sourcing（依 aggregate 設定）
- **Use Case 分類**：Command / Query / Reactor

### Code Organization (概念層級)
- **Domain**: Aggregates, Entities, Value Objects, Domain Events
- **Application**: Use Cases（Command/Query/Reactor ports）
- **Infrastructure**: Persistence adapters / ORM or direct SQL / Messaging / Integration
- **Adapter**: REST API Controllers, DTOs

完整專案結構與命名規則：[project-structure.md](./standards/project-structure.md)

### Persistence Port Model

- `IAggregateRepository<TAggregate, TId>`：Aggregate Root persistence canonical port。
- `IDomainRepository<TAggregate, TId>`：相容既有產品的 compatibility port，繼承 `IAggregateRepository`。
- `IQueryRepository`：pure query port marker。
- Physical purge、Outbox、Projection、Import 等寫入使用 capability-specific ports。
- Child Entity 不得擁有可由 Application 獨立注入的 Repository。
- Database、ORM、event store 與 package 由 target repository 決定。
- Batch Aggregate persistence 是 target-specific opt-in capability，不屬於 portable default contract。

詞彙與責任邊界：

- `Use Case`、`Command`、`Query`、`Handler` 的關係見 [USECASE-COMMAND-HANDLER-RELATIONSHIP.MD](./standards/USECASE-COMMAND-HANDLER-RELATIONSHIP.MD)

### Application Inbound Port Model

- `I<Operation>UseCase` 是 Application inbound port。
- `<Operation>UseCase` 使用 `ExecuteAsync` 實作 application orchestration。
- HTTP Controller 預設直接依賴 Use Case interface。
- 只有明確核准的純查詢 endpoint 可例外直連唯讀 Query Repository/Service。
- Command/message Handler 只在真實 dispatch entry 存在，負責 mapping 後呼叫
  一個 Use Case；Handler 不得成為 Use Case implementation。
- Use Case 依賴 project-owned outbound event publisher port，不直接依賴
  Wolverine `IMessageBus`。
- Wolverine/MediatR/MQ-specific Handler 屬於 inbound adapter/composition
  boundary；package-neutral convention Handler 才可留在 Application。

### Target Repository Configuration

本 framework repository 不保存產品專用 `.dev/project-config.yaml`。

當 framework 被帶到目標 repo 時，先使用 `repo-structure-sync` 掃描 repo evidence，再依 `.ai/assets/skills/repo-structure-sync/templates/project-config.template.yaml` 產生 `.dev/project-config.yaml`。未確認的 architecture、database、messaging、frontend 或 deployment facts 必須保持空白。

本 framework 中的 EF Core、Dapper、Npgsql、WolverineFx、RabbitMQ 與 Kafka 文件屬於 conditional/reference guidance，不得自動轉成 target repository 的 mandatory truth。
