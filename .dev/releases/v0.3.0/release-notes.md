# REL-v0.3.0 — Version Governance And Safe Upgrades

## Status

Planned release candidate. No tag or published commit exists yet. Publication requires workflow closeout, `--no-ff` merge to `main`, post-merge validation, and explicit tag authorization.

## Highlights

- Defines SemVer meaning, immutable annotated tags, stable `REL-*` identities, and release lifecycle governance.
- Adds retrospective records and migration guidance for `v0.1.0` and `v0.2.0`.
- Introduces target `.dev/AI-CONTEXT-SOURCE.yaml` provenance with explicit local overrides and unresolved reconciliation.
- Adds the `ai-context-upgrader` skill with thin Codex and Claude wrappers and a human guide.
- Adds a read-only Git-backed three-way comparison tool.
- Adds fail-closed release/source-mode and target/manifest-mode validation with GWT regression tests.
- Keeps external graphs and indexes optional; Git and repository files remain evidence.

## Compatibility

This pre-1.0 minor release intentionally adds a required provenance/version gate. Existing targets must create a validated provenance manifest while adopting the upgrader. Root collaboration entries and target-owned project knowledge remain manual reconciliation surfaces.

## Known Limitations

- The comparison tool classifies paths and byte identity; semantic conflict resolution remains a human/agent decision.
- Unversioned or locally forked framework copies require manual baseline reconciliation.
- Dependency/version validation unrelated to this AI context release contract remains deferred.
