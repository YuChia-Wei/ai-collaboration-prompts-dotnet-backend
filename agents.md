# AGENTS.md

[Traditional Chinese](agents.zh-tw.md)

## Scope & Precedence

- This document is the root collaboration guide for AI agents and humans working in this repository.
- This repository is an AI collaboration knowledge base and reusable context framework, not a product application repository.
- If a subdirectory has another `AGENTS.*` file, the deeper file takes precedence.
- Command priority: User/Approval > Subfolder AGENTS > This file > Other general documents.
- If an IDE MCP server is configured and provides refactoring capabilities, prefer the IDE MCP refactoring tools.

## Default Execution Principles

- Do not invent project truth. State material assumptions, uncertainty, and tradeoffs. Ask only when an unresolved direction materially affects the outcome.
- Implement the smallest coherent change that satisfies the defined acceptance criteria. Avoid speculative features, abstractions, and context.
- Touch only files required by the task. Avoid unrelated cleanup, and remove artifacts introduced by your own changes.
- Establish verifiable completion criteria before execution. Iterate until they pass, or report concrete blockers and any skipped validation.

## Repository Identity

This repository exists to:

- extract software engineering, architecture, .NET backend, and AI collaboration knowledge;
- maintain reusable AI Agent context, skills, sub-agent prompts, and workflow rules;
- separate universal AI context from tech-stack-specific context;
- preserve current non-universal capability for .NET C# backend Web API development;
- remove, isolate, or templatize historical source-project facts.

Do not treat historical sample backend information as current product truth unless a file explicitly states that it is retained as a template, migration artifact, or dotnet-backend reference.

## Quick Start for AI Agents

1. Read `README.md` or `README.en.md` to understand this repo's purpose.
2. Read `.dev/standards/AI-CONTEXT-BOUNDARY.md` and `.dev/standards/AI-CONTEXT-LANGUAGE-POLICY.md` before moving or rewriting AI context.
3. Use `.ai/assets/skills/README.MD` as the canonical skill registry.
4. Use `.dev/guides/ai-collaboration-guides/README.MD` for human-facing skill and workflow guides.
5. Use `.ai/INDEX.MD` and `.ai/README.MD` for agent-facing AI asset navigation.

## Mandatory Workflows

### Workflow Gate

1. Read `.dev/standards/WORKFLOW-GATE-POLICY.md` when work may affect source-of-truth, AI context, skill routing, wrapper sync, or more than one stage.
2. Create workflow artifacts proactively when the gate requires workflow mode.
3. Keep small, local, single-pass changes in direct mode.

Workflow artifact location:

- Use `.dev/workflows/<workflow-id>/workflow-plan.md`
- Use `.dev/workflows/<workflow-id>/review-report.md` when review output is produced.
- Use `.dev/workflows/<workflow-id>/tasks/<task-id>.json` for task tracking.
- Do not scatter workflow artifacts under `.ai/`, `.agents/skills/`, `.claude/skills/`, or arbitrary folders unless the user explicitly requests it.

### Git Commit Policy

1. Follow `.dev/standards/GIT-COMMIT-POLICY.md`.
2. Use `<type>(#<issue-number>|<scope>): <summary>` when an issue number exists.
3. Use `<type>(<scope>): <summary>` when no issue number exists.
4. For workflow-stage commits, include `Why`, `What`, `Validation`, and `Workflow` body sections.

### AI Context Governance

Use `ai-context-governance` for:

- universal versus tech-stack-specific context classification;
- AI documentation cleanup;
- language policy changes;
- skill routing changes;
- runtime wrapper sync;
- context migration planning or execution.

Do not route pure AI documentation governance work to `bdd-gwt-test-designer`.

### AI Context Audit

Use `ai-context-auditor` for recurring, read-only AI context health and drift audits that must produce a durable report.

- Default to AI context and governance surfaces.
- Exclude `src/`, `tests/`, and other product implementation trees.
- If the user asks to scan product source or test code, stop and route that work to `code-reviewer` instead of expanding the audit.
- Keep audit findings separate from remediation; use `ai-context-governance` and `dev-workflow` only after remediation is authorized.

### Development Workflow Orchestration

Use `dev-workflow` when the work needs multi-stage planning, workflow artifacts, skill routing, sub-agent coordination, validation checkpoints, or commit checkpoints.

The skill may coordinate downstream skills, but it must not replace their domain responsibilities.

### Repo Init / Template Adaptation

Use `repo-structure-sync` as the first skill after this framework is copied into an existing or empty target repository.

The skill must:

1. inventory the target repository from file-backed facts;
2. identify copied template or historical source-project truth;
3. refresh target-specific `agents.md`, `.dev/`, and necessary `.ai/` entry docs;
4. preserve framework-level collaboration rules unless the target repo clearly invalidates them;
5. remove or rewrite source-repo-specific requirements, specs, operations docs, workflow artifacts, and ADRs.

Treat `.ai/assets/skills/repo-structure-sync/references/migration-boundaries.md` as the authoritative migration boundary.

### Code Review

Use `code-reviewer` only when reviewing .NET backend code or dotnet-backend implementation guidance.

When code review applies:

1. Read `.ai/assets/tech-stacks/dotnet-backend/references/CODE-REVIEW-INDEX.MD`.
2. Read `.ai/assets/skills/code-reviewer/references/checklist-reference.md`.
3. Identify file type and read the matching checklist under `.dev/standards/`.
4. Build a checklist comparison table.
5. Categorize issues as `CRITICAL`, `MUST FIX`, or `SHOULD FIX`.
6. If tests apply in the target repo, run the narrowest meaningful test command.

### Spec Compliance

When using problem-frame workflows:

1. Run `spec-compliance-validator`.
2. Gate: coverage must be 100%.
3. If coverage is not 100%, return to implementation or test generation before claiming completion.

## Skill Routing

- Canonical skill registry: `.ai/assets/skills/README.MD`
- Current runtime wrappers: `.agents/skills/README.md`
- Claude-compatible wrappers: `.claude/skills/README.md`
- Human-facing skill guides: `.dev/guides/ai-collaboration-guides/README.MD`

When canonical spec and runtime wrapper differ, treat `.ai/assets/skills/` as the source of truth.

Use these boundaries:

| Need | Skill |
| --- | --- |
| Multi-stage development workflow orchestration, workflow artifacts, skill routing, validation and commit checkpoints | `dev-workflow` |
| Recurring read-only AI context health, drift, and structure audit with a saved report | `ai-context-auditor` |
| AI context cleanup, prompt boundary, language policy, wrapper sync | `ai-context-governance` |
| First sync after copying this framework into a target repo | `repo-structure-sync` |
| .NET backend architecture design | `ddd-ca-hex-architect` |
| GWT scenario and assertion design | `bdd-gwt-test-designer` |
| .NET backend code review | `code-reviewer` |
| Requirement authoring | `requirement-author` |
| Spec authoring | `spec-author` |
| Problem frame authoring | `problem-frame-author` |
| Bounded implementation slice | `slice-implementer` |
| Local technical code change | `local-change-implementer` |

## File & Directory Index

### Root Entry Docs

| Path | Description |
| :--- | :--- |
| `README.md` | Human-facing Traditional Chinese repository identity |
| `README.en.md` | English repository identity |
| `agents.md` | Root agent collaboration guide |
| `.github/copilot-instructions.md` | GitHub Copilot repo-level instructions |

### AI Assets (`.ai/`)

| Path | Description |
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
| `.ai/scripts/` | Transitional AI workflow scripts, context governance checks, and local tool orchestration helpers |

### Project Knowledge and Governance (`.dev/`)

| Path | Description |
| :--- | :--- |
| `.dev/README.MD` | Human-facing project knowledge index |
| `.dev/standards/` | Governance, context, workflow, coding, review, and structure standards |
| `.dev/guides/` | Human-facing guides |
| `.dev/adr/` | ADR governance and retained decisions |
| `.dev/requirement/` | Requirements and requirement authoring materials |
| `.dev/domain-language/` | Domain ubiquitous language templates and target-repo vocabulary area |
| `.dev/specs/` | Specification organization and retained specs |
| `.dev/operations/` | Operations docs and operations document guides |
| `.dev/workflows/` | Workflow artifacts |

### Runtime Skill Wrappers

| Path | Description |
| :--- | :--- |
| `.agents/skills/README.md` | Current runtime wrapper index |
| `.agents/skills/<skill>/` | Current runtime skill wrapper |
| `.claude/skills/README.md` | Claude-compatible wrapper index |
| `.claude/skills/<skill>/` | Claude-compatible skill wrapper |

## Language Rules

- Agent-facing context should prefer English unless the source material is inherently human-facing Traditional Chinese.
- Human-facing guides and README content should prefer Traditional Chinese Taiwan usage.
- Keep runtime wrappers thin and point them to canonical specs.
- Prefer folder placement over per-file metadata for context classification.
