# .NET Backend Architecture and Coding Standards

This folder contains reusable .NET backend architecture and development standards.

DDD / Clean Architecture / CQRS boundaries are normative. Database, ORM, event store, message broker, test package, and runtime versions are selected by each target repository from file-backed evidence.

EF Core, Dapper, Npgsql, WolverineFx, RabbitMQ, Kafka, xUnit, BDDfy, and NSubstitute documents are conditional/reference guidance unless target repository configuration explicitly adopts them.

## Structure

- `ASPNET-CORE-CONFIGURATION-CHECKLIST.md`
  - ASP.NET Core configuration checklist
- `AI-CONTEXT-BOUNDARY.md`
  - AI context ownership and folder placement policy
- `AI-CONTEXT-LANGUAGE-POLICY.md`
  - language policy for agent-facing and human-facing context
- `CODE-REVIEW-CHECKLIST.md`
  - code review checklist 與審查準則
- `GIT-COMMIT-POLICY.md`
  - commit title, body, and timing policy for agent-assisted work
- `WORKFLOW-GATE-POLICY.md`
  - rules for when agents should create workflow artifacts
- `anti-patterns.md`
  - 反模式與禁止事項
- `best-practices.md`
  - 建議採用的 practices
- `coding-guide.md`
  - coding 標準入口，串接 standards 與 guides
- `coding-standards.md`
  - coding style 與 implementation-level rules
- `project-structure.md`
  - 專案目錄與資料夾用途的單一真相
- `rationale/`
  - 可攜式模式選擇理由
- `README.md`
  - standards 入口說明

Operational guides、setup walkthroughs、FAQ、troubleshooting 文件已移到 `.dev/guides/`。

## Belongs Here

- 規則性文件
- checklist
- anti-pattern / best-practice
- project structure single source of truth
- 需要長期穩定引用的標準入口
- AI context governance, commit policy, and workflow gate policy

## Do Not Put Here

- setup guide
- quick start walkthrough
- FAQ
- troubleshooting / solution note
- 單次重構提案或工作紀錄
- AI skill/prompt/workflow guide

這些內容應分別放到：

- `.dev/guides/implementation-guides/`
- `.dev/guides/design-guides/`
- `.dev/guides/learning-guides/`
- `.dev/guides/ai-collaboration-guides/`
- `.dev/workflows/`

## Notes
- ezDDD/ezSpec concepts must be preserved even without direct .NET packages.
- If no .NET equivalent exists, keep the rule and mark TODO rather than deleting it.
- `standards/` should not accumulate setup guides, troubleshooting guides, or FAQ-style documents.

