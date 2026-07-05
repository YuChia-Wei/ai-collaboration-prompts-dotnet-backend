# Projection 與 Query Repository 編碼規範 (.NET)

本文件定義 CQRS read side 的 port、adapter、optional Query Service 與 provider-specific 注意事項。

## 核心規則

- Query side 不修改 Domain state。
- Query side 回傳 DTO、read model、ID、scalar 或 page，不回傳可保存的 Aggregate Root。
- Query Repository 是 Application outbound port，implementation 是 Infrastructure adapter。
- 簡單 Query 不強制增加 pass-through Query Service。
- Provider-specific tracking、materialization 與 model registration 規則只套用於使用該 provider 的 adapter。

## Query Repository Port

所有 query repository port 必須實作 canonical marker：

```csharp
public interface IQueryRepository
{
}
```

```csharp
public interface IProductQueryRepository : IQueryRepository
{
    Task<ProductDetailsDto?> FindDetailsAsync(
        ProductId id,
        CancellationToken cancellationToken = default);

    Task<IReadOnlyList<ProductId>> FindIdsByStatusAsync(
        ProductStatus status,
        CancellationToken cancellationToken = default);

    Task<PagedResult<ProductSummaryDto>> SearchAsync(
        ProductSearchCriteria criteria,
        CancellationToken cancellationToken = default);
}
```

允許：

- use-case/read-model-specific criteria；
- DTO/read model projection；
- identity list、scalar、count、existence；
- paging、sorting、filtering；
- EF Core、Dapper、SQL 或其他 read adapter。

禁止：

- `Save`、`Add`、`Update`、`Delete`、`Remove`；
- `SaveChanges` 或等價 persistence write；
- 回傳 mutable Aggregate Root 或 child Entity；
- Domain behavior；
- 把 Query Repository 當成 Aggregate persistence port。

## Query Application Flow

### Simple query

Application boundary 可以直接依賴 Query Repository：

```text
Application Query Boundary
  -> IProductQueryRepository
  -> Infrastructure Query Adapter
  -> DTO / Read Model
```

### Composed query

只有在下列情況新增 Application Query Service：

- 組合多個 Query Repository；
- 組合 remote/read cache source；
- 可重用 query policy；
- 非單純 mapping 的 calculation/orchestration。

```text
Application Query Boundary
  -> ProductQueryService
     -> IProductQueryRepository
     -> IInventoryQueryRepository
  -> DTO / Read Model
```

Query Service implementation 位於 Application，且不得直接依賴 DbContext、connection 或 provider API。

Infrastructure 若直接實作 Query Repository port，不應再把該 adapter 命名為 Application Query Service。

## Candidate IDs for Aggregate Behavior

Query Repository 可以先取得符合 read criteria 的 Aggregate IDs：

```csharp
var ids = await productQueries.FindIdsByStatusAsync(
    ProductStatus.Expired,
    cancellationToken);
```

Application 接著依 identity 重新載入 Aggregate，並由每個 Aggregate 重新驗證當前狀態與 invariant。

Query 結果是 candidate snapshot，不得直接視為 command-side truth。

## DTO 與 Paging

DTO 建議使用 immutable `record`：

```csharp
public sealed record ProductSummaryDto(
    string Id,
    string Name,
    string Status);
```

Paged result 必須明確包含 items 與 paging metadata：

```csharp
public sealed record PagedResult<T>(
    IReadOnlyList<T> Items,
    long TotalCount,
    int Page,
    int PageSize);
```

不得要求所有 Query Repository 都提供 paging；只有 use case 需要時才加入。

## Conditional EF Core Guidance

只有 EF Core query adapter 適用：

- Read-only query 優先使用 direct projection。
- 若 global tracking policy 未關閉 tracking，read model query 應明確使用 `AsNoTracking()`。
- Aggregate command-side load 不套用本節的 read-model tracking規則。
- 使用符合 cardinality 的 async terminal operator：
  - collection: `ToListAsync`
  - zero-or-one: `SingleOrDefaultAsync` 或 `FirstOrDefaultAsync`
  - existence: `AnyAsync`
  - count: `CountAsync` / `LongCountAsync`
- 不得以 `ToList()`、`.Result` 或 `.Wait()` 取代 async execution。
- 避免 client-side evaluation 與不必要的 entity materialization。
- Optimistic concurrency 與 command-side persistence 不屬於 Query Repository。

EF projection read model 若需要 model registration validation，實作 `IProjectionReadModel` 或 target repo 的等價 marker。

## Conditional Dapper / SQL Guidance

- SQL 必須 parameterized。
- Mapping 必須覆蓋 DTO/read model required fields。
- 大量結果必須定義 paging、streaming 或 bounded materialization。
- Query cancellation 應傳遞給 provider API。
- Transaction 只有在 query consistency requirement 明確需要時使用。

## Automated Validation Ownership

- Roslyn analyzer：
  - `IQueryRepository` derived ports 不得宣告 persistence write methods；
  - 不得回傳 Aggregate Root 或 child Entity；
  - projection services 不得呼叫 provider write APIs。
- Configuration tests：
  - EF read models 的 assembled model registration。
- Tests / profiling / AI review：
  - query shape、N+1、index usage、tracking policy、mapping completeness、performance。

不得使用檔名或 grep 判斷 Query Repository 語意。

## Review Checklist

- [ ] Query Repository 實作 `IQueryRepository`。
- [ ] Port 位於 Application，adapter 位於 Infrastructure。
- [ ] 回傳 DTO/read model/ID/scalar/page。
- [ ] 沒有 write methods 或 provider writes。
- [ ] 簡單 Query 沒有不必要的 pass-through Query Service。
- [ ] Candidate IDs 在 command flow 中重新載入 Aggregate 並驗證 invariant。
- [ ] Provider-specific async/materialization 規則正確。
- [ ] Large result set 有 paging/streaming/bound。

## Related Documents

- [Repository Standards](repository-standards.md)
- [Use Case Standards](usecase-standards.md)
- [Query-side Layering Rationale](../rationale/query-side-layering-rationale.MD)
