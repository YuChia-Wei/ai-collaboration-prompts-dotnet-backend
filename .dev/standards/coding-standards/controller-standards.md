# Controller 編碼規範 (.NET)

本文件定義 ASP.NET Core Controller 層的編碼標準，包含 Controller 結構、Request/Response DTO、錯誤處理等規範。

---

## 📌 概述

Controller 僅負責傳輸層與輸入驗證，不應包含業務邏輯。

- **委派執行**：Controller 預設只委派給明確的 Use Case interface
- **請求驗證**：使用 ASP.NET Core Model Validation
- **錯誤回應**：使用統一格式（ProblemDetails）

---

## 🏷️ Pattern 標記（自動化檢查用）

以下標記供自動化 Code Review 腳本使用：

```yaml
# Controller 規則
Pattern (required): \[ApiController\]
Pattern (required): async Task<IActionResult>|async Task<IResult>

# 禁止規則
Pattern (forbidden, ignore-comment): DbContext
Pattern (forbidden): SaveChanges
Pattern (forbidden): new .*Handler
Pattern (forbidden): new .*UseCase
Pattern (forbidden, i, ignore-comment): IMessageBus|IMediator|IDispatcher
```

---

## 🔴 必須遵守的規則 (MUST FOLLOW)

### 1. REST API 路徑設計原則

**用巢狀的建立端點、用扁平的資源位址**

當處理 Aggregate Root 之間的關聯時，必須遵循以下設計原則：

#### 核心規則
1. **建立（Create）**：使用巢狀路徑表達歸屬關係
   - 範例：`POST /api/v1/resources/{resourceId}/work-items`
   - 語意：在特定 Resource 的 Work Item 集合中新增項目

2. **資源位址（Canonical URL）**：使用扁平路徑尊重獨立性
   - 範例：`GET/PATCH/DELETE /api/v1/work-items/{workItemId}`
   - 語意：Work Item 作為 Aggregate Root 有獨立的資源位址

#### 完整路由範例

```csharp
// WorkItems 路由
[HttpPost("/api/v1/resources/{resourceId}/work-items")]    // 建立 Work Item（檢查 Resource 存在）
[HttpGet("/api/v1/work-items/{workItemId}")]                  // 查詢單筆 Work Item
[HttpPatch("/api/v1/work-items/{workItemId}")]                // 更新 Work Item
[HttpDelete("/api/v1/work-items/{workItemId}")]               // 刪除 Work Item
[HttpGet("/api/v1/resources/{resourceId}/work-items")]     // 列出某 Resource 的所有 Work Item

// Task 路由
[HttpPost("/api/v1/work-items/{workItemId}/tasks")]           // 建立 Task（檢查 Work Item 存在）
[HttpGet("/api/v1/tasks/{taskId}")]                // 查詢單筆 Task
[HttpPatch("/api/v1/tasks/{taskId}")]              // 更新 Task
[HttpDelete("/api/v1/tasks/{taskId}")]             // 刪除 Task
```

---

### 2. 委派 Use Case 執行應用流程

```csharp
// ✅ Allowed: map HTTP DTO to Use Case input and invoke the inbound port
[HttpPost("/resources")]
public async Task<IActionResult> Create(
    CreateResourceRequest request,
    CancellationToken cancellationToken)
{
    var input = new CreateResourceInput(request.Name, request.UserId);
    var output = await this.createResourceUseCase.ExecuteAsync(
        input,
        cancellationToken);

    return Ok(output);
}

// ❌ Forbidden: controller contains business logic
[HttpPost("/resources")]
public IActionResult Create(CreateResourceRequest request)
{
    var entity = new Resource(request.Name);
    _dbContext.Add(entity);
    _dbContext.SaveChanges();
    return Ok();
}
```

Controller 不得注入 concrete Handler、`IMessageBus`、mediator/dispatcher、write
Repository、Aggregate 或 Domain Service。

只有經明確指定的純查詢 endpoint，才可直接注入唯讀
`IQueryRepository`-derived port 或 query service。這是允許但不建議的例外；
未明確指定時仍必須建立並呼叫 query Use Case。直接 query-handler dispatch
不屬於例外。

---

### 3. Request/Response DTO 設計

使用 `record` 定義 Request/Response DTO：

```csharp
// ✅ 正確：使用 record 定義 Request
public sealed record CreateResourceRequest(
    [Required] string Name,
    [Required] string UserId,
    string? Description = null);

public sealed record UpdateResourceRequest(
    [Required] string Name,
    string? Description = null);

// ✅ 正確：使用 record 定義 Response
public sealed record ResourceResponse(
    string Id,
    string Name,
    string State,
    DateTime CreatedAt);

// ❌ 錯誤：使用 class 定義 DTO
public class CreateResourceRequest  // 應該使用 record
{
    public string Name { get; set; }
    public string UserId { get; set; }
}
```

---

### 4. 依賴注入必須透過 Constructor

禁止使用 `[FromServices]` 或其他注入方式：

```csharp
// ✅ 正確：Constructor Injection
[ApiController]
[Route("api/v1/resources")]
public class ResourcesController : ControllerBase
{
    private readonly ICreateResourceUseCase createResourceUseCase;
    
    public ResourcesController(ICreateResourceUseCase createResourceUseCase)
    {
        this.createResourceUseCase = createResourceUseCase;
    }
}

// ❌ 錯誤：[FromServices] 注入
[HttpPost]
public async Task<IActionResult> CreateResource(
    [FromBody] CreateResourceRequest request,
    [FromServices] ICreateResourceUseCase useCase)  // FORBIDDEN!
{
    // ...
}
```

---

## 🎯 HTTP 狀態碼映射

### 成功狀態碼

```csharp
// GET - 200 OK
return Ok(resourceDto);

// POST - 201 Created
return CreatedAtAction(nameof(GetResource), new { id = resourceId }, response);

// PUT - 200 OK
return Ok(updatedResource);

// DELETE - 204 No Content
return NoContent();

// Async operation - 202 Accepted
return Accepted(operationId);
```

### 錯誤狀態碼

```csharp
// 400 Bad Request - 驗證錯誤
if (!result.IsSuccess)
    return BadRequest(new ProblemDetails 
    { 
        Detail = result.Error,
        Status = 400 
    });

// 404 Not Found - 資源不存在
if (resource is null)
    return NotFound();

// 409 Conflict - 資源衝突
if (result.Error?.Contains("already exists") == true)
    return Conflict(new ProblemDetails { Detail = result.Error });
```

---

## 🎯 錯誤處理

### 使用 ProblemDetails

```csharp
// ✅ 正確：使用標準 ProblemDetails
return BadRequest(new ProblemDetails
{
    Title = "Validation Failed",
    Detail = "Resource name is required",
    Status = StatusCodes.Status400BadRequest,
    Instance = HttpContext.Request.Path,
    Extensions = 
    {
        ["traceId"] = Activity.Current?.Id ?? HttpContext.TraceIdentifier
    }
});

// 或使用 ValidationProblemDetails
return ValidationProblem(ModelState);
```

---

## 🎯 請求驗證

### 使用 FluentValidation（推薦）

```csharp
public class CreateResourceRequestValidator : AbstractValidator<CreateResourceRequest>
{
    public CreateResourceRequestValidator()
    {
        RuleFor(x => x.Name)
            .NotEmpty().WithMessage("Resource name is required")
            .MaximumLength(100).WithMessage("Resource name must not exceed 100 characters");
            
        RuleFor(x => x.UserId)
            .NotEmpty().WithMessage("User ID is required");
            
        RuleFor(x => x.Price)
            .GreaterThan(0).When(x => x.Price.HasValue)
            .WithMessage("Price must be positive");
    }
}
```

---

## 🔍 檢查清單

### Controller 結構
- [ ] 繼承 `ControllerBase` (不是 `Controller`)
- [ ] 有 `[ApiController]` 屬性
- [ ] 有 `[Route]` 定義基礎路徑
- [ ] 使用 Constructor Injection
- [ ] 預設只注入 Use Case interface
- [ ] 不注入 concrete Handler、bus、mediator/dispatcher、write Repository 或 Domain Service
- [ ] 純查詢直連 Query Repository/Service 時有明確的 endpoint 選擇依據
- [ ] 路徑包含版本號（如 `/api/v1`）

### HTTP 規範
- [ ] 使用正確的 HTTP 方法
- [ ] 返回適當的狀態碼
- [ ] RESTful URL 設計
- [ ] 使用複數資源名稱

### Request/Response
- [ ] 使用 `record` 定義 DTO
- [ ] 有適當的驗證屬性
- [ ] 使用 `ProblemDetails` 回傳錯誤

### 文檔
- [ ] 有 `[ProducesResponseType]` 屬性
- [ ] 有 Swagger 說明（如需要）

---

## 📂 程式碼範例

更多完整範例請參考：

| 範例 | 路徑 |
|------|------|
| Controller 範例 | [../examples/controller/](../examples/controller/) |
| ASP.NET Core 範例 | [../examples/aspnet-core/](../examples/aspnet-core/) |
| DTO 範例 | [../examples/dto/](../examples/dto/) |

---

## 相關文件

- [usecase-standards.md](usecase-standards.md)
- [test-standards.md](test-standards.md)
