# Script To Validator Mapping

## Mapping Rules

- Use Roslyn analyzers for C# syntax, symbols, attributes, member signatures, type references, and forbidden API usage.
- Use architecture tests for assembly, namespace, project, and layer dependency boundaries.
- Use `.editorconfig` and `dotnet format` for formatting, style, and built-in analyzer severity.
- Use dotnet tests/tools for runtime config, file-system, spec, Dockerfile, prompt, and context checks.
- Keep shell/PowerShell only as orchestration or glue when it does not replace dotnet-native C# validation.

## Direct Mapping

| Current asset | Replacement target | Notes |
| --- | --- | --- |
| `check-repository-compliance.sh` | Roslyn analyzer first batch | Replace filename/grep checks with symbol-aware repository diagnostics. |
| `check-usecase-compliance.sh` | Roslyn analyzer first batch + architecture tests | Analyzer for handler/use case shape; architecture tests for layer boundaries. |
| `check-aggregate-compliance.sh` | Roslyn analyzer first batch | Analyzer for aggregate/entity dependencies and domain rules. |
| `check-controller-compliance.sh` | Roslyn analyzer + architecture tests | Analyzer for direct `DbContext`, `SaveChanges`, handler construction; architecture tests for Presentation boundary. |
| `check-mapper-compliance.sh` | Roslyn analyzer | Analyzer for mapper class shape and forbidden dependencies. |
| `check-projection-compliance.sh` | Roslyn analyzer + architecture tests | Analyzer for read-model/projection code patterns; architecture tests for dependency direction. |
| `check-archive-compliance.sh` | Roslyn analyzer | Only if archive conventions remain in the dotnet-backend profile. |
| `check-test-compliance.sh` | `.editorconfig`, Roslyn analyzer, test architecture rules | Split framework/package bans, naming, base test class, and substitute usage by target mechanism. |
| `check-test-di-compliance.sh` | Roslyn analyzer + test architecture rules | Replace DI pattern grep with analyzer/test checks. |
| `check-data-class-annotations.sh` | Roslyn analyzer | Attribute and symbol rules belong in analyzer. |
| `check-domain-events-compliance.sh` | Roslyn analyzer | Event shape and forbidden legacy interfaces belong in analyzer. |
| `check-framework-api-compliance.sh` | Roslyn analyzer | Forbidden/required framework API usage belongs in analyzer. |
| `check-dotnet-config.sh` | Dotnet tool/test + analyzer split | Package/config scanning to dotnet tool; source API usage to analyzer. |
| `check-projection-config.sh` | Dotnet tool/test + analyzer split | Config/file checks to dotnet tool; C# usage to analyzer. |
| `check-spec-compliance.sh` | Dotnet spec compliance tool | Reads spec and repo files; not a Roslyn analyzer concern unless it compiles semantic model from projects. |
| `check-dockerfile-csproj-copy-sync.ps1` | Dotnet tool or CI file validation | Keep PowerShell short term; can become dotnet repo validation tool. |
| `check-mutation-coverage.sh` | Stryker.NET config + CI orchestration | Keep only as local runner if useful. |
| `test-profile-startup.sh` | Integration/smoke tests | Shell can remain as local convenience until tests cover it. |
| `validate-dual-profile-config.sh` | Integration/config tests or dotnet tool | Keep only if dotnet test/tool replacement is not yet available. |
| `check-prompt-portability.sh` | AI context lint script or dotnet context-lint tool | Keep as AI workflow script for now; not C# validation. |
| `check-coding-standards.sh` | AI context lint script or dotnet context-lint tool | Keep as docs/context consistency lint, not C# semantic validation. |
| `check-all.sh` | Thin orchestrator | Future target is to call dotnet restore/build/test/format/analyzers/tools. |
| `code-review.sh` | Analyzer/test/report collector + AI review helper | Future target is to collect diagnostics and route AI to relevant context; not regex validation. |
| `generate-check-scripts-from-md.sh` | Retire | Replace with analyzer authoring workflow and docs. |
| `parse-md-rules.py` | Retire | Retire with markdown-to-shell generator. |
| `MD-SCRIPT-GENERATION-GUIDE.md` | Replace/archive | Replace with analyzer authoring guide or archive as historical artifact. |
| `.ai/scripts/generated/*` | Retire | Generated regex checks should not remain formal validation assets. |

## First Backlog

### Analyzer Backlog

1. Repository analyzer rules. Bootstrap rule: `DBA1001`.
2. Use case analyzer rules. Bootstrap rule: `DBA1002`.
3. Aggregate/domain entity analyzer rules. Bootstrap rule: `DBA1003`.

### Architecture Test Backlog

1. Domain project must not depend on infrastructure/presentation projects.
2. Presentation must not instantiate handlers/use cases directly.
3. Use case/application layer must not violate selected dependency boundaries.

### Dotnet Tool/Test Backlog

1. Spec-to-implementation existence validation.
2. Dockerfile csproj copy sync.
3. Context portability lint for shared AI assets.
4. Profile startup and dual-profile config validation.

## Transitional Orchestrator Target

`check-all.sh` should eventually become:

```bash
dotnet restore
dotnet build
dotnet test
dotnet format --verify-no-changes
dotnet tool run repo-context-lint
```

It should not call generated grep-based C# checks once analyzer/test replacements exist.

## Transitional Code Review Target

`code-review.sh` should eventually:

- collect changed files;
- run dotnet-native validation;
- summarize analyzer/test output;
- point the AI agent to the relevant skill references;
- avoid deciding C# architecture compliance through regex.
