# dev-workflow Skill 比較報告

- 報告日期：2026-07-22
- 比較對象：
  - A 版：本 repo（WorkService）`.ai/assets/skills/dev-workflow/`
  - B 版：`~/gitproj/ai-collaboration-prompts-dotnet-backend` `.ai/assets/skills/dev-workflow/`
- 分析方式：直接完整閱讀兩邊 skill.yaml、全部 references 與 templates（未調用任何 skill），並抽查本 repo `.dev/workflows/` 實際落地的 artifact 作為實證。
- 關聯報告：`2026-07-09-ai-context-quality-review.md`（AI context 整體品質評估）

---

## 1. 執行摘要

兩者是同一族系（canonical `.ai/assets/skills/` + thin wrapper 架構），但屬於不同世代：

| | A 版（WorkService） | B 版（ai-collaboration-prompts） |
|---|---|---|
| 定位 | repo 專屬「工序指揮（監造）」 | 可攜的通用開發生命週期協調器 |
| 規模 | 9 檔 / 約 514 行 | 15 檔 / 約 953 行（template 有版本號 1.0.0→1.2.0） |
| 啟動 | 僅限使用者明確呼叫 | trigger phrases + gate policy 主動判定 |
| 模式 | direct / workflow 兩種 | direct / assessment / workflow 三種 |
| 路由 | 兩條寫死流程 + 具名 skill | capability slot → profile → discovery → fallback 四層抽象 |
| 治理 | 敘述性 guide（`.dev/guides/`） | 政策文件（`.dev/standards/` 六份 policy） |
| 強制力 | 單點紀律（issue 追蹤、Gating 問點） | 制度性硬閘（branch 政策、closing checklist、gate policy） |

B 版可視為 A 版的演進重寫：把「repo 綁定的固定流程」抽象成「可攜核心 + 本地 profile」，並把約束從「參考文件裡的敘述」升級為「artifact 欄位 + 檢核清單」層級的結構性強制。

本報告同時針對本 repo 實際發生的三個問題做根因分析（見第 5 節）：

1. 使用 dev-workflow 時任務分層不明確
2. skill 交接時未正確 commit，事後需額外花 token 整理
3. 曾發生完全沒有 `.dev/workflows/` 資料夾產出的狀況（乾淨環境、非 memory 汙染）

結論先講：**這三個問題都能從 A 版 skill 文本設計直接推導出來，不是執行環境或個人操作的偶發問題。**

---

## 2. 流程強制力比較

| 面向 | A 版（WorkService） | B 版（ai-collaboration-prompts) |
|---|---|---|
| 啟動條件 | 僅限使用者明確呼叫（"never self-apply on a plain prompt"），決定權完全交還使用者 | trigger phrases 觸發，且 `WORKFLOW-GATE-POLICY.md` 有「Must Create a Workflow」清單（≥2 stages、跨 skill 交接、改 source-of-truth、動到 ≥5 檔、使用者用「規劃／整理／重構／治理」等字眼）— agent 必須主動判定進 workflow mode |
| 模式數 | 2 種：direct / workflow | 3 種：direct / assessment（唯讀稽核，產出放 `.dev/assessments/`，不授權修復）/ workflow |
| 分支紀律 | 無任何分支要求，在當前 branch 作業 | 硬性：禁止在 main 上建 workflow；必須先開 `codex/<workflow-id>` 專用 branch；checkpoint merge/push ≠ 完成；merge 預設 `--no-ff`；plan 內含 Branch Lifecycle 追蹤表 |
| 收尾把關 | Step 4「收斂回報」— 敘述性要求 | Workflow Closing Checklist（硬閘）：final response 前必須逐項驗證 artifact 狀態、驗證是否通過、commit policy 是否要求 commit、未 commit 需引用確切政策例外、不得因 branch 已 merge 就視為完成 |
| 問使用者的規則 | 明確列出 6 個 Gating 點（mode 判不準、無 issue number、template 差異過大、scope expansion、高影響決策等），其餘一路不停 | 「只在無法從 repo 證據或既有政策安全推斷時才問」— 更自主，但缺具體列舉 |
| Issue 追蹤 | 強制：workflow id 必含 `issueNo`；沒有編號要先問，經同意才能用 `no-issue`；後續拿到編號要 rename + 同步 metadata | 無 issue 要求：id 格式 `YYYY-MM-DD-topic[-NN]`（此點 A 版較嚴，符合銀行環境可追溯需求） |
| Commit 紀律 | 每個驗證過的 bounded slice 先 commit 再進下一個；禁止巨型 commit；依 `COMMIT-CONVENTIONS.md` | 依 `GIT-COMMIT-POLICY.md`；stage 完成 + 驗證通過後 commit；closing checklist 會回頭查核是否照辦 |

小結：B 版的「制度性強制力」壓倒性地高（gate policy、branch 政策、closing checklist 都是可查核的閘）；A 版強的是「單點紀律」（issue 追蹤與 Gating 問點比 B 版嚴格）。

---

## 3. 做事方式（架構思路）比較

| 面向 | A 版 | B 版 |
|---|---|---|
| 角色定位 | 「工序指揮／監造」，絕不親自做設計、實作、review 判斷；連 `workflow-plan.md` 的 owner 都是 `ddd-ca-hex-architect`，dev-workflow 不填領域內容 | 同樣禁止取代下游 skill，但 plan / locator 的 `owner_skill` 是 dev-workflow 自己 — 它擁有流程 artifact，只把領域工作外包 |
| 路由方式 | 寫死兩條主流程 + 具名 skill 清單（requirement-author → spec-author → architect → test-designer → `*-use-case-implementer` → code-reviewer → spec-compliance-validator） | 四層抽象：stage → 10 個 generic capability slot → `capability-profile.yaml`（機讀映射）→ 無 profile 時走 skill discovery（信心分級 high/medium/low/none，low 要問使用者）→ 都沒有時走 per-capability fallback playbook（最小 checklist，明文「不得聲稱與專家 skill 同品質」） |
| 治理文件位置 | 引 `.dev/guides/ai-collaboration-guides/` 的敘述性 guide | 治理外移到 `.dev/standards/`（WORKFLOW-GATE / WORKFLOW-ARTIFACT / GIT-COMMIT / TEAM-GIT-FLOW / WORKFLOW-HANDOFF / ASSESSMENT-ARTIFACT 六份 policy）— 政策與 skill 分離 |
| 可攜性 | repo-specific（流程直接寫本 repo 的 skill 名） | 明確設計為 repo-portable：`portability` / `schema_version` 欄位；repo 專屬名稱只准放 profile，核心保持可發佈 |
| 範圍邊界 | 無明確排除 | 明文排除 AI context audit / context governance / docs-only cleanup / repo init — 路由給各自 owning skill |
| 輸出格式 | 無固定格式 | `output-contract.md` 定義 Planning / Stage Handoff / Final 三種固定輸出區塊，Final 必附 validation evidence 與 commits |
| Runtime 整合 | 無 | `runtime-coordination.md`：Codex Goal / Claude workflow prompt patterns、四層分層模型、entry-point detection 表（有 spec 就不必從 requirements 重跑） |
| 語言 | 參考檔為繁體中文 | 全英文 |

---

## 4. Task 與 Commit 做法差異（重點深掘）

這一節是兩版差異最大、也直接對應本 repo 實際痛點的部分。

### 4.1 Task 的建立時機與擁有權

| | A 版 | B 版 |
|---|---|---|
| 誰建立 task | `*-implementer` 角色 skill（artifact-ownership.md：task 擁有者是 implementer）；dev-workflow 只「叫對的 skill 去建」 | dev-workflow 自己在 Step 3 一次建立（"create or update development workflow artifacts from this skill's templates"） |
| 建立時機 | 「需要時」（OPTIONAL-MINIMAL-WORKFLOW-MODE 的用語是「需要時建立」）— 惰性、由各角色 skill 自行判斷 | 進入 workflow mode 後、開始任何 stage 之前 — 前置、由指揮者統一 scaffold |
| 流程覆蓋 | **流程 1（需求驅動開發）的 7 個步驟完全沒提到 `tasks/*.json` 由誰、何時建立**；只有流程 2（重構驅動）第 3 步提到。task template 的預設 `owner_skill` 也寫死為 `staged-refactor-implementer`，明顯偏向重構流程 | 每個 stage 在 plan 中就有 `stage_id` / `capability slot` / `owner skill` / `validation` / `commit checkpoint` 欄位，task JSON 與 stage 一一對應，不分流程種類 |

### 4.2 Task JSON 欄位對照

| 欄位群 | A 版 `workflow-task-template.json` | B 版 `development-workflow-task-template.json` |
|---|---|---|
| 狀態 | `status: "draft"` 起手；**無狀態機定義**（沒有規定何時翻 in_progress／completed） | `pending → in_progress → completed` 狀態機 + 轉移規則：動工前必須翻 `in_progress`、產出存在且窄域驗證通過才准翻 `completed`、跳過驗證必須記錄原因、`deferred` 需說明理由 |
| 時間 | `timeline` 區塊完整：`created_at` / `started_at` / `completed_at` / `last_validated_at` / `updated_at` / `timezone`，且明文「不得只靠 git commit time 或檔案時間」（A 版優勢） | 只有 `created_at` / `updated_at`（ISO-8601 含時區偏移） |
| Commit | **完全沒有任何 commit 相關欄位**。`results` 只有 `summary` / `files_changed` / `tests_run` / `follow_up_needed` | `execution.commit_checkpoint`（事前宣告何時 commit）+ `results.commits`（事後回填 commit 證據）+ `results.validation_evidence` |
| 授權與依據 | 無 | implementation 類 task 必填 `implementation_contract`：`intent` / 單一 `execution_mode`（command/query/reactor/generic）/ `overlays` / `authorization_source` / `normative_truth` / `finding_evidence` / `subject_revision`（40 字 Git SHA）/ `acceptance_criteria` — 把「誰授權、依據什麼真相、修哪個 finding、驗收標準」硬性分離 |
| 追溯 | `issue_tracking` 區塊（user_story / implementation_task / related_issue）（A 版優勢） | 無 issue 欄位，但有 `template_source` / `template_version` / `workflow_locator` |

### 4.3 Commit 紀律的落點差異

A 版的 commit 紀律只存在於**敘述層**：

- skill.yaml constraint："Keep commit discipline: commit each verified bounded slice before the next"
- orchestration-playbook Step 3：「每個已完成且有最小驗證的 bounded slice 先 commit 再進下一個 slice」

沒有任何 artifact 欄位承載它、沒有收尾檢核查核它。模型讀過就算數，忘了也不會有任何結構性訊號提醒。

B 版的 commit 紀律存在於**四個互相勾稽的層**：

1. **Plan 層**：每個 stage 有 `Commit checkpoint:` 欄位（事前規劃）
2. **Task 層**：`execution.commit_checkpoint` + `results.commits`（事前宣告 + 事後回填）
3. **政策層**：`GIT-COMMIT-POLICY.md` + `TEAM-GIT-FLOW-RULES.MD`（checkpoint merge/push 語意、`--no-ff`、continuation branch）
4. **收尾層**：Workflow Closing Checklist 硬性要求 — 送出 final response 前必須確認「commit policy 是否要求 commit；要求則 commit 必須已存在；沒 commit 必須引用確切的政策例外條款」

另外還有一個時序性差異：B 版要求**先開專用 branch 才能建 artifact**（gate policy：不得在 main 上建 workflow），commit 行為從一開始就被框在 branch 生命週期裡；A 版無 branch 概念，commit 散落在當前 branch 上。

### 4.4 本 repo 實際落地狀況（實證）

抽查 `.dev/workflows/20260706-1809607-logic-use-case-bdd-test-coverage/tasks/*.json`（最近一次正式 workflow，2026-07-06）：

- 3 個 task 皆 `status: completed`，timeline 填寫完整（含 timezone）— A 版 timeline 設計有被遵守
- `results` 只有 `summary` / `files_changed` / `tests_run` / `follow_up_needed` — **無任何 commit 記錄**（因為欄位根本不存在）
- 另發現 reference 與 template 自相矛盾：`artifact-ownership.md` 要求 `results` 回填 `deferred_items_actual` / `scope_expansion_actual`，但 template 沒有這兩個欄位 — 實際 task 也確實都沒填

另外 `.dev/workflows/` 下 30 個項目中，只有 6 個符合 `<yyyyMMdd>-<issueNo>-<goal>` 命名規範，其餘為舊格式（`customer-folder-gwt-refactor` 等）或散檔（`auth-http-only-cookie-migration-plan.html`）— 顯示規範是後來才加上、且未回補整理。

---

## 5. 觀察到的三個實際問題：根因分析

### 問題 1：任務分層不明確

**根因：A 版把 task 建立設計成「惰性 + 分散擁有權」，且需求驅動流程根本沒有 task 步驟。**

- 流程 1（需求驅動開發，本 repo 日常開發的主流程）的步驟清單完全沒提 `tasks/*.json`；task template 預設 owner 是 `staged-refactor-implementer`（重構流程的 skill）。走需求驅動流程時，沒有任何指令告訴任何 skill「去建 task」。
- artifact 由各角色 skill「需要時建立」— 每個 skill 都可以合理判斷「不需要」，結果就是沒有分層。
- 對照 B 版：dev-workflow 進入 workflow mode 的第一件事就是自己 scaffold plan + tasks，每個 stage 有 `stage_id` / `capability slot` / `owner skill`，分層是結構的副產品，不是各 skill 的善意。

### 問題 2：skill 交接時未正確 commit，事後需額外花 token 整理

**根因：commit 紀律只寫在敘述層，artifact 無承載欄位、收尾無檢核，且本 repo 的驗證前提在本機不成立。**

- Task JSON 沒有 `commit_checkpoint` 也沒有 `results.commits` — commit 從未被要求記錄，自然不會被檢查。
- 沒有 closing checklist — 收尾時沒有任何步驟強迫回答「該 commit 的都 commit 了嗎」。
- 加重因素（本 repo 特有）：A 版 commit 規則綁定「已完成**且有最小驗證**的 bounded slice」，但本機因內部 NuGet 無法編譯、無法跑測試（見 memory：dotnet build/test 一律 deferred）。「驗證」永遠不成立 → commit 的前置條件永遠掛起 → 模型自然把 commit 全部往後推 → 最後累積成一次大整理，還要額外花 token 讓 AI 分類。B 版的設計（「跳過驗證需明確記錄原因」+ checkpoint commit 照常執行）正好處理了這種驗證不可得的情境。

### 問題 3：完全沒有 workflows 資料夾出現（乾淨環境）

**根因：A 版的觸發鏈每一環都是軟的，任何一環斷掉就整個不會發生。**

觸發鏈是：使用者明確呼叫 → agent 判 mode → 判成 workflow mode → scaffold。四個環節逐一檢視：

1. **明確呼叫**：skill 明文 "Run only when the user explicitly invokes this skill"、wrapper 描述 "Invoke ONLY when the user explicitly asks"。同仁若用自然語言描述任務而沒有點名 dev-workflow，skill 從頭到尾不會啟動 — 這與環境乾不乾淨、有沒有 memory 無關，是設計如此。
2. **mode 判定**：A 版的 direct/workflow 分界是敘述性舉例（「單次 review、局部抽方法…」），沒有 B 版那種可操作的硬性判準（≥2 stages、≥5 檔、關鍵字清單）。跨 skill 的任務被判成 direct mode 完全在裁量空間內，而 direct mode 明文「不建 artifact」。
3. **入口文件未接力**：repo 入口 `agents.md` 的 Mandatory Workflows 沒有把「開發任務必走 dev-workflow」列為強制（且其引用的 checklist 檔案不存在，見 2026-07-09 報告 S1 findings）— 入口層也不會把人導進來。
4. **OPTIONAL 的心智定位**：整套 mode 規範的檔名就叫 `OPTIONAL-MINIMAL-WORKFLOW-MODE.md`，開宗明義「這些 skill 預設都應該可以直接使用」。整個系統的預設值是「不建 workflow」，建 workflow 才是例外。

換言之：**「沒有 workflows 資料夾」不是異常行為，而是 A 版設計下的預設路徑。** B 版把預設值反過來了：gate policy 是「命中清單就必須建」，且建之前還必須先開 branch — 想跳過反而需要理由。

---

## 6. 改善建議

依「解決上述三個問題的直接程度」排序。原則：不需要整套照搬 B 版，把「敘述性紀律」升級為「結構性欄位 + 收尾檢核」即可解決大部分問題。

### P0（直接對應現況痛點，皆為小改動）

1. **task template 加入 commit 欄位**：`execution.commit_checkpoint` + `results.commits[]`。同步修正 template 與 `artifact-ownership.md` 的欄位不一致（`deferred_items_actual` / `scope_expansion_actual`）。
2. **加入 Workflow Closing Checklist**：收斂（Step 4）從「回報」改為硬性逐項查核 — artifact 回填了嗎、該 commit 的 commit 了嗎、沒 commit 引用哪條例外。可直接參考 B 版 `WORKFLOW-GATE-POLICY.md` 第 107-117 行。
3. **流程 1 補上 task 步驟**：需求驅動流程明定「進入 workflow mode 時由 dev-workflow 一次 scaffold 全部 stage 的 `tasks/<stage-id>-<descriptor>.json`」，task template 的 `owner_skill` 改為佔位符而非寫死 `staged-refactor-implementer`。
4. **處理「驗證不可得」情境**：commit 規則加一條 — 本機無法執行驗證時，記錄 `validation: deferred（原因）` 後照常 commit，不得以驗證未完成為由延後 commit。這條直接化解本 repo 內部 NuGet 限制造成的 commit 堆積。

### P1（提升觸發可靠性）

5. **建立明確的 workflow gate**：參考 B 版「Must Create a Workflow」清單，給出可操作判準（≥2 skill 接力、≥N 檔、改 source-of-truth 等）。是否保留「僅限明確呼叫」是治理決定：若保留，至少在 `agents.md` 的 Mandatory Workflows 明定「符合清單的開發任務必須呼叫 dev-workflow」，把觸發責任從個人習慣移到入口文件。
6. **引入 assessment mode**：本 repo 已多次實際發生稽核類工作（本報告即是），但現行只有 direct/workflow 兩分法，無對應軌道。

### P2（結構強化）

7. **template versioning**：artifact 記錄 `template_source` / `template_version`，解決 template 漂移時的判斷成本。
8. **`.dev/workflows/` 命名回補**：30 個項目僅 6 個符合現行命名規範；至少在 README 標註舊格式為 legacy，避免 AI 讀取時把舊格式當慣例學走。
9. **視團隊 git flow 決定是否採納 branch 紀律**（專用 workflow branch、checkpoint 語意）。

### 保留的 A 版優勢（B 版反而該學的）

- `issueNo` 強制進 workflow id（可追溯性）
- `timeline` 區塊含 `timezone` / `last_validated_at`（實證顯示有被確實遵守）
- 較完整的 review report template（五維評分、分層 findings、下一 skill 建議表）
- 明確列舉的 Gating 問點清單

---

## 附錄：兩版檔案清單

**A 版（WorkService）** — 9 檔約 514 行：

```text
.ai/assets/skills/dev-workflow/
  skill.yaml                                    (57)
  references/orchestration-playbook.md          (138)
  references/artifact-ownership.md              (58)
  assets/templates/workflow-plan-template.md    (63)
  assets/templates/review-report-template.md    (101)
  assets/templates/workflow-task-template.json  (45)
.claude/skills/dev-workflow/SKILL.md            (24)
.agents/skills/dev-workflow/SKILL.md            (24)
.agents/skills/dev-workflow/agents/openai.yaml  (4)
```

**B 版（ai-collaboration-prompts-dotnet-backend）** — 15 檔約 953 行：

```text
.ai/assets/skills/dev-workflow/
  skill.yaml                                              (99)
  references/routing-playbook.md                          (83)
  references/skill-discovery-playbook.md                  (93)
  references/capability-profile.md                        (45)
  references/capability-profile.yaml                      (16)
  references/fallback-playbooks.md                        (94)
  references/runtime-coordination.md                      (98)
  references/workflow-artifact-playbook.md                (96)
  references/output-contract.md                           (66)
  templates/workflow-locator-template.yaml                (21)
  templates/development-workflow-plan-template.md         (82)
  templates/development-workflow-task-template.json       (43)
  templates/development-review-report-template.md         (49)
.claude/skills/dev-workflow/SKILL.md                      (34)
.agents/skills/dev-workflow/SKILL.md                      (34)
```

B 版另引用 `.dev/standards/` 政策：WORKFLOW-GATE-POLICY (117)、WORKFLOW-ARTIFACT-POLICY (140)、GIT-COMMIT-POLICY (222)、TEAM-GIT-FLOW-RULES (157)，以及 WORKFLOW-HANDOFF-POLICY、ASSESSMENT-ARTIFACT-POLICY。
