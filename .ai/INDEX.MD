# .ai Index

本文件是 `.ai/` 的 agent-facing 索引。

## Core

- `README.MD`
  - `.ai/` 目錄用途與分工
- `DIRECTORY-RULES.MD`
  - `.ai/` 與 `.dev/` 的放置規則
- `SUB-AGENT-SYSTEM.MD`
  - sub-agent 系統、routing、artifact 讀寫規則
- `assets/tech-stacks/dotnet-backend/references/CODE-REVIEW-INDEX.MD`
  - .NET backend code review workflow 入口

## Prompt Assets

- `assets/`
  - canonical source root for reusable AI assets
- `assets/shared/`
  - universal shared rules / prompt fragments / reusable supporting materials
- `assets/tech-stacks/`
  - tech-stack-specific reusable AI context
- `assets/tech-stacks/dotnet-backend/`
  - .NET backend-only agent context; excludes Razor, Blazor, MAUI, and other .NET frontend frameworks
- `assets/sub-agent-role-prompts/`
  - delegated sub-agent role prompt canonical assets
- `assets/skills/`
  - canonical skill registry and skill specs
- `assets/templates/`
  - canonical templates for skills / prompts / commands

## Script Assets

- `scripts/`
  - transitional AI workflow scripts, context governance checks, and local tool orchestration helpers
- `scripts/generated/`
  - generated regex checks planned for retirement after dotnet-native replacements exist
- `scripts/README.md`
  - script transition policy and inventory entry

## Supporting References

- `assets/tech-stacks/dotnet-backend/references/BUILDING-BLOCKS-CLASS-INDEX.MD`
  - .NET backend BuildingBlocks type index
- `assets/tech-stacks/dotnet-backend/references/CODE-REVIEW-INDEX.MD`
  - .NET backend code review quick index
- `assets/tech-stacks/dotnet-backend/references/FAILURE-CASES.MD`
  - .NET backend failure cases
- `assets/tech-stacks/dotnet-backend/references/COMMON-PITFALLS.MD`
  - .NET backend common pitfalls
- `assets/tech-stacks/dotnet-backend/references/CODE-TEMPLATES.MD`
  - .NET backend code templates

## Related Human-Facing Docs

- `../.dev/guides/README.MD`
  - human-facing guides 入口
- `../.dev/guides/ai-collaboration-guides/README.MD`
  - AI collaboration guides 入口
- `../.dev/guides/ai-collaboration-guides/REPO-STRUCTURE-SYNC-SKILL-GUIDE.md`
  - template 移植到新 repo 後的架構同步指南
- `../.dev/guides/ai-collaboration-guides/AI-ASSET-LOCATION-STRATEGY.md`
  - 多 agent 情境下的 skill / prompt / guide 收納策略
- `../.claude/skills/README.md`
  - repo-local skill definition 入口
