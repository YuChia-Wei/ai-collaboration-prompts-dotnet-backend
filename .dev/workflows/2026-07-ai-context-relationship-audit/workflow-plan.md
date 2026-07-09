# AI Context Relationship Audit

## Purpose

Inventory document relationship problems across the AI collaboration context and produce an overall AI context governance score.

## Scope

- Root entry documents: `README.md`, `README.en.md`, `agents.md`, `agents.zh-tw.md`
- Agent-facing context: `.ai/**`
- Runtime wrappers: `.agents/**`, `.claude/**`
- Human/project governance context: `.dev/**`

## Workflow Mode Reason

Workflow mode is required because this audit uses sub-agent handoff, crosses `.ai`, `.dev`, `.agents`, and `.claude`, and may affect future AI context governance decisions.

## Classification Criteria

Use `ai-context-governance` criteria:

- Audience: `agent`, `human`, `both`
- Scope: `universal`, `dotnet-backend`, `repo-specific`, `runtime-wrapper`
- Language: `en`, `zh-TW`, `bilingual-entry`
- Action: `keep`, `split`, `move`, `rewrite`, `index-sync`, `defer`

## Tasks

1. Audit `.ai/**` canonical assets and references.
2. Audit `.agents/**` and `.claude/**` runtime wrapper sync.
3. Audit `.dev/**` governance, guides, workflow, requirement, spec, and operations relationships.
4. Aggregate findings and score overall context health.

## Validation

- Use `rg -uu` to include hidden context directories.
- Cross-check discovered issues against `.dev/standards/AI-CONTEXT-BOUNDARY.md` and `.dev/standards/AI-CONTEXT-LANGUAGE-POLICY.md`.
- Record skipped validation or deferred cleanup explicitly.
