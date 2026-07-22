# v0.5.0 macOS Portability External Review Intake

## Template Metadata

- `template_id`: `ai-context-auditor-report`
- `template_version`: `2.1.0`
- `template_created_at`: `2026-07-10T18:22:49+08:00`
- `template_updated_at`: `2026-07-15T08:39:00+08:00`

## Metadata

- `assessment_id`: `ASM-20260722-003`
- `assessment_type`: `ai-context-audit`
- `owner_skill`: `ai-context-auditor`
- `status`: `final`
- `audit_date`: `2026-07-22`
- `created_at`: `2026-07-22T20:35:44+08:00`
- `updated_at`: `2026-07-22T20:35:44+08:00`
- `template_source`: `.ai/assets/skills/ai-context-auditor/templates/ai-context-audit-report-template.md`
- `template_version`: `2.1.0`
- `repository`: `C:/Github/YuChia/ai-collaboration-prompts-dotnet-backend`
- `subject_branch`: `main`
- `subject_commit`: `9ac40bee4ab3d4ac169c05c6229895d7a22265ff`
- `previous_assessment`: [`ASM-20260722-002`](../ASM-20260722-002/report.md)
- `workflow_refs`: [`2026-07-22-v0-5-0-macos-portability`](../../workflows/2026-07-22-v0-5-0-macos-portability/workflow.yaml)
- `external_review_source`: [`fable5-macos`](evidence/fable5-macos/v050-macos-portability-report.md)
- `external_review_sha256`: `A762BC4E24DE304B8BFBEB90212E51A39C66BBE5955A9656369D1E4B39FDF5E3`

## Executive Summary

- Overall assessment: **macOS gate evidence is healthy, with one reproducible
  validation-fixture isolation defect and two stale portability disclosures**.
- Overall score: **8.5/10**
- Decision: **remediation-recommended**
- Primary strengths: the owner-arranged independent macOS host executed the
  same quick and critical entrypoints at the exact release candidate commit,
  reported 33/33 required checks passing when Python was discoverable on PATH,
  and verified release-state fail-closed behavior.
- Primary risks: following the documented `AI_CONTEXT_PYTHON` override leaks a
  real interpreter into synthetic fixtures, producing eight false failures;
  the SDK floor is not explicit; current release records still say macOS was
  not executed.

The receiving Windows host independently reproduced the eight-failure harness
defect. It did not rerun macOS; macOS execution remains attributed to the raw
Fable 5 report and is not generalized beyond its pinned environment and commit.

## Scope

### Included AI Context Surfaces

- Raw Fable 5 macOS portability report.
- Aggregate runner, fail-closed fixture suite, source-tool prerequisites,
  v0.5.0 release notes, and current roadmap/backlog portability claims.
- Git identity for the assessed release candidate.

### Default Exclusions

- `src/**`
- `tests/**`, `test/**` outside AI-context validation surfaces
- product implementation trees
- generated and dependency trees

### Additional Exclusions

- A second macOS execution by the receiving host.
- Provider-native attribution fixtures.
- Changes to release compatibility or automatic upgrade sources.

### Code Review Handoff

- Requested: `no`
- Paths not scanned: product source and product tests
- Recommended skill: not applicable

## Methodology And Evidence

### Pass A: Independent Baseline

- Preserved the external report without rewriting its language, structure, or
  conclusions.
- Required platform claims to identify OS, architecture, shell, Python, SDK,
  subject commit, commands, exit status, and selected/passed counts.
- Reproduced the environment-leak mechanism independently on Windows by setting
  the parent `AI_CONTEXT_PYTHON` to the active real interpreter before running
  the focused fixture suite.

### Pass B: Repository-Aware Skill Review

- Applied the external-review intake, evidence-boundary, assessment, release,
  workflow, and AI-context governance contracts.
- Compared the report against `SyntheticRunnerRepo.execute`, `check-all.sh`
  interpreter precedence, `global.json`, current release notes, and backlog.
- Kept historical final assessments and completed workflow evidence immutable.

### Delegation

- Sub-agents used: `no`
- Assigned surfaces: none for baseline intake

### Discovery Accelerators

| Tool / generated view | Source revision or input digest | Freshness / dirty state | Scope and exclusions | Unsupported relationships | File-backed fallback |
| --- | --- | --- | --- | --- | --- |
| codebase-memory-mcp | `9ac40bee4ab3d4ac169c05c6229895d7a22265ff` | indexed candidate; external report untracked at intake | Python fixture symbols only | external macOS execution and Markdown lifecycle truth | direct source reads, Git state, raw report, and focused execution |

## Repository Context Inventory

| Surface | Files / Size | Audience | Scope | State | Notes |
| --- | ---: | --- | --- | --- | --- |
| External review | 1 report | maintainers/agents | attributed platform evidence | preserved | reviewer-native Traditional Chinese structure retained |
| Runner fixture | 1 Python suite | agents/maintainers | portable validation | defective | inherits an explicit interpreter override into synthetic repos |
| Prerequisites | README plus `global.json` | maintainers | source tooling | incomplete | Python floor is explicit; exact SDK floor is not |
| Release planning | notes, roadmap, TOOL-001 | users/maintainers | current v0.5.0 truth | stale | still records macOS as unexecuted |

## Strengths

1. The external run pins the exact then-current `main` commit and a clean
   detached worktree.
2. Native macOS bash 3.2.57 passed both governed quick and critical entrypoints
   when a compliant Python interpreter was discoverable.
3. Candidate validation and its dirty/detached fail-closed paths behaved as
   designed.
4. The external report distinguished a harness defect from a platform failure
   and supplied a minimal, testable correction.

## Findings

| ID | Severity | Finding | Evidence | Impact | Recommendation | Owner / Next Skill |
| --- | --- | --- | --- | --- | --- | --- |
| AIC-001 | HIGH | `SyntheticRunnerRepo.execute` leaks the parent's `AI_CONTEXT_PYTHON` into disposable fixtures. | The receiving host set the variable to its real Python and reproduced 8 failures; fixture errors attempted to open absent real test paths instead of invoking the PATH stub. | Users following the documented macOS override receive a false required-gate failure, and the regression suite depends on the caller environment. | Remove inherited `AI_CONTEXT_PYTHON` before applying test-owned overrides and add a GWT regression proving the PATH stub remains authoritative. | `ai-context-governance` |
| AIC-002 | MEDIUM | Source-tool prerequisites omit the effective .NET SDK floor. | `global.json` requires `10.0.300` with `latestMajor`; the external macOS host reports installed `10.0.203` is rejected. | A clean host can fail before the gate despite following the current README. | State the governed SDK 10.0.300-or-newer requirement in source tooling and release runbook guidance. | `ai-context-governance` |
| AIC-003 | LOW | Current candidate notes and roadmap still say macOS was not executed. | The external report records quick and critical 33/33 at the pinned candidate, while active v0.5.0 notes and roadmap retain the old limitation. | Published notes would understate executed portability evidence and leave future agents with stale release truth. | Record the owner-arranged attributed macOS execution without implying a receiving-host rerun or universal support. | `ai-context-governance` |

## Baseline And Skill Comparison

### Confirmed

- The eight-failure `AI_CONTEXT_PYTHON` leak is independently reproduced.
- The exact SDK floor is absent from the current source-tool prerequisites.
- Active v0.5.0 release wording is stale relative to the supplied execution.

### Added By Repository-Aware Review

- Historical final assessments and completed workflow records must retain the
  truth that macOS was unverified at their subject revisions.
- The macOS claim must remain attributed to the owner-arranged Fable host; it
  cannot be promoted into a broad provider or platform-support guarantee.

### Downgraded Or Deferred

- Adding `python3.11` through `python3.14` discovery aliases is optional and is
  not needed once the documented override works correctly.
- Provider-native Copilot and Claude fixtures remain separate residuals.

### Overturned

- The external suggestion to defer the harness fix to v0.5.x/v0.6.0 is
  superseded by the owner's explicit instruction to make the basic correction
  before publishing v0.5.0.

## Validation

| Check | Result | Evidence / Notes |
| --- | --- | --- |
| Git subject identity | pass | `main@9ac40bee4ab3d4ac169c05c6229895d7a22265ff` matches the report |
| Raw source integrity | pass | SHA-256 `A762BC4E...B39FDF5E3` |
| Environment-leak reproduction | fail as expected | 26 focused tests ran; exactly 8 failed after inheriting the real interpreter |
| macOS quick and critical gates | attributed pass | Fable report records 33/33, exit 0, on macOS 26.5.1 arm64 |
| Candidate release state | attributed pass | Fable report records candidate pass and expected fail-closed negative paths |
| Current portability prose | stale | active notes, roadmap, and TOOL-001 retain the previous unverified statement |

### Skipped Validation

- The receiving host did not rerun macOS, as explicitly permitted by the owner.
- Product code and tests were excluded.

## Recommended Action Order

1. Isolate inherited `AI_CONTEXT_PYTHON` and add the focused regression.
2. Document the Python override path and .NET SDK floor.
3. Update only active candidate/release-planning truth with attributed macOS
   evidence; do not rewrite historical final assessments or workflows.
4. Run focused tests, full critical gates, and independent post-remediation
   verification before creating the immutable tag.

## Deferred Items

- Provider-native runtime fixtures remain outside this macOS portability scope.
- Named Python minor-version discovery aliases remain unnecessary unless the
  supported override itself later proves insufficient.

## Appendix

### Commands Run

```text
git status --short --branch
Get-FileHash -Algorithm SHA256 <raw-report>
AI_CONTEXT_PYTHON=<active-real-python> python .ai/scripts/tests/test_fail_closed_validation.py -v
git show main:.ai/scripts/tests/test_fail_closed_validation.py
```

### Notes

- The raw external report remains unchanged under `evidence/fable5-macos/`.
- Platform execution is accepted as owner-arranged attributed evidence, not as
  a receiving-host reproduction.

## Lifecycle Handoff

- Assessment path: `.dev/assessments/ASM-20260722-003/report.md`
- Stable finding references: `ASM-20260722-003#AIC-001` through `AIC-003`
- Remediation owner: `ai-context-governance`
- Related remediation workflow: `2026-07-22-v0-5-0-macos-portability`
- Verification assessment: pending
- Remediation intentionally not performed by this skill: `yes`
