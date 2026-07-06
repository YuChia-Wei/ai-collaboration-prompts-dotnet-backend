# Dev Workflow Skill Guide

本文件說明如何使用 `dev-workflow` 作為開發流程協調 skill，讓 AI Agent 先判斷 direct mode / workflow mode，再決定要把各階段交給哪個 skill 或 sub-agent。

`dev-workflow` 的重點不是自己做架構設計、實作、review 或文件治理，而是把這些工作切成可追蹤的 stage，先對應到通用 capability slot，再透過本 repo 的 capability profile 派給對應 skill。

若沒有對應的下游 skill 或 project standard，`dev-workflow` 只能降級為 fallback-mode：產出最低限度 checklist、handoff prompt 與風險說明。這種輸出不能宣稱與專職 skill 的品質相同。

## 這個 Skill 可以做什麼

適合用在下列工作：

- 判斷一個需求是否需要 workflow mode
- 建立或更新 `.dev/workflows/<workflow-id>/` 下的 workflow plan 與 task JSON
- 規劃 multi-skill handoff，例如 requirement -> spec -> architecture -> implementation -> review
- 判斷每個 stage 屬於哪個 capability slot
- 依 capability profile 找出本 repo 對應的 skill
- 在沒有 profile 對應時，依 skill discovery playbook 檢查可用 skill 並標示 confidence
- 在缺少對應 skill 時切換 fallback-mode
- 設定 validation checkpoint 與 commit checkpoint
- 整理交棒給 sub-agent 或其他 skill 的 source packet
- 在 workflow 結束時回報 validation、commit、尚未決策事項與後續建議
- 在 final response 前執行 workflow closing checklist，確認 commit policy 是否要求 commit；若要求，必須先 commit 才能宣稱完成

## 這個 Skill 不應該做什麼

不應該拿來做：

- 取代 `ddd-ca-hex-architect` 做架構設計
- 取代 `code-reviewer` 做 code review
- 取代 `ai-context-governance` 做 AI context 分類、語言政策或 wrapper sync
- 取代 `repo-structure-sync` 做 repo init
- 取代 `bdd-gwt-test-designer` 做 GWT scenario 與 assertion design
- 直接跳過 requirement / spec / review，只因為已經有 workflow plan
- 在沒有下游 skill 的情況下宣稱已完成同等品質的架構、review、test design 或 implementation 判斷

## 最適合什麼時候用

建議在下列情境使用：

1. 你想讓 AI Agent 自行規劃工作階段與 commit 時機
2. 任務會跨越兩個以上 skill
3. 任務需要 workflow artifacts 保留 decision trail
4. 任務會修改 `.ai/`、`.dev/`、`.agents/`、`.claude/` 或 skill routing
5. 任務需要 sub-agent 或不同模型分工
6. 你想把「開發流程怎麼跑」從單一 skill 中抽出來統一管理

## 三種使用模式

| 模式 | 說明 | 品質邊界 |
| --- | --- | --- |
| Core mode | 只使用 `dev-workflow` 的通用 orchestration 規則 | 可以規劃 stage、handoff、validation，但不保證專業內容品質 |
| Profile mode | 使用本 repo 的 capability profile，把 stage 派給現有 skills | 可以維持目前這種明確 skill 分工品質 |
| Discovery mode | 沒有 profile 對應時，掃描可用 skill metadata 或 wrapper description | 可半自動找出候選 skill，但必須標示 confidence |
| Fallback mode | 找不到對應 skill 或標準時，使用最低限度 checklist | 只能作為臨時風險控管與交棒，不等同專職 skill |

目前本 repo 預設使用 Profile mode。

## Runtime Coordination：Codex Goal 與 Claude Workflow

`dev-workflow` 可以和 runtime 內建的 goal / workflow 功能搭配，但分工不同：

| 層級 | 負責內容 |
| --- | --- |
| Codex Goal | 保存本次 thread 的 durable objective，讓長任務有明確完成條件 |
| Claude workflow / slash command / routine | 作為 Claude runtime 中可重複觸發的流程入口 |
| `dev-workflow` | 定義本 repo/team 的開發流程協調規則、artifact、skill routing、validation 與 commit checkpoint |
| downstream skills | 執行 requirement、spec、architecture、test-design、implementation、review 等專業階段 |

原則是：runtime 負責承載與追蹤，`dev-workflow` 負責流程政策與 skill routing。

### Codex Goal Prompt 範例

在 Codex 中建立 goal 時，可以這樣下：

```text
Goal:
- 完成 <描述目標>。

Use $dev-workflow as the orchestration policy.

Rules:
- Detect the current entry point from existing requirement/spec/workflow artifacts.
- If only raw intent exists, route the first stage to requirements.
- If requirement/spec already exists, continue from the earliest missing capability.
- Create or update .dev/workflows/<workflow-id>/ when workflow mode applies.
- Resolve stages through capability slots, local profile, or skill discovery.
- Use fallback-mode only when no downstream skill or reliable standard exists.
- Commit after coherent validated stages.
- Keep working until the goal is complete or a direction decision is required from me.

Return:
1. current entry point
2. selected stages and owner skills
3. workflow artifacts
4. validation checkpoints
5. commits
6. open decisions
```

### Claude Workflow Prompt 範例

在 Claude workflow、slash command 或 routine 中，可以把 `dev-workflow` 放進 workflow prompt：

```text
Run the team development workflow.

Use $dev-workflow as the orchestration policy for this repository.

Objective:
- <描述目標>

Existing artifacts:
- <requirement/spec/workflow/task paths, if any>

Constraints:
- follow the repo's branch and commit policy
- create workflow artifacts when required
- route stages through capability slots and the active profile
- use skill discovery when no profile mapping exists
- report fallback-mode stages explicitly
- stop only when complete, blocked by a direction decision, or validation fails

Return:
1. direct/workflow mode decision
2. entry point detection
3. stage plan
4. selected skills and discovery confidence
5. workflow artifact paths
6. validation and commit checkpoints
7. open decisions
```

### 已完成前置步驟後再接續

如果你已先使用 `requirement-author` 或 `spec-author`，不要要求 `dev-workflow` 重跑前置階段。改用：

```text
Use $dev-workflow to continue from existing artifacts.

Objective:
- <描述目標>

Completed upstream artifacts:
- requirement: <path>
- spec: <path or none>

Rules:
- Do not redo completed upstream artifacts unless they conflict with current repo evidence.
- Detect the earliest missing capability.
- Continue with architecture, test-design, implementation, review, and validation as needed.
- Create or update workflow artifacts if workflow mode applies.
- Commit after coherent validated stages.
```

## 建議輸出

使用 `dev-workflow` 時，建議要求它輸出：

- workflow mode 判斷
- capability slot 與選用 skill
- skill discovery confidence 與 mapping evidence
- 是否有 stage 使用 fallback-mode
- workflow artifact path
- stage 清單與每個 stage 的 owner skill
- validation checkpoint
- commit checkpoint
- 需要使用者決策的事項

## Workflow 收尾 Checklist

在 workflow mode 的 final response 前，AI Agent 必須確認：

- workflow plan 與 task artifacts 已反映 completed 或 deferred 狀態
- 必要 validation 已通過，或已明確記錄 skipped validation 與原因
- 已檢查 `.dev/standards/GIT-COMMIT-POLICY.md` 是否要求 commit
- 若 commit policy 要求 commit，必須先完成 commit 才能宣稱 workflow completed
- 若沒有 commit，final response 必須引用適用的 policy exception

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
6. inferred skill mappings and confidence
7. fallback-mode stages, if any
```

### 範本 2：只規劃，不先執行

```text
Use $dev-workflow to plan the workflow only.

Goal:
- <描述目標>

Please return:
1. whether this should be direct mode or workflow mode
2. stage breakdown
3. capability slot and skill routing for each stage
4. files likely to change
5. decisions I must make before execution
6. which stages would use discovered skills
7. which stages would fall back if no specialist skill is available
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
| 通用 capability slot 判斷 | `dev-workflow` |
| 本 repo capability profile 維護 | `.ai/assets/skills/dev-workflow/references/capability-profile.md` |
| 可用 skill 自動辨識與 confidence 規則 | `.ai/assets/skills/dev-workflow/references/skill-discovery-playbook.md` |
| 缺少下游 skill 時的最低限度 checklist | `.ai/assets/skills/dev-workflow/references/fallback-playbooks.md` |
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
- portable core 應使用 generic capability slot，不直接綁定本 repo 的 skill 名稱。
- 本 repo 的 skill 對應應放在 capability profile。
- 下游 skill 若要被穩定自動辨識，應宣告 `capability_slots`；沒有宣告時只能推論並標示 confidence。
- fallback playbook 必須明確標示品質限制，不能包裝成專職 skill 結果。
- 若 routing 規則改變，先更新 `.ai/assets/skills/dev-workflow/skill.yaml` 與 references，再同步 wrapper 與 guide。
- 若 workflow artifact 格式改變，應同步檢查 `.dev/standards/WORKFLOW-GATE-POLICY.md` 與 `.dev/standards/GIT-COMMIT-POLICY.md`。
