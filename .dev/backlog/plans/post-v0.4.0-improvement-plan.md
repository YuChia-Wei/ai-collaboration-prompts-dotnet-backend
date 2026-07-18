# AI Context 待辦與改進計畫（v0.4.0 之後）

- 基準：main @ v0.4.0（tag `5af1db6`）之後的 HEAD，2026-07-17 逐項複驗
- 性質：本文件**只列尚未修正的項目**；v0.4.0 已完成的改進一律不重複記載
- 佐證：全量基線稽核 `.dev/assessments/ASM-20260717-004/report.md`（finding 以 `#AIC-xxx` 引用）與 v0.4.0 驗證鏈（ASM-20260715-002 → ASM-20260717-003）
- 用途：直接作為 v0.4.1 / v0.4.2 / v0.5.0 的工作定義；每項含位置、驗收條件、估時、是否需要使用者決策

---

## 0. 版本切分原則

| 版本 | 定位 | 收錄標準 |
| --- | --- | --- |
| **v0.4.1** | 內容修正 patch | 免決策、純文件與 wrapper 修正，直接影響 agent 產出正確性；不動工具、不動結構 |
| **v0.4.2** | 工具修正 patch | gate 可攜性與 CI；有少量技術決策但無內容/契約變更 |
| **v0.5.0** | minor | 需要政策決策、新標準設計、或結構調整的項目 |

原則：**「agent 今天就會學錯的」進 0.4.1；「證據無法重現的」進 0.4.2；「需要決策或設計的」進 0.5.0。**

---

## 1. v0.4.1 — 內容修正（估 2~3 天，建議一週內出）

目標：發佈後任何 runtime 的 agent 載入 context 都得到一致、正確的教義與路由。全部免使用者決策。

### 1.1 Wrapper 跨 runtime 用語修正（最高優先）
- 問題：5 個 Claude wrapper 的 description 寫「Use when **Codex** needs」，直接劣化 Claude 的 skill 路由；已存活三個版本，因為 wrapper 驗證器只查路徑同位、不查用語。
- 位置：`.claude/skills/{bdd-gwt-test-designer, ddd-ca-hex-architect, requirement-author, problem-frame-author, spec-author}/SKILL.md:3`；`.agents/skills/` 側需同步檢查對稱殘留（至少 `ai-context-governance/SKILL.md:3` 有 Claude 字樣）。
- 工作：
  1. 十四個 skill 兩側 wrapper 的 description 全面改為 runtime 中性措辭（建議「Use when the agent needs …」）或各自正確的 runtime 名稱。
  2. `validate-ai-context.py` wrapper 檢查加規則：`.claude/**` 的 frontmatter description 禁含 `Codex`、`.agents/**` 禁含 `Claude`（canonical-source 引用行白名單放行），fail-closed。
  3. 補 GWT 測試（`.ai/scripts/tests/`）。
- 驗收：grep 兩側 wrapper description 零跨 runtime token；新驗證規則有紅→綠測試證明。
- 估時：修字 0.5h；驗證規則 + 測試 0.5d。對應 `#AIC-001`。

### 1.2 Use Case / Handler 教義單一化
- 問題：三方矛盾——canonical 禁止 Handler 依賴 Repository，但兩份活文件的 ✅ 正面範例正是該反模式，AI 載到哪份就寫出哪種形狀。
- 位置與工作：
  1. `best-practices.md:65-77`：`CreatePlanHandler` 注入 `IAggregateRepository` 的 ✅ 範例 → 改為「Controller → `I<Op>UseCase`、thin Handler 只 dispatch」的 canonical 形狀（`usecase-standards.md:135-166` 已有可抄的正確範本）。
  2. `anti-patterns.md`：同性質 ✅ 修正範例（`CreateOrderHandler` 注入 repository）同步改寫。
  3. `learning-guides/LEARNING-PATH.md:118-131`：「Use case handler shape (Wolverine)」static handler 教學重寫，並把 `USECASE-COMMAND-HANDLER-RELATIONSHIP.MD` 加入必讀清單。
  4. 為 `best-practices.md`、`anti-patterns.md` 加 precedence 標頭：「與 `coding-standards/*` 或 `USECASE-COMMAND-HANDLER-RELATIONSHIP.MD` 衝突時以後者為準」。
- 驗收：全 repo 活文件（workflow 歷史紀錄除外）不存在「Handler 注入 Repository 作為 ✅ 範例」；LEARNING-PATH 教學與 canonical 一致。
- 估時：1d（含交叉校對）。對應 `#AIC-002`。

### 1.3 時間 API 統一
- 問題：`anti-patterns.md` 禁 `DateTime.UtcNow`（要求 DateProvider/TimeProvider），但 ✅ 範本自己在用。
- 位置：`aggregate-standards.md:141,228,257`；`examples/dto/TaskDto.cs:52,90,181`；`examples/projection/EfTasksDueTodayProjection.cs:19`。
- 工作：統一為 .NET 8+ 原生 `TimeProvider`（或 repo 既有 DateProvider 慣例，擇一並在 anti-patterns 指名唯一權威）。`examples/aggregate/Plan.cs` 已是改好的參考做法。
- 驗收：活標準與 examples 的 ✅ 內容零裸 `DateTime.UtcNow`。
- 估時：0.5d。對應 `#AIC-008`。

### 1.4 快修集（合計約 1.5h）
| 項 | 位置 | 工作 | 對應 |
| --- | --- | --- | --- |
| C# 命名事實錯誤 | `CODE-REVIEW-CHECKLIST.md:24` | 「camelCase for methods」→ PascalCase；`.ai/assets/.../shared/code-review-checklist.md` 副本同步（目前用省略迴避而非修正） | `#AIC-008` |
| AGENTS 路由表 13/14 | `AGENTS.md:172-186`、`AGENTS.zh-TW.md` 對應表 | 補 `spec-compliance-validator` 一列 | `#AIC-010` |
| Sub-agent 表 17/18 | `.ai/SUB-AGENT-SYSTEM.MD` 路由表 | 補 `context-translator` 一列（role 已存在且被 repo-structure-sync 引用） | `#AIC-010` |
| workflows INDEX 死連結 | `.dev/workflows/INDEX.MD:67` | `[templates/](templates/)` 指向不存在目錄——刪列或改指現行模板持有者 | `#AIC-006` |
| auditor 孤兒模板 | `.ai/assets/skills/ai-context-auditor/templates/` | 刪除 3 個無 inbound 引用、編碼已廢止持久化模型的模板（workflow-locator / workflow-plan / task；保留 report template） | `#AIC-004` |
| requirements 收尾 | `DOTNET-VALIDATOR-PHASE-2-REQUIREMENTS.MD:8`、`HISTORICAL-CONTEXT-NORMALIZATION-REQUIREMENTS.MD:8` | 補 Implementation Outcome 段（同儕檔案已有格式可循） | `#AIC-018` |

### 1.5 v0.4.1 發版檢查
- 本版無 breaking、無檔案搬移 → disposition manifest 可為 trivial（全 kept + content-updated 註記），但仍建議產出以維持慣例。
- 發版前跑全量 `ai-context-auditor` baseline（不是只驗這次改的），確認 1.1~1.4 之外無新增回歸。

---

## 2. v0.4.2 — 工具與 CI（估 2~3 天；若時程緊可併入 v0.5.0 前置，但建議先出）

目標：release 證據在任何乾淨環境可重現；enforcement 從「本機自律」變成「制度」。

### 2.1 Gate 可攜性（TOOL-001 擴充範圍）
- 問題：`check-all.sh` 全用裸 `python`（`:222,226,230…`），原生 macOS/Ubuntu 無此指令→13/14 required 直接失敗；`validate-ai-context.py:13` `import yaml` 無依賴 bootstrap；`.ai/scripts/README.md` 零前置需求宣告；實際 Python 下限為 ≥3.10（`ai_context_package.py:507` 的 `write_text(newline=)`，3.9 會掛 44/107 測試）；`global.json` 釘 `10.0.300` 且來源 commit 名為「temp」。
- 工作：
  1. `python` → `python3`（或 interpreter 偵測），**同一變更內**同步 `shell-assets.yaml` 的 `check_all_required_commands`（parity 契約烤死了裸 python 形式）。
  2. 依賴 bootstrap：`requirements.txt` + 文件化 venv 流程，或 vendored 純 Python YAML fallback，擇一。
  3. `.ai/scripts/README.md` 宣告 Python ≥3.10 門檻與安裝步驟。
  4. `global.json`：改為明意圖的版本策略，或 gate 對 SDK 缺席給明確 SKIP 而非 FAIL。
  5. `check-test-compliance.sh` 處置：`BASE_DIR`（`:25-26`）解析到 repo 上層的 bug——修 `../..` 或直接刪除（shell-assets 已標 retirement-candidate、analyzer 為替代者；建議刪）。
- 驗收：乾淨的 macOS 與 Ubuntu（僅 `python3`、無預裝 PyYAML）照 README 步驟可跑出與 release 紀錄一致的 gate 結果。
- 估時：1~2d（含雙平台驗證）。對應 `#AIC-003`、`#AIC-005`、`#AIC-013`；backlog `TOOL-001`（建議升 HIGH 並把上述寫進 acceptance）。

### 2.2 治理 CI
- 問題：`.github/workflows/` 只有打包兩條；v0.4.0 建的大量驗證器在一般 PR 完全不跑——1.1 那類「驗證器盲區 + 沒人手動跑」的問題會繼續漏。
- 工作：新增 governance workflow：PR 觸發（路徑 `.ai/**`、`.dev/**`、`.claude/**`、`.agents/**`、`AGENTS*`、`CLAUDE.md`、`README*`）執行全部 Python 驗證器 + `.ai/scripts/tests/` GWT 套件；依賴 2.1 完成（CI runner 就是「乾淨環境」）。
- 決策點：runner 的 Python 版本策略（建議與打包 CI 同用 3.12）。
- 驗收：任一 PR 觸碰治理面時，破壞 wrapper 同位/索引/證據宣稱的變更無法綠燈合併。
- 估時：2.1 完成後 0.5d。對應 `#AIC-007`。

---

## 3. v0.5.0 — 政策、設計與收尾（規劃期定案）

目標：把 v0.4.0 做對的一次性行為制度化，並完成需要決策/設計的項目。

### 3.1 政策制度化（需決策）
| 項 | 工作 | 決策點 |
| --- | --- | --- |
| Disposition manifest 制度化 | 把「breaking release 必附 file-disposition manifest + 專用驗證器通過」寫入 `AI-CONTEXT-VERSION-POLICY.md`。v0.4.0 的 163 筆 manifest 做得很好，但它是單次 workflow 產物，無政策保證下次會再做 | manifest 正式落點：隨 release 資產發佈，或留 workflow 目錄由 `metadata/migration.yaml` 投影（現狀） |
| 發版前全量 baseline | 把「minor release 前跑一次全量 `ai-context-auditor` baseline（非僅 remediation verification）」寫入 version policy。理由：v0.4.0 驗證鏈只驗「這次改的」，範圍外殘留（本計畫 1.1、1.2）正是這樣活過三個版本 | 是否含 patch 版 |
| first-parent 驗證留檔 | 為「guarded history rewrite + commit 驗證收窄為 first-parent」補 ADR 或 workflow 附註：決策理由、適用邊界、為何不構成放寬先例。main 歷史現有兩組主旨相同的 commit 序列，不留檔會被未來讀史者誤判 | ADR 或附註形式（0.5h 工作） |
| 檔名規則（前瞻性） | 訂一句話規則「新檔案一律小寫 `.md`」。v0.4.0 剛做完大規模搬移，不建議回溯改名 | 是否採納 | 

### 3.2 設計項目
| 項 | 工作 | 備註 |
| --- | --- | --- |
| Observability 標準（backlog `OBS-001`） | 完整 CrossCutting Observability/AOP 設計，獨立 architecture workflow | v0.4.0 已出「Domain 禁依賴」邊界；設計必須消費 `TECHNOLOGY-SELECTION-POLICY.md` 的 `observability.runtime` slot，勿另起爐灶 |
| spec-compliance 規則現代化 | `spec-compliance-rules.md:39` 移除「ezSpec」（Java 生態名詞）改 BDDfy/GWT 中性措辭；`:46-47` 驗證等級 L1→L3 跳號，補 L2 或重編號 | 1h；對應 `#AIC-011` |
| EZDDD 對照表定案 | `design-guides/EZDDD-FRAMEWORK-REFERENCE.md` 仍是 30 行 TODO stub。v0.4.0 的 BuildingBlocks 契約已是它想要的答案——改寫為「ezDDD 概念 → 本 repo 契約」對照表，或併入 `BUILDING-BLOCKS-RECONSTRUCTION-CONTRACT.md` 後刪除 | 對照表素材可餵 backlog `CAP-001`（術語表）；對應 `#AIC-015` |
| 安裝流程現代化 | `implementation-guides/quick-setup.md:31-32` 仍教 `cp -r /path/to/ai-plan/.ai`（來源 repo 舊名）。現在有 governed package 了——整段改為正式安裝流程：下載 release 資產 → 解壓 → `repo-structure-sync` | 0.5h；對應 `#AIC-015` |
| Prompt guide 狀態行 | `REQUIREMENT-DESIGNER-PROMPT-GUIDE.md:5`、`SPEC-DESIGNER-PROMPT-GUIDE.md:5` 仍稱「目前它不是正式 skill」，但 skill 已存在於全部 runtime | 10min；對應 `#AIC-014` |

### 3.3 既有 backlog 收尾（納入 v0.5.0 規劃盤點）
| Backlog | 建議處置 |
| --- | --- |
| `GOV-001`（legacy workflow 對帳） | 執行；1.4 的 requirements 收尾若 0.4.1 沒做，併入此項 |
| `VAL-001`（依賴/版本驗證） | 二選一定案：開案實作，或刪除 `check-all.sh:338-340` 的 `check-dependencies.sh` deferred 佔位並在 shell-assets 記 retired——懸置是最差選項 |
| `LANG-001`（翻譯債） | 盤點時納入 v0.4.0 新增的英文 canonical（TECHNOLOGY-SELECTION-POLICY、BUILDING-BLOCKS-RECONSTRUCTION-CONTRACT、migration guide）；`context-translator` sub-agent 已存在，可寫入執行機制 |
| `CAP-001`（術語表） | 可延；若 EZDDD 對照表成案，以其為第一批素材 |
| `TOOL-001` | 由 2.1 吸收並結案 |

---

## 4. 版本目標一覽（快查表）

| 版本 | 必須完成 | 完成後的狀態宣稱 |
| --- | --- | --- |
| **v0.4.1** | 1.1 wrapper 用語 + 驗證規則；1.2 Handler 教義單一化；1.3 時間 API；1.4 快修集（6 項） | 「任何 runtime 的 agent 載入本 context，路由與教義一致且正確」 |
| **v0.4.2** | 2.1 gate 可攜性（含 shell-assets 同步、壞腳本處置）；2.2 治理 CI | 「release 證據可在乾淨環境重現；治理驗證是 PR 門檻而非自律」 |
| **v0.5.0** | 3.1 政策制度化（manifest、全量 baseline、first-parent ADR、命名規則）；3.2 設計項目（OBS-001、ezSpec/L2、EZDDD、安裝流程、prompt guide）；3.3 backlog 收尾（GOV/VAL/LANG 定案） | 「一次性的好行為成為制度；無懸置 backlog」 |

## 5. 追蹤對映

- 本計畫各項的證據與嚴重度全文：`.dev/assessments/ASM-20260717-004/report.md`（finding `#AIC-001`~`#AIC-019`；其中 AIC-009/012 等已由 v0.4.0 修復，本文件不再收錄）。
- 建議把 1.1/1.2 建為 backlog 項（如 `WRAP-001`、`DOCT-001`，格式照 `.dev/backlog/items/TOOL-001.yaml`）後以 `ai-context-governance` 開 remediation workflow 執行；2.x 擴充 `TOOL-001` 後執行；3.x 於 v0.5.0 規劃 workflow 中逐項給 disposition。
