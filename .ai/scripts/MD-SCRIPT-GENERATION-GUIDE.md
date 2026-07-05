# Markdown-Based Script Generation Guide

## Status

This mechanism is deprecated for C# architecture enforcement.

Markdown remains the human-readable source of repository-pattern decisions, but
regular-expression extraction cannot determine type inheritance, Aggregate Root
constraints, compatibility interfaces, or read/write capability boundaries.
Repository compliance is therefore enforced by the Roslyn analyzer under
`tools/DotnetBackendAnalyzers`.

Do not generate or maintain repository checks from Markdown. In particular, do not
infer that every interface whose name contains `Repository` is writable or that
domain-specific repository names are inherently invalid.

## Current Repository Contract

- Aggregate writes use `IAggregateRepository<TAggregate, TId>`.
- `IDomainRepository<TAggregate, TId>` is a compatibility alias and must inherit
  the canonical interface.
- Both canonical and derived write interfaces target Aggregate Roots only.
- The portable write contract exposes `FindByIdAsync` and `SaveAsync`.
- Read ports inherit `IQueryRepository` and expose no write operations.
- Public generic writable CRUD repositories are prohibited.
- Batch ports are target-specific and require measured need plus explicit execution
  semantics.

See
[Repository Standards](../../.dev/standards/coding-standards/repository-standards.md)
for the complete policy and the analyzer tests for executable examples.

## Remaining Generator Scope

The generic Markdown parser and generator are transitional assets for non-semantic,
non-C# checks only. They must not be presented as a formal substitute for Roslyn
analysis. The legacy repository shell checks are retired as part of the repository
analyzer alignment workflow.
