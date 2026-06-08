# Skill Naming and Domain Language Requirement Drafting Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-06-requirements-skill-naming-domain-language`
- `owner_skill`: `requirement-author`
- `status`: `completed`

## Context

- Problem statement:
  - The current refactor implementer skill names can mislead agents into routing feature work, bug fixes, or remediation work as refactoring.
  - Domain ubiquitous language needs a template, standards, and storage area, while technical glossary work should be deferred.
  - The repository identity is clearer after recent dev-workflow and context governance work, so the next changes should be grounded in requirement documents before implementation.
- Current scope:
  - Draft requirements only.
  - Do not rename skills or create glossary files yet.
- Why this workflow now:
  - The user wants requirement-author to clarify decisions and recommended approach before dev-workflow drives implementation.

## Target Direction

- Target architecture summary:
  - Create one requirement for implementation skill naming and test authoring decisions.
  - Create one requirement for domain ubiquitous language template, standards, and storage area.
  - Record decisions required from the user before implementation.
- Key constraints:
  - Use `requirement-author`.
  - Stop at requirement quality.
  - Do not update root agents unless the repository purpose is unclear or current guidance is misleading.
- Non-goals:
  - No skill rename implementation.
  - No new test author skill implementation.
  - No technical glossary implementation.
  - No agents.md rewrite unless needed.

## Stages

### Stage 1: Repository Context Check
- Goal:
  - Confirm whether root repository identity is clear enough to avoid root agent updates.
- Result:
  - README and agents already define the repository as an AI collaboration knowledge base and reusable context framework.
  - No root agents update is required for this requirement drafting pass.

### Stage 2: Skill Naming Requirement
- Goal:
  - Draft requirement for renaming refactor implementer skills and evaluating test author/writer needs.

### Stage 3: Domain Language Requirement
- Goal:
  - Draft requirement for domain ubiquitous language templates, standards, and storage area while deferring technical glossary work.

### Stage 4: Validation
- Goal:
  - Validate JSON, changed references, and whitespace.

## Validation Strategy

- Parse task JSON files with `ConvertFrom-Json`.
- Search for new requirement titles and open decision sections.
- Run `git diff --check`.

## Completion Summary

- Added requirements for implementation skill naming and domain ubiquitous language management.
- Documented user decisions and recommended approaches in both requirement files.
- Assessed root repository identity and decided not to update agents in this pass.
