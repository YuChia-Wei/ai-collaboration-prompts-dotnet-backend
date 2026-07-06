# Use Case 編碼規範 (.NET)

本文件定義同步 Command/Query Use Case、Input/Output、Handler、transaction 與
event lifecycle 的編碼標準。角色關係以
[USECASE-COMMAND-HANDLER-RELATIONSHIP.MD](../USECASE-COMMAND-HANDLER-RELATIONSHIP.MD)
為準。

## 核心模型

```text
Controller / Handler (inbound adapter)
  -> I<Operation>UseCase (inbound port)
  -> <Operation>UseCase (orchestration)
  -> Domain / outbound ports
```

- Use Case 與 Handler 是不同物件。
- 同步 API 預設由 Controller 直接注入 Use Case interface。
- Handler 只在真實 dispatch/message entry 存在。
- Wolverine 是 conditional adapter technology，不是 portable Use Case
  dependency。

## MUST 規則

### 1. Interface、implementation 與 operation 命名

```csharp
public interface ICreateProductUseCase
{
    Task<CreateProductOutput> ExecuteAsync(
        CreateProductInput input,
        CancellationToken cancellationToken);
}

public sealed class CreateProductUseCase : ICreateProductUseCase
{
    public Task<CreateProductOutput> ExecuteAsync(
        CreateProductInput input,
        CancellationToken cancellationToken)
    {
        // Orchestrate Domain behavior and outbound ports.
    }
}
```

- interface 使用 `I<Operation>UseCase`。
- implementation 使用 `<Operation>UseCase`。
- operation 固定使用 `ExecuteAsync`。
- 非同步 operation 必須宣告不可省略的 `CancellationToken`。
- Use Case 不同時暴露 `Handle` entry point。

### 2. Input 必須與 delivery contract 分離

預設為 Use Case 建立專屬、transport-neutral 的 `*Input`：

```csharp
public sealed record CreateProductInput(
    string ProductId,
    string Name,
    string UserId);
```

允許兩項例外：

- 沒有 cancellation 以外的輸入時，不建立 input。
- 只有一個 scalar built-in/BCL 值時，可直接接受該值。

Scalar 例外限 `string`、數值型別、`bool`、`Guid` 與 date/time 類型。
collection、tuple、自訂 record/class 或多值必須使用專屬 input。

Use Case 不接受：

- ASP.NET Request DTO
- Wolverine/MediatR Command 或 Query
- broker contract
- package marker interface

### 3. Output 必須與 transport 分離

```csharp
public sealed record CreateProductOutput(ProductId ProductId);
```

Use Case 只回傳完成操作後產生的 transport-neutral object。沒有 object 時回傳
`Task`。不得回傳 `IActionResult`、broker acknowledgement、retry/dead-letter
instruction 或 framework envelope。

### 4. Command 與 Query 責任分離

- Command Use Case 修改 state 並透過 Aggregate behavior 維護 invariant。
- Query Use Case 只讀取 read model，不修改 Domain state。
- Command/message contract 只有在 dispatch entry 存在時才建立。
- Command/message Handler 將 delivery contract map 成 Use Case input。
- Query 預設仍使用 query Use Case；只有明確核准的純查詢 endpoint 可直連
  `IQueryRepository`-derived port 或 query service。

### 5. Dependency injection

Use Case 使用 constructor injection，且只依賴 Domain types 與 Application
outbound ports：

```csharp
public sealed class CreateProductUseCase : ICreateProductUseCase
{
    private readonly IAggregateRepository<Product, ProductId> repository;
    private readonly IApplicationEventPublisher eventPublisher;

    public CreateProductUseCase(
        IAggregateRepository<Product, ProductId> repository,
        IApplicationEventPublisher eventPublisher)
    {
        this.repository = repository;
        this.eventPublisher = eventPublisher;
    }
}
```

禁止：

- `IServiceProvider` / Service Locator
- DI registration attribute
- framework package dependency in portable Use Case
- direct Wolverine `IMessageBus`
- another Use Case dependency

在 composition root 使用 `IServiceCollection` 顯式註冊：

```csharp
services.AddScoped<ICreateProductUseCase, CreateProductUseCase>();
```

不得把 `ICreateProductUseCase` 註冊到 `CreateProductHandler`。

### 6. Handler 必須是薄 inbound adapter

只有真實 dispatch/message entry 才建立 Handler：

```csharp
public sealed class CreateProductCommandHandler
{
    private readonly ICreateProductUseCase useCase;

    public CreateProductCommandHandler(ICreateProductUseCase useCase)
    {
        this.useCase = useCase;
    }

    public Task<CreateProductOutput> HandleAsync(
        CreateProductCommand command,
        CancellationToken cancellationToken)
    {
        var input = new CreateProductInput(
            command.ProductId,
            command.Name,
            command.UserId);

        return this.useCase.ExecuteAsync(input, cancellationToken);
    }
}
```

Handler 不得：

- 載入或儲存 Aggregate
- 依賴 Repository / Domain Service
- commit transaction
- 發布 business event 或 Command
- 注入或編排多個 Use Case

Package-neutral convention Handler 可位於 Application；framework/transport
specific Handler 位於 inbound adapter 或 composition boundary。

### 7. Strong consistency 必須顯式宣告

Eventual consistency 是跨 Aggregate coordination 的預設。只有 Use Case
具有明確 all-or-nothing business requirement 時才注入 `IUnitOfWork`：

```csharp
public sealed class CompleteReservationUseCase
{
    private readonly IUnitOfWork unitOfWork;

    public async Task ExecuteAsync(CancellationToken cancellationToken)
    {
        // Load Aggregates, invoke Domain behavior, and save through ports.
        await this.unitOfWork.CommitAsync(cancellationToken);
    }
}
```

- 不得因減少 I/O round trips 宣告 strong consistency。
- Repository 參與 Unit of Work 時不得自行 commit。
- Handler 不得新增 transaction 或在 Use Case 後 commit。
- commit 成功後才能 acknowledge/clear pending Domain Events。

### 8. Event publication 使用 outbound port

Domain object 產生 Domain Event；Use Case 協調 persistence、outbox 與
publication lifecycle。

```csharp
public interface IApplicationEventPublisher
{
    Task PublishAsync(
        object applicationEvent,
        CancellationToken cancellationToken);
}
```

實際 port 應使用 target domain language，而不是建立萬用 bus abstraction。
Infrastructure 可用 Wolverine/outbox 實作 port。Use Case 不直接注入
`IMessageBus`，也不得透過 publisher 發布 Command。

## 測試規則

- Use Case unit test 直接建立 concrete `*UseCase`。
- Mock Aggregate Repository、Query Repository、gateway、clock、publisher 等
  outbound ports。
- 驗證 `ExecuteAsync` output、Domain behavior、persistence 與 event lifecycle。
- Handler test 只驗證 mapping、一次 Use Case invocation 與 delivery failure
  mapping。
- 不以 Handler test 取代 Use Case business-flow test。

## 檢查清單

### Use Case

- [ ] interface 與 concrete class 使用 `*UseCase` 命名。
- [ ] operation 是 `ExecuteAsync`。
- [ ] `CancellationToken` 不可省略。
- [ ] Input/Output 與 HTTP、MQ、Wolverine/MediatR 分離。
- [ ] 只依賴 Domain types 與 outbound ports。
- [ ] 不依賴 `IServiceProvider`、`IMessageBus` 或其他 Use Case。
- [ ] transaction 與 event lifecycle 位於 Use Case。

### Handler

- [ ] 只因真實 dispatch/message entry 而存在。
- [ ] 將 delivery input map 成 Use Case input。
- [ ] 只呼叫一個 Use Case。
- [ ] 不直接操作 Repository、Aggregate、transaction 或 event publication。
- [ ] framework/transport coupling 位於 adapter/composition boundary。

## 相關文件

- [Controller Standards](controller-standards.md)
- [Repository Standards](repository-standards.md)
- [Test Standards](test-standards.md)
- [Project Structure](../project-structure.md)
