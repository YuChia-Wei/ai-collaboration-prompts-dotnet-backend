# Dotnet-Native Validation Strategy

## Position

The repository should stop using shell scripts as the final authority for C# semantic validation when dotnet-native mechanisms can represent the rule more accurately.

Shell and PowerShell scripts may remain when they are workflow glue, context governance checks, file-system automation, or tool orchestration.

## Validation Layers

| Layer | Use For | Example |
| --- | --- | --- |
| `.editorconfig` | Formatting, style, analyzer severity, naming where built-in support is enough | nullable/style severity, naming rules, generated code exclusions |
| Built-in .NET analyzers | General C# quality and framework guidance | `AnalysisLevel`, `EnforceCodeStyleInBuild`, Microsoft code quality rules |
| Roslyn analyzers | C# syntax and semantic rules tied to DDD/CA/CQRS conventions | repository interfaces, aggregate dependencies, use case constructor/handler shape |
| Architecture tests | Cross-project, namespace, assembly, or layer dependency boundaries | Domain must not reference Infrastructure; Presentation must not instantiate handlers directly |
| Unit/integration tests | Runtime behavior, DI, config, startup, profile, broker/db integration | profile startup, DI registration, options binding |
| Dotnet tools | Repo/file/spec/context checks that are not C# semantic analysis | spec-to-file existence, Dockerfile csproj sync, context portability lint |
| Shell/PowerShell orchestrators | Local or CI glue that invokes the above tools | `check-all.sh` as a thin runner |

## AI Reasoning Context Is Preserved

Roslyn analyzers and CI gates cannot replace software engineering judgement.

Keep theory and design context for:

- DDD aggregate modelling;
- Clean Architecture boundary reasoning;
- CQRS tradeoff analysis;
- BDD scenario design;
- code review judgement;
- architecture decision framing;
- prompt and skill routing.

Skills such as `bdd-gwt-test-designer`, `code-reviewer`, and `ddd-ca-hex-architect` should continue to use the engineering theory context in `.ai`, `.dev`, and skill references.

## First Source-Included Analyzer Shape

Initial implementation should live in this repository and be usable as a source-included template.

Suggested future structure:

```text
tools/
  DotnetBackendAnalyzers/
    DotnetBackendAnalyzers.csproj
    Rules/
      Repository/
      UseCases/
      Aggregates/
    Tests/
      DotnetBackendAnalyzers.Tests.csproj
```

The analyzer project should be split into another repo only after the rule set and AI context integration stabilize.

Current bootstrap:

- `tools/DotnetBackendAnalyzers/`
- `tools/DotnetBackendAnalyzers.Tests/`
- `DBA1001` repository query method rule
- `DBA1002` use case / handler `IServiceProvider` injection rule
- `DBA1003` aggregate/entity infrastructure dependency rule

## First Analyzer Rule Families

### Repository Rules

Target current `check-repository-compliance.sh` behavior, then refine semantics:

- forbid custom query methods on domain repositories when the profile requires projection/inquiry/archive;
- require repository abstractions to follow the selected generic repository pattern when applicable;
- detect repository interfaces/classes using syntax and symbol analysis instead of filename grep.

Bootstrap coverage: `DBA1001` reports query-style methods on domain repository interfaces while allowing identity lookup methods.

### Use Case Rules

Target current `check-usecase-compliance.sh` behavior, then refine:

- forbid service locator style patterns such as `IServiceProvider` injection where not allowed;
- require explicit dependencies through constructor parameters;
- validate handler/use case public entry point shape by symbol, not text pattern;
- detect direct infrastructure calls when architecture boundaries forbid them.

Bootstrap coverage: `DBA1002` reports `IServiceProvider` constructor injection on use case or handler classes.

### Domain Entity / Aggregate Rules

Target current `check-aggregate-compliance.sh` behavior, then refine:

- forbid infrastructure dependencies such as `DbContext` in aggregates/entities;
- validate domain event application conventions where the target profile requires them;
- validate guard/invariant usage only where the rule can be expressed without forcing one implementation style.

Bootstrap coverage: `DBA1003` reports `DbContext` references in classes that look like aggregates/entities.

## CI Gate Model

Formal gates should run through dotnet-native commands:

```bash
dotnet restore
dotnet build
dotnet test
dotnet format --verify-no-changes
```

Analyzer diagnostics that represent hard rules should be configured as build errors through project configuration or `.editorconfig`.

Architecture tests should fail through `dotnet test`.

Mutation testing can remain a separate, slower gate such as nightly or release validation.

## AI Review Aid Model

AI review aid is not a CI gate. It should:

- preserve software engineering reasoning;
- read analyzer/test outputs when available;
- point the AI agent to relevant skill references and design checklists;
- help produce review tables, risk framing, and recommendations;
- avoid pretending that regex scripts are authoritative semantic validation.

## Script Retention Policy

Keep shell/PowerShell when:

- the script invokes dotnet-native tools;
- the script validates non-C# text or repository context;
- the script automates file-system or environment checks;
- the script is temporary glue while a dotnet-native replacement is being built.

Retire or replace shell/PowerShell when:

- it uses `grep`, `find`, or filename matching to decide C# architecture correctness;
- it duplicates an `.editorconfig`, analyzer, formatter, test, or dotnet tool responsibility;
- it is generated from markdown examples and used as a formal quality gate.
