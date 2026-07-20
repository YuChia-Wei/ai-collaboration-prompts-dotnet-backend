# AI Context Review Report — by Claude Fable 5 (post-v0.4.2)

- 報告產生日:2026-07-20
- 分析對象:`ai-collaboration-prompts-dotnet-backend` @ `main` = `71c41dbd9c4f2b65105a616d15b7f1cc9db2a338`(v0.4.2 tag = `f474c3b`)
- 產生者:Claude Fable 5(獨立審查,非 repo 內 workflow 產物)
- 目標讀者:Codex 工作機上的 AI agent,以及 repo 維護者

## 用途

這份報告的任務是讓工作機 agent:

1. 修復 v0.4.2 發布收尾遺留的損壞狀態(現在 main 上 critical gate 是失敗的);
2. 把本報告發現、但現有 roadmap/backlog 未涵蓋的缺口補進 backlog;
3. 依 `05-process-improvement-plan.md` 安排 release 流程強化與模型換手護欄;
4. (較低優先)在 roadmap 完成後執行 `06-simplification-plan.md` 的減法計畫。

## 檔案索引(建議依序閱讀)

| 檔案 | 內容 | 語言 |
| --- | --- | --- |
| `01-post-v0.4.0-change-review.md` | v0.4.1 / v0.4.2 改了什麼(背景) | EN |
| `02-v0.4.2-incident-timeline.md` | tag 事故完整時間線、證據、根因分析 | EN |
| `03-current-state-findings.md` | 目前 main 上的損壞狀態清單(F1–F7),含重現指令 | EN |
| `04-roadmap-backlog-gap-analysis.md` | 覆蓋度分析 + 建議新增 backlog items 草稿(YAML) | EN |
| `05-process-improvement-plan.md` | 流程強化計畫:runbook、模板、機械 gate、換手 gate | EN |
| `06-simplification-plan.md` | roadmap 完成後的減法/降 token 計畫 | EN |

## 給工作機 agent 的執行指引

- 先讀 `03`,在 repo 內逐條執行 "Reproduce" 指令確認 findings 仍然成立(main 可能已前進)。
- 依 repo 的 `AGENTS.md` 規範作業:hotfix 收尾走 workflow mode、建立專屬 branch、artifacts 放 `.dev/workflows/<id>/`。
- `04` 內的 backlog item YAML 是「草稿提案」,不是寫入授權;依 repo 的 backlog schema 校對後再落檔。
- 所有 findings 的證據都以 commit hash 標註,可用 `git show <hash>` 自行驗證;不要把本報告的敘述當成免驗證的事實。

## 重要結論摘要(TL;DR)

1. v0.4.2 事故的根因不是缺 `GEMINI.md`(接手的 Gemini 有讀到規範:commit 格式完全合規),而是三個規範缺陷:發布程序沒有 runbook、artifacts 靠複製上一版實例而非真模板、關鍵動作(打 tag、收尾)的唯一機械檢查只在 tag push 後於 CI 觸發(事後偵測而非事前阻擋)。
2. 目前 main 上 `validate-workflow-artifacts.py`(critical gate)失敗;v0.4.2 release.yaml 停在 `validated`,會讓下一次 candidate discovery 找到兩個 candidate 而失敗,實質擋住 v0.5.0。
3. 這些收尾/流程缺口不在現有任何 backlog item 範圍內;`04` 提出 R042-005(hotfix)與 REL-001(release automation hardening)、HANDOFF-001(換手 gate)三個新 item。
4. 發布本身是從正確的 commit `f474c3b`(run #5 `29679273269`)產出的;問題在 in-repo registry/evidence 與**已公開的 release body 掛著一個無效的 provenance SHA** `1c13d7966b93...`(非真實 git 物件)。真實 run 資料已確認並寫進 `03`/`04`,hotfix 不需再查。
