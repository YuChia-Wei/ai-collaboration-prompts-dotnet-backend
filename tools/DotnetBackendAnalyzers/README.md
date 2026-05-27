# Dotnet Backend Analyzers

Source-included Roslyn analyzer template for this AI context framework's .NET backend profile.

The first rules intentionally mirror only the highest-priority transition targets from `.ai/scripts`:

- `DBA1001`: domain repositories should not expose query-style methods.
- `DBA1002`: use cases or handlers should not inject `IServiceProvider`.
- `DBA1003`: aggregates/entities should not reference infrastructure types such as `DbContext`.

These analyzers replace grep-based C# semantic checks over time. They do not replace AI software engineering reasoning context used by review and architecture skills.

## Run Tests

```bash
dotnet test tools/DotnetBackendAnalyzers.Tests/DotnetBackendAnalyzers.Tests.csproj
```

## Source-Included Usage Direction

For now this project is intended to travel with the AI context framework as source. Do not package it as NuGet until the rules and AI skill integration stabilize.
