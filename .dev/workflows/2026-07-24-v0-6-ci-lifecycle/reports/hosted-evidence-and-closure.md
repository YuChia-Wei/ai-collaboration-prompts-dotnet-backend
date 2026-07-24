# CI-001 And CI-002 Hosted Evidence And Closure

## Resolution Boundary

The combined CI workstream is complete. It owns the design and enforcement of
the four active GitHub workflow boundaries, Node.js 24-native artifact action
selection, bounded pull-request concurrency, version-owned release phase
contracts, and fail-closed static tests.

Release execution remains deliberately separate:

- the v0.6.0 candidate pull request must execute `actions/upload-artifact@v7`;
- the user-created v0.6.0 tag must execute `actions/download-artifact@v8`;
- release finalization must record the successful hosted publication run and
  public asset evidence.

These are candidate, tag, publication, and finalization gates. They do not
reopen the completed CI implementation unless execution exposes a defect.

## Hosted Integration Evidence

PR #7, `Integrate v0.6.0 product and governance contracts`, merged to `main` as
`0cd4298d96948dcc0d1bef54b1b04488338442cf` after all required jobs passed:

- `Read-only governance contract`;
- `Ubuntu quick gate`;
- `Build and validate candidate`.

The candidate job correctly discovered that no governed candidate existed on
the integration PR and exited as not applicable. This proves the accepted
discovery boundary but does not claim that artifact upload executed.

## Remaining Release Evidence

The independent v0.6.0 release-publication workflow must retain:

1. a candidate PR run in which release discovery, exact candidate validation,
   deterministic packaging, archive parity, and artifact upload all execute;
2. a tag-triggered run in which the validated tag job produces the artifact,
   the publication job downloads only that artifact, re-verifies every
   identity and checksum, and publishes the GitHub Release;
3. final registry evidence recorded only after observing the immutable tag,
   hosted run, public URL, and assets.
