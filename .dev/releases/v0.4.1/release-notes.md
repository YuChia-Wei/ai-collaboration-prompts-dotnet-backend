# REL-v0.4.1 — Executable Upgrade And Downstream Gates

## Status

Planned governed patch release. Publication remains pending immutable candidate
validation, independent verification, merge, and the user-authorized annotated
tag.

## Highlights

- Replaces the clean-install-only migration metadata emitted by v0.4.0 with a
  versioned operation set bound to the exact published v0.3.0 files manifest.
- Derives deterministic add, replace, remove, rename, and reconcile operations
  from immutable previous and incoming inventories.
- Keeps clean installation independently supported while making the declared
  v0.3.0 upgrade path executable through the extracted package planner.
- Excludes source release-governance and package-builder tests from the public
  payload while keeping them required in the source repository.
- Keeps the packaged safe-apply suite required and reports source-only checks as
  not applicable in downstream repositories.
- Preserves package, files, and migration schema version 1.0.0. This patch does
  not add a multi-source migration contract or remove a published path.

## Compatibility

This is a contract-preserving patch for the governed v0.3.0 package source.
Automatic package migration is declared only from `v0.3.0`.

Targets already on v0.4.0 should remain there and upgrade directly to v0.5.0
after the multi-source contract in `PKG-003` is published. A v0.4.0 target may
perform an explicitly reviewed manual reconciliation to v0.4.1, but v0.4.1
does not claim that path as a governed package-planner source.

Targets originating from v0.0.1 must first follow the published v0.3.0 manual
reconciliation route through the v0.1.0 and v0.2.0 contracts. After validated
v0.3.0 provenance is established, this release provides the governed automatic
v0.3.0-to-v0.4.1 package path.

## Deferred Work

- The full correction set originally assigned to v0.4.1 is moved to required
  v0.4.2 work.
- Multi-source direct upgrades, including v0.4.0-to-latest and the retained
  `dotnet-mq-arch-lab` acceptance target, are assigned to v0.5.0.

## Release Validation

Pending final immutable candidate and independent verification evidence.
