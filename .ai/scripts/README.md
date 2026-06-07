# AI Scripts

This directory contains transitional AI workflow scripts, context governance checks, and local tool orchestration helpers.

It is no longer the long-term home for authoritative C# semantic validation. Rules that inspect C# syntax, symbols, type dependencies, attributes, or framework API usage should move to dotnet-native validation mechanisms such as Roslyn analyzers, `.editorconfig`, `dotnet format`, architecture tests, integration tests, or dotnet tools.

## Current Transition

Workflow: `.dev/workflows/2026-05-dotnet-script-to-analyzer-transition/`

Key files:

- `script-inventory.md`
- `dotnet-validation-strategy.md`
- `script-to-validator-mapping.md`

## Retention Policy

Shell or PowerShell scripts may remain when they are:

- AI workflow glue;
- prompt or context portability checks;
- repository file-system automation;
- local or CI orchestration over dotnet-native tools;
- non-C# semantic checks.

Shell or PowerShell scripts should be retired or replaced when they:

- use grep/find/plain-text matching to decide C# architecture correctness;
- duplicate `.editorconfig`, built-in analyzers, Roslyn analyzers, `dotnet format`, architecture tests, or dotnet tests;
- generate regex-based C# validation scripts from markdown and present them as formal gates.

## Script Classes

### Keep As AI Workflow Or Context Governance

- `check-prompt-portability.sh`
- `check-coding-standards.sh`

These scripts inspect AI context, markdown, prompt portability, or repository hygiene. They are not substitutes for dotnet C# validation.

### Keep As Orchestrator Only

- `check-all.sh`
- `code-review.sh`

These may remain as local workflow entry points, but their future role is to invoke dotnet-native validation and summarize outputs. They should not remain regex-based C# validators.

Future `check-all.sh` shape:

```bash
dotnet restore
dotnet build
dotnet test
dotnet format --verify-no-changes
dotnet tool run repo-context-lint
```

Current transitional behavior:

- runs `dotnet test tools/DotnetBackendAnalyzers.Tests/DotnetBackendAnalyzers.Tests.csproj`;
- still runs legacy grep-based C# checks until analyzer coverage is wired into target projects;
- labels first-batch grep checks as transitional.

### Replace With Roslyn Analyzer Or Architecture Tests

- `check-repository-compliance.sh`
- `check-usecase-compliance.sh`
- `check-aggregate-compliance.sh`
- `check-controller-compliance.sh`
- `check-mapper-compliance.sh`
- `check-projection-compliance.sh`
- `check-archive-compliance.sh`
- `check-test-compliance.sh`
- `check-test-di-compliance.sh`
- `check-data-class-annotations.sh`
- `check-domain-events-compliance.sh`
- `check-framework-api-compliance.sh`

First analyzer batch:

1. repository rules: bootstrap coverage exists as `DBA1001`;
2. use case rules: bootstrap coverage exists as `DBA1002`;
3. domain entity / aggregate rules: bootstrap coverage exists as `DBA1003`.

Analyzer source template:

- `tools/DotnetBackendAnalyzers/`
- `tools/DotnetBackendAnalyzers.Tests/`

### Replace With Dotnet Tool Or Tests

- `check-dockerfile-csproj-copy-sync.ps1`
- `check-dotnet-config.sh`
- `check-projection-config.sh`
- `check-spec-compliance.sh`
- `check-mutation-coverage.sh`
- `test-profile-startup.sh`
- `validate-dual-profile-config.sh`

These are not necessarily Roslyn analyzer rules. They belong in dotnet tools, integration tests, config tests, Stryker.NET configuration, or CI orchestration.

### Retire Generated Regex Checks

- `generate-check-scripts-from-md.sh`
- `parse-md-rules.py`
- `MD-SCRIPT-GENERATION-GUIDE.md`
- `generated/`

These assets generate or document grep-based C# checks from markdown. They should be retired once analyzer/test replacements exist.

## AI Reasoning Context

Do not remove software engineering reasoning context from `.ai`, `.dev`, or skills as part of this transition.

Analyzers and CI gates can enforce formalizable rules, but they do not replace design reasoning used by:

- `bdd-gwt-test-designer`;
- `code-reviewer`;
- `ddd-ca-hex-architect`;
- requirement/spec/problem-frame authoring skills.

The context remains useful even when executable validation moves to dotnet-native tooling.

## Related Files

- `.dev/workflows/2026-05-dotnet-script-to-analyzer-transition/script-inventory.md`
- `.dev/workflows/2026-05-dotnet-script-to-analyzer-transition/dotnet-validation-strategy.md`
- `.dev/workflows/2026-05-dotnet-script-to-analyzer-transition/script-to-validator-mapping.md`
- `.ai/assets/tech-stacks/dotnet-backend/README.MD`
- `.dev/standards/AI-CONTEXT-BOUNDARY.md`
