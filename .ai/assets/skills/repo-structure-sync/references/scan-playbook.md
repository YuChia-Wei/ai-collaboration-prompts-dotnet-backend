# Repo Init and Scan Playbook

Use this reference as the first pass after this AI context framework is copied into a target repository.

The goal is repo initialization, not product feature planning. Establish what the target repository actually is, then refresh only the copied context files that depend on repo-specific facts.

## Target Repository Modes

Classify the target before editing:

| Mode | Evidence | First Action |
| --- | --- | --- |
| Empty or near-empty repo | no solution, source, tests, or product docs yet | keep framework rules, create minimal placeholder architecture entries, and ask for stack/product direction before inventing facts |
| Existing repo | source, tests, package files, deployment config, or product docs already exist | rebuild repo-specific truth from file-backed evidence |
| Copied-template repo | framework docs exist with stale source-project names or paths | preserve framework-level rules and rewrite copied project truth |

Do not infer product domains, bounded contexts, queues, routes, or deployment topology for an empty repo.

## Evidence Order

Prefer sources in this order:

1. repository file tree
2. `*.sln`, `*.csproj`, `Directory.Packages.props`, `global.json`
3. deployment and infra config
4. existing repo README / docs
5. copied template docs that may now be stale

## Minimum Scan Checklist

Capture these facts before editing:

- top-level directories
- solution names and project count, if present
- executable projects versus libraries, if present
- primary source roots such as `src/`, `tests/`, `apps/`, `services/`
- shared kernel or building-block projects
- test frameworks and test project naming
- database, ORM, message broker, and API host packages
- container or deployment folders

## .NET Structure Hints

When the repo is .NET-based, inspect:

- target framework from `TargetFramework` or `TargetFrameworks`
- package references for EF Core, Dapper, Npgsql, Wolverine, MassTransit, MediatR, xUnit, NUnit, MSTest
- project names and folders for API, worker, consumer, contracts, shared libraries
- solution folders or naming patterns that imply bounded contexts

## Safe Inference Rules

- Folder names alone are weak evidence.
- `*.csproj` plus package references are stronger evidence.
- Startup or host projects are stronger than class library names.
- If multiple patterns exist, summarize the mixed state instead of forcing one architecture label.
- If no product files exist, preserve the AI context framework and mark product architecture as not initialized.
