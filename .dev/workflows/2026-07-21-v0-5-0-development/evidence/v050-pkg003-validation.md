# PKG-003 Multi-Source Upgrade Validation

## Subject

- Core subject commit:
  `49a20868fedba70e14270bc815a6d9dfde1fa374`
- Migration schema: `2.0.0`
- Supported automatic sources: `v0.3.0`, `v0.4.0`, `v0.4.1`
- Clean installation: independent `clean_install.operations`
- Legacy reader compatibility: migration schema `1.0.0`

## Contract Evidence

- The builder accepts repeatable exact `(version, files.yaml)` inputs, rejects
  duplicate source versions, sorts sources by semantic version, and binds each
  operation list to the source manifest SHA-256.
- The planner selects schema 2.0 operations only when both
  `--previous-version` and `--previous-files` match one declared source.
  Partial, unknown, mismatched, duplicate, ambiguous, or unordered source
  identities fail closed.
- Clean installation selects only `clean_install.operations`.
- Schema 1.0 single-source packages remain readable without a new version
  argument.
- Candidate and publication workflows iterate every automatic source rendered
  from the release record through repeatable `--migration-source` arguments.
- v0.0.1 remains a reviewed reconciliation source to v0.3.0, followed by the
  direct v0.3.0-to-v0.5.0 route. It is not falsely declared as automatic.

## Executed Validation

| Gate | Result |
| --- | --- |
| Package-apply GWT suite | 18 passed; one existing Windows symlink-privilege fixture skipped |
| Packaging suite after core commit | 16 passed |
| Three real source packages to one v0.5.0 candidate | passed for extracted `v0.3.0`, `v0.4.0`, and `v0.4.1`; archive parity, dry-run, apply, receipt, target-template preservation, and managed-local-override preservation verified |
| Retained downstream | `dotnet-mq-arch-lab@2eeddf392ca79deb4407c47d13ad53178015ba90`, clean `main`, provenance `v0.4.0`; local-cloned temp target upgraded successfully and more than 20 existing declared override files remained byte-identical |
| Version governance | 15 passed |
| AI context version registry | passed for 7 release records |
| AI context validation | passed |
| Workflow lifecycle | 6 passed |

The retained downstream source repository was read-only. All application writes
occurred in a temporary local clone that was deleted after the test.

## Residual Boundaries

- Hosted Ubuntu execution of the same release gate remains owned by `ENF-001`
  and `TOOL-001`.
- The v0.5.0 release registry, notes, and final package build remain owned by
  `REL-001`.
- This evidence proves release-candidate behavior; it does not publish a tag or
  mutate the retained downstream repository.
