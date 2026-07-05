# Historical Context Normalization Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-07-historical-context-normalization`
- `owner_skill`: `dev-workflow`
- `status`: `completed`

## Inputs

- `.dev/requirement/HISTORICAL-CONTEXT-NORMALIZATION-REQUIREMENTS.MD`
- repository identity in `README.md`, `README.en.md`, `agents.md`, and `agents.zh-tw.md`
- `repo-structure-sync` canonical spec and references

## Dependency Decision

This workflow covers repository truth and repo initialization because both operate on the same copied-context boundary.

Dotnet validator replacement phase 2 is excluded and will use a separate workflow because it changes analyzer/tooling behavior, has different validation, and should not share completion criteria with documentation migration.

## Workstreams

### 1. Governance Metadata Normalization

- Close completed workflows that still report active or omit status.
- Add implementation outcomes to completed requirements without rewriting original decisions.

### 2. Historical Product Truth Retirement

- Inventory product-specific requirements, specs, test specs, problem frames, operations files, guides, config, and indexes.
- Remove artifacts already covered by canonical templates.
- Convert only unique reusable guidance into neutral templates or explicitly labeled future-planning material.
- Remove old product names and fixed local runtime facts from active context.

### 3. Repo Structure Sync Project Config

- Add a canonical project-config template owned by `repo-structure-sync`.
- Define evidence-based generation and empty-repo behavior.
- Remove the source-product `.dev/project-config.yaml`.
- Update canonical spec, references, wrapper links, and human guide where needed.

### 4. Final Validation

- Parse workflow JSON and YAML templates.
- Search active context for retired product names and fixed credentials.
- Validate links and expected paths.
- Run `git diff --check`.

## Constraints

- Preserve React / Vite only as future multi-stack context placement guidance.
- Do not create a frontend profile or frontend skill.
- Do not rewrite historical workflow task content solely to remove old names.
- Do not retain product artifacts when canonical templates already cover the same purpose.
- Use separate coherent commits for metadata, historical truth, repo-init config, and workflow closure.

## Completion Summary

- Completed governance metadata normalization, historical product truth retirement, and repo-structure-sync project config integration.
- Removed product-specific requirements, specs, test specs, problem frames, operations truth, fixed credentials, and frontend implementation assets from active paths.
- Preserved React / Vite only as future multi-stack context placement exploration.
- Dotnet validator replacement phase 2 remains a separate next workflow.
