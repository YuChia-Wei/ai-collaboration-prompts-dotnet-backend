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
- **Infrastructure**: Repository / ORM / Messaging / Integration
- **Adapter**: REST API Controllers, DTOs

完整專案結構與命名規則：[project-structure.md](./standards/project-structure.md)

詞彙與責任邊界：

- `Use Case`、`Command`、`Query`、`Handler`、`Application Service` 的關係見 [USECASE-COMMAND-HANDLER-RELATIONSHIP.MD](./standards/USECASE-COMMAND-HANDLER-RELATIONSHIP.MD)

### Target Repository Configuration

本 framework repository 不保存產品專用 `.dev/project-config.yaml`。

當 framework 被帶到目標 repo 時，先使用 `repo-structure-sync` 掃描 repo evidence，再依 `.ai/assets/skills/repo-structure-sync/templates/project-config.template.yaml` 產生 `.dev/project-config.yaml`。未確認的 architecture、database、messaging、frontend 或 deployment facts 必須保持空白。
