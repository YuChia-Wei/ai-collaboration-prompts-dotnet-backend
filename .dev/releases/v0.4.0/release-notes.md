# REL-v0.4.0 — Truth Alignment And Reconstruction Contracts

## Status

Planned candidate. No `v0.4.0` tag or published commit exists yet. The declared
archive names are release targets, not evidence that packages have been built
or published.

## Highlights

- Centralizes target-owned technology selections so products can override
  framework defaults for mocking, ORM, broker, and similar implementation
  choices without rewriting unrelated architecture rules.
- Keeps NSubstitute as the default mocking library while making the choice an
  explicit product profile rather than a universal invariant.
- Defines soft delete as the default Aggregate Repository profile, supports an
  explicit target opt-out, and preserves hard delete as a separate
  purpose-specific capability.
- Replaces historical BuildingBlocks assumptions with an interface-first
  reconstruction contract. The only retained optional base class is the
  executable-tested `EsAggregateRoot<TId>` replay/pending-event mechanism.
- Defines one logical solution grammar using
  `<workload>/DomainCore` and `<workload>/Presentation`, with workload mapped to
  a bounded context for micro-system mono repos and to a system for mono-system
  repos. Physical solution-folder layout remains target-owned.
- Aligns Controller examples and delegated guidance with asynchronous
  `ExecuteAsync`, request cancellation, typed results, and separate immutable
  DTOs.
- Reclassifies examples by machine-readable evidence tier, consolidates
  duplicate BDD and Outbox routes, and retires hollow fixture or placeholder
  material that had no executable evidence.
- Moves human migration/tooling guidance out of normative standards, retires
  legacy product-shaped prompt bodies after recording current skill routes,
  and separates README purpose from INDEX catalogs across standards and guide
  areas.
- Adds Git-backed file-disposition validation so every changed distributable
  framework path is accounted for without treating incoming intent as target
  write authorization.

## Compatibility

This pre-1.0 minor release intentionally changes several reusable contracts and
therefore declares breaking changes. `v0.3.0` is the governed reconciliation
source. No source version is declared safe for unattended upgrade: target-owned
truth, local overrides, renamed paths, retired examples, and copied source
includes require a reviewed dry-run plan.

The full Observability/AOP framework remains deferred in backlog item
`OBS-001`. This release only retains the bounded rule that runtime
CrossCutting/Observability concerns must not become a Domain dependency.

## Publication Gate

Before this candidate can become published:

1. complete the remediation workflow and independent verification assessment;
2. pass repository quick/full validation and focused .NET tests;
3. build deterministic ZIP and tar.gz artifacts from the selected immutable
   release commit and validate parity/checksums;
4. update this record with the immutable commit and completed validation
   evidence;
5. let the user create the annotated `v0.4.0` tag. Automation must not create,
   move, or replace that tag.
