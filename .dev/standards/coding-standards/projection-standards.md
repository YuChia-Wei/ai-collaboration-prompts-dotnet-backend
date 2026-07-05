# Projection 編碼規範 (.NET)

本文件定義 Projection Pattern 的編碼標準，用於處理查詢需求和資料投影。

---

## 📌 概述

Projection 為 CQRS 的 Read Model，負責查詢與效能優化。

- **只讀操作**：Projection 不得包含 Domain 變更行為
- **讀寫分離**：Read Model 與 Write Model 必須分離
- **效能優化**：使用 EF Core Query/Projection 提升效能

**Projection** 是一種查詢模式，在 CQRS 架構中，專門用於「Query Model」：

- 複雜查詢需求（Repository 只限定在 Command Model 操作單一 Aggregate 使用）
- 跨聚合查詢
- 報表和統計查詢
- 返回 DTO (Data Transfer Object) 而非領域物件
- Handler 層的 Query 物件會呼叫 Projection，取得 DTO 傳給呼叫端

---

## 🏷️ 自動化驗證責任

- `DBA1013`：實作 canonical `IProjection` marker 的 query service 不得呼叫 EF Core persistence write operations。
- `DotnetBackendValidation`：實作 `IProjectionReadModel` marker 的 EF read model 必須存在於 assembled `DbContext.Model`。
- `AsNoTracking`、projection shape 與 query efficiency：依 provider、global tracking policy 與實際 query 由 tests、profiling 和 AI review 判斷，不以 source text 作為 CI gate。
- Dapper-only DTO 與 query service 不受 EF model registration gate 約束。

---

## 🔴 必須遵守的規則 (MUST FOLLOW)

### 1. Query Service Interface 設計

#### 命名空間

```csharp
// ✅ 正確：定義在 Application 層
namespace YourProject.Application.Records.Queries;

// ❌ 錯誤：不要放在 Infrastructure 層
namespace YourProject.Infrastructure.Queries;  // 錯誤！
```

#### Interface 命名規範

```csharp
// ✅ 正確：使用 I[Aggregate]QueryService 命名
public interface IRecordQueryService { }
public interface IIterationQueryService { }
public interface IWorkItemQueryService { }

// ❌ 錯誤：不要使用其他命名模式
public interface IRecordProjection { }       // 不要用 Projection
public interface IRecordFinder { }           // 不要用 Finder
public interface RecordDtoProjection { }     // 不要用 DtoProjection
```

#### 方法設計

```csharp
// ✅ 正確：返回 DTO 物件
public interface IRecordQueryService
{
    Task<RecordDto?> GetByIdAsync(RecordId id, CancellationToken ct = default);
    Task<List<RecordDto>> GetByStateAsync(string state, CancellationToken ct = default);
    Task<PagedResult<RecordDto>> GetPagedAsync(
        string? filter, 
        int page, 
        int size, 
        CancellationToken ct = default);
}

// ❌ 錯誤：不要返回領域物件
public interface IRecordQueryService
{
    Task<Record?> GetByIdAsync(RecordId id);  // 錯誤！應返回 DTO
}

// ❌ 錯誤：不要返回 Data (Persistence Object)
public interface IRecordQueryService
{
    Task<RecordData?> GetByIdAsync(string id);  // 錯誤！應返回 DTO
}
```

---

### 2. Query Service 實作

#### 實作位置

```csharp
// ✅ 正確：實作放在 Infrastructure 層
namespace YourProject.Infrastructure.Persistence.QueryServices;
```

#### EF Core 實作範例

```csharp
// ✅ 正確：使用 EF Core 實作
namespace YourProject.Infrastructure.Persistence.QueryServices;

public class RecordQueryService : IRecordQueryService
{
    private readonly ApplicationDbContext _context;

    public RecordQueryService(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<RecordDto?> GetByIdAsync(RecordId id, CancellationToken ct = default)
    {
        var data = await _context.Records
            .AsNoTracking()
            .Where(x => x.Id == id.Value)
            .FirstOrDefaultAsync(ct);
        
        return data is null ? null : RecordMapper.ToDto(data);
    }

    public async Task<List<RecordDto>> GetByStateAsync(string state, CancellationToken ct = default)
    {
        return await _context.Records
            .AsNoTracking()
            .Where(x => x.State == state)
            .Select(x => RecordMapper.ToDto(x))
            .ToListAsync(ct);
    }

    public async Task<PagedResult<RecordDto>> GetPagedAsync(
        string? filter,
        int page,
        int size,
        CancellationToken ct = default)
    {
        var query = _context.Records.AsNoTracking();
        
        if (!string.IsNullOrEmpty(filter))
        {
            query = query.Where(x => x.Name.Contains(filter));
        }
        
        var totalCount = await query.CountAsync(ct);
        
        var items = await query
            .OrderBy(x => x.Name)
            .Skip(page * size)
            .Take(size)
            .Select(x => RecordMapper.ToDto(x))
            .ToListAsync(ct);
        
        return new PagedResult<RecordDto>(items, totalCount, page, size);
    }
}
```

---

### 3. DI 註冊

```csharp
// ✅ 正確：在 Program.cs 或 ServiceExtensions 中註冊
public static class QueryServiceExtensions
{
    public static IServiceCollection AddQueryServices(this IServiceCollection services)
    {
        services.AddScoped<IRecordQueryService, RecordQueryService>();
        services.AddScoped<IIterationQueryService, IterationQueryService>();
        services.AddScoped<IWorkItemQueryService, WorkItemQueryService>();
        
        return services;
    }
}
```

---

### 4. PagedResult 定義

```csharp
// ✅ 定義分頁結果類別
public sealed record PagedResult<T>(
    IReadOnlyList<T> Items,
    int TotalCount,
    int Page,
    int PageSize)
{
    public int TotalPages => (int)Math.Ceiling(TotalCount / (double)PageSize);
    public bool HasPreviousPage => Page > 0;
    public bool HasNextPage => Page < TotalPages - 1;
}
```

---

## 🎯 使用場景指南

### 何時使用 Projection (Query Service)

- ✅ 複雜查詢需求（JOIN、聚合、統計）
- ✅ 跨聚合查詢
- ✅ 報表和分析查詢
- ✅ UI 特定的查詢需求
- ✅ 分頁和排序
- ❌ Write Model 的 CRUD 操作（使用 Repository）

### 與 Repository 的區別

```csharp
// Repository：Write Model 的 Aggregate 持久化
IRepository<Record, RecordId> repository;
await repository.FindByIdAsync(id);  // 返回 Record 領域物件
await repository.SaveAsync(record); // 儲存領域物件

// Query Service (Projection)：Read Model 的查詢和資料投影
IRecordQueryService queryService;
await queryService.GetByIdAsync(id);       // 返回 RecordDto
await queryService.GetPagedAsync(...);     // 返回分頁結果
```

---

## 🎯 DTO 設計

### 使用 Record 定義 DTO

```csharp
// ✅ 正確：使用 record 定義 DTO
public sealed record RecordDto
{
    public required string Id { get; init; }
    public required string Name { get; init; }
    public required string State { get; init; }
    public DateTime CreatedAt { get; init; }
    public List<string> Tags { get; init; } = new();
    public int? TaskCount { get; init; }
}

// DTO with nested objects
public sealed record RecordDetailDto
{
    public required string Id { get; init; }
    public required string Name { get; init; }
    public DefinitionOfDoneDto? DefinitionOfDone { get; init; }
    public List<TaskDto> Tasks { get; init; } = new();
}
```

---

## 🔍 檢查清單

### Query Service Interface
- [ ] 定義在 `Application` 層
- [ ] 使用 `I[Aggregate]QueryService` 命名
- [ ] 方法返回 DTO，不是領域物件或 Data 物件
- [ ] 支援 `CancellationToken`
- [ ] 有分頁方法

### Query Service 實作
- [ ] 實作在 `Infrastructure.Persistence.QueryServices`
- [ ] 使用 `AsNoTracking()` 提升效能
- [ ] 處理 null 值和空集合
- [ ] 使用 Mapper 轉換為 DTO
- [ ] 透過 DI 註冊

### DTO
- [ ] 使用 `record` 定義
- [ ] 使用 `required` 標記必要欄位
- [ ] 使用 `init` setter
- [ ] 集合有預設值

---

## 📂 程式碼範例

更多完整範例請參考：

| 範例 | 路徑 |
|------|------|
| Projection 範例 | [../examples/projection/](../examples/projection/) |
| Projection 指南 | [../examples/projection-example.md](../examples/projection-example.md) |
| DTO 範例 | [../examples/dto/](../examples/dto/) |

---

## 相關文件

- [repository-standards.md](repository-standards.md)
- [usecase-standards.md](usecase-standards.md)
- [mapper-standards.md](mapper-standards.md)
