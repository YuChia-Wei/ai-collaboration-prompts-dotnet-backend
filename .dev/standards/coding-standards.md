# .NET DDD Wolverine Coding Standards

## 概述

這是 .NET 技術棧的編碼標準主文件，統整所有專門領域的編碼規範。
保留 DDD / Clean Architecture / CQRS / Event Sourcing 的設計精神。

**技術範圍**：.NET backend。Database、ORM、event store、broker 與 package 由 target repository evidence 決定；本 repo 的套件文件是 conditional/reference guidance。

## 專門領域編碼標準

### 1. [Aggregate Standards](./coding-standards/aggregate-standards.md)
- Aggregate Root 設計與事件溯源規範
- Domain Event 生命週期
- Invariant/Contract 的定義方式

### 2. [UseCase Standards](./coding-standards/usecase-standards.md)
- Command / Query 分離
- Handler 與交易邊界
- Input/Output DTO 規範

### 3. [Controller Standards](./coding-standards/controller-standards.md)
- ASP.NET Core API 設計規範
- Request/Response 處理
- 錯誤處理與驗證

### 4. [Repository Standards](./coding-standards/repository-standards.md)
- Aggregate Repository canonical/compatibility contract
- Pure Query Repository marker
- Conditional adapter guidance
- Outbox 與一致性要求

### 5. [Test Standards](./coding-standards/test-standards.md)
- xUnit 測試規範（未來將加入 BDDfy）
- NSubstitute mock 使用規則
- Profile-based testing

### 6. [Projection Standards](./coding-standards/projection-standards.md)
- CQRS Read Model 規範
- EF Core Projection 與效能策略

### 7. [Mapper Standards](./coding-standards/mapper-standards.md)
- DTO / Domain 轉換規則
- Mapper 類別結構

### 8. [Archive Standards](./coding-standards/archive-standards.md)
- Archive Pattern 與軟刪除
- 歷史資料追蹤

### 9. [Reactor Standards](./coding-standards/reactor-standards.md)
- Reactor 介面型別與事件處理邊界
- `DomainEventData` 規則
- replay / duplicate delivery 注意事項

### 10. [Profile / Environment Configuration Standards](./coding-standards/profile-configuration-standards.md)
- `DOTNET_ENVIRONMENT` / `ASPNETCORE_ENVIRONMENT` 規則
- `appsettings.{Environment}.json` 命名與覆蓋邏輯
- InMemory / Outbox profile-specific DI 約束

## 核心設計原則

### 1. Domain-Driven Design (DDD)
- Domain 邏輯集中於 Domain 層
- 使用 Ubiquitous Language
- Bounded Context 明確分離

### 2. Clean Architecture
- 依賴方向由外向內
- Domain 層不依賴框架
- Port & Adapter 模式

### 3. CQRS
- Command 與 Query 分離
- Read Model 與 Write Model 拆分

### 4. Event Sourcing
- 狀態變更以事件為主
- WolverineFx 作為事件/訊息處理框架

### 5. Testing Discipline
- Mutation Testing (Stryker.NET)
- Contract Testing（API/Message 契約）

## 實作規則

### ⚠ 程式碼風格
- **Prefer `this.` usage**：建議使用 `this.` 存取成員
- **資料夾命名**：專案內資料夾使用複數名稱
- **XML 文件註解**：Public API 必須撰寫 XML summary（使用繁體中文，台灣用語）

### ⚠ DTO 命名規則

| 層級 | Input 命名 | Output 命名 |
|------|-----------|------------|
| `<DomainName>.WebApi` | `*Request` | `*Response` |
| `<DomainName>.Applications` | `*Input` | `*Output` |

### ⚠ CQRS & Wolverine 規則

1. **不可變性**：Commands/Queries/Events 應為 immutable（建議使用 `record`）
2. **命名風格**：使用動作優先命名（如 `CreateOrder`、`GetProduct`）
3. **Handler 原則**：保持 Handler 小而專注，避免在 Handler 內處理基礎設施細節（使用注入的服務）
4. **冪等性**：Event 處理必須考慮 at-least-once delivery，在執行外部 I/O 前檢查重複

### ⚠ Command/Query 檔案放置規則

| 類型 | 規則 | 檔案命名 |
|------|------|---------|
| Command | Command + Handler 放同一 `.cs` 檔 | 以 Command 名稱命名 |
| Query | Query + Handler 放同一 `.cs` 檔 | 以 Query 名稱命名 |

### ⚠ Event 放置規則

| Event 類型 | 放置位置 |
|-----------|---------|
| Domain Events | `./src/<Domain>/DomainCore/<DomainName>.Domains/DomainEvents` |
| Domain Event Handlers | `./src/<Domain>/DomainCore/<DomainName>.Applications/DomainEventHandlers` |
| Integration Event Handlers | `./src/<Domain>/Presentation/<DomainName>.Consumer/IntegrationEventHandlers` |
| Integration Event Schema | `./src/BC-Contracts/Lab.MessageSchemas.<Domain>` |

### ⚠ Repository 與 Query Port 規範

Portable Aggregate Repository：

```csharp
public interface IAggregateRepository<TAggregate, TId>
    where TAggregate : AggregateRoot<TId>
{
    Task<TAggregate?> FindByIdAsync(TId id, CancellationToken cancellationToken = default);
    Task SaveAsync(TAggregate aggregate, CancellationToken cancellationToken = default);
}
```

Compatibility：

```csharp
public interface IDomainRepository<TAggregate, TId>
    : IAggregateRepository<TAggregate, TId>
    where TAggregate : AggregateRoot<TId>
{
}
```

核心規則：

- Repository root 必須是 Aggregate Root，禁止 child Entity repository。
- Shared Aggregate Repository 只有 `FindByIdAsync` 與 `SaveAsync`。
- Soft delete 是 Aggregate behavior + `SaveAsync`。
- Physical purge 使用 restricted capability port。
- Query ports 必須實作 `IQueryRepository` 且只讀。
- 簡單 Query 可直接使用 Query Repository；只有 composition/policy/calculation 才增加 Application Query Service。
- Database、ORM、event store 與 package 由 target repo 決定。
- Batch persistence 是 target-specific opt-in pattern，不是 portable default interface。
- 一般單 Aggregate Use Case 不預設注入 `IUnitOfWork`；只有明確 strong consistency requirement 才顯式依賴。
- Commit 成功前不得 clear/acknowledge pending Domain Events。

完整規則：

- [Repository Standards](./coding-standards/repository-standards.md)
- [Projection Standards](./coding-standards/projection-standards.md)
- [Aggregate Repository Rationale](./rationale/generic-repository-only-rationale.MD)
- [Query-side Layering Rationale](./rationale/query-side-layering-rationale.MD)

### ⚠ Profile-Based Testing
- **禁止使用 BaseTestClass / BaseUseCaseTest 作為測試父類**
- 所有測試必須支援 `test-inmemory` 與 `test-outbox` profiles
- 使用 `appsettings.*.json` 控制 profile
- profile 命名、載入、DI 分支與 profile-specific infra 規則以 [Profile / Environment Configuration Standards](./coding-standards/profile-configuration-standards.md) 為準

### ⚠ Outbox / Inbox Pattern
- 使用 WolverineFx 的 Outbox 機制確保事件發佈的可靠性
- 如導入 Inbox Pattern，Consumer 端亦應遵循相同慣例
- 交易邊界：命令處理內的狀態改變需與儲存一致性策略對齊

## 自動化檢查

```bash
# Transitional local orchestrator
.ai/scripts/check-all.sh

# Transitional spec helper
.ai/scripts/check-spec-compliance.sh <spec-file> <task-name>

# Mutation testing runner
.ai/scripts/check-mutation-coverage.sh
```

> `.ai/scripts` 目前是過渡期 AI workflow / orchestration 區。C# 語意規則應逐步移轉到 Roslyn Analyzer、`.editorconfig`、`dotnet format`、architecture tests、dotnet tests 或 dotnet tools。

## 相關文件

- [最佳實踐](./best-practices.md)
- [反模式](./anti-patterns.md)
- [編碼指南](./coding-guide.md)
- [程式碼審查清單](./CODE-REVIEW-CHECKLIST.md)
