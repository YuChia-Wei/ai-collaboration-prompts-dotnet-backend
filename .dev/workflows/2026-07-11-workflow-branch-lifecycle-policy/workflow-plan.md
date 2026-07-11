# Workflow Branch Lifecycle Policy

## Metadata

- `workflow_id`: `2026-07-11-workflow-branch-lifecycle-policy`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-11-workflow-branch-lifecycle-policy`
- `base_branch`: `main`
- `branch_segment`: `1`
- `artifact_root`: `.dev/workflows/2026-07-11-workflow-branch-lifecycle-policy`
- `created_at`: `2026-07-11T00:02:10+08:00`
- `updated_at`: `2026-07-11T00:23:58+08:00`
- `status`: `completed`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.0.0`

## Problem

- Recent AI-context workflows were created directly on `main`, so their commits did not preserve an independent workflow branch boundary.
- Existing Git flow guidance recommends short-lived branches and `--no-ff`, but the workflow gate and artifact contract do not enforce branch creation before workflow artifacts or material edits.
- A user-requested merge and push may be needed as a transport or machine-handoff checkpoint before a workflow is complete. Current rules can incorrectly imply that merge equals workflow closure.
- Workflow metadata does not record its working branch or base branch, so resume and validation cannot detect accidental work on `main`.

## Decisions

1. Every workflow-mode task uses a dedicated short-lived branch.
2. Create or switch to the workflow branch before creating workflow artifacts or making material task edits.
3. Default Codex branch naming is `codex/<workflow-id>`; other runtimes use their declared prefix.
4. Every new locator records `branch` and `base_branch`.
5. Merging or pushing an incomplete workflow is a checkpoint handoff, not closure.
6. A checkpoint handoff preserves `status: active`, pending tasks, exact continuation instructions, and push/merge evidence.
7. After a checkpoint merge, continuation starts from the updated base branch on a new dedicated continuation branch; do not continue material work directly on `main`.
8. Workflow and multi-commit branches merge with `git merge --no-ff` by default. A different strategy requires explicit user or maintainer direction.

## Scope

- Workflow gate, artifact, Git flow, and commit policies.
- Root English and Traditional Chinese agent instructions.
- Workflow-producing skill locator/plan templates and branch playbooks.
- Active human guides that describe workflow creation or merge behavior.
- Workflow validator checks for required branch metadata and branch safety.
- PyYAML-backed validation of the three recently updated runtime skills.

## Non-Goals

- Do not rewrite or rebase commits already pushed to `main`.
- Do not retroactively recreate historical workflow branches.
- Do not merge this branch into `main` unless the user requests merge closeout.
- Do not begin remediation of the separate `2026-07-10-ai-context-self-audit` findings.

## Tasks

### WBLP-001 — Validate Skills With PyYAML

- Status: completed.
- Validate `dev-workflow`, `ai-context-governance`, and `ai-context-auditor` wrappers with `skill-creator` tooling.

### WBLP-002 — Define Branch Lifecycle Policy

- Status: completed.
- Make branch-first workflow creation mandatory.
- Define checkpoint merge versus workflow closure.
- Define default `--no-ff` merge behavior.
- Add branch metadata to templates and validation.

### WBLP-003 — Validate And Close

- Status: completed.
- Validate JSON/YAML/frontmatter, workflow metadata, references, Git state, and repository quick checks.
- Commit the policy stage on the workflow branch.
- Leave merge/push for explicit user authorization.

## Acceptance Criteria

- No active policy says a workflow branch is merely preferred.
- Agents must create/switch branches before workflow artifacts or material edits.
- Locator templates and new workflows declare `branch` and `base_branch`.
- Validator rejects a new workflow missing branch metadata and rejects an active workflow whose declared branch is `main`.
- Checkpoint merge rules retain active status and continuation state.
- Default workflow merge command includes `--no-ff`.
- All three skill wrappers pass `quick_validate.py` using installed PyYAML.
- Repository quick checks pass.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-11-workflow-branch-lifecycle-policy` | `main` | N/A | N/A | N/A | N/A | Initial policy implementation | Completed locally; branch commit is the handoff point, with merge/push left to explicit request |

## Completion Summary

- Made a dedicated branch mandatory before workflow artifacts or material edits.
- Split push-only handoff from checkpoint-merge continuation so unmerged work is never resumed from an incomplete base.
- Made `--no-ff` the default workflow merge strategy and kept checkpoint handoff separate from completion.
- Added branch/base metadata validation and generalized branch history for push and merge checkpoints.
- Validated all three affected skills with PyYAML 6.0.3 and `quick_validate.py`.
- Passed workflow metadata validation, JSON/YAML parsing, `git diff --check`, and repository quick checks including 49 .NET tests.
- Merge and push were intentionally not performed because they were not requested for this workflow branch.
