# Repository 編碼規範 (.NET)

本文件是 Aggregate persistence 與 query-side data access 的 canonical standard。

本規範定義 application port 語意，不指定資料庫、ORM、event store 或套件。EF Core、Dapper、Npgsql 與其他 adapter 的內容只作條件式實作指引。

## 核心邊界

Repository 規則分為三種角色：

| 角色 | 用途 | 可否修改資料 | 主要回傳型別 |
| --- | --- | --- | --- |
| Aggregate Repository | 重新載入與持久化 Aggregate Root | 是 | Aggregate Root |
| Query Repository | 純查詢 read model | 否 | DTO、read model、ID、scalar、page |
| Capability-specific Writer | Outbox、projection、import、purge 等明確能力 | 是 | 依能力定義，不回傳 Aggregate |

Repository interface 是 Application outbound port。EF Core、Dapper、SQL、event store、file 或 remote persistence implementation 是 Infrastructure outbound adapter。

## Aggregate Repository

### Canonical contract

```csharp
public interface IAggregateRepository<TAggregate, TId>
    where TAggregate : AggregateRoot<TId>
{
    Task<TAggregate?> FindByIdAsync(
        TId id,
        CancellationToken cancellationToken = default);

    Task SaveAsync(
        TAggregate aggregate,
        CancellationToken cancellationToken = default);
}
```

規則：

- `TAggregate` 必須是 Aggregate Root。
- Child Entity 不得擁有可由 Application 獨立注入的 Repository。
- `FindByIdAsync` 只按 Aggregate identity 載入。
- `SaveAsync` 表達「持久化已完成 domain behavior 的 Aggregate」。
- Adapter 可依技術採 insert、update、upsert、tracked persistence 或 event append。
- Repository 不得包含 status、name、filter、paging 或 DTO query methods。
- Repository 不得自行執行 domain behavior。
- Repository 不得在 persistence 成功前清除 pending Domain Events。

### Compatibility contract

既有產品可能已使用 `IDomainRepository` 表示 Aggregate Repository。為降低 context 導入時的無效遷移噪音，保留 compatibility contract：

```csharp
public interface IDomainRepository<TAggregate, TId>
    : IAggregateRepository<TAggregate, TId>
    where TAggregate : AggregateRoot<TId>
{
}
```

規則：

- 新程式碼優先使用 `IAggregateRepository<TAggregate, TId>`。
- `IDomainRepository<TAggregate, TId>` 不是第二種 repository model。
- Compatibility contract 仍必須套用所有 Aggregate Root 限制。
- `IDomainRepository<ChildEntity, TId>` 是違規，不得因相容性而忽略。
- Aggregate-specific interface 只有在相容既有程式碼或增加穩定 Aggregate lifecycle 語意時才建立。
- 禁止只為重新命名而建立無語意的空殼 interface。

## 禁止的通用寫入介面

Application code 不得依賴可接受任意 Entity 或 table model 的公開 CRUD abstraction，例如：

- `IRepository<TEntity, TId>`
- `IGenericRepository<TEntity, TId>`
- `IWritableRepository<TEntity, TId>`
- `ICrudRepository<TEntity, TId>`

Infrastructure adapter 內部可以使用 private/internal DAO、table gateway 或 persistence helper，但不得把它們直接暴露為 Application port。

## Query Repository

### Marker

```csharp
public interface IQueryRepository
{
}
```

Query-specific port 必須實作 marker：

```csharp
public interface IProductQueryRepository : IQueryRepository
{
    Task<ProductDetailsDto?> FindDetailsAsync(
        ProductId id,
        CancellationToken cancellationToken = default);

    Task<IReadOnlyList<ProductId>> FindIdsByStatusAsync(
        ProductStatus status,
        CancellationToken cancellationToken = default);
}
```

規則：

- Query Repository 是純讀取 port。
- 允許回傳 DTO、read model、ID、scalar 或 page。
- 禁止回傳可被修改後保存的 Aggregate Root 或 child Entity。
- 禁止 `Save`、`Add`、`Update`、`Delete`、`Remove` 或等價 persistence write。
- Query criteria 可以依 use case/read model 設計，不必模擬 Aggregate Repository。
- Query Repository implementation 位於 Infrastructure。

### Optional Query Service

簡單 Query 可以由 Application boundary 直接依賴 Query Repository。

只有在下列情況才新增 Application Query Service：

- 組合多個 Query Repository 或外部 read source；
- 有可重用的 query policy；
- 有非單純 mapping 的 calculation 或 orchestration。

禁止為每個 Query 強制建立 pass-through Query Service。

## Delete 與 Purge

### Soft delete

Soft delete 是 Aggregate behavior：

```csharp
aggregate.Delete(actorId, reason);
await repository.SaveAsync(aggregate, cancellationToken);
```

Repository 不應以 physical row deletion 取代 Aggregate deletion invariant。

### Physical purge

Physical deletion 使用獨立且受限的 capability port，不放入 shared Aggregate Repository：

```csharp
public interface IAggregatePurgePort<TAggregate, TId>
    where TAggregate : AggregateRoot<TId>
{
    Task PurgeAsync(
        TId id,
        CancellationToken cancellationToken = default);
}
```

Purge Use Case 必須先完成：

- authorization；
- retention policy；
- legal/audit constraints；
- Aggregate eligibility；
- related outbox/archive/attachment cleanup policy。

## Transaction 與 Unit of Work

Eventual consistency 是跨 Aggregate coordination 的預設。

一般單一 Aggregate Use Case 不因使用 Repository 就自動注入 `IUnitOfWork`。

只有 Use Case 明確要求多個 persistence participant 同步 commit/rollback 時，才顯式依賴：

```csharp
public interface IUnitOfWork
{
    Task CommitAsync(CancellationToken cancellationToken = default);
}
```

規則：

- 顯式 dependency 表達 exceptional strong-consistency requirement。
- Repository 在參與外部 Unit of Work 時不得自行 commit。
- Repository-owned independent commits 不得破壞 Aggregate + Outbox atomicity。
- Transaction middleware/decorator 可以實作 mechanics，但不得隱藏 Use Case 宣告的強一致性 dependency。

Domain Event lifecycle：

1. 執行 Use Case orchestration 與 Aggregate behavior。
2. 取得 pending Domain Events。
3. 原子持久化 Aggregate state/events 與必要 Outbox records。
4. Commit。
5. Commit 成功後才 acknowledge/clear pending events。
6. 失敗時保留 retry 與 optimistic concurrency 語意。

## Target-specific Aggregate Batch Capability

Portable building blocks 不發布 mandatory `IAggregateBatchRepository`。

Target repository 只有在具備量測證據時，才可定義 batch port，例如：

```csharp
public interface IProductAggregateBatchPort
{
    Task<IReadOnlyList<ProductAggregate>> FindByIdsAsync(
        IReadOnlyCollection<ProductId> ids,
        CancellationToken cancellationToken = default);

    Task SaveAllAsync(
        IReadOnlyCollection<ProductAggregate> aggregates,
        CancellationToken cancellationToken = default);
}
```

啟用條件：

- 預期 cardinality 確實大於一；
- 已量測 N+1 IO、latency 或 throughput 問題；
- Adapter 確實能提供有效 batch optimization；
- 已定義 missing/duplicate IDs、ordering 與 maximum batch size；
- 已定義 optimistic concurrency、partial failure、retry 與 resume；
- 已定義每個 Aggregate 的 pending events 與 Outbox 語意；
- 不把 batch port 放入 default template、default DI 或一般 Use Case。

Batch port：

- 不繼承 `IAggregateRepository<TAggregate, TId>`；
- 只接受 Aggregate Root；
- `FindByIdsAsync` 仍是 identity-based load；
- 不允許 status/filter query；
- 不得替代逐一執行 Aggregate behavior。

`IUnitOfWork` 決定 all-or-nothing business transaction；batch methods 只決定 IO shape。

大量工作預設採 bounded chunks、retry 與 resumable progress。禁止對無上限集合建立單一長交易。

Imports、migrations、projection rebuilds 或 purge 若不執行正常 Aggregate behavior，應使用 capability-specific writer，而不是 Aggregate batch port。

## Conditional Adapter Guidance

### EF Core

- Query/read-model flow 應依 tracking policy 使用 `AsNoTracking` 或 direct projection。
- Aggregate load 是否 tracking，取決於 adapter 採 direct domain mapping、persistence model mapping 或 tracked aggregate strategy。
- 使用符合 cardinality 的 async terminal operator，例如 `ToListAsync`、`SingleOrDefaultAsync`、`FirstOrDefaultAsync`、`AnyAsync` 或 `CountAsync`。
- 不得使用 sync-over-async。
- Optimistic concurrency 必須有明確 token/version mapping 與 conflict handling。
- `SaveChangesAsync` 成功前不得 clear Domain Events。

### Dapper / direct SQL

- Connection/transaction lifetime 必須與 Unit of Work 或 adapter atomic operation 對齊。
- Update/delete SQL 必須檢查 optimistic concurrency version 或等價條件。
- Multi-statement Aggregate persistence 與 Outbox 必須共用 atomic boundary。
- Mapping completeness 由 tests 與 review 驗證。

### Event store

- Append 必須帶 expected version 或等價 concurrency condition。
- 只 append pending events。
- Append/commit 成功後才 mark events committed。
- Snapshot 是 optimization，不得取代 event stream source of truth。

## Automated Validation Ownership

Repository semantic diagnostics 使用 Roslyn symbol/type analysis，不使用 filename 或 grep 作為 CI authority。

必須驗證：

- canonical `IAggregateRepository<,>` generic argument 是 Aggregate Root；
- compatibility `IDomainRepository<,>` 與所有 derived interfaces 套用相同規則；
- shared Aggregate Repository method surface 只有 `FindByIdAsync` 與 `SaveAsync`；
- Query Repository marker 的 ports 不包含 writes 或 mutable domain return types；
- child Entity 不得成為 repository root；
- violations 的 default severity 是 `error`。

Target-specific batch ports 的 analyzer/architecture-test 規則由 target repository 依 local marker 啟用。Portable analyzer 不依賴尚未完成的 Use Case/Handler taxonomy。

## Review Checklist

### Aggregate Repository

- [ ] 使用 `IAggregateRepository<TAggregate, TId>`，或相容的 `IDomainRepository<TAggregate, TId>`。
- [ ] `TAggregate` 是 Aggregate Root。
- [ ] Shared contract 只有 `FindByIdAsync` 與 `SaveAsync`。
- [ ] 沒有 child Entity repository。
- [ ] 沒有 DTO/filter/paging query methods。
- [ ] Repository 不執行 domain behavior。

### Query Repository

- [ ] 實作 `IQueryRepository` marker。
- [ ] 只回傳 read-side types、IDs 或 scalar。
- [ ] 沒有 persistence writes。
- [ ] 簡單 Query 沒有不必要的 pass-through Query Service。

### Transaction / Events

- [ ] `IUnitOfWork` 只用於明確 strong-consistency Use Case。
- [ ] Repository 參與 Unit of Work 時不自行 commit。
- [ ] Aggregate state/events 與 Outbox 的 atomicity 已定義。
- [ ] Commit 成功後才 clear/acknowledge pending events。

### Optional Batch

- [ ] Target repo 有量測證據與明確 batch semantics。
- [ ] Batch port 未進入 portable/default contract。
- [ ] 大量工作採 bounded chunks。
- [ ] Partial failure、retry、concurrency 與 event/outbox 已定義。

## Related Documents

- [Aggregate Standards](aggregate-standards.md)
- [Projection Standards](projection-standards.md)
- [Use Case Standards](usecase-standards.md)
- [Generic Repository Rationale](../rationale/generic-repository-only-rationale.MD)
- [Query-side Layering Rationale](../rationale/query-side-layering-rationale.MD)
