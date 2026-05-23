# AGENTS.md

## Scope & Precedence

- This document serves as the collaboration guideline for AI agents and humans across the entire repository.
- If a subdirectory has another AGENTS.* file, the deeper one takes precedence.
- Command priority: User/Approval > Subfolder AGENTS > This file > Other general documents.
- 若有設定 IDE 的 MCP Server 則優先使用 IDE MCP Server 中有提供的重構功能。

## Quick Start for AI Agents

1. Read `.dev/ARCHITECTURE.MD` and `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`.
2. Use `.dev/ARCHITECTURE.MD`, `.dev/standards/`, and `.dev/guides/` as the canonical source of architecture and collaboration rules.
3. For reusable AI-specific prompts, use `.ai/` folder.
4. For top-level skills, use `.ai/assets/skills/README.MD` as the canonical skill registry.
5. When preparing this framework for reuse in another repo, run `repo-structure-sync` and follow its migration boundary reference.

---

## Mandatory Workflows

### Code Review (Required)

1. Read `.ai/CODE-REVIEW-INDEX.MD`.
2. Read `.ai/assets/skills/code-reviewer/references/checklist-reference.md` for the canonical review quick reference.
3. Identify file type and read the matching section in `.dev/standards/CODE-REVIEW-CHECKLIST.md`.
4. Build a checklist comparison table.
5. Categorize issues (CRITICAL / MUST FIX / SHOULD FIX).
6. If tests apply, run `dotnet test --filter FullyQualifiedName~[TestClassName]`.

### Spec Compliance (Required for Problem Frames)

When using problem-frame workflows:
1. Run `spec-compliance-validator` skill.
2. **Gate**: coverage must be 100%. If not, return to implementation/test generation.

### Task Execution (If task-*.json is used)

1. Read task JSON.
2. Implement.
3. Run tests (if required).
4. Update `status` + `results` in task JSON.

Workflow artifact location:
- Use `.dev/workflows/<workflow-id>/workflow-plan.md`
- Use `.dev/workflows/<workflow-id>/review-report.md`
- Use `.dev/workflows/<workflow-id>/tasks/<task-id>.json`
- Do not scatter workflow artifacts under `.ai/`, `.agents/skills/`, `.claude/skills/`, or arbitrary feature folders unless the user explicitly requests it.

### Repo Structure Sync (When framework files are copied to another repo)

1. Keep framework-level guides, standards, scripts, and collaboration rules.
2. Remove or rewrite project-specific requirement, spec, operations, workflow, and legacy decision history.
3. Rebuild `.dev/requirement/`, `.dev/specs/`, `.dev/operations/`, and any project-specific decision history from the target project's facts.
4. Run `repo-structure-sync` to scan the target repo structure and refresh repo-specific architecture sections in `agents.md`, `.dev/`, and necessary `.ai/` entry docs.
5. Treat `.ai/assets/skills/repo-structure-sync/references/migration-boundaries.md` as the authoritative migration boundary.

---

## Sub-agent System Overview

- Primary reference: `.ai/SUB-AGENT-SYSTEM.MD`
- Use `.ai/assets/sub-agent-role-prompts/` for canonical delegated sub-agent definitions.
- Use `.ai/assets/shared/` for shared rules, examples, and supporting materials.
- Use `.ai/scripts/` for .NET code generation scripts.

---

## Skill Routing

- Canonical skill registry: `.ai/assets/skills/README.MD`
- Current runtime wrappers: `.agents/skills/README.md`
- Claude-compatible wrappers: `.claude/skills/README.md`
- Human-facing skill guides: `.dev/guides/ai-collaboration-guides/README.MD`

When canonical spec and runtime wrapper differ, treat `.ai/assets/skills/` as the source of truth.

---

## File & Directory Index

### AI-Specific (`.ai/`)

| Path | Description |
| :--- | :--- |
| `.ai/INDEX.MD` | AI 文件入口 |
| `.ai/README.MD` | .NET Framework 概覽 |
| `.ai/CODE-REVIEW-INDEX.MD` | Code Review 索引 |
| `.ai/SUB-AGENT-SYSTEM.MD` | Sub-agent 系統說明 |
| `.ai/BUILDING-BLOCKS-CLASS-INDEX.MD` | 共用介面索引 |
| `.ai/assets/` | Canonical reusable AI assets |
| `.ai/scripts/` | .NET code generation scripts |

### Project Knowledge (`.dev/`)

| Path | Description |
| :--- | :--- |
| `.dev/ARCHITECTURE.MD` | 系統架構 |
| `.dev/README.MD` | 專案知識入口 |
| `.dev/adr/` | ADR 治理層（template / index / 建立時機） |
| `.dev/guides/` | 學習指南 |
| `.dev/lessons/` | 經驗教訓 |
| `.dev/requirement/` | 技術需求 |
| `.dev/workflows/` | 跨 skill / subagent workflow artifacts（plan / review-report / task） |
| `.dev/specs/` | 功能規格與行為規格 |
| `.dev/standards/` | Code Review Checklist, Project Structure |

### Claude Skills (`.claude/skills/`)

| Path | Description |
| :--- | :--- |
| `.claude/skills/README.md` | Claude-compatible runtime wrapper index |
| `.claude/skills/<skill>/` | Claude-compatible skill wrapper |

### Agents Skills (`.agents/skills/`)

| Path | Description |
| :--- | :--- |
| `.agents/skills/README.md` | Current runtime wrapper index |
| `.agents/skills/<skill>/` | Current runtime skill wrapper |

### AI Collaboration Guides (`.dev/guides/ai-collaboration-guides/`)

| Path | Description |
| :--- | :--- |
| `.dev/guides/ai-collaboration-guides/README.MD` | AI collaboration guides 入口 |
| `.dev/guides/ai-collaboration-guides/LOCAL-RUNTIME-WRAPPER-GUIDE.md` | Repo wrapper 與本機 runtime 的使用說明 |
| `.dev/guides/ai-collaboration-guides/DDD-CA-HEX-ARCHITECT-SKILL-GUIDE.md` | Human-facing guide and prompt templates for invoking the architect skill |
| `.dev/guides/ai-collaboration-guides/BDD-GWT-TEST-DESIGNER-SKILL-GUIDE.md` | Human-facing guide and prompt templates for invoking the BDD GWT test designer skill |
| `.dev/guides/ai-collaboration-guides/USE-CASE-IMPLEMENTER-SKILL-GUIDE.md` | Human-facing guide and prompt templates for command / query / reactor implementer skills |
| `.dev/guides/ai-collaboration-guides/REPO-STRUCTURE-SYNC-SKILL-GUIDE.md` | Human-facing guide and prompt templates for invoking the repo structure sync skill |
| `.dev/guides/ai-collaboration-guides/PROBLEM-FRAME-AUTHORING-GUIDE.md` | Human-facing guide for deriving a first problem frame from requirement/spec/code |
| `.dev/guides/ai-collaboration-guides/STAGED-REFACTOR-IMPLEMENTER-SKILL-GUIDE.md` | Human-facing guide and prompt templates for invoking the refactor implementation skill |
| `.dev/guides/ai-collaboration-guides/TACTICAL-REFACTOR-IMPLEMENTER-SKILL-GUIDE.md` | Human-facing guide and prompt templates for invoking the tactical refactor skill |
| `.github/copilot-instructions.md` | GitHub Copilot repo-level instructions |
