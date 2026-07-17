# REL-v0.4.0 — Truth Alignment And Reconstruction Contracts

## Status

Validated candidate. No `v0.4.0` tag or published commit exists yet. The declared
archive names are release targets, not evidence that packages have been built
or published. Candidate package validation used
`79db0d199016af5c17f0e47e1a821c9a69704633`; this is validation provenance,
not the eventual published commit identity.

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
- Renames the coding standards shell gate to structural integrity, expands its
  catalog coverage, and classifies every shell asset by execution role,
  lifecycle, distribution, authority, and replacement direction so packaging
  is not mistaken for semantic endorsement.
- Removes the stale test-compliance grep helper from automatic gates and marks
  it as a packaged retirement candidate for the v0.4.0 migration window.

## Compatibility

This pre-1.0 minor release intentionally changes several reusable contracts and
therefore declares breaking changes. `v0.3.0` is the governed reconciliation
source. No source version is declared safe for unattended upgrade: target-owned
truth, local overrides, renamed paths, retired examples, and copied source
includes require a reviewed dry-run plan.

The full Observability/AOP framework remains deferred in backlog item
`OBS-001`. This release only retains the bounded rule that runtime
CrossCutting/Observability concerns must not become a Domain dependency.

## Candidate Validation

The remediation workflow completed, and independent closeout assessment
`ASM-20260717-003` reported no new release-blocking findings. At candidate commit
`79db0d199016af5c17f0e47e1a821c9a69704633`:

- the composed full gate passed 21/21 required checks with zero failures or
  advisories;
- focused profile, analyzer, validation, and executable BuildingBlocks tests
  passed;
- two package builds produced byte-identical ZIP and tar.gz archives;
- archive envelopes, inventories, member checksums, external checksum sidecars,
  and ZIP/tar parity passed validation.

The candidate archives are local validation artifacts. The publication
automation will rebuild final assets from the eventual user-created tag.

## Remaining Publication Gate

Before this candidate can become published:

1. obtain user review and authorization to merge the workflow branch into
   `main` with `--no-ff`;
2. rerun release validation against the resulting immutable `main` commit;
3. let the user create and push the annotated `v0.4.0` tag on that validated
   commit;
4. let tag-triggered automation rebuild, validate, and publish the governed
   artifacts without creating, moving, or replacing the tag;
5. finalize the trusted release registry with the published tag, commit, and
   hosted-publication evidence after publication succeeds.
