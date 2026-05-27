# Dotnet Script To Analyzer Transition Workflow

Status: completed

## Goal

Reclassify `.ai/scripts` and migrate C# semantic validation away from grep-based shell scripts toward dotnet-native validation mechanisms.

The goal is not to remove every shell or PowerShell script. The goal is to remove or downgrade scripts that use plain-text analysis for checks better handled by Roslyn analyzers, `.editorconfig`, `dotnet format`, architecture tests, integration tests, or dotnet tools.

## Decisions Already Made

- Analyzer and validation source should live in this repository first.
- The first analyzer distribution model is source-included template, not NuGet package.
- Analyzer and AI context should evolve together during the transition.
- The first formal validation candidates are:
  - repository rules;
  - use case rules;
  - domain entity / aggregate rules.
- AI reasoning context must remain available for skills such as `bdd-gwt-test-designer`, `code-reviewer`, and `ddd-ca-hex-architect`.
- Software engineering theory, design judgement, and review reasoning are not CI gates and are not replaced by Roslyn analyzers.
- Shell or PowerShell scripts may remain when they are workflow glue, repo/file automation, context linting, tool orchestration, or non-C# semantic checks.
- `check-all.sh` may remain as an orchestrator, but not as a C# regex validation engine.
- `code-review.sh`, if kept, should become an analyzer/test/report collector and AI review helper, not a C# regex validator.
- `check-prompt-portability.sh` is not dotnet code validation. It should be evaluated as AI context governance / portability lint before removal.

## Classification Model

Use these target classes:

| Class | Meaning |
| --- | --- |
| `keep-ai-workflow-script` | Shell/PowerShell is acceptable because the script supports AI workflow, context governance, repo glue, or non-C# semantic checks. |
| `keep-as-orchestrator` | Script may remain only as a thin runner for dotnet-native tools and reports. |
| `replace-with-roslyn-analyzer` | Current script checks C# syntax/semantics that should become Roslyn diagnostics. |
| `replace-with-architecture-test` | Current script checks project, namespace, or layer dependencies that fit architecture tests. |
| `replace-with-dotnet-tool-or-test` | Current script checks files, specs, runtime config, startup, or environment behavior better handled by a dotnet tool or test. |
| `retire-generated-regex-check` | Generated grep checks should be removed after analyzer/test coverage exists. |
| `needs-decision` | More context is required before a stable target can be assigned. |

## Stages

1. Bootstrap workflow artifacts.
2. Inventory `.ai/scripts` and classify each script.
3. Define dotnet-native validation strategy.
4. Map scripts to analyzer, architecture test, dotnet tool, orchestrator, or retirement targets.
5. Update script README and context indexes to reflect transitional status.
6. Update skill and guide routing so AI agents keep engineering reasoning context while executable C# validation moves to dotnet-native mechanisms.
7. Final validation and commit summary.

## Non-Goals For This Workflow

- Do not remove C# validation scripts until the replacement path is documented.
- Do not claim Roslyn analyzer coverage before analyzer rules exist.
- Do not remove software engineering theory context used by AI skills.
- Do not split analyzer code into a separate repository yet.

## Commit Policy

Use `.dev/standards/GIT-COMMIT-POLICY.md`.

No issue number is currently assigned, so commits use:

```text
<type>(<scope>): <summary>
```

Workflow-stage commits include `Why`, `What`, `Validation`, and `Workflow` body sections.

## Completion Criteria

- Every current `.ai/scripts` file has a documented transition class.
- The target dotnet-native validation strategy is documented.
- `check-all.sh`, `code-review.sh`, and generated regex checks have explicit future roles.
- AI reasoning context is explicitly preserved as separate from executable validation gates.
- Script README and indexes no longer imply grep-based C# checks are the final validation mechanism.
- Validation passes for JSON task files, markdown whitespace, and updated references.

## Completion Summary

- Inventoried `.ai/scripts` and classified each script into AI workflow, orchestrator, analyzer, architecture test, dotnet tool/test, generated regex retirement, or update-needed targets.
- Defined dotnet-native validation strategy while explicitly preserving AI software engineering reasoning context.
- Mapped the first analyzer backlog to repository, use case, and domain entity / aggregate rules.
- Rewrote `.ai/scripts/README.md` to mark scripts as transitional workflow/context/orchestration helpers.
- Updated skill and guide routing so transitional `.ai/scripts` are not treated as final C# semantic validation.
- Fixed current code review index references to the dotnet-backend reference path.
- Created the first source-included Roslyn analyzer template under `tools/DotnetBackendAnalyzers/`.
- Added initial analyzer tests for repository, use case, and aggregate/entity rules.
- Fixed `global.json` from invalid `10.0.0` SDK version to installed feature band `10.0.300`.
