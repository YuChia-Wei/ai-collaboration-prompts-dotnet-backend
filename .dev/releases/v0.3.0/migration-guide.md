# Migrate To v0.3.0

This guide is a candidate until `REL-v0.3.0` is published. Do not claim a target is on `v0.3.0` until the tag exists and resolves to the release registry's published commit.

## Package Safety Sequence

Use the release archive as a versioned proposal, not as a whole-repository overwrite.

1. Preserve a rollback commit and require a clean target worktree.
2. Download either governed archive and its matching `.sha256` sidecar.
3. Validate the archive, member checksums, inventory, modes, and sidecar before inspecting a migration plan:

   ```text
   python .ai/scripts/validate-ai-context-package.py <archive>
   ```

4. Use `plan-ai-context-package-apply.py` in its default dry-run mode. Supply the previous governed `files.yaml` when upgrading so replacement, removal, and rename decisions can use previous released hashes.
5. Review every reconciliation item. Never acknowledge a conflict without determining whether the target or framework owns the truth.
6. Apply only from a clean worktree after the dry-run output is accepted. Pass every accepted reconciliation operation ID separately with `--acknowledge`, then add `--apply`:

   ```text
   python payload/.ai/scripts/plan-ai-context-package-apply.py --package-root . --target-root <target-repository> --previous-files <previous-files.yaml> --acknowledge <operation-id> --apply
   ```

   Acknowledgement preserves and skips the reconciled target path; it never grants overwrite or deletion permission.
7. Run `repo-structure-sync` after a clean installation, or `ai-context-upgrader` after a versioned upgrade.
8. Run target validation and write `.dev/AI-CONTEXT-SOURCE.yaml` only after the accepted payload and target-specific rewrites pass.

Framework-managed files may be replaced, removed, or renamed automatically only when their target bytes match the previous released hash. Target templates may be created only when absent. Target-owned truth and locally modified files always require reconciliation.

Archive validation alone does not authorize application. This candidate remains unreleased until the workflow closeout gates complete.

## From v0.2.0

1. Preserve a target rollback commit and verify the current source as `REL-v0.2.0` / `v0.2.0` / `9abc75b543ae201865c1e119d29fac2bcd2f4542` when possible.
2. Read the incoming version policy, upgrader skill, provenance contract, and this guide from the trusted framework registry.
3. Run the read-only comparison with `--target-root`; reconcile root entries, target-owned knowledge, changed wrappers, and local framework customizations.
4. Validate the `v0.3.0` archive. If a governed `v0.2.0` `files.yaml` baseline is available, supply it to the package planner for hash-gated operations; otherwise treat the target as a manual reconciliation source and do not infer managed-file ownership.
5. Apply accepted reusable framework paths only after all reconciliation items are acknowledged. Do not copy source workflow instances, assessment instances, backlog items, or `.dev/releases/` into the target.
6. Run `ai-context-upgrader` to reconcile target-owned context and create `.dev/AI-CONTEXT-SOURCE.yaml` from the canonical template. Record the published `v0.3.0` tag and full commit, framework deviations only, and any unresolved collisions.
7. Run target-mode version validation, AI-context validation, workflow validation when applicable, and the target's required repository gate.
8. Update provenance only after validation succeeds.

## From v0.1.0

First account for the `v0.1.0 → v0.2.0` reconciliation in the `REL-v0.2.0` migration guide, including root entries, assessment governance, workflow/commit policy, and slice remediation contracts. Then validate the `v0.3.0` package. Supply a governed `v0.1.0` `files.yaml` only when that version-specific baseline exists and matches the recorded release; otherwise use the upgrader's unresolved-provenance reconciliation path. Every intermediate breaking contract must remain visible in the plan.

## From An Unversioned Or Forked Copy

Do not guess the base. Produce an unresolved-provenance inventory, identify a credible source tag/commit or manually reconcile the current target against the requested release, and preserve the decision as migration evidence. Only then create the provenance manifest.

Commit `ac2e2937b5209ece93e104c4a389a15e164c0d1b` does not establish `v0.0.1` compatibility. Until a tag, installed file selection, and retrospective baseline manifest are confirmed, treat copies associated with that commit as unresolved provenance.

## Mandatory Reconciliation

- `AGENTS.md`, `CLAUDE.md`, translations, and root README identity.
- Target requirements, specs, ADRs, architecture, operations, domain language, and project configuration.
- Target catalog indexes for workflows, assessments, and backlog.
- Any locally modified canonical skill, runtime wrapper, script, or validation command.

An `automatic-candidate` remains a proposal until application is explicitly authorized.
