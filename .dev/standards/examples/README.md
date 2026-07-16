# Examples (.NET)

This directory contains .NET examples and historical/reference material used by
the AI coding assistant for the Clean Architecture + DDD + CQRS stack.

## Evidence Contract

[`evidence-manifest.yaml`](evidence-manifest.yaml) is the machine-readable
classification source. Its allowed tiers and evidence requirements are defined
by [`evidence-schema.yaml`](evidence-schema.yaml).

The tiers are:

- `executable-tested`: implementation with declared build and test commands;
- `structure-validated`: structure/configuration with named validators;
- `illustrative`: explanatory snippets that are not copy-ready;
- `reference-only`: conceptual material selected on demand;
- `historical`: retained provenance and migration evidence.

Unclassified legacy material defaults to `historical`. Nothing is promoted to a
stronger tier by inference.

There is currently no directory-wide verified-template or single-source-of-truth
claim. Target package versions, technology selections, namespaces, and physical
layouts must come from target repository evidence.

## Directory Highlights

- `contract/` - Design by Contract docs and examples
- `projection/` - Read model/projection patterns
- `usecase/` - Use case interfaces + services
- `test/` - BDDfy + xUnit patterns (Gherkin-style naming)
- `bdd-gherkin-example/` - Reqnroll `.feature` examples (reference only)
- `bdd-gherkin-test/` - Reqnroll `.feature` test patterns (reference only)
- `reference/` - Reference docs

## Contract Quick Reference

```csharp
Contract.RequireNotNull("param", param);
Contract.Require(condition, "reason");
Contract.Ensure(condition, "reason");
Contract.Invariant(condition, "reason");
```
