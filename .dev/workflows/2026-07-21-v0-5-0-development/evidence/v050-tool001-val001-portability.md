# TOOL-001 And VAL-001 Portability Evidence

## Evidence Metadata

- Workflow: `2026-07-21-v0-5-0-development`
- Task: `V050-006`
- Backlog items: `TOOL-001`, `VAL-001`
- Subject commit: `4cefb944e29781e2989422573ac4959899028f3f`
- Verified at: `2026-07-21T01:49:30+08:00`

## Decisions

The v0.5.0 runner is retained. Its literal multiline declaration format is
format-sensitive, but the sensitivity is now an explicit contract:

- `shell-assets.yaml` owns the exact required script and command sets;
- `validate-shell-assets.py` compares those sets without fixed counts;
- a negative fixture proves that a one-line formatting change fails closed
  instead of silently removing a required command;
- the runner remains a small orchestrator and does not become semantic
  authority.

A manifest-driven runner rewrite would add migration and regression surface
without evidence of a current portability or correctness benefit. Retention is
therefore the smallest coherent v0.5.0 decision. A future redesign must change
the documented grammar, validator, manifest, and negative fixtures together.

The historical dependency deferral is retired. The required replacement is an
offline consistency gate. Online package currency and vulnerability data remain
advisory because their truth is mutable and network-dependent.

## Offline Dependency Contract

`validate-dependency-versions.py` uses only the Python standard library and
validates repository-owned facts:

- source and package Python requirements are exact, byte-identical pins;
- source GitHub workflows install `requirements.txt` instead of copying inline
  package versions;
- all source workflows select one exact Python version at or above 3.11;
- framework-managed `tools/**/*.csproj` direct package versions are exact and
  consistent;
- `global.json` selects an exact SDK new enough for the highest managed-tool
  `netN.0` target;
- installed targets do not require source-only workflows or distribution
  controls.

The source fixture suite contains 12 GWT cases, including source-marker
deletion resistance, requirement drift, unpinned dependencies, inline workflow
pins, conflicting NuGet versions, missing versions, SDK incompatibility,
`netstandard2.0`, newer-SDK compatibility, and target-mode applicability.

## Low-Cost Sub-Agent Review

A bounded `gpt-5.6-terra` low-reasoning worker authored only the initial
dependency fixture file. Main-agent review found and corrected three material
problems before acceptance:

1. negative tests asserted only a non-zero exit, so a missing validator could
   create false-positive passes;
2. the initial SDK fixture incorrectly rejected a newer SDK building an older
   target framework;
3. project fixtures were outside the framework-managed `tools/` scope.

The accepted tests require validator-specific diagnostics, reject only an SDK
that is too old, and exercise the actual managed path. The sub-agent result was
useful as a bounded draft, but was not accepted without main-agent correction
and rerun.

## Windows Git Bash

- Environment: Windows Git Bash `5.3.9`, Python `3.13.14`, .NET SDK
  `10.0.302`.
- Command: `C:\Program Files\Git\bin\bash.exe .ai/scripts/check-all.sh --quick`
- Subject: exact clean checkout at `4cefb944e29781e2989422573ac4959899028f3f`
- Result: exit success; 23 required selected, 23 executed, 23 passed, 0 failed,
  0 warnings, 0 deferred, and 2 not applicable.
- Completed: `2026-07-21T01:48:04+08:00`

The new dependency validator reported source mode with one Python dependency,
five managed projects, and seven distinct NuGet dependencies. All 12 dependency
fixtures and all 23 aggregate-runner/shell-registry fixtures passed.

## Hosted Ubuntu

- Workflow: `Portable AI Context Gates`
- Event: draft pull request `#1`
- Run: [29764778490](https://github.com/YuChia-Wei/ai-collaboration-prompts-dotnet-backend/actions/runs/29764778490)
- Head commit: `4cefb944e29781e2989422573ac4959899028f3f`
- Executed PR merge commit:
  `cbf5a77965572aea65b22a3642b021b5484706c9`
- Environment: `ubuntu-latest`, Python `3.12.13`, .NET SDK `10.0.302`
- Result: success; 23 required selected, 23 executed, 23 passed, 0 failed,
  0 deferred.

The hosted job ran the same
`bash .ai/scripts/check-all.sh --quick` entrypoint and declared gate set as the
Windows execution. It also passed the 12 dependency fixtures and 23
runner/registry fixtures.

## CI Boundary

The separate `Package AI Context Candidate` PR job failed in run
`29764778480` because the branch does not yet contain a governed `planned` or
`validated` v0.5.0 release record. The failure is expected fail-closed evidence
for pending `REL-001` / `V050-009`; it is not a failure of the portable quick
gate. No skip or copied v0.4.2 release data was added to hide this state.

## Claims And Residual Boundary

- Windows Git Bash and hosted Ubuntu are verified for the same quick gate set.
- macOS was not executed and remains explicitly unverified.
- The result proves offline declaration consistency, not current package
  versions or vulnerability status.
- `TOOL-001` and the retained implementation portion of `VAL-001` are complete.
  The draft PR remains intentionally non-release-ready until the other v0.5.0
  blockers and the planned release record are complete.
