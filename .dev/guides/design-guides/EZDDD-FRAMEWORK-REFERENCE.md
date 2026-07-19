# Historical ezDDD Concept Mapping (.NET)

本文件只保留歷史名稱與目前 repository 契約的對照，不是目前 package
roadmap、套件建立承諾或必要 namespace 清單。若對照內容與 canonical
standards 衝突，以 canonical standards 為準。

## Historical Concept Mapping

| Historical label | Current repository contract |
| --- | --- |
| `AggregateRoot` | 一般 aggregate 直接實作 `IAggregateRoot<TId>`；只有選用 Event Sourcing 時才使用 `EsAggregateRoot<TId>` 行為契約。 |
| `Entity` | 由 target domain 定義 identity 與 lifecycle；不要求共用 `DomainEntity<TId>` base class。 |
| `ValueObject` | 優先使用 immutable `record` 或 `record struct`；不要求共用 `ValueObject` base class。 |
| `DomainEvent` | 使用 project-owned `IDomainEvent` contract；具體 shape 依 target requirement 與 tech-stack profile。 |
| `UseCase` | Application inbound port 與實作，擁有一個 business action 的 orchestration。Command/Query 是 request model。 |
| `Handler` | 只有真實 dispatch/message entry 存在時才使用的薄 inbound adapter；它映射 delivery contract 並呼叫一個 Use Case，不是 Use Case 實作。 |
| `Repository` | 由 target 選擇的 project-owned persistence port；預設 aggregate repository 行為以 reconstruction contract 與 repository standards 為準。 |
| `MessageBus` / `MessageProducer` | 透過 project-owned ports 隔離 runtime；具體技術由 technology selection policy 決定。 |
| `Contract` | Design by Contract 的語意契約；helper 名稱與套件不是框架必要 API。 |
| `CqrsOutput` | 可重用 output pattern，不代表所有 target 必須採用同一共用套件。 |

## Current Authority

- [BuildingBlocks Reconstruction Contract](../../standards/BUILDING-BLOCKS-RECONSTRUCTION-CONTRACT.md)
- [Technology Selection Policy](../../standards/TECHNOLOGY-SELECTION-POLICY.md)
- [Use Case, Command, Query, And Handler Relationship](../../standards/USECASE-COMMAND-HANDLER-RELATIONSHIP.MD)
- [Design By Contract Semantics](../../standards/DESIGN-BY-CONTRACT.md)

未來若要建立跨技術棧術語 capability，應由 roadmap `CAP-001` 另行定義；
本歷史對照不得自行形成新 package 或新治理合約。
