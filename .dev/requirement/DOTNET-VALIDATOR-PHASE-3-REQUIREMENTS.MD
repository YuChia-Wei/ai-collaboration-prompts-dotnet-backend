# .NET Validator Phase 3 需求

## Metadata

- Title: .NET Validator Phase 3
- Version: 0.1
- Date: 2026-07-05
- Owner: YuChia-Wei
- Status: Draft - awaiting Mapper policy decision
- In Scope: Mapper、Aggregate、UseCase、Projection 的 validator ownership、dotnet-native validation 與對應 script retirement
- Out of Scope: Repository interface 規範、dependency/version validation、產品專屬架構規則

## Context & Goals

Phase 2 已以 Roslyn Analyzer 取代 Controller grep validation，但 Mapper、Aggregate、UseCase 與 Projection 仍在 `check-all.sh` 中列為待替換項目。

Phase 3 的目標不是把 grep 規則逐字改寫成 C#，而是先依規則性質選擇可靠的 enforcement mechanism：

| 規則性質 | Owner |
| --- | --- |
| 格式、命名與 C# coding style | `.editorconfig`、standard .NET analyzers、formatter |
| 可由 syntax / semantic model 確定的架構規則 | Custom Roslyn Analyzer |
| 跨型別、組件或 EF Core model registration | Architecture test 或 configuration test |
| Business invariant、mapping completeness 與設計意圖 | Unit/integration test 與 AI review |

成功標準是每個被移除的 script 都有等價或更可靠的 replacement，且不把無法機械證明的軟體設計品質偽裝成 CI gate。

## Personas

- Framework Maintainer：維護可重用的 .NET backend validation template。
- Application Engineer：在目標 repository 中取得明確且低誤判的 diagnostics。
- AI Agent：依 analyzer evidence 與 software engineering context 執行實作或 review，不以文字搜尋結果取代設計判斷。

## Functional Requirements

### FR-1：Rule Ownership Classification

- 每一項舊 script 規則必須分類為 `.editorconfig`、Roslyn Analyzer、architecture/configuration test、AI review 或移除。
- 已可由 standard .NET analyzer 支援的 coding style 不得重複實作 custom analyzer。
- `.editorconfig` 規則只有在 build、`dotnet format --verify-no-changes` 或其他 CI command 實際執行且 severity 足以阻擋時，才能宣稱為 gate。

### FR-2：Mapper Validation

Mapper 的角色是執行 Domain、Data 與 DTO 間的資料轉換，不應查詢 Repository、呼叫 UseCase/Handler，或承擔 business orchestration。

下列政策尚待決策：

#### Option A：Static-only Mapper

- Mapper 必須是 `static class`，mapping methods 必須是 static。
- 優點：強制純轉換、沒有 instance state、沒有 DI graph、analyzer 規則單純。
- 缺點：不適合需要注入 serialization policy、localization 或其他 conversion collaborator 的情境；替換與 mocking 彈性較低。
- 若轉換需要外部 dependency，應將該行為建模為 adapter、assembler 或 translator service，而不是 Mapper。

#### Option B：Static 或 Sealed Stateless Mapper Service

- 允許 `static class`，也允許 `sealed class` 的 instance mapper。
- Instance mapper 不得依賴 Repository、UseCase、Handler 或其他會執行 I/O／business orchestration 的服務。
- 優點：可經 DI 組合 conversion collaborators，也能實作介面並替換。
- 缺點：更容易讓 Mapper 累積 state、I/O 或 business logic；analyzer 必須定義並維護更複雜的 dependency allowlist。

無論採用何種 option：

- Argument null handling 優先交由 standard analyzers、nullable reference types 或 tests，不以方法內是否出現固定文字判斷。
- 欄位是否完整對稱映射必須由 mapping tests 或 AI review 驗證，不由 syntax analyzer 猜測。

### FR-3：Aggregate Validation Profiles

Aggregate validation 採用 shared baseline 加上 type-specific profile：

#### Shared Baseline

- `AggregateRoot` 與 `EsAggregateRoot` 都不得依賴 `DbContext` 或其他 Infrastructure type。
- 兩者都必須維護 invariant、封裝狀態變更，並由 tests 與 AI review 驗證 business behavior。
- 一般 Aggregate 可以發布 Domain Event，但不因此成為 Event Sourcing Aggregate。

#### Event Sourcing Profile

- 只有繼承 `EsAggregateRoot` 的 Aggregate 強制使用 `Apply/When` event transition model。
- Event Sourcing Aggregate 必須支援 event replay，且不得繞過 event transition 直接建立不可重播的狀態。
- 可由 analyzer 判定的 type hierarchy 與 forbidden direct mutation 才能成為 diagnostic；event history completeness 由 tests 與 review 驗證。

#### Normal Aggregate Profile

- 繼承一般 `AggregateRoot` 的 Aggregate 不強制使用 `Apply/When`。
- Normal Aggregate 可以直接在 domain method 中變更封裝狀態，並視需求發布 notification-style Domain Events。
- 不得因為沒有 event history 或 replay constructor 而產生 Event Sourcing diagnostic。

兩種 Aggregate 若完全採用相同規範，雖可降低文件與工具分支、提高表面一致性，也較容易將 normal Aggregate 遷移至 Event Sourcing；但會迫使不需要 replay 的模型承擔 event schema、versioning、rehydration 與測試成本，並混淆「Domain Event」和「Event Sourcing source of truth」。因此 Phase 3 採 shared baseline 加 profile-specific rules，不採完全相同規範。

### FR-4：UseCase Validation

- 保留 `DBA1002` 對 `IServiceProvider` constructor injection 的禁止。
- 補足可可靠判定的 Service Locator 或 property injection 規則。
- Command 與 Query 分離只能依明確的 marker interfaces／base types 判定，不以 `Handle(`、檔名或 method name 作為 CI gate。
- `private readonly`、公開 constructor、primary constructor 等 coding style 由 `.editorconfig` 與 standard analyzers 管理，不建立 custom architecture diagnostic。

### FR-5：Projection Configuration Validation

- 以 `IProjectionReadModel` marker interface 識別需要 EF Core model registration 的 projection read model。
- EF Core configuration test 必須列舉 `IProjectionReadModel` implementations，並確認每一型別存在於 `DbContext.Model`。
- Dapper-only projection/query DTO 不必實作 `IProjectionReadModel`，也不受 EF Core registration gate 約束。
- Query service interface（例如 `IRecordProjection`）不得因名稱包含 `Projection` 而被視為 EF Core entity。
- 不再以檔名、`DbSet<` source text 或 `Entity<` source text 判定 registration。

### FR-6：Transitional Script Retirement

- Mapper、Aggregate、UseCase、Projection 的 script 只能在其可機械驗證規則已有 replacement 且測試通過後移除。
- 不適合自動化的規則必須明確轉移至 AI review 或 test guidance，不得因 script 移除而消失。
- `check-all.sh` 必須以 analyzer tests 或 configuration tests 取代完成項目的 TODO。
- Repository TODO 保留到獨立規範整理完成。

## Non-Functional Requirements

- Analyzer 必須使用 Roslyn syntax / semantic APIs，不得改用 source text regex。
- Diagnostics 必須具有 positive、negative 與 false-positive regression tests。
- Validator template 不得依賴單一產品的 namespace、aggregate name、projection name 或 folder layout。
- Rule ownership 必須可由文件追溯到 source standard、test 或 AI review context。

## Constraints & Assumptions

- Repository interface 規範將在另一個 worktree 與 conversation 重新整理，Phase 3 不修改 `DBA1001` 或 repository script。
- `EsAggregateRoot` 與 `AggregateRoot` 是目前 dotnet-backend profile 的 canonical type distinction。
- Projection marker interface 名稱暫定為 `IProjectionReadModel`；若實際 framework 已存在等價介面，實作時應採用既有 canonical type。
- 現有 `.editorconfig` 已包含 primary constructor 與多項 coding-style preference，但部分 severity 為 `suggestion` 或 `silent`，目前不等同 CI failure。
- Mapper policy 是唯一尚未確認、會阻擋對應 analyzer implementation 的方向決策。

## Domain / Architecture Rules

- Custom analyzer 補足的是 standard tooling 無法表達的 architecture semantics，不是重複實作 formatter。
- Normal Aggregate 與 Event Sourcing Aggregate 共享 domain purity 與 invariant responsibility，但 persistence source of truth 不同。
- Projection registration 是 assembled EF Core model 的事實，應在 model 建立後驗證。
- AI review 保留對 design intent、business completeness 與合理 tradeoff 的判斷責任。

## Acceptance Criteria

- 每項 Phase 3 規則都具有明確 enforcement owner。
- Repository validation 沒有被 Phase 3 修改或移除。
- Mapper policy 經使用者確認後才實作 diagnostic。
- Event Sourcing diagnostics 只套用於 `EsAggregateRoot`。
- Normal `AggregateRoot` 不因缺少 `Apply/When` 被回報。
- UseCase custom diagnostics 不重複 `.editorconfig` 可處理的 coding style。
- EF Core projection registration 透過 `IProjectionReadModel` 與 model/configuration test 驗證。
- 每個被移除的 script 都有 replacement evidence 與通過的 tests。
- Analyzer 與 configuration-test suites 全部通過。
- `check-all.sh` 不再列出已完成的 Mapper、Aggregate、UseCase、Projection TODO。
- `git diff --check` 通過。

## Open Decision

- Mapper 採 Option A（static-only）或 Option B（static 或 sealed stateless service）。

## References

- `.editorconfig`
- `.dev/requirement/DOTNET-VALIDATOR-PHASE-2-REQUIREMENTS.MD`
- `.dev/standards/coding-standards/mapper-standards.md`
- `.dev/standards/coding-standards/aggregate-standards.md`
- `.dev/standards/coding-standards/usecase-standards.md`
- `.dev/standards/coding-standards/projection-standards.md`
- `.ai/assets/tech-stacks/dotnet-backend/references/CODE-REVIEW-INDEX.MD`
- `.ai/scripts/check-all.sh`
- `tools/DotnetBackendAnalyzers/`

