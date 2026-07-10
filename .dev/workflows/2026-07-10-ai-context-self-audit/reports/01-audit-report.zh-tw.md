# AI Context 自檢報告

## 中繼資料

- `report_id`: `review-report-2026-07-10-ai-context-self-audit`
- `owner_skill`: `ai-context-auditor`
- `workflow_id`: `2026-07-10-ai-context-self-audit`
- `related_plan_id`: `2026-07-10-ai-context-self-audit`
- `report_kind`: `baseline-audit-translation`
- `status`: `final`
- `audit_date`: `2026-07-10`
- `created_at`: `2026-07-10T17:47:01+08:00`
- `created_at_source`: `git-history; first tracked commit`
- `updated_at`: `2026-07-10T23:39:54+08:00`
- `template_source`: `.dev/workflows/2026-07-10-ai-context-self-audit/reports/01-audit-report.md`
- `template_version`: `derived-translation-v1`
- `metadata_addendum_at`: `2026-07-10T23:39:54+08:00`
- `metadata_addendum_reason`: `補上衍生來源版本；未變更翻譯內容、發現、分數、證據或結論。`
- `derived_from`: `.dev/workflows/2026-07-10-ai-context-self-audit/reports/01-audit-report.md`
- `origin_workflow_id`: `2026-07-ai-context-audit-report-translation`
- `origin_commit`: `648f920`
- `repository`: `ai-collaboration-prompts-dotnet-backend`
- `branch`: `main`
- `previous_report`: `none`

本報告記錄加入 `ai-context-auditor` 之前所評估的儲存庫狀態。原始工作流程中的技能建立變更，不會被視為原始發現已完成修正的證據。

## 執行摘要

- 整體評估：儲存庫具備成熟的 AI Context 治理概念，但現行規則、canonical ownership、schema、執行環境宣告與驗證閘門，尚未形成可靠且可由機器驗證的閉環。
- 整體評分：`6.5/10`
- 決策：`remediation-recommended`
- 主要優勢：清楚的儲存庫定位、刻意設計的 context 分層、證據優先的事實處理、有界限的委派、精簡的執行環境 wrapper，以及明確的驗證遷移方向。
- 主要風險：雙重規範介面、過時但仍有效的入門指引事實、互不相容的測試規則、規範結構描述漂移、工作流程授權缺口，以及驗證腳本失敗時仍放行的行為。

### 評分明細

| 維度 | 分數 |
| --- | ---: |
| Context 架構與治理設計 | 8.0/10 |
| 導覽與可發現性 | 7.0/10 |
| 規則一致性 | 5.0/10 |
| 執行環境與機器驗證閉環 | 5.5/10 |
| 可攜性與目標儲存庫安全性 | 6.0/10 |

## 範圍

### 納入的 AI Context 範圍

- 根目錄 README 與代理程式指示檔案。
- `.ai/**` canonical assets、skill registry、sub-agent prompts、參考資料、範本與 context scripts。
- `.dev/**` 治理、標準、指南、需求、規格、維運與工作流程紀錄。
- `.agents/**` 與 `.claude/**` 執行環境包裝器。
- `.github/**` 下的 AI 助理宣告。
- 驗證發現所需的 Git 中繼資料與 context validation commands。

### 預設排除項目

- `src/**` 實作內容。
- `tests/**` 與 `test/**` 實作內容。
- 產品功能、領域、應用程式、基礎設施、API 與測試程式碼。
- 產生的輸出與相依性目錄樹。

儲存庫盤點顯示了產品與工具路徑，但未檢閱其中的實作內容。本報告的所有結論皆不屬於產品程式碼發現。

### 其他排除項目

- 發現的修正。
- 生產架構重新設計。
- BDD 情境設計。
- 大範圍文件翻譯。
- Gemini 或 Copilot 包裝器實作。

### 程式碼檢閱移交

- 是否要求：`no`
- 未掃描路徑：`src/**`、`tests/**`、產品實作與測試程式碼。
- 若日後提出要求，建議使用的技能：`code-reviewer`。

## 方法與證據

### 階段 A：獨立基準

- 採用一般 AI Context engineering、知識庫、文件架構、runtime adapter、驗證完整性與可攜性原則。
- 此階段未讀取或套用儲存庫技能規格。
- 以平行且唯讀的稽核涵蓋結構／導覽、內容／事實品質，以及執行環境／結構描述／腳本關係。
- 從根目錄進入點、索引、現行標準、入門指南、context rules、wrapper 清單與 scripts 中，驗證高嚴重度證據。

### 階段 B：Repo-aware Skill 檢閱

- 套用 `dev-workflow` 處理工作流程、產出物、路由與驗證邊界。
- 套用 `ai-context-governance` 處理受眾、範圍、語言、放置位置、規範擁有權與包裝器同步。
- 將發現與 `AI-CONTEXT-BOUNDARY.md`、`AI-CONTEXT-LANGUAGE-POLICY.md`、規範技能登錄、包裝器索引、工作流程閘門及提交政策進行比較。
- 當技能邊界要求延後處理時，重新分類過於廣泛或屬於歷史性的疑慮。

### 委派

- 是否使用子代理程式：`yes`，三個有界限的稽核介面。
- 指派介面：結構／導覽；內容／事實／語言；執行環境／包裝器／結構描述／腳本。
- 主代理程式職責：範圍管控、證據驗證、重複項目處理、嚴重度排序、技能比較與最終綜整。

## Repository Context 清單

| 介面 | 稽核時的檔案／大小 | 受眾 | 範圍 | 狀態 | 備註 |
| --- | ---: | --- | --- | --- | --- |
| 儲存庫總計 | 612 個檔案 | 混合 | 框架儲存庫 | 使用中 | 347 個 Markdown、43 個 YAML、94 個 JSON |
| `.ai/**` | 155 個檔案，約 59K tokens | 代理程式 | 通用與 dotnet-backend | 使用中／過渡中 | 結構健全；語言、結構描述與腳本仍有漂移 |
| `.dev/**` | 390 個檔案，約 242K tokens | 兩者 | 治理、可重用標準、專案／工作流程事實 | 使用中／歷史 | 最大的認知負荷與擁有權熱點 |
| 規範技能 | 12 | 代理程式 | 規範技能 | 使用中 | 稽核時與兩組執行環境包裝器相符 |
| Codex 包裝器 | 12 | 代理程式 | 執行環境包裝器 | 使用中 | 稽核時精簡且同步 |
| Claude 包裝器 | 12 | 代理程式 | 執行環境包裝器 | 使用中 | 稽核時精簡且同步 |
| 工作流程紀錄 | 18 個非範本目錄 | 兩者 | 工作流程與歷史狀態 | 混合生命週期 | 缺少使用中／已完成／已取代／封存登錄 |

## 優勢

1. 儲存庫定位明確指出這是可攜式 AI 協作框架，而非產品儲存庫。
2. `.ai`、`.dev`、規範技能、子代理程式提示詞與執行環境包裝器之間具有刻意設計的概念邊界。
3. README 與 INDEX 的職責區分為目的／邊界及目錄／導覽。
4. 根目錄代理程式規則強調以檔案為依據的事實、最小且一致的變更，以及可驗證的完成條件。
5. 子代理程式委派具明確界限，並將綜整與驗證保留給主代理程式。
6. 規範、Codex 與 Claude 技能集為 `12 / 12 / 12`，抽樣的包裝器皆保持精簡。
7. 儲存庫明確認知到，以 grep 為基礎的 C# 驗證應遷移至 Roslyn、測試或其他 .NET 原生機制。
8. 稽核時 Git 衛生狀態良好，沒有追蹤中的 `bin/` 或 `obj/` 輸出。

## 發現

| ID | 嚴重度 | 發現 | 證據 | 影響 | 建議 | 負責人／下一個技能 |
| --- | --- | --- | --- | --- | --- | --- |
| AIC-001 | HIGH | 可重用的 .NET 代理程式規則有兩個規範介面：`.ai/assets/tech-stacks/dotnet-backend/**` 與 `.dev/standards/**`。 | `.dev/standards/README.md` 將其內容稱為可重用標準，而 `.ai` 檔案則宣告強制性代理程式規則。 | 代理程式可能同時收到互相衝突的有效事實，且沒有明確的優先順序。 | 建立逐條規則的擁有權矩陣，並只保留一個規範擁有者。 | `ai-context-governance`，接著由架構／測試負責人做出領域決策 |
| AIC-002 | HIGH | 測試規則彼此不相容。 | `common-rules.md` 與 `testing-strategy.md` 要求僅使用 BDDfy 並禁止 `.feature`；`GHERKIN-FEATURE-STORAGE-GUIDE.MD` 則要求在 `tests/Features/` 下存放正式 `.feature` 資產。 | 遵循規範的代理程式無法同時滿足兩份有效契約。 | 決定 feature 檔案應為禁止、依設定檔選用，或正式支援，然後同步所有使用端。 | 測試決策負責人，由 `dev-workflow` 協調 |
| AIC-003 | HIGH | 現行入門指引包含過時的產品事實與已淘汰的拓撲。 | `coding-guide.md` 描述 Todo List 應用程式，以及固定的 Wolverine／EF／Event Sourcing 選擇；`NEW-PROJECT-GUIDE.md` 建立舊版 `.ai` 與 `.dev` 根目錄並安裝固定套件；學習文件引用不存在的 `CLAUDE.md`。 | 目標儲存庫可能繼承不受支援的技術與目錄決策。 | 在再次使用這些現行入門進入點之前，先將其停用或重寫。 | `ai-context-governance` 搭配 `ddd-ca-hex-architect` 處理技術選擇 |
| AIC-004 | HIGH | 規範資產未遵循規範資產結構描述。 | 所有 12 份技能規格皆使用 `asset_id`，而不是必要的 `id`；其中 8 份缺少部分已宣告為必要的中繼資料；17 份子代理程式資訊清單也有相同的識別碼不符問題；重複的範本系列採用互不相容的格式。 | 機器驗證或匯出無法依賴已宣告的結構描述。 | 為結構描述建立版本，選定 `id` 或 `asset_id`，定義穩定的型別／列舉，遷移資產並加入驗證器。 | `ai-context-governance` |
| AIC-005 | HIGH | `dev-workflow` 的探索與設定檔契約不完整。 | 探索機制偏好 `capability_slots`，但受稽核技能皆未宣告此欄位；能力設定檔將 `local-change-implementer` 對應到 `implementation`，且缺少 `local-change` 資料列。 | 可攜式探索會退化為依名稱推論，而本機路由可能選到意義不明確的實作者。 | 加入能力中繼資料，並驗證設定檔與技能的一致性。 | `dev-workflow` / `ai-context-governance` |
| AIC-006 | HIGH | 工作流程政策缺少唯讀稽核／僅報告的例外。 | 兩個階段、使用子代理程式或進行檢閱時，必須建立工作流程產出物，而提交政策要求在工作流程與盤點邊界進行提交。 | 唯讀分析可能在未明確表達修正意圖的情況下，被迫修改並提交儲存庫狀態。 | 加入僅稽核模式，在保留路由與報告的同時，允許明確略過會造成變更的產出物。 | `dev-workflow` 治理 |
| AIC-007 | HIGH | 即使略過重要檢查，context script gate 仍可能通過。 | 受追蹤的 shell 檔案模式為 `100644`；`check-all.sh` 將不可執行的腳本轉為警告，並在有警告時仍以 `0` 結束；Windows Git Bash 掩蓋了檔案模式問題。 | CI 或使用者可能因成功的結束代碼而產生錯誤信心。 | 讓必要檢查失敗時關閉 gate、驗證 Git 可執行模式，並區分僅警告的 preflight 與正式 gate。 | Tooling workflow；不屬於 AI Context 自檢修正 |
| AIC-008 | MEDIUM | 文件將 Gemini 與 Copilot 支援描述為現行功能，但進入點根目錄並不存在。 | 根目錄進入點與執行環境指南引用 `.gemini/`、`.github/prompts/` 與 `.github/copilot-instructions.md`；這些項目全都不存在。 | 使用者與代理程式會高估支援的執行環境矩陣。 | 將支援標示為規劃中，或建立並驗證所承諾的進入點。 | `ai-context-governance` |
| AIC-009 | MEDIUM | 導覽、語言、受眾與生命週期政策未持續接受驗證。 | `.dev/INDEX.md` 包含三處常值 ``|`n|`` 損毀；現行索引不完整；面向 agent 的中文教學內容仍留在 `.ai`；workflow 缺少生命週期導覽。 | 即使治理政策撰寫完善，漂移仍會持續累積。 | 加入 context lint，檢查路徑、表格、語言例外、雙語一致性、wrapper 一致性與 workflow lifecycle。 | `ai-context-governance` |

## 基準與技能比較

### 已確認

- 條件式規則與強制性規則之間的衝突。
- 過時的入門指引與遺失的路徑。
- 語言政策漂移與不完整的索引關係。
- 工作流程認知負荷與缺少生命週期。
- 腳本與結構描述／範本的遷移債務。

### 由理解儲存庫的檢閱新增

- 規則衝突源自 `.ai` 與 `.dev/standards` 之間的雙重規範擁有權。
- 現行 `coding-guide.md` 是產品事實外洩，而不只是舊範例。
- 結構描述漂移涵蓋所有頂層技能與所有子代理程式資訊清單。
- `dev-workflow` 存在能力設定檔與僅稽核授權缺口。
- `.dev/specs/tests` 同時存在放置位置與語言不明確的問題。

### 降級或延後

- 穩定的雙語根目錄進入點是允許的；它們需要擁有權／一致性檢查，而非移除。
- 執行環境包裝器重複是預期行為，且稽核時狀態健全；剩餘問題是缺少自動化漂移閘門。
- 歷史工作流程紀錄的放置位置正確；問題在於生命週期導覽，而非紀錄本身的存在。
- 大範圍翻譯、腳本停用與產品架構決策需要各自獨立的工作流程。

### 推翻

- 沒有證據顯示受稽核的 Codex 與 Claude 包裝器，在技能清單或規範參考資料方面已彼此漂移。
- README 大小寫與空白預留位置目錄未被保留為主要治理發現。

## 驗證

| 檢查 | 結果 | 證據／備註 |
| --- | --- | --- |
| 稽核完成時的 Git 狀態 | PASS | 在技能建立工作流程開始之前，工作樹是乾淨的 |
| 登錄與包裝器一致性 | PASS | 規範／Codex／Claude 技能集為 `12 / 12 / 12` |
| 路徑與參考資料檢查 | FINDINGS | Gemini 與 Copilot 進入點不存在；已確認 `.dev/INDEX.md` 表格損毀 |
| 結構描述／結構化檔案稽核 | FAIL | 規範結構描述與資產欄位不一致 |
| 提示詞可攜性檢查 | PASS | `.ai/scripts/check-prompt-portability.sh` 在 Git Bash 下通過 |
| 程式碼標準完整性檢查 | PASS WITH WARNINGS | 完成時有 14 個警告，包括缺少反向參考與可能的重複內容 |
| 腳本閘門語意 | FAIL | 已確認必要腳本略過行為，以及僅警告卻以 `0` 結束的行為 |

### 略過的驗證

- 未執行產品建置與測試，因為產品原始碼與測試程式碼不在稽核範圍內。
- 未執行 `code-reviewer` 工作流程。
- 未執行修正驗證，因為本次稽核為唯讀。
- 不需要進行網際網路研究。

## 建議行動順序

1. 停止現行錯誤指引：解決 `.feature` 決策、停用或重寫過時的入門指引、修復索引損毀、修正執行環境支援宣告，並加入僅稽核工作流程例外。
2. 建立規範擁有權與共用的規則強度詞彙：`invariant`、`profile-default`、`conditional-if-selected`、`example` 與 `historical`。
3. 修復機器治理：為資產結構描述建立版本、對齊範本、加入能力中繼資料、驗證路由設定檔，並加入包裝器／路徑漂移檢查。
4. 當情境／工具驗證被當作閘門時，應讓其失敗時關閉閘門。
5. 加入工作流程生命週期與針對性的語言／受眾清理，且不啟動大範圍翻譯遷移。

## 延後項目

- 選定最終 BDD／測試產出物策略。
- 選定強制性與條件式 .NET 套件及架構慣例。
- 實作或停用 Roslyn、shell 與產生式驗證器。
- 產品原始碼與測試程式碼檢閱。
- 大範圍翻譯與歷史工作流程封存。
- 修正本報告中的所有發現。

## 附錄

### 執行過的代表性命令

```text
rg --files --hidden -g '!**/.git/**' ...
rg -n --hidden ...
git status --short
git ls-files -s .ai/scripts/*.sh
Git Bash ./.ai/scripts/check-prompt-portability.sh
Git Bash ./.ai/scripts/check-coding-standards.sh
path-existence and canonical/wrapper set comparisons with PowerShell
```

### 備註

- 本報告刻意區分稽核事實與後續建立 `ai-context-auditor` 的工作。
- 未來的稽核應與本報告比較，並記錄已解決、重複發生及新引入的發現。
