# Dotnet Backend Analyzers

Source-included Roslyn analyzer template for this AI context framework's .NET backend profile.

Current diagnostics:

- `DBA1001`: domain repositories should not expose query-style methods.
- `DBA1002`: use cases or handlers should not inject `IServiceProvider`.
- `DBA1003`: aggregates/entities should not reference infrastructure types such as `DbContext`.
- `DBA1004`: concrete controller classes should declare `ApiControllerAttribute`.
- `DBA1005`: controllers should not reference `DbContext` or call `SaveChanges`.
- `DBA1006`: controllers should not directly construct handler or use-case types.
- `DBA1007`: object mappers should be static classes.
- `DBA1008`: object mappers should not depend on repositories, use cases, or handlers.

`DBA1004` through `DBA1006` replace the former controller grep compliance script. `DBA1007` and `DBA1008` replace the former mapper grep compliance scripts.

Analyzers do not replace AI software engineering reasoning context used by review and architecture skills.

## Run Tests

```bash
dotnet test tools/DotnetBackendAnalyzers.Tests/DotnetBackendAnalyzers.Tests.csproj
```

## Source-Included Usage Direction

For now this project is intended to travel with the AI context framework as source. Do not package it as NuGet until the rules and AI skill integration stabilize.

## Wire Into A Target Repo

After copying this analyzer source into a target repo, wire it into target projects through `Directory.Build.props`.

Use:

- `templates/Directory.Build.props.snippet`

The snippet adds the analyzer project as a `ProjectReference` with:

- `OutputItemType="Analyzer"`
- `ReferenceOutputAssembly="false"`
- `PrivateAssets="all"`

This lets target projects receive analyzer diagnostics during `dotnet build` without referencing the analyzer as a runtime assembly.
