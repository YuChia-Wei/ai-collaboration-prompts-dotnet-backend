# AI Context Tool Evidence Boundary

## Workflow Metadata

- `workflow_id`: `2026-07-13-ai-context-tool-evidence-boundary`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-13-ai-context-tool-evidence-boundary`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `remediation-planning`
- `artifact_root`: `.dev/workflows/2026-07-13-ai-context-tool-evidence-boundary`
- `created_at`: `2026-07-13T22:29:17+08:00`
- `updated_at`: `2026-07-13T22:29:17+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.1.0`

## Objective And Scope

- Problem statement: AI-context skills must not treat code graph, codebase memory, IDE indexes, or other optional discovery tools as authoritative evidence. Tool-specific omissions such as `.claude/**` exclusion or missing Markdown link relationships can otherwise distort audits and make the skills unusable for team members with different tooling.
- Authorized remediation scope: define a tool-neutral evidence boundary; update AI-context skill contracts and runtime wrappers; add deterministic fallback checks for excluded roots and unsupported Markdown relationships; document the observed Codebase Memory MCP limitations without making that product a required dependency.
- Exclusions: product source and test review; adoption of `.dev/assessments/`; persistent Codebase Memory artifacts; installing or configuring third-party tools; changing Codebase Memory itself.
- Completion criteria:
  - AI-context skills describe optional discovery accelerators as non-authoritative hints.
  - Findings require direct file-backed or deterministic validator evidence independent of a specific external tool.
  - Known tool omissions can be checked quickly with repository-native commands or validators.
  - Canonical specs and runtime wrappers remain synchronized.
  - Repository validators pass and the workflow is committed.

## Evidence Freeze

- The Codex-side MCP instruction was active in this session and the Codebase Memory MCP tools were callable.
- The repository was not indexed automatically; a manual `full` index created 10,002 nodes and 13,461 edges.
- The index exposed 309 Markdown file nodes and 3,090 Markdown section nodes across 306 Markdown files.
- The indexer explicitly excluded `.claude/`.
- Markdown headings were queryable, while Markdown document-link relationships were not represented as graph edges in the observed schema.
- No repository `.codebase-memory/` artifact or active Git hook was created by the test.

## Task Plan

| Task | Purpose | Status | Validation |
| --- | --- | --- | --- |
| `TOOLB-001` | Define the canonical tool-neutral evidence and fallback-verification contract. | `in_progress` | Direct policy inspection and targeted searches. |
| `TOOLB-002` | Apply the contract to AI-context skills, wrappers, guides, and validation surfaces. | `pending` | Skill/context/workflow validators and quick repository checks. |

## Artifact Contract

- This is a policy and skill-contract remediation workflow; no baseline or post-remediation audit report is required.
- Tasks: `.dev/workflows/2026-07-13-ai-context-tool-evidence-boundary/tasks/`
- Durable evidence and decisions are recorded in this plan and task results.

## Resume Checkpoint

- Last completed action: Created the dedicated branch and durable workflow locator.
- Current task: `TOOLB-001`
- Exact next action: Inventory current AI-context skill evidence rules and select the smallest canonical policy surface.
- Validation already completed: Git state was clean on `main`; Codebase Memory MCP Markdown capability was probed without repository mutation.
- Git state: workflow files are newly created and uncommitted on the dedicated branch.
- Branch history and checkpoint handoffs: segment 1 started from `main` at `5991365`.
- Blockers or unresolved decisions: none.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-13-ai-context-tool-evidence-boundary` | `main` | started | `5991365` | local | `2026-07-13T22:29:17+08:00` | Implement the authorized AI-context tool evidence boundary. | Continue `TOOLB-001`. |
