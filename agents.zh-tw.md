# AGENTS.md

[English](agents.md)

## 適用範圍與優先順序

- 本文件是 AI agents 與人類在此 repository 中協作時的根目錄指南。
- 這個 repository 是 AI 協作知識庫與可重用 context framework，不是產品應用程式 repository。
- 如果子目錄有其他 `AGENTS.*` 檔案，較深層的檔案優先。
- 指令優先順序：User/Approval > Subfolder AGENTS > This file > Other general documents。
- 若有設定 IDE 的 MCP Server，且該 MCP Server 提供重構功能，優先使用 IDE MCP Server 的重構能力。

## Repository 定位

這個 repository 的用途是：

- 萃取軟體工程、架構、.NET backend 與 AI 協作知識；
- 維護可重用的 AI Agent context、skills、sub-agent prompts 與 workflow rules；
- 區分通用 AI context 與技術棧專用 context；
- 保留目前的非通用能力：.NET C# backend Web API 開發；
- 移除、隔離或 template 化歷史來源專案資訊。

除非檔案明確標示為 template、migration artifact 或 dotnet-backend reference，否則不要把歷史 sample backend 資訊視為目前產品真相。

## AI Agents 快速開始

1. 閱讀 `README.md` 或 `README.en.md` 以理解本 repo 的用途。
2. 在移動或重寫 AI context 前，先閱讀 `.dev/standards/AI-CONTEXT-BOUNDARY.md` 與 `.dev/standards/AI-CONTEXT-LANGUAGE-POLICY.md`。
3. 使用 `.ai/assets/skills/README.MD` 作為 canonical skill registry。
4. 使用 `.dev/guides/ai-collaboration-guides/README.MD` 查閱 human-facing skill 與 workflow guides。
5. 使用 `.ai/INDEX.MD` 與 `.ai/README.MD` 瀏覽 agent-facing AI assets。

## 必要工作流程

### Workflow Gate

1. 當工作可能影響 source-of-truth、AI context、skill routing、wrapper sync，或跨越多個階段時，閱讀 `.dev/standards/WORKFLOW-GATE-POLICY.md`。
2. 當 gate 要求 workflow mode 時，主動建立 workflow artifacts。
3. 小型、局部、單次可完成的變更可維持 direct mode。

Workflow artifact 位置：

- 使用 `.dev/workflows/<workflow-id>/workflow-plan.md`
- 若有 review output，使用 `.dev/workflows/<workflow-id>/review-report.md`
- 使用 `.dev/workflows/<workflow-id>/tasks/<task-id>.json` 追蹤 task
- 除非使用者明確要求，不要把 workflow artifacts 分散到 `.ai/`、`.agents/skills/`、`.claude/skills/` 或任意資料夾。

### Git Commit Policy

1. 遵循 `.dev/standards/GIT-COMMIT-POLICY.md`。
2. 有 issue number 時使用 `<type>(#<issue-number>|<scope>): <summary>`。
3. 沒有 issue number 時使用 `<type>(<scope>): <summary>`。
4. workflow-stage commits 需包含 `Why`、`What`、`Validation` 與 `Workflow` body sections。

### AI Context Governance

以下情境使用 `ai-context-governance`：

- 通用與技術棧專用 context 分類；
- AI 文件整理；
- 語言政策調整；
- skill routing 調整；
- runtime wrapper sync；
- context migration 規劃或執行。

不要將純 AI 文件治理工作交給 `bdd-gwt-test-designer`。

### Development Workflow Orchestration

當工作需要多階段規劃、workflow artifacts、skill routing、sub-agent coordination、validation checkpoint 或 commit checkpoint 時，使用 `dev-workflow`。

該 skill 可以協調 downstream skills，但不應取代它們各自的專業責任。

### Repo Init / Template Adaptation

當這套 framework 被複製到既有或全新目標 repository 後，第一個 skill 應使用 `repo-structure-sync`。

該 skill 必須：

1. 依據檔案證據盤點目標 repository；
2. 辨識 copied template 或歷史來源專案真相；
3. 更新目標 repo 專屬的 `agents.md`、`.dev/` 與必要 `.ai/` entry docs；
4. 除非目標 repo 明確推翻，否則保留 framework-level collaboration rules；
5. 移除或重寫來源 repo 專屬的 requirements、specs、operations docs、workflow artifacts 與 ADRs。

以 `.ai/assets/skills/repo-structure-sync/references/migration-boundaries.md` 作為 authoritative migration boundary。

### Code Review

只有在 review .NET backend code 或 dotnet-backend implementation guidance 時才使用 `code-reviewer`。

適用 code review 時：

1. 閱讀 `.ai/assets/tech-stacks/dotnet-backend/references/CODE-REVIEW-INDEX.MD`。
2. 閱讀 `.ai/assets/skills/code-reviewer/references/checklist-reference.md`。
3. 辨識檔案類型，並閱讀 `.dev/standards/` 下對應 checklist。
4. 建立 checklist comparison table。
5. 將問題分類為 `CRITICAL`、`MUST FIX` 或 `SHOULD FIX`。
6. 若目標 repo 適用測試，執行最窄且有意義的 test command。

### Spec Compliance

使用 problem-frame workflows 時：

1. 執行 `spec-compliance-validator`。
2. Gate：coverage 必須是 100%。
3. 若 coverage 不是 100%，回到 implementation 或 test generation 後再宣稱完成。

## Skill Routing

- Canonical skill registry：`.ai/assets/skills/README.MD`
- Current runtime wrappers：`.agents/skills/README.md`
- Claude-compatible wrappers：`.claude/skills/README.md`
- Human-facing skill guides：`.dev/guides/ai-collaboration-guides/README.MD`

當 canonical spec 與 runtime wrapper 不一致時，以 `.ai/assets/skills/` 作為 source of truth。

使用下列邊界：

| 需求 | Skill |
| --- | --- |
| 多階段開發流程協調、workflow artifacts、skill routing、validation 與 commit checkpoint | `dev-workflow` |
| AI context cleanup、prompt boundary、language policy、wrapper sync | `ai-context-governance` |
| 將此 framework 複製到目標 repo 後的第一次同步 | `repo-structure-sync` |
| .NET backend architecture design | `ddd-ca-hex-architect` |
| GWT scenario 與 assertion design | `bdd-gwt-test-designer` |
| .NET backend code review | `code-reviewer` |
| Requirement authoring | `requirement-author` |
| Spec authoring | `spec-author` |
| Problem frame authoring | `problem-frame-author` |
| Bounded implementation slice | `slice-implementer` |
| 局部技術程式變更 | `local-change-implementer` |

## 檔案與目錄索引

### 根目錄入口文件

| Path | 說明 |
| :--- | :--- |
| `README.md` | Human-facing 繁體中文 repository identity |
| `README.en.md` | English repository identity |
| `agents.md` | Root agent collaboration guide |
| `agents.zh-tw.md` | 繁體中文台灣用語版 root agent collaboration guide |
| `.github/copilot-instructions.md` | GitHub Copilot repo-level instructions |

### AI Assets (`.ai/`)

| Path | 說明 |
| :--- | :--- |
| `.ai/INDEX.MD` | Agent-facing AI asset index |
| `.ai/README.MD` | `.ai/` purpose and boundary guide |
| `.ai/assets/` | Canonical reusable AI assets |
| `.ai/assets/shared/` | Universal shared AI context |
| `.ai/assets/tech-stacks/dotnet-backend/` | .NET backend-specific context |
| `.ai/assets/tech-stacks/dotnet-backend/references/CODE-REVIEW-INDEX.MD` | .NET backend code review entry |
| `.ai/assets/tech-stacks/dotnet-backend/references/BUILDING-BLOCKS-CLASS-INDEX.MD` | .NET backend building block reference |
| `.ai/assets/skills/` | Canonical skill specs |
| `.ai/assets/sub-agent-role-prompts/` | Canonical sub-agent role prompts |
| `.ai/scripts/` | 過渡期 AI workflow scripts、context governance checks 與本機工具 orchestration helpers |

### Project Knowledge and Governance (`.dev/`)

| Path | 說明 |
| :--- | :--- |
| `.dev/README.MD` | Human-facing project knowledge index |
| `.dev/standards/` | Governance、context、workflow、coding、review 與 structure standards |
| `.dev/guides/` | Human-facing guides |
| `.dev/adr/` | ADR governance and retained decisions |
| `.dev/requirement/` | Requirements and requirement authoring materials |
| `.dev/specs/` | Specification organization and retained specs |
| `.dev/operations/` | Operations docs and operations document guides |
| `.dev/workflows/` | Workflow artifacts |

### Runtime Skill Wrappers

| Path | 說明 |
| :--- | :--- |
| `.agents/skills/README.md` | Current runtime wrapper index |
| `.agents/skills/<skill>/` | Current runtime skill wrapper |
| `.claude/skills/README.md` | Claude-compatible wrapper index |
| `.claude/skills/<skill>/` | Claude-compatible skill wrapper |

## 語言規則

- Agent-facing context 應優先使用英文，除非來源材料本質上就是 human-facing 繁體中文。
- Human-facing guides 與 README content 應優先使用繁體中文台灣用語。
- Runtime wrappers 應保持輕量，並指向 canonical specs。
- Context 分類優先使用資料夾位置，而不是每個檔案各自加 metadata。
