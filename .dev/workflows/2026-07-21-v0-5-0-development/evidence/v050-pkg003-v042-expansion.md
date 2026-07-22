# PKG-003 v0.4.2 Automatic-Source Expansion

## Evidence Metadata

- Workflow: `2026-07-21-v0-5-0-development`
- Task: `V050-009`
- Backlog item: `PKG-003`
- Original three-source evidence:
  [`v050-pkg003-validation.md`](v050-pkg003-validation.md)
- Working-tree base commit: `74eb1663ca4ed4be84ef5960ae210b62268126e3`
- Evidence state: expanded working tree validated; immutable checkpoint pending
- Verified at: `2026-07-22T07:35:04+08:00`

## Owner Amendment

On 2026-07-22 the repository owner explicitly required v0.4.2 to be an
automatic v0.5.0 source. This supersedes the temporary planned-candidate
assumption that v0.4.2 would require manual reconciliation. The v0.5.0
automatic source set is now:

- v0.3.0;
- v0.4.0;
- v0.4.1;
- v0.4.2.

The schema remains `2.0.0`. No new migration mechanism is introduced: every
source still binds its stable version, exact immutable `files.yaml` SHA-256,
and deterministic operation list.

## Immutable v0.4.2 Source

- Tag type: annotated tag
- Tag: `v0.4.2`
- Tag commit: `f474c3b058cb9f89f93929e0732fc1f276422dd9`
- Source inventory: `metadata/files.yaml` built from the immutable tagged tree

The package builder rejects duplicate source versions and emits sources in
semantic version order. The planner accepts v0.4.2 only when both version and
manifest digest match the declared fourth source.

## Executed Proof

Command:

```text
python .ai/scripts/tests/test_ai_context_packaging.py -v VersionedMigrationPackagingGwtTests.test_gwt_017_given_four_real_supported_sources_when_one_v050_candidate_is_built_then_each_upgrades_without_overwriting_target_truth
```

Result: passed, one test in 240.554 seconds.

The fixture built and extracted the immutable v0.3.0, v0.4.0, v0.4.1, and
v0.4.2 packages; bound all four exact inventories into one v0.5.0 candidate;
verified ZIP/tar.gz parity and sidecars; then dry-ran and applied every route.
For the v0.4.2 route it preserved a target-owned `AGENTS.md`, preserved a
locally changed managed planner after explicit reconciliation acknowledgement,
and emitted the v0.5.0 pending-apply receipt with the acknowledged operation
IDs.

The release-state, preparation, and renderer suites also pass with the fourth
declared source: 15/15, 4/4, and 3/3 respectively.

The complete source critical gate then passed 33/33 required checks with zero
failed or deferred checks. Its packaging suite passed 19 tests with one
existing Windows symlink-privilege skip; the four-source real upgrade case was
included and passed.

## Remaining Boundary

This proof validates the added source route but does not freeze the complete
v0.5.0 candidate. The expanded release files must pass the complete critical
gate, be committed, rebuilt from the immutable checkpoint, and pass hosted
candidate CI before PKG-003 and REL-001 can be treated as release-ready.
