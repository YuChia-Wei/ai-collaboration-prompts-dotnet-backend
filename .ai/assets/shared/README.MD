# Universal Shared Canonical Assets

本目錄放置 skill 與 sub-agent role 共同依賴、且不綁定特定技術棧的中立資產。

技術棧專用但仍可重用的 agent-facing context 應放在 `.ai/assets/tech-stacks/<profile>/`，例如 `.ai/assets/tech-stacks/dotnet-backend/`。

## 可包含的內容

- rules
- contracts
- prompt packages
- reusable templates
- examples

## 目的

- 減少 skill spec 與 sub-agent canonical asset 的重複內容
- 讓 wrapper 與 human-facing guides 能共同引用同一份 canonical source
- 避免把 .NET backend-only rules 混入 universal shared context
