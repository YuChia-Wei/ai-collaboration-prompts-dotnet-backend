# AI Context Package Installation

This package is a versioned framework payload, not a whole-repository overwrite.

1. Start from a clean Git worktree and record the current commit.
2. Use Python 3.11 or newer and install the checksum-governed target-tool dependency from the extracted envelope root:

   ```text
   python -m pip install -r requirements.txt
   ```

3. Validate the archive and its external `.sha256` sidecar.
4. From the extracted envelope root, run a dry-run against the target and review every add, replace, remove, rename, and reconcile result:

   ```text
   python payload/.ai/scripts/plan-ai-context-package-apply.py --package-root . --target-root <target-repository>
   ```

   For a migration-schema `2.0.0` upgrade, also pass
   `--previous-version <vMAJOR.MINOR.PATCH>` and
   `--previous-files <previous-files.yaml>`. Both values must exactly match one
   source identity in `metadata/migration.yaml`. Schema `1.0.0` packages remain
   readable and infer their single declared source version.
   If `--plan-output` is used, its path must be outside both the extracted envelope and the target repository so it does not invalidate package checksums or the clean-worktree gate.

5. Apply only after all reconciliation items are acknowledged by operation ID.
   Acknowledgement skips a reconciliation item; it never authorizes overwriting
   or deleting the target path:

   ```text
   python payload/.ai/scripts/plan-ai-context-package-apply.py --package-root . --target-root <target-repository> --apply --acknowledge <operation-id>
   ```

6. Review `.dev/AI-CONTEXT-APPLY-PENDING.yaml`, then run
   `repo-structure-sync` after a clean installation or `ai-context-upgrader`
   for a versioned upgrade. The package tool does not update validated
   `.dev/AI-CONTEXT-SOURCE.yaml` provenance.
7. Commit target-specific synchronization separately from the framework application when practical.

Framework-managed content may be replaced or removed only when its current hash matches the previous released hash. Target templates and target-owned truth are never silently overwritten or deleted.
