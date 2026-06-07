# AI Collaboration Knowledge Base and .NET Backend Context Framework

[繁體中文](README.md)

This repository extracts, organizes, and evolves my software development knowledge together with reusable AI Agent context, skills, sub-agent prompts, and collaboration workflows.

It is not a product repository. It is a portable AI collaboration framework. When this context is copied into an existing repository or an empty new repository, run `repo-structure-sync` first as the repo initialization skill so target-repository facts replace template or historical source-project facts.

## Goals

- Extract software development knowledge, including software engineering, system architecture, software architecture, DDD, Clean Architecture, CQRS, testing strategy, and .NET development experience.
- Maintain AI Agent context, skills, sub-agent prompts, workflow rules, and validation rules.
- Separate universal knowledge from tech-stack-specific knowledge.
- Preserve the current non-universal capability set: .NET, C#, backend Web API, and DDD / CA / CQRS / message-driven backend development.
- Remove or isolate historical source-project facts, converting them to templates or repo-init inputs when useful.

## Context Layers

### Universal AI Context

Universal context should be reusable across languages, frameworks, and product types. Examples:

- AI collaboration workflows and workflow gates
- git commit policy
- skill routing and sub-agent collaboration rules
- system and software architecture principles
- conceptual DDD, Clean Architecture, and CQRS guidance
- requirement, spec, ADR, review, and validation governance

### Non-Universal AI Context

This repository's current non-universal context is `.NET backend`:

- C# / .NET backend implementation standards
- Web API / worker / consumer backend project structure
- WolverineFx, Dapper, EF Core, PostgreSQL, RabbitMQ, and Kafka experience
- DDD / CA / CQRS implementation planning and code review rules for .NET backend systems

These assets belong under `.ai/assets/tech-stacks/dotnet-backend/` or must be clearly marked as dotnet-backend-specific.

## Main Directories

| Path | Purpose |
| --- | --- |
| `.ai/` | Agent-facing reusable AI context, canonical assets, scripts, and skill specs |
| `.ai/assets/shared/` | Universal prompt fragments, rules, and reusable materials |
| `.ai/assets/tech-stacks/dotnet-backend/` | .NET C# backend Web API specific context |
| `.ai/assets/skills/` | Canonical skill specs and skill registry |
| `.ai/assets/sub-agent-role-prompts/` | Canonical source for sub-agent role prompts |
| `.agents/skills/` | Codex/current runtime skill wrappers |
| `.claude/skills/` | Claude-compatible skill wrappers |
| `.dev/` | Human-facing governance, standards, guides, requirements, specs, and workflow artifacts |
| `.dev/workflows/` | Cross-skill and sub-agent workflow plans, tasks, and review reports |
| `.github/copilot-instructions.md` | GitHub Copilot repo-level instructions |

## Important Skills

- `dev-workflow`
  - Coordinates multi-stage development, documentation cleanup, refactoring, and AI collaboration workflows; owns workflow-mode decisions, skill routing, validation checkpoints, and commit checkpoints.
- `ai-context-governance`
  - Governs context boundaries, language policy, skill routing, wrapper sync, AI documentation cleanup, and context moves.
- `repo-structure-sync`
  - Performs repo initialization. After this AI context is copied into an existing or empty target repository, use this skill first to inventory the target repo and refresh `agents.md`, `.dev/`, and required `.ai/` entry docs.
- `ddd-ca-hex-architect`
  - Designs .NET backend DDD / Clean Architecture / Hexagonal / CQRS architecture.
- `code-reviewer`
  - Reviews .NET backend code.

The canonical skill registry is `.ai/assets/skills/README.MD`.

## Language Policy

- Agent-facing context should prefer English to reduce token cost and improve cross-agent portability.
- Human-facing documents should prefer Traditional Chinese for Taiwan usage.
- Root README files are maintained in both languages:
  - `README.md`
  - `README.en.md`
- See `.dev/standards/AI-CONTEXT-LANGUAGE-POLICY.md` for the full policy.

## Using This Framework in Another Repo

When this context is copied into another repository:

1. Copy the needed `.ai/`, `.dev/`, `.agents/`, `.claude/`, and agent entry files.
2. Run `repo-structure-sync` immediately.
3. Rebuild repo-specific truth from the target repo's files, solution, projects, packages, infrastructure config, and existing docs.
4. Remove or rewrite source-repo-specific requirements, specs, operations docs, workflow artifacts, and ADRs.
5. Preserve framework-level rules unless the target repo clearly requires a change.

See `.ai/assets/skills/repo-structure-sync/references/migration-boundaries.md` for the detailed boundary.

## Current Cleanup Direction

Some early sample-backend and historical source-project material still exists in this repository. It should gradually be:

- deleted;
- moved into `.ai/assets/tech-stacks/dotnet-backend/`;
- rewritten as templates;
- or kept under `.dev/` only when clearly marked as historical workflow or migration artifacts.
