# AI Context Package Installation

This package is a versioned framework payload, not a whole-repository overwrite.

1. Start from a clean Git worktree and record the current commit.
2. Validate the archive and its external `.sha256` sidecar.
3. Run the installer in dry-run mode and review every add, replace, remove, rename, and reconcile result.
4. Apply only after all reconciliation items are acknowledged.
5. Run `repo-structure-sync` after a clean installation, or `ai-context-upgrader` for a versioned upgrade.
6. Commit target-specific synchronization separately from the framework application when practical.

Framework-managed content may be replaced or removed only when its current hash matches the previous released hash. Target templates and target-owned truth are never silently overwritten or deleted.
