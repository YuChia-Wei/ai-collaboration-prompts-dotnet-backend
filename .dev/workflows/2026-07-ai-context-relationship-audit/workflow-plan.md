# AI Context Relationship Audit

## Purpose

Inventory document relationship problems across the AI collaboration context, remediate the approved issues, and produce an updated AI context governance state.

## Scope

- Root entry documents: `README.md`, `README.en.md`, `agents.md`, `agents.zh-tw.md`
- Agent-facing context: `.ai/**`
- Runtime wrappers: `.agents/**`, `.claude/**`
- Human/project governance context: `.dev/**`

## Workflow Mode Reason

Workflow mode is required because this work uses sub-agent handoff, crosses `.ai`, `.dev`, `.agents`, and `.claude`, and affects future AI context governance decisions.

## Classification Criteria

Use `ai-context-governance` criteria:

- Audience: `agent`, `human`, `both`
- Scope: `universal`, `dotnet-backend`, `repo-specific`, `runtime-wrapper`
- Language: `en`, `zh-TW`, `bilingual-entry`
- Action: `keep`, `split`, `move`, `rewrite`, `index-sync`, `defer`

## Completed Audit Tasks

1. Audit `.ai/**` canonical assets and references.
2. Audit `.agents/**` and `.claude/**` runtime wrapper sync.
3. Audit `.dev/**` governance, guides, workflow, requirement, spec, and operations relationships.
4. Aggregate findings and score overall context health.

## README And INDEX Responsibility Rule

Apply this rule during remediation:

- README files explain the purpose, scope, and usage of the containing folder.
- INDEX files own file and directory inventories, including per-file or per-directory descriptions.
- When a README currently contains detailed catalog tables or path-by-path descriptions, move that catalog responsibility to the nearest INDEX instead of keeping duplicate listings.

## Remediation Roadmap

The audit produced a `76/100` overall AI context governance score. Remediation proceeds in small batches so each source-of-truth boundary can be validated independently.

### Execution Order

1. `enforce-readme-index-responsibility`
   - Establish README purpose-only and INDEX catalog-owner responsibility before link cleanup.
2. `fix-dev-entry-index-relationships`
   - Remove or correct stale `.dev` entry references before deeper content work.
3. `settle-dev-specs-domains-contract`
   - Decide whether `.dev/specs/domains/` is an active production-spec root or a template-only concept.
4. `settle-dev-operations-truth-contract`
   - Align operations guides with actual canonical operation truth files or explicitly template-scope them.
5. `normalize-ai-entry-language`
   - Rewrite agent-facing `.ai` entry docs to English and preserve zh-TW explanation only in human-facing guides.
6. `repair-sub-agent-human-guide-routing`
   - Repoint or rename sub-agent manifest guide fields so human-facing links target `.dev/guides/**`.
7. `split-sub-agent-system-active-routing`
   - Separate active sub-agent routing from roadmap, TODO, and retired compatibility notes.
8. `label-runtime-wrapper-metadata`
   - Clarify runtime-only metadata under wrapper trees if ambiguity remains after the higher-impact fixes.

### Commit Boundaries

Commit after each completed task or coherent pair of small tasks once validation passes. Do not batch `.ai` language rewrites with `.dev` index fixes unless the user asks to complete the full workflow in one coordinated pass.

### Shared Validation

Each remediation task should run the narrowest relevant checks:

- `git diff --check`
- JSON parse for changed task files
- targeted `rg -n -uu` reference searches for changed paths
- hidden-directory inventory with `rg --files -uu` when indexes or wrapper references change
