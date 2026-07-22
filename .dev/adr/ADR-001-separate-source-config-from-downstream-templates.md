# ADR-001: Separate Source Repository Configuration From Downstream Templates

## Status

Proposed

## Date

2026-07-23

## Context

The source repository currently uses its root `.editorconfig` and
`.gitattributes` both to govern its own checkout and as `target-template` files
in the published package. Those responsibilities are no longer equivalent.

The source repository needs rules for dated assessments, immutable external
evidence, release tooling, and cross-host maintenance. A downstream project
needs portable seed defaults that become target-owned after initialization.
Putting source-only path rules in a file that is copied directly downstream
leaks repository history and prevents either side from evolving independently.

The immediate trigger was an externally supplied Markdown report whose original
CRLF bytes and recorded SHA-256 were unintentionally normalized. A narrow local
`.gitattributes` fixed that instance, but copying such files into every evidence
directory would scatter policy. Treating every external file as binary would
also remove useful text diffs without a demonstrated integrity requirement.

Alternatives considered:

1. Continue packaging the source root files and prohibit source-specific rules.
2. Normalize every external text input to LF and give up byte provenance.
3. Treat every assessment evidence file as binary and lose useful text diffs.
4. Separate source and downstream configuration ownership, then preserve only
   explicitly classified immutable originals byte-for-byte.

## Decision

Propose separate ownership for repository integration configuration:

- Root `.editorconfig` and `.gitattributes` govern this source repository only.
- Downstream `.editorconfig` and `.gitattributes` are dedicated
  `repo-structure-sync` public-root templates mapped to target root paths.
- Downstream copies retain `target-template` / `seed` behavior and become
  target-owned after initialization; upgrades do not silently overwrite them.
- Source-only path rules are centralized in source root configuration and must
  not appear in downstream template bytes.
- External origin alone does not imply binary treatment. Only content explicitly
  classified as immutable original evidence, with a provenance or digest need,
  is stored under `evidence/external/original/` and byte-preserved.
- Normalized assessments, ordinary external references, and repository-native
  JSON or logs remain text-normalized and diffable.

This decision remains Proposed until `CFG-001` proves package, migration,
cross-platform, and evidence-policy consequences and the owner selects either a
v0.5.1 patch or v0.6.0 implementation horizon.

## Consequences

### Positive

- Source governance can evolve without leaking source-only paths downstream.
- Linux, macOS, and Windows contributors receive one coherent source text rule.
- Downstream defaults become explicit package assets rather than accidental
  copies of source-repository state.
- Future immutable evidence reuses one convention instead of per-assessment
  `.gitattributes` files.
- Byte preservation is evidence-driven rather than applied to all external data.

### Negative

- Source and downstream configurations become two intentionally separate files.
- Moving a target-template source changes package inventory and migration
  evidence even when the installed target path remains the same.
- A v0.5.1 implementation needs exact v0.5.0 upgrade and patch-compatibility
  proof; otherwise the work waits for v0.6.0.
- Binary originals do not receive normal line diffs or automatic text merging.

### Follow-up

- Use `.dev/backlog/items/CFG-001.yaml` to classify v0.5.1 versus v0.6.0.
- If accepted, update the package profile, public-root template manifest,
  package/migration tests, and cross-platform text fixtures together.
- Add the accepted evidence classification rule to
  `.dev/standards/ASSESSMENT-ARTIFACT-POLICY.md`; do not leave it only here.
- Replace the current tactical `.gitattributes` only after the centralized
  source rule and downstream-template separation land atomically.

## Notes

- This ADR records a proposed structural boundary, not implementation approval.
- The current branch's package projection remains unchanged; `CFG-001`
  implementation is outside the backlog-intake change set.
