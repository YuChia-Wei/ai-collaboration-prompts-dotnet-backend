# Use Case、Command、Query 與 Handler 關係

本文件定義本 repo 在 DDD、Clean Architecture、CQRS 與 Hexagonal
Architecture 下，`Use Case`、`Input`、`Command`、`Query`、`Handler`、
`Controller` 與相關 port 的標準責任邊界。

## 核心結論

- `Use Case interface` 是 Application 的 inbound port。
- `*UseCase` concrete class 是應用流程編排的實作。
- `Controller` 是 HTTP inbound adapter，預設只呼叫 Use Case interface。
- `Command` / message contract 是 dispatch 或 transport input，不是 Use Case
  input。
- `Handler` 只在真的存在 dispatch、message、consumer 或 scheduled entry
  時存在；它負責轉換 input 並呼叫一個 Use Case。
- Use Case 與 Handler 是不同物件，Handler 不得成為預設的 Use Case
  implementation。
- Use Case 依賴 outbound ports；Wolverine、MediatR、HTTP、MQ 與 persistence
  package 不得洩漏到可攜式 Use Case contract。
- 此 workflow 不定義或擴充 `Application Service`；若既有產品使用該名詞，
  必須由另一個明確決策定義其用途。

## 標準呼叫鏈

### 同步 Command 型 API

```text
HTTP Request
  -> Controller
  -> I<CreateOperation>UseCase
  -> <CreateOperation>UseCase
  -> Aggregate / Domain Service / outbound ports
  -> Use Case Output
  -> HTTP Response
```

Controller 不透過 `IMessageBus`、mediator 或 Command Handler 執行一般同步
API Use Case。

### 同步 Query 型 API

預設流程：

```text
HTTP Request
  -> Controller
  -> I<GetOperation>UseCase
  -> <GetOperation>UseCase
  -> I<Feature>QueryRepository / Query Service
  -> Use Case Output
  -> HTTP Response
```

只有經明確指定的純查詢 endpoint，才可以直接注入唯讀
`IQueryRepository`-derived port 或 query service。這是允許但不建議的例外；
未明確指定時仍必須使用 query Use Case。直接 query-handler dispatch 不屬於
此例外。

### Dispatch 或 Message Entry

```text
Command / Message / Scheduled Trigger
  -> Handler (inbound adapter)
  -> I<CreateOperation>UseCase
  -> <CreateOperation>UseCase
```

Handler 只負責 delivery contract validation、input mapping、呼叫一個 Use
Case，以及將失敗映射為該 delivery mechanism 的 retry/dead-letter 語意。
它不得載入 Aggregate、操作 Repository、commit transaction 或自行發布業務
事件。

### Cross-BC Flow

```text
BC A Use Case
  -> outbound event publisher port
  -> Infrastructure messaging/outbox adapter
  -> MQ
  -> BC B Consumer / Handler
  -> BC B Use Case
```

跨 BC communication 只能使用 MQ。Use Case 不直接依賴 Wolverine
`IMessageBus`，由 Infrastructure 將專案擁有的 event publisher port 轉接到
選定的 broker/framework。

## Use Case Contract

### 命名

- interface：`ICreateProductUseCase`
- implementation：`CreateProductUseCase`
- operation：`ExecuteAsync`
- input：`CreateProductInput`
- output：`CreateProductOutput`

### Signature

每個非同步 Use Case 都必須宣告不可省略的 `CancellationToken`。

```csharp
public interface ICreateProductUseCase
{
    Task<CreateProductOutput> ExecuteAsync(
        CreateProductInput input,
        CancellationToken cancellationToken);
}
```

專屬且 transport-neutral 的 `*Input` 是預設。允許兩項例外：

1. 沒有 cancellation 以外的輸入時，可省略 input。
2. 只有一個 scalar built-in/BCL 值時，可直接接受該值。

標準 scalar 包含 `string`、數值型別、`bool`、`Guid` 與 date/time
型別。collection、tuple、自訂 record/class 或多個值都必須建立專屬 input。

```csharp
Task ExecuteAsync(CancellationToken cancellationToken);

Task<FindProductOutput> ExecuteAsync(
    Guid productId,
    CancellationToken cancellationToken);
```

HTTP Request、broker message、Wolverine Command 或其他 delivery contract
不得直接作為 Use Case input。

### Output

Use Case 只回傳完成操作後產生且 transport-neutral 的 output。沒有 output
物件時回傳 `Task`，不得為了格式一致建立空 output。Use Case 不回傳：

- `IActionResult` / `IResult`
- broker acknowledgement
- Wolverine/MediatR envelope
- retry/dead-letter instruction

## 責任與依賴

### Use Case 負責

- application-level validation 與 authorization orchestration
- 載入 Aggregate 或 read-side data
- 呼叫 Aggregate behavior / Domain Service
- 使用 Aggregate Repository、Query Repository、gateway 等 outbound ports
- 明確 strong consistency 情境下的 `IUnitOfWork`
- outbox 與 pending Domain Event acknowledgement coordination
- 透過專案擁有的 event publisher port 發布 application/integration events
- 組裝 transport-neutral output

Domain Event 應由 Domain object 產生；Use Case 負責協調 persistence、outbox
與 dispatch lifecycle。

### Controller 負責

- HTTP model binding 與 transport validation
- HTTP Request 到 Use Case input 的 mapping
- 呼叫 Use Case interface
- Use Case outcome 到 HTTP response 的 mapping

Controller 不得注入 concrete Handler、`IMessageBus`、mediator/dispatcher、
write repository、Aggregate 或 Domain Service。純查詢例外只允許明確核准的
唯讀 Query Repository / Query Service。

### Handler 負責

- 接收實際 dispatch/message input
- delivery-level validation 與 mapping
- 呼叫一個 Use Case interface
- delivery-specific failure mapping

Handler 不得：

- 成為 Use Case implementation
- 直接操作 Repository、Aggregate 或 Domain Service
- 自行建立 transaction 或在 Use Case 後 commit
- 使用 bus 發布另一個 Command
- 注入或串接多個 Use Case

需要多步驟完成同一個 business goal 時，建立一個較高階 Use Case；不要由
Controller 或 Handler 編排多個 Use Case。

## Handler 放置位置

- package-neutral convention Handler 可以放在 Application。
- Wolverine/MediatR-specific Handler 放在 inbound adapter 或 composition
  boundary。
- MQ Consumer / Integration Event Handler 放在 Consumer/Presentation adapter。
- Domain Event Handler / Reactor 依事件與一致性規則放在 Application 的明確
  reaction boundary，但不得與同步 API Use Case 混為同一角色。

Handler 的位置由 delivery/framework coupling 決定，不由 `Handler` suffix
單獨決定。

## DI 規則

同步 API：

```csharp
services.AddScoped<ICreateProductUseCase, CreateProductUseCase>();
```

只有真實 dispatch entry 才註冊 Handler。不得使用
`ICreateProductUseCase -> CreateProductHandler` 將兩個角色重新合併。

Use Case、Handler 與 adapter 均使用 constructor injection，並在 composition
root 透過 `IServiceCollection` 顯式註冊；不得使用 Service Locator、DI
attribute 或 assembly-scanning magic。

## Transaction 與 Event 規則

- Eventual consistency 是跨 Aggregate / 跨 BC 的預設。
- 只有明確 all-or-nothing business requirement 才由 Use Case 注入
  `IUnitOfWork`。
- Handler 不得引入隱藏的 strong consistency。
- Repository 參與 Unit of Work 時不得自行 commit。
- commit 成功前不得 acknowledge/clear pending Domain Events。
- Use Case 使用 project-owned event publisher port；Infrastructure 可用
  Wolverine outbox 實作該 port。
- Use Case 不得透過任何 bus 或 publisher 發布 Command。

## 測試與 Analyzer 邊界

- Use Case unit test 直接測試 concrete `*UseCase`，mock outbound ports。
- Handler test 只驗證 mapping、單一 Use Case invocation 與 delivery failure
  mapping。
- Controller test mock Use Case interface，不 mock Handler 或 Repository。
- deterministic boundary violation 應由 analyzer 回報 error。
- naming-only 或無可靠 target evidence 的 migration advisory 維持 warning。
- 明確純查詢例外必須有 target-repository 可判定的 evidence，否則 analyzer
  仍以預設 Use Case boundary 判定。

## Migration Boundary

本標準不發布通用 migration recipe。既有
`ICreateProductUseCase -> CreateProductHandler`、Controller-to-Handler 或
combined `Execute`/`Handle` 實作，必須在實際產品重構時先盤點 callers、DI
registration、真實 dispatch entry、transaction 與 event ownership，再安排
遷移。

## 與 Spec 的關係

在 `.dev/specs/` 中，Use Case 是 production behavior 的主名稱。Command、
Query、HTTP Request 與 message contract 是 delivery/input model；Handler 是
adapter implementation detail，不應成為 spec 的主要 business behavior 名稱。
