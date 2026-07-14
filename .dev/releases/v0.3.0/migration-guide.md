# Migrate To v0.3.0

This guide is a candidate until `REL-v0.3.0` is published. Do not claim a target is on `v0.3.0` until the tag exists and resolves to the release registry's published commit.

## From v0.2.0

1. Preserve a target rollback commit and verify the current source as `REL-v0.2.0` / `v0.2.0` / `9abc75b543ae201865c1e119d29fac2bcd2f4542` when possible.
2. Read the incoming version policy, upgrader skill, provenance contract, and this guide from the trusted framework registry.
3. Run the read-only comparison with `--target-root`; reconcile root entries, target-owned knowledge, changed wrappers, and local framework customizations.
4. Apply accepted reusable framework paths. Do not copy source workflow instances, assessment instances, backlog items, or `.dev/releases/` into the target.
5. Create `.dev/AI-CONTEXT-SOURCE.yaml` from the canonical template. Record the published `v0.3.0` tag and full commit, framework deviations only, and any unresolved collisions.
6. Run target-mode version validation, AI-context validation, workflow validation when applicable, and the target's required repository gate.
7. Update provenance only after validation succeeds.

## From v0.1.0

First apply the `v0.1.0 → v0.2.0` reconciliation in the `REL-v0.2.0` migration guide, including root entries, assessment governance, workflow/commit policy, and slice remediation contracts. Then follow the `v0.2.0 → v0.3.0` steps above. The upgrader may perform this as one planned migration, but every intermediate breaking contract must remain visible in the plan.

## From An Unversioned Or Forked Copy

Do not guess the base. Produce an unresolved-provenance inventory, identify a credible source tag/commit or manually reconcile the current target against the requested release, and preserve the decision as migration evidence. Only then create the provenance manifest.

## Mandatory Reconciliation

- `AGENTS.md`, `CLAUDE.md`, translations, and root README identity.
- Target requirements, specs, ADRs, architecture, operations, domain language, and project configuration.
- Target catalog indexes for workflows, assessments, and backlog.
- Any locally modified canonical skill, runtime wrapper, script, or validation command.

An `automatic-candidate` remains a proposal until application is explicitly authorized.
