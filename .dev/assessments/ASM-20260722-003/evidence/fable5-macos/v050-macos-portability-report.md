# v0.5.0 macOS Portability 驗證報告

- 產生日:2026-07-22 ・ 產生者:Claude Fable 5(獨立 macOS 檢閱機,非開發機)
- 受測 commit:`9ac40bee4ab3d4ac169c05c6229895d7a22265ff`(當時的 `origin/main`,= PR #4 merge)
- 受測方式:`git worktree` 乾淨 checkout(detached at 9ac40be),與開發工作樹完全隔離,全程未修改 repo 任何檔案
- 對應缺口:`v050-tool001-val001-portability.md` 明列「macOS was not executed and remains explicitly unverified」;ASM-20260722-001#AIC-004 accepted residual

## TL;DR

- **macOS quick gate 與 critical gate 均 33/33 全綠(exit 0)**,與 Windows Git Bash / hosted Ubuntu 同一 entrypoint、同一 gate 集合。macOS(原生 bash 3.2.57)可正式從「unverified」改列「verified」。
- **但發現一個真實的 harness bug**:當按照 check-all.sh 自己的錯誤指引設定 `AI_CONTEXT_PYTHON` 時,quick gate 出現 1 項 required 失敗(`test_fail_closed_validation.py` 8 個 GWT 案例)。原因是 fixture 子行程未清除 `AI_CONTEXT_PYTHON`,環境變數洩入 fixture、繞過 `bin/python` stub。**這與 a1c32f1「supply Git Bash child environment」是同一族 bug,且 macOS 正是最容易踩到的平台。**
- `validate-ai-context-release-state.py --phase candidate --version v0.5.0` 在 macOS 通過(9ac40be on main);兩個 fail-closed 防護(detached HEAD 需 `--branch`、髒工作樹拒絕)行為正確。

## 1. 測試環境

| 項目 | 本機(macOS) | Windows 證據 | Ubuntu 證據 |
| --- | --- | --- | --- |
| OS | macOS 26.5.1 (arm64) | Windows Git Bash 5.3.9 | ubuntu-latest |
| bash | **3.2.57**(系統原生,/bin/bash) | 5.3.9 | 5.x |
| Python | 3.14.4(Homebrew)+ PyYAML 6.0.3(=requirements.txt pin) | 3.13.14 | 3.12.13 |
| .NET SDK | **10.0.302**(dotnet-install.sh 本地安裝,未動系統) | 10.0.302 | 10.0.302 |

環境前置注意(給文件/migration guide):

- 本機原有 SDK 10.0.203 會被 `global.json`(`10.0.300` + `rollForward: latestMajor`)拒絕,`dotnet` 直接無法執行。**SDK ≥ 10.0.300 是硬前置**,建議在 runbook 或 README 明列。
- 原生 macOS 沒有名為 `python` 的執行檔、`python3` 是 3.9.6(過舊)。`resolve_python()` 只嘗試 `python`/`python3`,因此 stock macOS 一定落入「請設 `AI_CONTEXT_PYTHON`」的指引——而這正好觸發下述 bug。

## 2. 測試矩陣與結果

| # | 命令 | 環境條件 | 結果 |
| --- | --- | --- | --- |
| A | `bash .ai/scripts/check-all.sh --quick` | `AI_CONTEXT_PYTHON=<venv python>`(照錯誤訊息指引) | **exit 1**;33 執行 / 32 過 / **1 required 失敗**(Aggregate Runner And Shell Registry Fail-Closed Tests,8 案例) |
| B | `bash .ai/scripts/check-all.sh --quick` | PATH 上提供 `python`(≥3.11),未設 `AI_CONTEXT_PYTHON` | **exit 0;33/33 全綠**,0 warning / 0 deferred / 2 not applicable |
| C | `bash .ai/scripts/check-all.sh --critical` | 同 B | **exit 0;33/33 全綠**(含三個 dotnet test 專案 49+2+5 案例全過) |
| D | `validate-ai-context-release-state.py --phase candidate --version v0.5.0 --branch main` | 乾淨 worktree | **exit 0**:「validation passed for v0.5.0 candidate phase at 9ac40be...on main」 |
| D' | 同 D,但 detached HEAD 未給 `--branch` / 或髒工作樹 | — | 均 fail-closed,訊息明確(設計內行為,非缺陷) |

執行時間:quick 約 2 分 10 秒、critical 約 2 分(乾淨 checkout、含 NuGet restore)。

結論:**Run B/C 與 Windows/Ubuntu 證據完全同構(同 entrypoint、同 gate 宣告、同 SDK 版本),macOS 一欄可回填為 verified。**Run A 的失敗不是 macOS 平台問題,而是測試 harness 的環境洩漏缺陷,見下節。

## 3. Bug 報告:`AI_CONTEXT_PYTHON` 洩入 fixture 子行程

**位置**:`.ai/scripts/tests/test_fail_closed_validation.py` → `SyntheticRunnerRepo.execute()`

**機制**:

1. `check-all.sh` 的 `resolve_python()` 給予 `AI_CONTEXT_PYTHON` 絕對優先權(高於 PATH 查找)。
2. `SyntheticRunnerRepo` 的設計是把 `bin/python` stub 前置到 PATH,攔截 fixture 內所有 `python ...` 宣告。
3. `execute()` 以 `dict(os.environ)` 繼承父環境,只 pop 了 `SPEC_FILE`、`TASK_NAME`、`COMMIT_RANGE`、`WORKFLOW_ID`——**沒有 pop `AI_CONTEXT_PYTHON`**。
4. 因此外層若設了 `AI_CONTEXT_PYTHON`,fixture 內的 check-all.sh 會用真實直譯器執行 fixture 中不存在的測試檔(`can't open file '.../aic007-check-all-*/.ai/scripts/tests/test_profile_projection_contract.py'`),8 個 GWT 案例(gwt_005/006/007a/008/009×2/010/012)以 returncode 斷言失敗。

**為何 Windows/Ubuntu 沒踩到**:兩者 PATH 上都有 `python` ≥3.11,不需要設 `AI_CONTEXT_PYTHON`。macOS 是唯一「照文件走就必須設這個變數」的已支援平台,所以這個洩漏專門打擊 macOS 的合規路徑——使用者按照 check-all.sh 自己印的指引操作,反而得到一個 required 失敗。

**建議修法**(擇一或並用):

1. `execute()` 的 pop 清單加入 `AI_CONTEXT_PYTHON`(最小修改,與 a1c32f1 同族處理)。
2. 加一個 GWT 負向案例:「given 外層 `AI_CONTEXT_PYTHON` 已設,when fixture 執行,then stub 仍被選中」——把這個環境隔離契約本身納入 fail-closed 保護。
3. (可選)`resolve_python()` 的候選清單納入 `python3.11`~`python3.14` 具名執行檔,降低 macOS 對 `AI_CONTEXT_PYTHON` 的依賴。

**嚴重度評估**:不擋 v0.5.0 打 tag——工作機(Windows)與 hosted gate 不受影響,macOS 在正確環境下也全綠。但它是「文件指引路徑必然失敗」的缺陷,建議進 backlog 當 v0.5.x/v0.6.0 的 portability 項目,和 REL-002 的 pre-tag 系列放同一族。

## 4. 現況核對(給工作機的狀態確認)

- v0.5.0 開發 workflow 已關閉並經 PR #1 併入 main;之後三個 pre-tag portability PR(#2/#3/#4)也已併入。
- `release.yaml`:`status: validated`、`tag/commit/tagged_at/recorded_at` 皆為 null——**符合設計**(publish-mode 前必須留空)。
- **v0.4.2 已列入 `automatic_upgrade_sources`(v0.3.0/v0.4.0/v0.4.1/v0.4.2 四來源)——先前「v0.4.2 被靜默遺漏」的缺口已修復。**
- Runbook `AI-CONTEXT-RELEASE-PUBLICATION-RUNBOOK.MD` 已含「Current-Main Command Invalidation」規則:任何 pre-tag 成功後的 main 合併都會使先前印出的 tag command 過期,**打 tag 前必須在當前 clean main 重跑 `prepare-ai-context-release.py --version v0.5.0` 並只用該次輸出**。
- 本機為檢閱者角色,未執行 `prepare-ai-context-release.py`(其輸出為 owner 專用 tag command,且跨機重用違反 invalidation 規則)。

## 5. 建議回填的證據欄位

若工作機要把本結果併入 portability 證據(或後續 assessment):

- Platform: macOS 26.5.1 arm64, native bash 3.2.57, Python 3.14.4 + PyYAML 6.0.3, .NET SDK 10.0.302
- Subject commit: `9ac40bee4ab3d4ac169c05c6229895d7a22265ff`(clean worktree checkout)
- Command: `bash .ai/scripts/check-all.sh --quick` / `--critical`
- Result: 均 exit 0;33 required selected / 33 executed / 33 passed / 0 failed / 0 warnings / 0 deferred / 2 not applicable
- Completed: 2026-07-22T03:25:28Z(quick)/ 2026-07-22T03:31 前後(critical)
- 附註殘留:AI_CONTEXT_PYTHON 環境洩漏 bug(見第 3 節),不影響上列綠燈條件,但需列為已知缺陷與後續修復項。
