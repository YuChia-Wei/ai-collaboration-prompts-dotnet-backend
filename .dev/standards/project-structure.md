# .NET CA + WolverineFx 專案結構指南

本專案採用 **多 Bounded Context (BC)** 架構，每個 Domain 有獨立的 DomainCore 與 Presentation 層。

## 專案目錄結構

```
project-root/
├── src/
│   ├── BC-Contracts/                    # 跨 BC 通訊合約 (Published Language)
│   │   └── Lab.BoundedContextContracts.<Domain>/ # 各 Domain 的 Integration Events / Interactions / DTOs
│   ├── BuildingBlocks/                  # 共用建構模組（架構基礎設施）
│   │   ├── Lab.BuildingBlocks.Domain/   # Domain 層共用
│   │   ├── Lab.BuildingBlocks.Application/
│   │   └── Lab.BuildingBlocks.Infrastructure/
│   ├── Shared/                          # 通用領域核心 (Shared Kernel)
│   │   └── Lab.SharedKernel/            # 跨 BC 共享的 Value Objects、Enums 等領域概念
│   └── <DomainName>/                    # 特定 Domain (如 Order, Product)
│       ├── DomainCore/                  # Domain 核心層
│       │   ├── <DomainName>.Domains/        # Domain Model
│       │   ├── <DomainName>.Applications/   # Application Services
│       │   └── <DomainName>.Infrastructure/ # 技術基礎設施
│       └── Presentation/                # 展示層
│           ├── <DomainName>.WebApi/         # REST API
│           └── <DomainName>.Consumer/       # MQ Consumer (Console App)
├── tests/
│   └── <TargetProject>.Tests/           # 對應專案的測試
├── docker-compose/                      # Docker Compose 配置
├── docs/                                # 文件與設計筆記
├── https/                               # HTTP 測試檔案
│   └── <Context>/                       # 特定 BC 的 HTTP 測試
├── sql-script/                          # 資料庫腳本
├── .ai/                                 # 給 agent 重用的 prompts, shared rules, scripts
├── .dev/                                # 給人看的 specs, ADRs, requirements, guides
├── .gemini/                             # Gemini CLI 設定
├── .github/                             # GitHub & Copilot 資源
└── *.slnx                               # .NET Solution
```

## 專案層級規則

| 層級 | 職責 | 命名規則 | 位置 |
|------|------|---------|------|
| Domain | Domain Model | `<DomainName>.Domains` | `./src/<DomainName>/DomainCore` |
| Application | Application Services | `<DomainName>.Applications` | `./src/<DomainName>/DomainCore` |
| Infrastructure | 技術基礎設施 | `<DomainName>.Infrastructure` | `./src/<DomainName>/DomainCore` |
| Presentation | Web API | `<DomainName>.WebApi` | `./src/<DomainName>/Presentation` |
| Presentation | Queue Consumer | `<DomainName>.Consumer` | `./src/<DomainName>/Presentation` |
| Cross-BC | 跨 BC 通訊合約 | `Lab.BoundedContextContracts.<Domain>` | `./src/BC-Contracts` |
| BuildingBlocks | 架構基礎設施 | `Lab.BuildingBlocks.<Layer>` | `./src/BuildingBlocks` |
| SharedKernel | 通用領域核心 | `Lab.SharedKernel` | `./src/Shared` |
| Tests | 測試專案 | `<TargetProject>.Tests` | `./tests` |

## 文件與 AI 資產分工

| 路徑 | 主要讀者 | 用途 |
|------|---------|------|
| `./.dev/guides/ai-collaboration-guides` | Human | AI collaboration guides、workflow、prompt 範本 |
| `./.dev/guides` | Human | 一般開發與設計指南（ai collaboration / design / implementation / learning） |
| `./ai` | Agent | prompt 元件、shared rules、scripts |
| `./.claude/skills` | Agent | skill 定義本體與 skill-local references |

## 方案檔 (.slnx) 規則

- `.slnx` 的方案資料夾（Solution Folder）採「邏輯分組」，可不對應實體資料夾結構。
- 方案資料夾命名固定使用前後斜線格式：`/{Group}/`、`/{Group}/{SubGroup}/`（例如：`/Order/DomainCore/`）。
- 邏輯分組建議以 Bounded Context 與層級語意為主（如 `<ContextA>/DomainCore`、`<ContextB>/Presentation`）。
- `tests` 可維持單一頂層群組：`/tests/`。

## Application 層資料夾結構

```
<DomainName>.Applications/
├── Ports/                       # 介面定義 (依賴反轉)
│   ├── Queries/
│   │   └── I<Feature>QueryRepository.cs
│   ├── Persistence/             # 只有 domain-specific capability 才放置
│   │   └── I<Capability>Port.cs
│   └── I<Feature>QueryService.cs # optional composition port
├── QueryServices/               # Optional Application query composition
│   └── <Domain>QueryService.cs
├── Commands/                    # Command + Handler
│   └── Create<Entity>Command.cs
├── Queries/                     # Query + Handler
│   └── Get<Entity>Query.cs
├── DomainEventHandlers/         # Domain Event 處理器
└── Dtos/                        # Application 層 DTO (Input/Output)
```

Portable Aggregate Repository contract 位於 `BuildingBlocks.Application`：

- `IAggregateRepository<TAggregate, TId>`
- compatibility `IDomainRepository<TAggregate, TId>`
- `IQueryRepository` marker

不要為每個 Aggregate 預設建立空殼 `I<Aggregate>Repository`。只有相容既有程式碼或增加已核准的 Aggregate lifecycle/capability 語意時才建立 domain-specific port。

### Application 詞彙與責任

- `Use Case`
  - application boundary 與一次 business operation 的名稱，例如 `CreateProduct`
- `Command` / `Query`
  - 進入 use case 的 request model
- `Handler`
  - command / query 的 application-layer executor
- `Application Service`
  - 只有在 orchestration 明顯變複雜或需要重用時才抽出

預設規則：

- handler 可直接作為 use case implementation
- 不要求每個 use case 一定再多包一層 `*UseCaseService`
- 若 handler 只是單行轉呼叫同名 service，通常代表多包了一層無效抽象

推薦關係鏈：

```text
Controller
  -> Command / Query
  -> Handler
  -> Aggregate / Domain Service / Repository / Query Service
  -> Result DTO
```

補充規則見 [`USECASE-COMMAND-HANDLER-RELATIONSHIP.MD`](./USECASE-COMMAND-HANDLER-RELATIONSHIP.MD)

## Infrastructure 層資料夾結構

```
<DomainName>.Infrastructure/
├── Repositories/                # Aggregate Repository adapters
│   └── <Aggregate>Repository.cs
├── QueryRepositories/           # Query Repository 實作
│   └── <Feature>QueryRepository.cs
├── Persistence/                 # Target-selected DB/ORM/event-store configuration
├── Writers/                     # Outbox/Projection/Import/Purge capability adapters
└── Messaging/                   # MQ 相關實作
```

## Clean Architecture 分層

- **Domain**：Aggregate、Entity、Value Object、Domain Events
- **Application**：UseCase/Handler、Ports、Policies
- **Infrastructure**：target-selected persistence、Outbox、Message Bus、Repository/Query/Writer adapters
- **Presentation**：Controllers、DTO 轉換、驗證、MQ Consumers

## 命名與依賴方向

- Domain 不依賴其他層
- Application 依賴 Domain
- Infrastructure 依賴 Application/Domain
- Presentation 依賴 Application（不直接依賴 Infrastructure，透過 DI）

### Adapter 與 Bus 的關係

- Controller 應依賴 application boundary，而不是直接依賴 repository 或 aggregate
- 同 BC / 同 process 內，可使用 in-process dispatcher、mediator、Wolverine handler invocation 或直接呼叫 application port
- 跨 BC communication 才強制使用 MQ / message bus
- 不要把 message bus 視為 use case 本身

### Persistence Port Rules

- Aggregate Repository 只接受 Aggregate Root。
- Child Entity 透過 owning Aggregate Root 持久化。
- Query Repository 實作 `IQueryRepository` 且只讀。
- Physical purge、Outbox、Projection、Import 等使用 capability-specific ports。
- Target-specific batch persistence 不進入 portable/default project template。

## 跨 BC 通訊規則

> ⚠️ **重要限制**：跨 Domain 服務 **禁止** 透過 Web API 通訊，只能使用 Message Queue (RabbitMQ/Kafka)。
> 💡 **一致性模型**：跨 Domain 的資料同步採用「**最終一致性（Eventual Consistency）**」，不要求強一致。

| 通訊類型 | 使用機制 | 定義位置 |
|---------|---------|---------|
| 同一 BC 內 | Domain Events | `<Domain>.Domains/DomainEvents` |
| 跨 BC | Integration Events | `./src/BC-Contracts/Lab.BoundedContextContracts.<Domain>` |

## 共用專案分類（Shared Projects Classification）

> 詳細設計理由與 DDD 概念說明，應以本文件與相對應的 rationale / guide 文件為準。

本專案有三個跨領域共用區域，各自對應不同的 DDD 概念：

| 專案 | DDD 概念 | 職責 | 依賴權限 |
|------|---------|------|----------|
| `BuildingBlocks` | 架構基礎設施 | 無業務語義的抽象基底與介面 | 所有層均可引用 |
| `SharedKernel` | Shared Kernel | 跨 BC 共享的通用領域概念（VO、Enum） | Domain 層可引用 |
| `BC-Contracts` | Published Language | BC 間通訊合約（Integration Events、Request/Reply） | **Domain 層禁止引用** |

### 依賴方向約束

```
BuildingBlocks ← 所有層均可引用
SharedKernel   ← Domain / Application / Infrastructure / Presentation
BC-Contracts   ← Application / Infrastructure / Presentation（Domain 禁止）
```

### BC-Contracts 內部子分類

| 子目錄 | 用途 | 範例 |
|--------|------|------|
| `IntegrationEvents/` | 非同步事件合約（MQ Payload） | `OrderPlaced`, `ProductStockDecreased` |
| `Interactions/` | Request/Reply 合約 | `ReserveInventoryRequestContract` |
| `DataTransferObjects/` | 跨 BC 查詢回傳合約 | `OrderDetailsResponse` |

使用時應確保不會破壞 Bounded Context 的邊界隔離。
