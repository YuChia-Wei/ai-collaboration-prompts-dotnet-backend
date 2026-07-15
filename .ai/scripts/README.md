# AI Scripts

This directory contains transitional AI workflow scripts, context governance checks, and local tool orchestration helpers.

It is no longer the long-term home for authoritative C# semantic validation. Rules that inspect C# syntax, symbols, type dependencies, attributes, or framework API usage should move to dotnet-native validation mechanisms such as Roslyn analyzers, `.editorconfig`, `dotnet format`, architecture tests, integration tests, or dotnet tools.

## Current Boundary

`shell-assets.yaml` is the machine-readable lifecycle registry for retained shell assets, and `validate-shell-assets.py` enforces registry, Git mode, and aggregate-runner parity. Current standards and validators own the active contract; packaged documentation must not depend on excluded source workflow history.

## Retention Policy

Shell or PowerShell scripts may remain when they are:

- AI workflow glue;
- prompt or context portability checks;
- repository file-system automation;
- local or CI orchestration over dotnet-native tools;
- non-C# semantic checks.

Shell or PowerShell scripts should be retired or replaced when they:

- use grep/find/plain-text matching to decide C# architecture correctness;
- duplicate `.editorconfig`, built-in analyzers, Roslyn analyzers, `dotnet format`, architecture tests, or dotnet tests;
- generate regex-based C# validation scripts from markdown and present them as formal gates.

## Script Classes

### Keep As AI Workflow Or Context Governance

- `check-prompt-portability.sh`
- `check-coding-standards.sh`
- `validate-ai-context.py`
- `validate-assessment-artifacts.py`
- `validate-ai-context-versions.py`
- `validate-git-commits.py`
- `build-ai-context-package.py`
- `validate-ai-context-package.py`
- `plan-ai-context-package-apply.py`
- `render-ai-context-release-notes.py`

These scripts inspect AI context, markdown, prompt portability, or repository hygiene. They are not substitutes for dotnet C# validation.

`validate-ai-context.py` checks objective repository facts: active index paths, literal table corruption, declared runtime-root status, canonical/Agents/Claude skill inventory parity, case-safe `AGENTS.md` and thin `CLAUDE.md` root entries, canonical wrapper-metadata target/path integrity, policy-scoped agent-facing language, root bilingual entry ownership/link/structural markers, rule ownership registry structure, canonical skill/sub-agent schema compliance, canonical template-family hygiene, and deterministic development capability routing. It scans both tracked and untracked non-ignored files so a new context file cannot bypass the gate before staging, while filtering tracked paths that are deleted in the working tree. Language lint uses exact path-and-line exceptions for deliberate routing triggers; other Han prose fails with a file and line number. Script source, generated/example/archive/migration material, workflows, product `src`/`test` trees, and human-facing `.dev` documentation are outside that language scan; Markdown documentation under `.ai/scripts` remains in scope. Root bilingual validation checks reciprocal ownership links, heading-level shape, and ordered backtick table paths, not full semantic parity. Canonical schema validation is structural and path-based; it does not claim semantic equivalence between projections.

`validate-workflow-artifacts.py` validates post-adoption workflow locator/task metadata, complete `.dev/workflows/INDEX.MD` directory coverage, locator-backed title/owner/status/timestamp/entrypoint parity, explicit legacy/no-locator rows, durable `.dev/backlog/items/*.yaml` identity/lifecycle/reference integrity, and fail-closed development implementation contracts for intent, execution mode, overlays, layered sources, subject revision, and acceptance criteria. Historical tasks before contract adoption remain compatible.

`validate-assessment-artifacts.py` validates `.dev/assessments/` locator and
index coverage, `ASM-YYYYMMDD-NNN` identity, template and report paths, assessed
Git revision metadata, branch and timestamp contracts, lifecycle sections,
resume safety, and assessment relationship integrity. It does not evaluate
report prose or replace the producing skill's evidence review.

`validate-ai-context-versions.py` validates governed release identity, SemVer,
immutable published tag-to-commit mappings, compatibility declarations, and an
optional target `.dev/AI-CONTEXT-SOURCE.yaml`. It automatically uses source mode
when release records exist and target mode when only the installed provenance
manifest exists. `compare-ai-context-versions.py`
is a read-only Git-tree comparison helper; it proposes an automatic candidate
only when a supplied target file is byte-identical to the recorded base. Target
truth, deletions, absent evidence, and source history remain reconciliation or
exclusion items.

`validate-git-commits.py` validates an explicitly selected commit or revision
range against `.dev/standards/GIT-COMMIT-POLICY.yaml`. It enforces the subject,
final AI signature, assessment ID trailer, and—when `--workflow-id` is
provided—ordered workflow body sections and matching workflow identity. The
aggregate gate invokes it only when `COMMIT_RANGE` is set, so ordinary working
tree checks do not guess whether a human-only commit used AI assistance.

`build-ai-context-package.py` reads an immutable Git commit tree and the
canonical distribution profile to produce normalized ZIP and tar.gz release
archives. `validate-ai-context-package.py` verifies the envelope, inventory,
member checksums, external archive checksum sidecars, and ZIP/tar member parity.
Their shared `ai_context_package.py` module rejects checkout-dependent bytes,
unsafe paths, output collisions, unsupported Git entry types, and existing
output files. These source-side packaging tools are excluded from the installed
target payload.

`plan-ai-context-package-apply.py` is the dry-run-first target-side package
entrypoint. It runs from the extracted envelope's `payload/.ai/scripts/`
directory, requires a clean committed target, and binds the package manifest,
target HEAD, and observed path hashes and modes into the plan. Existing target
templates and locally changed managed files become reconciliation items.
Acknowledging such an item skips it; acknowledgement never grants overwrite or
delete permission. `--apply` rechecks the complete binding, applies only safe
operations transactionally, and writes
`.dev/AI-CONTEXT-APPLY-PENDING.yaml`. It never updates validated source
provenance; `repo-structure-sync` or `ai-context-upgrader` owns validation and
provenance finalization.

`render-ai-context-release-notes.py` validates a governed release candidate and
renders the GitHub Release body from its canonical release notes, migration
guide, tag, and exact commit. Candidate mode can discover exactly one active
governed candidate; publish mode fails unless the tagged-tree record is
`validated`. The tag-triggered Action owns tag selection and Release mutation;
the renderer never creates or changes Git refs or remote releases.

Fail-closed validation and packaging regression tests use Given-When-Then
naming and comments and run entirely in disposable Git repositories:

```powershell
python .ai/scripts/tests/test_fail_closed_validation.py -v
python .ai/scripts/tests/test_ai_context_wrapper_metadata.py -v
python .ai/scripts/tests/test_ai_context_root_entries.py -v
python .ai/scripts/tests/test_workflow_implementation_contract.py -v
python .ai/scripts/tests/test_assessment_artifacts.py -v
python .ai/scripts/tests/test_git_commit_policy.py -v
python .ai/scripts/tests/test_ai_context_version_governance.py -v
python .ai/scripts/tests/test_ai_context_package_apply.py -v
python .ai/scripts/tests/test_ai_context_packaging.py -v
```

The shell fixture suite snapshots the real checkout before and after execution.
The wrapper-metadata fixture invokes only the bounded validator function against
temporary wrapper directories. Neither suite may source `check-all.sh` or
change files, modes, or index entries outside its temporary repository.

`shell-assets.yaml` classifies every tracked `.ai/scripts/**/*.sh` file as
`retained` or `retirement_candidates`. Retained shell assets must use Git index
mode `100755`; required entrypoints and child scripts must be retained.
`validate-shell-assets.py` enforces this contract with `git ls-files --stage`
instead of host filesystem executability, which is unreliable under Windows
Git Bash and `core.filemode=false`.

Required child-script calls in `check-all.sh` use the literal multiline form
`run_check "<script>"`, description, then `"required"` on the third line. The
shell asset validator compares those literal calls with
`check_all_required_scripts`; changing that call shape requires updating the
validator and its negative parity fixture in the same change.

### Keep As Orchestrator Only

- `check-all.sh`
- `code-review.sh`

These may remain as local workflow entry points, but their future role is to invoke dotnet-native validation and summarize outputs. They should not remain regex-based C# validators.

`check-all.sh` uses four enforcement classes:

- `required`: when selected by the active mode, the check must execute; missing,
  non-executable/unlaunchable, or non-zero outcomes fail the aggregate gate;
- `conditional-required`: absence of all applicability inputs is reported as not
  applicable, partial configuration fails, and an applicable check is required;
- `advisory`: execution problems and non-zero outcomes remain visible warnings
  but do not fail otherwise successful required checks;
- `deferred`: known future work is counted separately and is never described as
  a selected required check.

Mode-based omission is distinct from a selected required check being skipped.
Invalid modes or extra arguments return exit code `2`. A successful aggregate
result may contain explicit advisory warnings, deferred work, or not-applicable
conditional checks, but it cannot contain an unexecuted selected required check.

Future `check-all.sh` shape:

```bash
dotnet restore
dotnet build
dotnet test
dotnet format --verify-no-changes
dotnet tool run repo-context-lint
```

Current behavior:

- runs `dotnet test tools/DotnetBackendAnalyzers.Tests/DotnetBackendAnalyzers.Tests.csproj`;
- does not invoke the retired repository grep checks.

### Replace With Roslyn Analyzer Or Architecture Tests

- `check-test-compliance.sh`
- `check-test-di-compliance.sh`
- `check-data-class-annotations.sh`
- `check-domain-events-compliance.sh`
- `check-framework-api-compliance.sh`

Completed replacement:

- repository rules: `DBA1001` enforces canonical/compatibility inheritance,
  Aggregate Root constraints, aggregate method surface, query-port read-only
  behavior, and the generic writable CRUD prohibition; repository grep scripts
  have been removed.
- controller rules: `DBA1004`, `DBA1005`, and `DBA1006`; the controller grep scripts have been removed.
- mapper rules: `DBA1007` and `DBA1008`; the mapper grep scripts have been removed.
- aggregate rules: `DBA1003` and `DBA1009`; the aggregate grep scripts have been removed while invariant completeness remains test and AI review work.
- use case rules: `DBA1002` and `DBA1010` through `DBA1012`; the use case grep scripts have been removed while transaction and error-handling design remain AI review work.
- projection rules: `DBA1013` covers EF write operations and `DotnetBackendValidation` verifies marker-based EF model registration; the projection grep/config scripts have been removed.

Analyzer source template:

- `tools/DotnetBackendAnalyzers/`
- `tools/DotnetBackendAnalyzers.Tests/`

### Replace With Dotnet Tool Or Tests

- `check-dockerfile-csproj-copy-sync.ps1`
- `check-dotnet-config.sh`
- `check-spec-compliance.sh`
- `check-mutation-coverage.sh`
- `test-profile-startup.sh`
- `validate-dual-profile-config.sh`

These are not necessarily Roslyn analyzer rules. They belong in dotnet tools, integration tests, config tests, Stryker.NET configuration, or CI orchestration.

### Retired Generated Regex Checks

The markdown-to-shell generator, its parser and guide, and the `generated/`
outputs were removed under AIC-007. The root archive grep check was also removed
because its stale `HardDelete` text rule contradicted the active archive/purge
standard. Historical workflow evidence retains the original transition record.

`check-test-compliance.sh` remains temporarily as an explicitly advisory helper
until its rules are split across `.editorconfig`, analyzers, and test architecture
checks. It is manually maintained and cannot be regenerated from Markdown.

## AI Reasoning Context

Do not remove software engineering reasoning context from `.ai`, `.dev`, or skills as part of this transition.

Analyzers and CI gates can enforce formalizable rules, but they do not replace design reasoning used by:

- `bdd-gwt-test-designer`;
- `code-reviewer`;
- `ddd-ca-hex-architect`;
- requirement/spec/problem-frame authoring skills.

The context remains useful even when executable validation moves to dotnet-native tooling.

## Related Files

- `.ai/scripts/shell-assets.yaml`
- `.ai/scripts/validate-shell-assets.py`
- `.ai/assets/tech-stacks/dotnet-backend/README.MD`
- `.dev/standards/AI-CONTEXT-BOUNDARY.md`
