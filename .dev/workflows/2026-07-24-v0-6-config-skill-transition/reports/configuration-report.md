# CFG-001 Configuration Ownership Report

## Outcome

`CFG-001` is complete for v0.6.0. ADR-001 is accepted and the source
repository now owns its root `.editorconfig` and `.gitattributes` independently
from the dedicated downstream seed files.

The package projects:

- `.ai/assets/skills/repo-structure-sync/templates/public-root/.editorconfig`
  to target `.editorconfig`; and
- `.ai/assets/skills/repo-structure-sync/templates/public-root/.gitattributes`
  to target `.gitattributes`.

Both remain `software-development-core`, `target-template`, and `seed`. Existing
target files therefore enter reconciliation/preservation behavior rather than
automatic framework overwrite.

## Text And Evidence Policy

- Source and downstream defaults use LF with a final newline.
- Shell scripts use LF; Windows `.bat` and `.cmd` files use CRLF.
- Source-only assessment and immutable-evidence paths do not appear in the
  downstream seed bytes.
- New byte-exact originals use
  `.dev/assessments/<assessment-id>/evidence/external/original/<source-id>/`.
- Ordinary evidence remains normalized and text-diffable.
- The finalized WorkService report remains at its stable historical path with
  one exact root compatibility rule. Its SHA-256 remains
  `24A12C4FDA19FF8F7AAE6902E66C0D95F799BFBF2EF8BDC5CDF1CE710AAAB427`.
- The tactical assessment-local `.gitattributes` file was removed.

## Verification

- Repository configuration validator: passed.
- Repository configuration fail-closed tests: 13 passed.
- Staged skill transition validator: passed.
- Staged skill transition fail-closed tests: 7 passed.
- Package projection test: passed with dedicated seed source paths and no
  source-only evidence tokens.
- Deterministic package suite: 22 unaffected cases passed; the two initial
  source-reference failures were corrected and both exact real-upgrade tests
  passed on rerun, for 24 passed cases in total. One environment-bound
  downstream test remained skipped.
- Real v0.3.0 upgrade: passed.
- Four-source v0.3.0/v0.4.0/v0.4.1/v0.4.2 upgrade and target-truth preservation:
  passed.
- Package apply suite: 24 passed; one Windows symlink case skipped because the
  host lacks symlink privilege.
- Aggregate fail-closed runner regressions: 27 passed.
- ZIP/tar payload and mode parity and byte-identical repeat builds: passed.
- AI-context, workflow, shell-asset, Python compile, and diff checks: passed.
- Independent bounded review: READY with no actionable defects; it reran both
  contract validators and all 20 CFG/SKILL mutation tests, while relying on the
  primary run for the long package and four-source upgrade matrices.

## Remaining Boundary

This report does not activate `ai-context-init` or
`software-development-orchestrator`. Their taxonomy and compatibility contract
is staged in `.ai/assets/skills/transitions/v0.6.0.yaml`, while the existing
identifiers remain active. Activation still requires the owner-approved
model-in-the-loop portion of `EVAL-001`.
