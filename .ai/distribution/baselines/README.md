# Retrospective Distribution Baselines

This directory may store version-specific evidence for framework releases that predate the governed package format. It contains source-side distribution evidence and is never installed as target project truth.

## Admission Gate

Create `.ai/distribution/baselines/<version>/` only when all of these facts are confirmed:

- an immutable annotated `vMAJOR.MINOR.PATCH` tag exists;
- the tag resolves to the recorded full 40-character commit;
- the historical file-selection or copy recipe used by target repositories is known;
- generated file hashes come from Git blob bytes at that tag, not checkout bytes;
- the resulting baseline passes the distribution and migration validators.

A plausible commit is not a baseline. Do not infer historical selection from the current distribution profile, and do not create a `v0.0.1` record from `ac2e2937b5209ece93e104c4a389a15e164c0d1b` until the user confirms both its tag and installed file selection.

## Required Records

One admitted baseline directory must contain:

- `baseline.yaml`: version, release ID, tag, commit, record origin, historical selection contract, creation timestamp, and file-manifest digest;
- `profile.yaml`: the version-specific historical path selection and target mappings;
- `files.yaml`: normalized target paths, Git source paths, Git-derived SHA-256 values, modes, ownership, and installation behavior.

The profile describes what was historically distributed. It must not silently adopt paths added by later framework versions. Generated records may exist only in the current trusted registry; they do not alter or claim to have existed in the historical tagged tree.

## Compatibility Boundary

Adding a baseline supplies comparison evidence; it does not by itself make an existing package compatible. A release may name the baseline as a supported source only after dry-run, local-modification, removal, rename, reconciliation, and apply scenarios pass against it.

If a baseline is confirmed after `v0.3.0` is published, advertise new compatibility in a later governed release rather than broadening the published `v0.3.0` contract retrospectively. Prerelease tags require an explicit version-policy, validator, and publication-workflow decision and are not admitted by this baseline policy.
