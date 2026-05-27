# .ai

This directory contains agent-facing reusable AI assets. It is not the human-facing guide entry point and not the runtime installation location for a specific agent tool.

## Role

- reusable prompts
- shared rules
- automation and validation scripts
- sub-agent workflow references

## Directory Boundaries

- `.ai/`
  - reusable prompts, rules, scripts, and canonical AI assets for agents
- `.dev/guides/ai-collaboration-guides/`
  - human-facing AI collaboration guides, skill guides, prompt guides, and workflow guides
- `.ai/assets/skills/`
  - canonical skill registry and skill specs
- `.ai/assets/tech-stacks/`
  - tech-stack-specific reusable AI context
- `.agents/skills/` and `.claude/skills/`
  - repo-local runtime wrappers
- `.dev/workflows/`
  - cross-skill or sub-agent handoff artifacts

## Template Sync Rules

- Keep `.ai/` agent-facing and reusable.
- Prefer framework-level and repo-agnostic context under `.ai/assets/shared/`.
- Put stack-specific reusable context under `.ai/assets/tech-stacks/<profile>/`.
- Move project-specific source of truth back to `.dev/`.
- After copying this template into a target repo, use `repo-structure-sync` to refresh `agents.md`, `.dev/`, and needed `.ai/` entry docs from target repo facts.
- See `assets/skills/repo-structure-sync/references/migration-boundaries.md` for migration boundaries.

## Core Files

- `INDEX.MD`
  - `.ai/` navigation entry
- `SUB-AGENT-SYSTEM.MD`
  - sub-agent system and routing rules
- `DIRECTORY-RULES.MD`
  - `.ai` and `.dev` placement rules
- `assets/tech-stacks/dotnet-backend/references/CODE-REVIEW-INDEX.MD`
  - .NET backend code review entry

## Subdirectories

- `assets/`
  - canonical source for skills, sub-agent role prompts, shared packages, tech-stack profiles, and templates
- `scripts/`
  - transitional AI workflow scripts, context governance checks, and local tool orchestration helpers

## Multi-Agent Skill Storage

When using Codex, Gemini, GitHub Copilot, or Claude-compatible wrappers:

- `.ai/` is the cross-agent reusable asset root.
- `.dev/guides/ai-collaboration-guides/` is the human-facing guide root.
- `.ai/assets/skills/` is the canonical source for top-level skills.
- `.ai/assets/sub-agent-role-prompts/` is the canonical source for delegated worker roles.
- `.agents/skills/` and `.claude/skills/` are repo-local runtime wrappers.

Making a skill directly available to a local runtime is a runtime installation or wrapper sync task. Do not turn `.ai/` or `.dev/` into runtime-specific directories.

See also:

- `../.dev/guides/ai-collaboration-guides/AI-ASSET-LOCATION-STRATEGY.md`
- `../.dev/standards/AI-CONTEXT-BOUNDARY.md`
- `../.dev/standards/AI-CONTEXT-LANGUAGE-POLICY.md`


