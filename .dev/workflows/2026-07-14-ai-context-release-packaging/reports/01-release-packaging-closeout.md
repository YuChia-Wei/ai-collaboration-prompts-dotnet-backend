# AI Context Release Packaging Closeout

- Workflow: `2026-07-14-ai-context-release-packaging`
- Validated candidate commit: `1a25eb023e69d85c32a7459e7a9dc749e30e5d26`
- Recorded at: `2026-07-15T07:53:30+08:00`
- Release record: `REL-v0.3.0` (`validated`, not tagged or published)

## Outcome

The workflow produced a deterministic `dotnet-backend` package profile, public root seeds, derived translation adapters, safe package planning/application, candidate and user-tag-triggered GitHub Actions, versioned release metadata, and required regression gates. No tag, GitHub Release, merge, or push was performed.

`v0.1.0` and `v0.2.0` are reconciliation sources. They are not claims of unattended migration: automatic replace/remove/rename requires a matching governed previous `files.yaml`. No `v0.0.1` compatibility is claimed.

## Candidate Evidence

Two independent builds from `1a25eb023e69d85c32a7459e7a9dc749e30e5d26` produced identical bytes per output:

| Output | SHA-256 |
| --- | --- |
| `ai-context-dotnet-backend-v0.3.0.zip` | `aea244dd7ab70f5b82eec7d80cc7619ae2f1a6695d9f4774b3ee995b33e423c7` |
| `ai-context-dotnet-backend-v0.3.0.zip.sha256` | `d407e7d22de5149813c2f49a4e07069ff29b963ab611cf88ecb1f943903c9a70` |
| `ai-context-dotnet-backend-v0.3.0.tar.gz` | `214c6ca278b99b5f2a28e0528765bf49e5f4fd18ffdce801da4b20d79f134405` |
| `ai-context-dotnet-backend-v0.3.0.tar.gz.sha256` | `fe3b219dfdbdcd8ae861b133fbac7e3434110f33f7ea76ea9914363b0c77c8ab` |

ZIP/tar.gz envelope checksums, payload inventory, normalized modes, external sidecars, and cross-format parity passed.

## Forward-Test Evidence

- Extracted the actual ZIP into a disposable directory.
- Ran the shipped planner in dry-run mode against a clean committed Git target; no receipt or target mutation occurred.
- Ran the shipped planner with `--apply`; managed files were added, `.dev/AI-CONTEXT-APPLY-PENDING.yaml` was written, and `.dev/AI-CONTEXT-SOURCE.yaml` was not written prematurely.
- Synthetic upgrade scenarios applied hash-gated replace/remove/rename operations and preserved locally modified or target-owned truth through reconciliation.
- A first forward-test exposed packaged `__pycache__` checksum drift. Commit `cab3aa4` prevents bytecode creation before envelope validation and adds a real extracted-archive regression.

## Required Gates

- `check-all.sh --quick`: 12/12 required checks passed.
- Packaging and safe-apply GWT: 23 passed; one Windows symlink negative-path scenario skipped because the host lacks symlink privilege.
- Version governance GWT: 12 passed.
- Analyzer template tests: 47 passed.
- Configuration validation tests: 2 passed.
- AI context, workflow, release/version, shell asset, coding standards, package, Python compile, YAML, and diff checks passed.
- An independent sub-agent forward-review confirmed the release automation and compatibility claims, then found the missing target-side PyYAML declaration. The envelope now pins `PyYAML==6.0.3`, documents Python 3.11+, emits a clear missing-dependency error, and covers this path with an extracted-package smoke test.
- The generic .NET dependency/version validator remains the existing deferred check because its dotnet-native replacement is not available; the packaged planner's direct PyYAML runtime dependency is explicitly pinned and tested and is not part of that deferral.
- Spec compliance was not applicable because this workflow changed AI context rather than a product implementation spec.

## External Follow-Up

1. Merge this workflow branch with `--no-ff` when authorized.
2. Rerun the required quick gate and a final deterministic package build after merge.
3. Push the merged branch when authorized.
4. The user creates the `v0.3.0` tag when the release is approved.
5. Observe the tag-triggered Action and verify its four published assets and release body.
6. Select and tag the historical `v0.0.1` candidate separately before admitting a retrospective baseline manifest.

`actionlint` was not available locally; YAML parsing, embedded Git Bash syntax, and dedicated static workflow-contract tests covered the local validation boundary.
