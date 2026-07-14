# AI Context Distribution Contracts

This directory owns source-side, machine-readable contracts for building portable AI context packages. It is not copied into a target repository as project truth.

## Entry Points

- `profiles/dotnet-backend.yaml` defines the initial complete distribution profile, source allowlist, ownership classes, and exclusions.
- `schemas/package.schema.yaml` defines package-envelope metadata.
- `schemas/files.schema.yaml` defines the generated per-file inventory.
- `schemas/migration.schema.yaml` defines version-to-version migration operations.

## Boundary

- A builder must start from the profile allowlist. It must not archive the repository and then rely on exclusions for safety.
- Exclusions are a deny boundary over the allowlist. An `except` entry restores only the named reusable path and must also be covered by an allowlist entry.
- Source paths are resolved from a clean Git tree at the requested immutable commit or tag.
- Builders read Git blob bytes and Git tree modes, not checkout bytes; this prevents `autocrlf` or local mode settings from changing package output. Symlinks, submodules, and non-regular Git entries are rejected.
- Generated metadata belongs under the package envelope's `metadata/` directory and is not installed as target project truth.
- Root entries and empty target catalogs come from public templates owned by `repo-structure-sync`; active source-repository root documents and catalogs are not templates.
- External indexes or knowledge graphs may accelerate discovery but cannot prove package completeness.
- A profile entry marked `allow_empty_until` is a workflow bootstrap exception. A release candidate validator must reject every remaining empty entry.
- Template-manifest `source` paths are resolved relative to the manifest directory. Targets are repository-relative payload paths; reject absolute paths, `..`, backslashes, duplicates, and collisions. A template may exist once at its canonical managed path and once at its mapped target seed path.
- `metadata/SHA256SUMS.txt` covers every other envelope member and excludes itself. Archive digests are external `.sha256` sidecars because an archive cannot contain its own final digest.

## Ownership Classes

| Class | Meaning | Automatic update rule |
| --- | --- | --- |
| `framework-managed` | Reusable framework content whose released bytes are controlled by this repository. | May replace or remove only when the target hash matches the previous released hash. |
| `target-template` | Seed content that becomes target-owned after initialization or reconciliation. | Create only when absent; otherwise require reconciliation. Never automatically remove. |
| `target-owned` | Target-specific truth recorded for classification but not supplied as reusable payload. | Never overwrite or remove automatically. |

## Installation Behaviors

- `managed`: use three-way, previous-release-hash-aware replacement and removal.
- `seed`: create only when absent and hand ownership to the target.
- `reconcile`: report a required target-specific decision or rewrite; do not apply automatically.
- `exclude`: never place the source path in a distributable payload.
