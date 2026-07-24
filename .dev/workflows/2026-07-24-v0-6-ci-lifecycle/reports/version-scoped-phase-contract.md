# Version-Scoped Release Phase Contract

## Decision

The owner approved one immutable phase contract per stable release:
`.dev/releases/<version>/release-phase-checks.yaml`.

## Implemented Boundary

- The published v0.5.0 commands moved with the v0.5.0 release record.
- v0.6.0 owns a separate command set without creating a release candidate.
- The release-state validator resolves the requested stable version instead of
  accepting a singleton or a hard-coded v0.5.0 command.
- A release handoff records `release_phase_check.version`; the checkpoint
  validator resolves that version's contract and verifies both release identity
  and exact command equality.
- Canonical release-publication templates now include the version-owned phase
  contract.

## Validation

- Release-state phase contract tests: 18 passed.
- Workflow handoff contract tests: 20 passed.
- Registered handoff checkpoints: 2 passed.
- Workflow artifact metadata: passed.
- Git diff whitespace validation: passed.
- Quick aggregate gate: 44 required checks passed, 0 failed, 2 not
  applicable. The retained downstream integration fixture and Windows symlink
  fixture were skipped by their declared environment conditions.

The push handoff will separately record a fresh critical-gate observation after
the implementation commit.

## Hosted Boundary

The authorized branch push can prove remote transport and any push-triggered
checks. It cannot prove pull-request supersession/cancellation or tag-owned
artifact transfer. Those remain required hosted evidence before CI-001 and
CI-002 can close.
