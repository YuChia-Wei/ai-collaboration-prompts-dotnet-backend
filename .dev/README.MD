# AI 協作知識與 Context Governance

> 此目錄包含本 repo 的 human-facing 知識治理、AI context 標準、workflow artifacts、技術規範、歷史決策紀錄與經驗教訓。

## 📁 目錄結構

| 資料夾 | 說明 |
| :--- | :--- |
| `adr/` | ADR 治理層（template / index / 建立時機） |
| `domain-language/` | 領域統一詞彙的範本與目標 repo domain language 收納區 |
| `guides/` | 一般 human-facing guides（ai collaboration / design / implementation / learning） |
| `lessons/` | 經驗教訓與錯誤案例 |
| `operations/` | target repo runtime / 維運文件的 authoring guides 與收納位置 |
| `requirement/` | framework 與 target repo requirements 及 authoring materials |
| `workflows/` | 跨 skill / subagent workflow artifacts（plan / review-report / task） |
| `specs/` | 詳細規格指南 |
| `standards/` | 技術標準、Code Review Checklist、專案結構 |
| `TEAM-GIT-FLOW-RULES.MD` | single-mainline git flow 與 branch naming 規則 |

## 🚀 Quick Start

1. **Repo identity**: 請先閱讀 [`../README.md`](../README.md) 或 [`../README.en.md`](../README.en.md)
2. **AI context boundary**: [`standards/AI-CONTEXT-BOUNDARY.md`](standards/AI-CONTEXT-BOUNDARY.md)
3. **Language policy**: [`standards/AI-CONTEXT-LANGUAGE-POLICY.md`](standards/AI-CONTEXT-LANGUAGE-POLICY.md)
4. **Workflow gate**: [`standards/WORKFLOW-GATE-POLICY.md`](standards/WORKFLOW-GATE-POLICY.md)
5. **Git commit policy**: [`standards/GIT-COMMIT-POLICY.md`](standards/GIT-COMMIT-POLICY.md)
6. **Dev workflow skill guide**: [`guides/ai-collaboration-guides/DEV-WORKFLOW-SKILL-GUIDE.md`](guides/ai-collaboration-guides/DEV-WORKFLOW-SKILL-GUIDE.md)
7. **Repo init skill guide**: [`guides/ai-collaboration-guides/REPO-STRUCTURE-SYNC-SKILL-GUIDE.md`](guides/ai-collaboration-guides/REPO-STRUCTURE-SYNC-SKILL-GUIDE.md)

## 🔗 相關資源

- Human-facing AI Collaboration Guides: `guides/ai-collaboration-guides/`
- Dev Workflow Skill Guide: `guides/ai-collaboration-guides/DEV-WORKFLOW-SKILL-GUIDE.md`
- AI Context Governance Skill Guide: `guides/ai-collaboration-guides/AI-CONTEXT-GOVERNANCE-SKILL-GUIDE.md`
- Domain Language Templates: `domain-language/`
- AI Prompts: `.ai/`
- Canonical AI Assets: `.ai/assets/`
- Repo Structure Sync Guide: `guides/ai-collaboration-guides/REPO-STRUCTURE-SYNC-SKILL-GUIDE.md`
- Team Git Flow Rules: `TEAM-GIT-FLOW-RULES.MD`
- AI Context Boundary: `standards/AI-CONTEXT-BOUNDARY.md`
- AI Context Language Policy: `standards/AI-CONTEXT-LANGUAGE-POLICY.md`
- Git Commit Policy: `standards/GIT-COMMIT-POLICY.md`
- Workflow Gate Policy: `standards/WORKFLOW-GATE-POLICY.md`
- Canonical Skill Registry: `.ai/assets/skills/README.MD`
- Agents Runtime Wrappers: `.agents/skills/README.md`
- Claude Runtime Wrappers: `.claude/skills/README.md`
- 專案入口: `agents.md`

## 📌 內容定位

- `.dev/` 放給人看的知識、指南、規範與索引
- `.ai/` 放給 agent 重用的 prompts、shared rules、scripts
- `.ai/assets/skills/` 放 canonical skill specs
- `.agents/skills/` 與 `.claude/skills/` 放 runtime wrappers

### `.dev/` 內部常見協作文件

- `.dev/requirement/`: requirement docs 與 requirement authoring materials
- `.dev/domain-language/`: 領域統一詞彙、bounded context language、aggregate vocabulary、domain event language 的範本與收納區
- `.dev/specs/`: spec organization、function specs 與行為規格
- `.dev/operations/`: target repo runtime truth 的 authoring guides 與收納位置
- `.dev/workflows/`: 多 skill / subagent handoff 所需的 `plan`、`review-report`、`task`

當工作涉及多 skill 接力、subagent 分工或 staged refactoring 時，優先從這些文件建立共同上下文。

## Template Sync 使用原則

- `.dev/` 可作為新專案的知識治理骨架直接複製
- 但 `.dev/requirement/`、`.dev/domain-language/` 中已填寫的領域詞彙、`.dev/specs/`、`.dev/operations/` 與任何 project-specific 歷史決策紀錄通常屬於專案真相，不應原封不動沿用
- 移植規則與保留/重寫邊界由 `repo-structure-sync` skill 的 `migration-boundaries.md` 維護
