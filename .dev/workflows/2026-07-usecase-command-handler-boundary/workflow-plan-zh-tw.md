# Use Case 與 Command Handler 邊界 Workflow

## Metadata

- Plan ID: `workflow-plan-2026-07-usecase-command-handler-boundary`
- Workflow ID: `2026-07-usecase-command-handler-boundary`
- Owner skill: `dev-workflow`
- Status: `in-progress`
- Created: `2026-07-06`
- Branch: `codex/usecase-command-handler-alignment`
- Base: `main` at merge commit `343ab29`
- Issue: not provided
- Translation note: this is a human-readable reference copy in Traditional Chinese Taiwan usage. The canonical planning file remains [workflow-plan.md](./workflow-plan.md).

## 問題說明

目前的有效標準同時定義了兩種彼此不相容的同步應用程式入口模型：

1. `Controller -> Command/Query -> Handler`，其中 Handler 通常就是 Use Case 的實作。
2. `Controller -> IUseCase -> Use Case implementation`，其中 Handler 是獨立的傳遞／派送物件。

使用者在 repository-pattern workflow 已經確認的目標是第二種模型：

- Use Case 與 Handler 是分開的物件。
- API Controller 注入的是 Use Case 介面。
- 一般同步 API 行為不會透過 bus 發佈 Command。
- message/event Handler 的責任要和 Use Case 的流程編排維持分離。

目前的規範、範例、提示詞、專案結構、測試與 analyzer，並沒有一致地落實這個目標。

證據基準記錄在 [review-report.md](./review-report.md)。

## 範圍

### 納入範圍

- 定義 `Use Case`、`Input`、`Command`、`Query`、`Handler`、`Application Service`、`Controller`、`Consumer` 與 `Reactor` 的責任邊界。
- 定義同步 API 的預設呼叫鏈。
- 定義 command/query/message handler 何時存在，以及它們可以委派什麼。
- 定義 query 流程是否也要使用相同的明確 Use Case 邊界。
- 對齊 DI、命名、專案結構、提示詞、範例、測試與 analyzer。
- 讓 Wolverine 與其他 dispatch 套件維持條件式使用，依目標專案證據決定。

### 不納入範圍

- 不實作 production application。
- 不重設 message broker 或 transport。
- 不改 repository-pattern 設計。
- 不做大範圍標準翻譯。
- 不做目標專案專屬的 Wolverine API 設定。
- 除非之後明確要求，不進行 sub-agent 作業。

## 統御限制

- DDD + Clean Architecture + CQRS 仍然是基礎架構。
- Use Case 是應用層的流程編排邊界。
- Presentation adapter 不直接依賴 repository 或 Domain objects。
- 跨 bounded context 的溝通仍然只走 MQ。
- in-process 的同步 API 行為不需要發佈 message。
- Aggregate 之間預設維持最終一致性。
- 例外的強一致性需求，應該由 Use Case 明確依賴 `IUnitOfWork` 來表達，不要藏在 Handler 裡。
- Wolverine 這類 runtime 套件屬於依目標專案決定的條件式選項。

## 初步目標方向

以下方向是提案，仍待下面的決策確認：

```text
HTTP Request
  -> Controller
  -> I<CreateOperation>UseCase
  -> <CreateOperation>UseCase
  -> Aggregate / Domain Service / outbound ports
  -> Use Case Output
  -> HTTP Response
```

當真的需要 dispatch 或 message 入口時：

```text
Command / Message / Scheduled Trigger
  -> Handler (inbound adapter)
  -> I<CreateOperation>UseCase
  -> Use Case implementation
```

建議的責任切分如下：

- `Use Case interface`：穩定的 inbound Application port。
- `Use Case implementation`：應用流程編排、交易需求、Aggregate/query 協作，以及輸出合約。
- `Input` / `Output`：與 transport 無關的 Use Case 合約。
- `Command`：只有在刻意選用 command dispatch 時才使用的意圖訊息。
- `Handler`：特定傳遞機制的 adapter，負責 mapping 其輸入並呼叫 Use Case，不應變成預設的 Use Case 實作。
- `Controller`：HTTP adapter，負責把 HTTP DTO 對應成 Use Case input，且只注入 Use Case 介面。
- `Consumer` / event Handler / Reactor：message adapter 或最終一致性的 worker，需和同步 API Use Case 分開。

## 開放決策

### D1 — Use Case 介面形狀

決定標準的 operation signature 與 cancellation policy。

建議預設：

```csharp
public interface ICreateProductUseCase
{
    Task<CreateProductOutput> ExecuteAsync(
        CreateProductInput input,
        CancellationToken cancellationToken = default);
}
```

問題：

- `ExecuteAsync` 是否是強制的方法名稱？
- 每個 Use Case 是否都要接受專屬 input 物件，包括沒有參數的操作？
- 非同步 Use Case 是否一定要有 `CancellationToken`？

### D2 — Input 與 Command

決定 Use Case 是接受與 transport 無關的 `Input`，還是直接接受 `ICommand<T>` 物件。

建議方向：

- Controller 將 HTTP request 對應成 `CreateProductInput`。
- `CreateProductInput` 不實作任何 dispatcher/package marker。
- 當需要 dispatch 入口時，message/command Handler 只負責把 `CreateProductCommand` 對應到相同的 input。

這樣可以避免 Application port 被特定 dispatcher 綁死。

### D3 — Command Handler 的存在與角色

決定 Command Handler 是否：

1. 只在實際配置 command/message dispatch 入口時才存在；或
2. 對每個 command Use Case 都是必備，即使 Controller 根本不使用它。

建議方向是選項 1。若每個 Use Case 都強制放一個只有一行的 Handler，會多出一層沒被使用的包裝，等於只是換名字再製造一次模糊地帶。

### D4 — Controller 相依規則

確認 Controller 是否要嚴格禁止注入：

- concrete Handler。
- `IMessageBus`。
- mediator/dispatcher 抽象。
- repositories 或 Domain services。

建議預設是 Controller 只能注入一個或多個明確的 Use Case 介面。若是 framework 專屬的 endpoint model，則需要另外核准的 profile。

### D5 — Query 端對稱性

決定同步 query 是否也要比照：

```text
Controller -> I<GetProduct>UseCase -> GetProductUseCase -> IProductQueryRepository
```

或者仍然允許 Controller 直接派送到 query-handler。

commands 與 queries 都採用同一套 inbound-port 規則會比較一致，但不能因此強迫多出不必要的 QueryService 層。

### D6 — Handler 放置位置

依照 handler 類型決定放置位置：

- 與套件無關的 in-process command Handler。
- Wolverine/MediatR 專屬 Handler。
- MQ Consumer Handler。
- Domain Event Handler / Reactor。

建議規則：與套件無關的 Use Case 留在 Application；和 transport 或 framework 綁定的 handler 放在 inbound adapter／composition boundary。只有在完全沒有 package 或 transport 相依時，convention-only 的 Handler 才可以留在 Application。

### D7 — 結果與錯誤的擁有權

決定 Use Case Output 是否擁有型別化的 success/failure 語意，以及 Handler 能不能翻譯它們。

建議方向：

- Use Case 回傳與 transport 無關的 typed Output/Result。
- Controller 負責把它轉成 HTTP。
- message Handler 將失敗映射成 retry/dead-letter 行為。
- Use Case 不回傳 `IActionResult`、broker acknowledgement 或 framework 專屬 envelope。

### D8 — 交易與事件生命週期的擁有權

確認 repository、`IUnitOfWork`、outbox 協調，以及待處理 Domain Event acknowledgement 的相依性，都屬於 Use Case implementation。

建議方向是：Handler 不應偷偷引入強一致性，也不應該在呼叫 Use Case 之後自己獨立 commit。

### D9 — 具體實作命名

決定一個預設命名：

- `CreateProductUseCase`;
- `CreateProductService`;
- 其他明確後綴。

建議方向是採用 `CreateProductUseCase`，這樣 concrete role 會更清楚，也能避免 `Application Service` 這種模糊但可有可無的說法。

### D10 — 相容性與遷移

決定既有專案如果註冊成 `ICreateProductUseCase -> CreateProductHandler`，要怎麼遷移。

建議的分階段規則：

- 先把這種結構標成 legacy/deprecated，不要默默視為正確。
- 先導入 concrete Use Case，把流程編排搬過去。
- 只有在真的有 dispatch 入口會消費它時，才保留 Handler。
- 呼叫端遷移完成後，移除沒在用的 Handler 註冊。

### D11 — Analyzer 強制規則

決定 analyzer 對下列項目的強制程度與涵蓋範圍：

- Controller 對 Handler、dispatcher 或 message bus 的相依。
- Use Case interface 與 implementation 的結構。
- Handler 到 Use Case 的相依方向。
- Use Case 中的 transport/package 相依。
- 同時實作 Use Case 與 Handler 入口的 legacy class。

建議預設是：可確定的邊界違規一律當成 error；只有名稱或遷移提醒則先維持 warning，直到有目標專案的 marker 可以判斷。

### D12 — Wolverine 與 dispatcher 政策

確認 Wolverine 的定位是：

- messaging、outbox、consumer，以及刻意選擇的 dispatch 的條件式指引。
- 不是一般同步 API Use Case 的可攜式強制需求。
- 不會因為 command/query 實作提示詞就自動被引入。

## Skill Routing

| Stage | Capability | Skill | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| S0 | workflow orchestration | `dev-workflow` | High | 必要的 workflow gate 與既有的 deferred task |
| S0-S2 | architecture | `ddd-ca-hex-architect` | High | Use Case/Handler/Controller/adapter 邊界設計 |
| S3 | context governance | `ai-context-governance` | High | 提示詞、可重用 AI 資產、指南與範例 |
| S4 | implementation | `slice-implementer` | High | 有界的 analyzer 與驗證修改 |
| S5 | workflow validation | `dev-workflow` | High | 跨檔一致性與收尾 |

## 階段

### S0 — Workflow bootstrap 與 pre-analysis

- 狀態：completed
- 產出：
  - `workflow-plan.md`;
  - `review-report.md`;
  - `tasks/bootstrap-usecase-command-handler-workflow.json`。
- 驗證：
  - branch 是從已合併的 `main` 開出；
  - workflow 產物可解析，且連結可解析；
  - findings 有引用目前 repository 的有效證據。

### S1 — 釐清 architecture decisions

- 狀態：pending
- Owner：`ddd-ca-hex-architect`
- 產出：
  - 已核准的 D1-D12 決策；
  - `tasks/resolve-usecase-command-handler-decisions.json`。
- Gate：
  - 在使用者決策記錄完成前，不重寫 canonical standards。

### S2 — 對齊 canonical standards

- 狀態：pending
- Owner：`ddd-ca-hex-architect`
- 主要範圍：
  - `.dev/ARCHITECTURE.md`;
  - `.dev/standards/USECASE-COMMAND-HANDLER-RELATIONSHIP.MD`;
  - usecase/controller/test/project-structure standards;
  - DI and technology-profile rules.

### S3 — 同步 context、提示詞、指南與範例

- 狀態：pending
- Owner：`ai-context-governance`
- 主要範圍：
  - command/query/controller sub-agent prompts;
  - slice-implementer modes;
  - .NET backend templates and checklists;
  - controller/usecase/testing/DI examples and guides.

### S4 — 對齊 analyzers 與可執行驗證

- 狀態：pending
- Owner：`slice-implementer`
- 主要範圍：
  - Controller and Use Case analyzer rules;
  - positive, negative, migration, and false-positive tests;
  - analyzer documentation and severity template.

### S5 — 最終驗證與收尾

- 狀態：pending
- Owner：`dev-workflow`
- 驗證：
  - 所有 task JSON 都可解析；
  - analyzer 測試通過；
  - 變更過的 Markdown 連結都可解析；
  - 針對 role 與 invocation 的搜尋結果與已核准決策一致；
  - `git diff --check`；
  - 已記錄延後處理的遷移風險。

## Commit Checkpoints

1. `workflow(workflow): bootstrap use case handler alignment`
2. `workflow(workflow): record use case handler decisions`
3. `docs(architecture): align use case handler boundaries`
4. `docs(ai-context): synchronize use case handler guidance`
5. `feat(dotnet-backend): enforce use case handler boundaries`
6. `workflow(workflow): close use case handler alignment`

每個 workflow 階段的 commit 都要包含 `Why`、`What`、`Validation` 與 `Workflow` 區塊。

## 完成條件

- Controller、Use Case、Input/Output、Command/Query 與 Handler 各自只有一個標準角色。
- 同步 API 的呼叫鏈只有一個預設版本。
- framework 專屬的 dispatch 只能是條件式，不可以默默取代 Application port。
- 交易與事件生命週期的擁有權要明確。
- 提示詞、範例、測試、DI 指引與 analyzer 都要和已核准模型一致。
- 遷移指引要清楚區分 legacy 相容性與新的預設行為。

## 完成摘要

- D1-D12 都已完成決策或明確延後。
- 可攜式 aggregate persistence 使用 `IAggregateRepository<TAggregate, TId>`，只保留 `FindByIdAsync` 與 `SaveAsync`。
- `IDomainRepository<TAggregate, TId>` 仍然是衍生自 canonical interface 的相容契約，並且套用相同的 Aggregate Root 約束。
- 純讀取使用 `IQueryRepository` port；QueryService 仍然是條件式。
- target-specific 的 batch capability 指引已記錄，但沒有發布成強制性的 portable batch interface。
- DBA1001 已改成基於 inheritance 的 semantic validation，且 36 個 analyzer tests 全數通過。
- 舊的 repository grep scripts 已移除，無法再從 Markdown parser 重新產生。
- 另一個獨立的 Use Case/Handler 邊界工作，已刻意延後並記錄在 `tasks/follow-up-usecase-handler-boundary.json`。
