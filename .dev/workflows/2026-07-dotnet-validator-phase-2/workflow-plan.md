# Dotnet Validator Phase 2 Workflow

## Metadata

- `plan_id`: `workflow-plan-2026-07-dotnet-validator-phase-2`
- `owner_skill`: `dev-workflow`
- `status`: `in_progress`

## Inputs

- `.dev/requirement/DOTNET-VALIDATOR-PHASE-2-REQUIREMENTS.MD`
- `.dev/workflows/2026-05-dotnet-script-to-analyzer-transition/script-to-validator-mapping.md`
- `.dev/standards/coding-standards/controller-standards.md`

## Scope

- Implement controller diagnostics `DBA1004` through `DBA1006`.
- Add analyzer tests.
- Remove controller grep scripts and update orchestration/docs.

## Non-Goals

- No cross-assembly architecture tests.
- No mapper, projection, archive, test, or config validator migration.
- No generated-check framework retirement until remaining replacements exist.

## Validation

- `dotnet test tools/DotnetBackendAnalyzers.Tests/DotnetBackendAnalyzers.Tests.csproj`
- controller script/reference search
- JSON and Markdown checks
- `git diff --check`

## Completion Summary

- Pending.
