# Upgrade Playbook

## Entry Gate

Read, in order:

1. target `AGENTS.md` and any deeper instructions;
2. `.dev/standards/AI-CONTEXT-VERSION-POLICY.md` from the requested framework version;
3. target `.dev/ai-context/provenance.yaml` and referenced
   `.dev/ai-context/customizations.yaml`, or the legacy
   `.dev/AI-CONTEXT-SOURCE.yaml`;
4. requested `.dev/releases/<version>/release.yaml` and `migration-guide.md` from the trusted framework release registry;
5. the three-way boundary and output contract in this skill.

When a release migration guide projects a workflow file-disposition manifest,
treat `kept`, `moved-to`, `merged-into`, and `retired` as incoming intent only.
The projected disposition can improve path discovery, but it cannot establish
the target's base bytes, ownership, local changes, or write authorization.

Use `ai-context-init` if no initialization has occurred; the deprecated
`repo-structure-sync` entry follows that contract during transition. If
framework files exist but provenance is absent, stop automatic upgrade
classification and produce an unresolved-provenance inventory. The user must
identify a credible base or authorize a manual baseline reconciliation.

When only the legacy manifest exists, preserve every `local_overrides` entry as
an unresolved legacy path override during migration. Do not invent capability,
rule, or contract identity. If legacy and schema-2 provenance both exist, fail
closed until the duplicate authority is reconciled.

## Discovery

- Resolve both version tags to full commits with Git.
- Confirm the requested release is published and its record matches the tag target. For `record_origin: retrospective`, the record may exist only in the current trusted registry; the annotated tag and resolved commit remain publication identity.
- Preserve a clean rollback point for target-local work before applying changes.
- Use `.ai/scripts/compare-ai-context-versions.py --from-ref <old-tag> --to-ref <new-tag> --target-root <target-repo>` to discover and classify changed framework paths; verify target path existence and content with repository files.
- Read migration guides for every skipped version between the recorded and requested releases.

## Planning

Classify each relevant framework change as `automatic-candidate`, `reconcile`, or `exclude`. An automatic candidate is not authorization to write. Group reconciliation items by target owner and explain what would be lost under replacement.

The plan must state:

- from/to release ID, version, tag, and commit;
- manifest state and unresolved provenance;
- changed paths by classification and reason;
- incoming file dispositions and their target-side three-way classification;
- ordered migrations and validation;
- rollback boundary;
- items requiring user decision.
- customization subject, relationship, incoming equivalence, decision evidence,
  and proposed disposition when framework-managed behavior was customized.

## Application

Apply only explicitly accepted paths. Never use a bulk copy over the repository root. Re-read a path immediately before writing when it is target-owned or previously classified for reconciliation.

For `moved-to` or `merged-into`, preserve target-local source content until its
destination has been reconciled. For `retired`, remove automatically only when
the target source is byte-identical to base and the migration guide explicitly
permits automatic removal. A disposition marked `kept` remains a normal
three-way candidate; it is not a force-replace instruction.

After changes, run the target's narrow AI-context validation and then its required repository gate. If validation fails, retain the previous provenance and report the failed changes and rollback options.

## Completion

Update `.dev/ai-context/provenance.yaml` only when required validation succeeds.
Record authorized semantic reconciliation in
`.dev/ai-context/customizations.yaml`; keep unresolved legacy path overrides and
collisions in `reconciliation.unresolved`. Report the exact resulting version
and commit, validation evidence, remaining customizations, and deferred
migration. Do not retain the legacy manifest as a second authority after a
successful schema-2 migration.
