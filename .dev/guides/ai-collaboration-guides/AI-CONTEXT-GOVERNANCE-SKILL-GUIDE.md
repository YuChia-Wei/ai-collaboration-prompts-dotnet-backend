# AI Context Governance Skill Guide

本文件是 `ai-context-governance` 的 human-facing 使用指南。canonical skill 規則以 `.ai/assets/skills/ai-context-governance/skill.yaml` 與其 references 為準。

## 這個 Skill 可以做什麼

適合用在：

- 整理 `.ai/`、`.dev/`、`.agents/`、`.claude/` 的 AI context 邊界
- 拆分 universal AI context 與 tech-stack-specific context
- 定義或套用 AI context language policy
- 同步 canonical skill spec、runtime wrapper、human guide、index
- 建立 AI 文件整理 workflow
- 避免把純 AI 文件整理誤交給 BDD、code review、或 production implementer skill

## 不應該做什麼

不應該用它來：

- 設計 Given-When-Then scenarios
- 實作 production code
- 做正式 code review
- 重新設計 domain architecture
- 大量翻譯所有文件，除非 workflow 明確要求 translation migration

## 使用時機

當工作關鍵字包含下列意圖時，優先使用這個 skill：

- AI context cleanup
- prompt/context boundary
- language policy
- skill routing
- wrapper sync
- universal vs dotnet-backend split
- documentation governance

## Prompt 範本

```text
Use $ai-context-governance to classify and clean up AI context boundaries.

Focus on:
- universal AI context
- dotnet-backend-only context
- repo-specific project truth
- runtime wrappers
- human-facing guides

Do not use BDD scenario design for this task.
Return the files updated, boundary decisions, and validation performed.
```

## 與其他 Skill 的邊界

- `bdd-gwt-test-designer`
  - 只處理 BDD/Gherkin scenario 與 assertion 設計。
- `ddd-ca-hex-architect`
  - 處理 domain / architecture design；可協助重大 context 邊界決策。
- `repo-structure-sync`
  - 用於 template 複製到 target repo 後，依 target repo facts 重建架構入口文件。
- `staged-refactor-implementer`
  - 用於已決定的 staged refactor；若是 AI context governance，應先由本 skill 定義邊界。
