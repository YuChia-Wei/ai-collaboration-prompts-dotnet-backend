# Dev Workflow Skill Guide

本文件說明如何使用 `dev-workflow` 作為開發流程協調 skill，讓 AI Agent 先判斷 direct mode / workflow mode，再決定要把各階段交給哪個 skill 或 sub-agent。

`dev-workflow` 的重點不是自己做架構設計、實作、review 或文件治理，而是把這些工作切成可追蹤的 stage，並在正確時機派給對應 skill。

## 這個 Skill 可以做什麼

適合用在下列工作：

- 判斷一個需求是否需要 workflow mode
- 建立或更新 `.dev/workflows/<workflow-id>/` 下的 workflow plan 與 task JSON
- 規劃 multi-skill handoff，例如 requirement -> spec -> architecture -> implementation -> review
- 判斷每個 stage 應該使用哪個 skill
- 設定 validation checkpoint 與 commit checkpoint
- 整理交棒給 sub-agent 或其他 skill 的 source packet
- 在 workflow 結束時回報 validation、commit、尚未決策事項與後續建議

## 這個 Skill 不應該做什麼

不應該拿來做：

- 取代 `ddd-ca-hex-architect` 做架構設計
- 取代 `code-reviewer` 做 code review
- 取代 `ai-context-governance` 做 AI context 分類、語言政策或 wrapper sync
- 取代 `repo-structure-sync` 做 repo init
- 取代 `bdd-gwt-test-designer` 做 GWT scenario 與 assertion design
- 直接跳過 requirement / spec / review，只因為已經有 workflow plan

## 最適合什麼時候用

建議在下列情境使用：

1. 你想讓 AI Agent 自行規劃工作階段與 commit 時機
2. 任務會跨越兩個以上 skill
3. 任務需要 workflow artifacts 保留 decision trail
4. 任務會修改 `.ai/`、`.dev/`、`.agents/`、`.claude/` 或 skill routing
5. 任務需要 sub-agent 或不同模型分工
6. 你想把「開發流程怎麼跑」從單一 skill 中抽出來統一管理

## 建議輸出

使用 `dev-workflow` 時，建議要求它輸出：

- workflow mode 判斷
- 選用 skill 與理由
- workflow artifact path
- stage 清單與每個 stage 的 owner skill
- validation checkpoint
- commit checkpoint
- 需要使用者決策的事項

## 怎麼下 Prompt

### 範本 1：讓 AI 建立並執行 workflow

```text
Use $dev-workflow to plan and execute this work.

Goal:
- <描述目標>

Constraints:
- create a branch first
- create workflow artifacts when required
- route each stage to the right skill
- commit after coherent validated stages
- ask me only when a direction decision is required

Return:
1. workflow mode decision
2. selected skills
3. workflow artifacts
4. current stage status
5. validation and commits
```

### 範本 2：只規劃，不先執行

```text
Use $dev-workflow to plan the workflow only.

Goal:
- <描述目標>

Please return:
1. whether this should be direct mode or workflow mode
2. stage breakdown
3. skill routing for each stage
4. files likely to change
5. decisions I must make before execution
```

### 範本 3：整理既有 workflow 狀態

```text
Use $dev-workflow to inspect the current workflow state.

Check:
- current branch
- git status
- .dev/workflows/<workflow-id>/workflow-plan.md
- task JSON status
- validation gaps
- whether the next step is execution, review, commit, or user decision
```

## 與其他 Skill 的關係

| 情境 | 由誰負責 |
| --- | --- |
| 決定 direct mode / workflow mode | `dev-workflow` |
| 建立 workflow plan 與 task JSON | `dev-workflow` |
| AI context、語言政策、wrapper sync | `ai-context-governance` |
| repo init / template adaptation | `repo-structure-sync` |
| requirement 草稿與正規化 | `requirement-author` |
| spec 草稿與正規化 | `spec-author` |
| architecture direction | `ddd-ca-hex-architect` |
| GWT scenario / assertion design | `bdd-gwt-test-designer` |
| bounded implementation | 對應的 implementer skill |
| code review | `code-reviewer` |
| problem-frame compliance gate | `spec-compliance-validator` |

## 維護原則

- `dev-workflow` 只放流程協調規則。
- domain skill 的專業規則不要複製進 `dev-workflow`。
- 若 routing 規則改變，先更新 `.ai/assets/skills/dev-workflow/skill.yaml` 與 references，再同步 wrapper 與 guide。
- 若 workflow artifact 格式改變，應同步檢查 `.dev/standards/WORKFLOW-GATE-POLICY.md` 與 `.dev/standards/GIT-COMMIT-POLICY.md`。
