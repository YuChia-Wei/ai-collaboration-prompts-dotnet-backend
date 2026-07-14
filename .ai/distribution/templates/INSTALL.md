# AI Context Package Installation

This package is a versioned framework payload, not a whole-repository overwrite.

1. Start from a clean Git worktree and record the current commit.
2. Validate the archive and its external `.sha256` sidecar.
3. From the extracted envelope root, run a dry-run against the target and review every add, replace, remove, rename, and reconcile result:

   ```text
   python payload/.ai/scripts/plan-ai-context-package-apply.py --package-root . --target-root <target-repository>
   ```

   For an upgrade, also pass `--previous-files <previous-files.yaml>` matching
   the `metadata/migration.yaml` source manifest identity.
4. Apply only after all reconciliation items are acknowledged by operation ID.
   Acknowledgement skips a reconciliation item; it never authorizes overwriting
   or deleting the target path:

   ```text
   python payload/.ai/scripts/plan-ai-context-package-apply.py --package-root . --target-root <target-repository> --apply --acknowledge <operation-id>
   ```

5. Review `.dev/AI-CONTEXT-APPLY-PENDING.yaml`, then run
   `repo-structure-sync` after a clean installation or `ai-context-upgrader`
   for a versioned upgrade. The package tool does not update validated
   `.dev/AI-CONTEXT-SOURCE.yaml` provenance.
6. Commit target-specific synchronization separately from the framework application when practical.

Framework-managed content may be replaced or removed only when its current hash matches the previous released hash. Target templates and target-owned truth are never silently overwritten or deleted.
