# AI 協作知識庫與 .NET Backend Context Framework

[English](README.en.md)

本文件是 human-facing repository identity 的繁體中文（台灣）canonical 版本；`README.en.md` 是其英文翻譯。

這個 repository 用來萃取、整理並演化我的軟體開發知識，以及可被 AI Agents 重複使用的 context、skills、sub-agent prompts 與協作 workflow。

它不是產品專案本身，而是一個可攜式的 AI 協作框架。當這套 context 被帶到既有專案或全新空專案時，應先使用 `repo-structure-sync` 進行 repo init，讓目標專案的真實結構取代本 repo 中的 template 或歷史專案資訊。

## 目標

- 萃取軟體開發知識，包括軟體工程、系統架構、軟體架構、DDD、Clean Architecture、CQRS、測試策略與 .NET 開發經驗。
- 建立 AI Agents 可直接使用的 context、skills、sub-agent prompts、工作流規則與驗證規則。
- 區分通用知識與非通用技術棧知識。
- 保留目前可重用的非通用能力：.NET、C#、後端 Web API、DDD / CA / CQRS / message-driven backend 開發。
- 移除或隔離過往專案殘留資訊，必要時轉成 template 或 repo init 的輸入材料。

## Context 分層

### 通用 AI Context

通用內容應能被不同語言、框架、產品型態重複使用，例如：

- AI 協作流程與 workflow gate
- git commit policy
- skill routing 與 sub-agent 協作規則
- system/software architecture 設計原則
- DDD、Clean Architecture、CQRS 等概念層說明
- requirement、spec、ADR、review、validation 的文件治理方式

### 非通用 AI Context

目前本 repo 的非通用內容主要是 `.NET backend`：

- C# / .NET backend 實作規範
- Web API / worker / consumer 類型的 backend 專案結構
- WolverineFx、Dapper、EF Core、PostgreSQL、RabbitMQ、Kafka 等 backend stack 經驗
- DDD / CA / CQRS 在 .NET backend 中的實作規劃與 code review 規則

這些內容應放在 `.ai/assets/tech-stacks/dotnet-backend/` 或明確標示為 dotnet-backend 專用。

## 主要目錄

| Path | 用途 |
| --- | --- |
| `.ai/` | Agent-facing reusable AI context、canonical assets、scripts、skills specs |
| `.ai/assets/shared/` | 通用 prompt fragments、規則與可重用材料 |
| `.ai/assets/tech-stacks/dotnet-backend/` | .NET C# backend Web API 專用 context |
| `.ai/assets/skills/` | canonical skill specs 與 skill registry |
| `.ai/assets/sub-agent-role-prompts/` | sub-agent role prompt 的 canonical source |
| `.agents/skills/` | Codex/current runtime skill wrappers |
| `.claude/skills/` | Claude-compatible skill wrappers |
| `AGENTS.md` | Codex 與通用 agent 使用的 canonical root collaboration guide |
| `CLAUDE.md` | 匯入 `AGENTS.md` 的 Claude Code project-memory 薄入口 |
| `.dev/` | Human-facing governance、standards、guides、requirements、specs、workflow artifacts |
| `.dev/workflows/` | 跨 skill / sub-agent 的 workflow plan、task、review-report |

目前未提供 GitHub Copilot 的 repo-level wrapper；相關路徑屬於未來可選整合，不是目前 runtime catalog 的一部分。

## 重要 Skills

- `dev-workflow`
  - 用於 software/product development lifecycle 協調，涵蓋 requirement、spec、architecture、test、implementation、review 與 compliance；負責開發 workflow mode 判斷、skill routing、validation checkpoint 與 commit checkpoint，不負責 AI context 或 repo init workflow。
- `ai-context-governance`
  - 用於 context 分層、語言政策、skill routing、wrapper sync、AI 文件治理與搬移。
- `ai-context-auditor`
  - 用於唯讀 AI context 健康度與漂移自檢，預設排除產品程式碼，並比較獨立分析與 repo-aware 分析。結果可僅保留在對話中；只有需要保存正式報告時才建立 audit workflow 並將報告落地。
- `repo-structure-sync`
  - 用於 repo init。當這套 AI context 被複製到既有或全新目標 repo 後，第一個應使用此 skill 盤點目標 repo 並刷新 `AGENTS.md`、`.dev/` 與必要 `.ai/` 入口文件。
- `ddd-ca-hex-architect`
  - 用於 .NET backend 的 DDD / Clean Architecture / Hexagonal / CQRS 架構設計。
- `code-reviewer`
  - 用於 .NET backend code review。

完整 skill registry 以 `.ai/assets/skills/README.MD` 為準。

## 語言政策

- AI 主要使用的 context 優先使用英文，以降低 token 成本並提升跨 agent 可攜性。
- Human-facing 文件優先使用繁體中文台灣用語。
- 根目錄 README 維護中英雙語版本：
  - `README.md`
  - `README.en.md`
- 詳細規範請見 `.dev/standards/AI-CONTEXT-LANGUAGE-POLICY.md`。

## 在其他 repo 使用

當這套 context 被帶到其他 repository：

1. 複製必要的 `.ai/`、`.dev/`、`.agents/`、`.claude/` 與 agent entry files。
2. 立即執行 `repo-structure-sync`。
3. 依目標 repo 的檔案、solution、project、package、infra config 與既有文件重建 repo-specific truth。
4. 移除或重寫與來源 repo 綁定的 requirement、spec、operation、workflow 與 ADR。
5. 保留通用 framework-level rules，除非目標 repo 明確需要調整。

詳細邊界請見 `.ai/assets/skills/repo-structure-sync/references/migration-boundaries.md`。

## 目前整理方向

產品專用 requirements、specs、operations truth、problem frames、project config 與 frontend implementation assets 已從 active paths 移除或範本化。

後續新增內容必須維持以下邊界：

- reusable .NET backend context 放在 `.ai/assets/tech-stacks/dotnet-backend/`；
- target-repository truth 由 `repo-structure-sync` 依目標 repo evidence 建立；
- 歷史決策只保留在明確標示的 workflow / migration artifacts；
- frontend 與其他語言目前只保留 context placement exploration，不視為 active profile。
