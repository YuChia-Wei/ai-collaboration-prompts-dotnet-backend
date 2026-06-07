# Dev Workflow Core/Profile Adjustment Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-06-dev-workflow-core-profile`
- `owner_skill`: `dev-workflow`
- `status`: `completed`

## Context

- Problem statement:
  - `dev-workflow` was introduced to coordinate this repository's existing skills.
  - The user wants the skill to move toward a publishable shape without overpromising quality when downstream skills are unavailable.
  - The current routing playbook directly names this repository's skills, which makes it useful locally but less portable.
- Current scope:
  - `dev-workflow` canonical spec, references, human guide, and workflow tracking.
- Why this workflow now:
  - The skill should explicitly distinguish core orchestration, repo-local routing profiles, and fallback playbooks.

## Target Direction

- Target architecture summary:
  - `dev-workflow` core defines generic workflow orchestration.
  - A local profile maps generic capability slots to this repository's concrete skills.
  - Fallback playbooks describe minimum viable checks when a downstream skill is missing.
  - The skill must state that professional stage quality depends on downstream skills or equivalent project standards.
- Key constraints:
  - Do not remove current repo-local routing value.
  - Do not claim standalone mode can match downstream specialist skill quality.
  - Keep agent-facing skill material in English.
  - Keep human-facing guide material in Traditional Chinese Taiwan usage.
- Non-goals:
  - Do not package the skill for external release in this workflow.
  - Do not redesign other skills.
  - Do not merge or delete downstream skills.

## Stages

### Stage 1: Workflow Bootstrap
- Goal:
  - Create workflow artifacts for this adjustment.
- Scope:
  - `.dev/workflows/2026-06-dev-workflow-core-profile/`.

### Stage 2: Core/Profile/Fallback Refactor
- Goal:
  - Refactor the canonical spec and references to distinguish core orchestration, local profile routing, and fallback playbooks.
- Scope:
  - `.ai/assets/skills/dev-workflow/`.

### Stage 3: Human Guide Sync
- Goal:
  - Explain standalone quality boundaries and recommended usage modes for humans.
- Scope:
  - `.dev/guides/ai-collaboration-guides/DEV-WORKFLOW-SKILL-GUIDE.md`.

### Stage 4: Final Validation
- Goal:
  - Validate JSON, references, and whitespace before commit.
- Scope:
  - Changed files only.

## Validation Strategy

- Parse task JSON files with `ConvertFrom-Json`.
- Search for `capability profile`, `fallback`, and local skill mappings.
- Run `git diff --check`.

## Notes

- Open questions:
  - None currently. The assumed direction is core + profile + fallback, not a fully detached release package yet.

## Completion Summary

- Refactored `dev-workflow` toward a portable core orchestration model.
- Added generic capability slots and local profile resolution.
- Added fallback playbooks for missing downstream skills or project standards.
- Updated runtime wrappers and the human guide to document profile-mode and fallback-mode quality boundaries.
