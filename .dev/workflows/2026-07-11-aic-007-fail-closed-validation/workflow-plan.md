# AIC-007 Fail-Closed Validation And Executable Modes

## Template Metadata

- `template_id`: `dev-workflow/development-workflow-plan`
- `template_version`: `1.1.0`
- `template_created_at`: `2026-07-10T18:25:11+08:00`
- `template_updated_at`: `2026-07-11T00:22:30+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-11-aic-007-fail-closed-validation`
- `plan_id`: `development-plan-2026-07-11-aic-007-fail-closed-validation`
- `owner_skill`: `dev-workflow`
- `branch`: `codex/2026-07-11-aic-007-fail-closed-validation`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `completed`
- `created_at`: `2026-07-11T23:43:23+08:00`
- `updated_at`: `2026-07-12T14:03:59+08:00`
- `template_source`: `.ai/assets/skills/dev-workflow/templates/development-workflow-plan-template.md`
- `template_version`: `1.1.0`
- `workflow_locator`: `.dev/workflows/2026-07-11-aic-007-fail-closed-validation/workflow.yaml`
- `artifact_root`: `.dev/workflows/2026-07-11-aic-007-fail-closed-validation/`
- `source_backlog_item`: `.dev/backlog/items/AIC-007.yaml`

## Development Objective

- Product or software outcome: make the repository validation orchestrator fail closed whenever a check selected as required is missing, unlaunchable, skipped, or fails; verify shell executable modes from Git metadata across platforms.
- Current lifecycle entry point: confirmed HIGH finding AIC-007 from the completed AI-context self-audit and independent post-remediation audit.
- User constraints: independent workflow branch; durable analysis and task split before implementation; checkpoint commits at coherent stages; future merge defaults to `--no-ff`.
- Non-goals: product `src/` or `tests/` review; restoring regex-based C# semantic checks as formal gates; making every advisory warning fatal; introducing CI infrastructure without separate authorization.

## Evidence And Decisions

- All 18 tracked `.ai/scripts/**/*.sh` entries are Git mode `100644`.
- Local `core.filemode=false` and Windows Git Bash report scripts executable, masking the index truth that Unix-like checkouts receive.
- `check-all.sh` currently increments warnings, not failures, when a selected script is not executable; final exit remains `0` when `FAILED_CHECKS=0`.
- `run_check_pending` represents deferred/advisory work and must not be confused with a required check.
- Spec compliance is `conditional-required`: absent inputs mean not applicable; partial configuration is an error; once applicable, failure blocks.
- Enforcement vocabulary: `required`, `conditional-required`, `advisory`, `deferred`.
- Default executable policy: every retained `.ai/scripts/**/*.sh` asset is Git mode `100755`; exclusions require explicit retirement/removal rather than silent `100644` retention.
- Legacy grep checks, including the stale `HardDelete` archive rule, remain advisory or are retired; they are not promoted to required semantic gates.

## Development Stages

### Stage 1 — Evidence And Contract

- `stage_id`: `AIC007-001`
- Goal: preserve file-backed failure paths, enforcement vocabulary, mode matrix, and negative scenarios.
- Capability slot: `workflow-orchestration`
- Owner skill: `dev-workflow`
- Scope: `.ai/scripts/check-all.sh`, invoked scripts, Git index modes, relevant transition policies.
- Non-goals: implementation edits.
- Dependencies: completed self-audit report.
- Validation: read-only Git mode checks, targeted script inspection, persisted task evidence.
- Commit checkpoint: workflow bootstrap commit.

### Stage 2 — Durable Discovery Integrity

- `stage_id`: `AIC007-002`
- Goal: prevent `.dev/backlog/INDEX.MD` and `.dev/workflows/INDEX.MD` from drifting from YAML items and workflow locators.
- Capability slot: `local-change`
- Owner skill: `local-change-implementer`
- Scope: backlog schema validation, workflow-index locator parity, `.dev` navigation.
- Non-goals: task-level status duplication or migration of legacy workflows.
- Dependencies: Stage 1 bootstrap.
- Validation: positive parse plus missing-row/status/timestamp mutation probes.
- Commit checkpoint: discovery-governance commit.

### Stage 3 — Git Executable-Mode Contract

- `stage_id`: `AIC007-003`
- Goal: set retained shell assets to Git mode `100755` and validate index modes without trusting host filesystem executability.
- Capability slot: `implementation`
- Owner skill: `slice-implementer`
- Scope: `.ai/scripts/**/*.sh`, an index-based validator, required-runner declarations, usage documentation.
- Non-goals: arbitrary chmod of non-shell files or generated asset legitimization without classification.
- Dependencies: Stage 1 enforcement contract.
- Validation: fixture/mutation cases for `100755`, `100644`, missing runner, and ignored non-shell paths; `bash -n` for retained scripts.
- Commit checkpoint: executable-integrity commit.

### Stage 4 — Enforcement-Aware Orchestrator

- `stage_id`: `AIC007-004`
- Goal: refactor selected checks so required outcomes are pass/fail and cannot disappear into warnings.
- Capability slot: `implementation`
- Owner skill: `slice-implementer`
- Scope: explicit enforcement class, quick/critical/full selection matrix, conditional spec behavior, invalid CLI arguments, truthful summary counts.
- Non-goals: making advisory coding-standard warnings fatal.
- Dependencies: Stages 1 and 3.
- Validation: required missing/non-executable/nonzero cases exit `1`; invalid arguments exit `2`; advisory warnings may exit `0` only when required checks pass.
- Commit checkpoint: fail-closed orchestration commit.

### Stage 5 — Transitional Script Disposition

- `stage_id`: `AIC007-005`
- Goal: classify legacy grep/generated checks and remove stale `HardDelete` semantics from formal gate claims.
- Capability slot: `local-change`
- Owner skill: `local-change-implementer`
- Scope: `check-archive-compliance.sh`, generated duplicate, transition inventory and runner classification.
- Non-goals: reimplementing archive semantics with regex.
- Dependencies: Stage 4 enforcement classes.
- Validation: active runner/reference searches and no required mapping to known-invalid grep semantics.
- Commit checkpoint: transitional-tooling cleanup commit.

### Stage 6 — GWT Test Matrix And Cross-Platform Evidence

- `stage_id`: `AIC007-006`
- Goal: add deterministic Given-When-Then tests for runner and mode validation behavior.
- Capability slot: `test-design`, then `implementation`
- Owner skills: `bdd-gwt-test-designer`, then `slice-implementer`
- Scope: fixture-based Bash/Python tests, Windows Git Bash evidence, Linux/Unix-compatible commands.
- Non-goals: mandatory `.feature` files; 3A-style tests; new CI platform setup.
- Dependencies: Stages 3 through 5.
- Validation: scenario matrix for required/advisory/conditional/deferred outcomes, Git mode masking regression, mode selection, syntax, synthetic full mode, and permitted real critical/quick smoke.
- Commit checkpoint: test and portability evidence commit.

### Stage 7 — Review, Audit Handoff, And Closure

- `stage_id`: `AIC007-007`
- Goal: review implementation, verify fail-closed behavior, resolve backlog item, and close workflow with evidence.
- Capability slot: `review`
- Owner skill: `code-reviewer` for script/tooling review where applicable; `dev-workflow` owns lifecycle closure.
- Scope: changed tooling, validators, docs, workflow tasks, backlog resolution.
- Non-goals: reopening resolved AIC-001 through AIC-006/AIC-008/AIC-009.
- Dependencies: all implementation/test stages.
- Validation: narrow tests, mutation probes, context/workflow validation, real aggregate gate, Git mode evidence, independent AIC-007 verification if needed.
- Commit checkpoint: final validation and closure commit.

## Validation Strategy

- Requirement/spec traceability: map each AIC-007 evidence statement and backlog acceptance boundary to a task and negative scenario.
- Architecture validation: enforcement classes remain explicit; Git index is the executable-mode truth; workflow/backlog/index ownership remains single-source.
- Test and implementation validation: GWT scenarios, Bash syntax, fixture-based negative tests, Windows Git Bash evidence, and Unix-compatible commands.
- Review/compliance gates: `validate-ai-context.py`, `validate-workflow-artifacts.py`, discovery-index validator added by Stage 2, `git diff --check`, and `check-all.sh` modes after semantics are fixed.

## Progress And Handoff

- Current stage: all stages completed; AIC007-007 independent re-review found no remaining blocker and backlog AIC-007 is resolved.
- Completed stages: AIC007-001 through AIC007-007, including 16 synthetic GWT fixture tests, runner/manifest parity remediation, and permitted real critical/quick smoke.
- Deferred stages and reasons: hosted Linux CI requires separate authorization and remains an explicit residual gap; real full mode is excluded because its advisory helper can inspect product test code.
- Open decisions: none blocking. Optional future decision: add Linux CI after local cross-platform semantics are proven.
- Continuation instructions: none. Optional future work requires a new workflow for hosted Linux CI or manifest-driven runner execution.
- Branch history and checkpoint handoffs: branch created from `main` at merge commit `52d8f4b`.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-11-aic-007-fail-closed-validation` | `main` | workflow bootstrap | `2d4d50f` | local branch | `2026-07-11T23:43:23+08:00` | Execute durable AIC-007 tooling remediation | Complete AIC007-002 discovery-integrity validator |

## Completion Summary

- Outcome: AIC-007 resolved. Selected required checks fail closed, retained shell modes use Git index truth, runner child declarations are parity-checked, and regression fixtures protect enforcement semantics.
- Changed artifacts: validation runner and manifest, shell/workflow validators, GWT fixtures, retired generated regex tooling, backlog/index discovery, review report, and seven task records.
- Validation evidence: 16/16 GWT fixtures; 14 retained shell assets at Git mode 100755; real critical and quick gates; 47/47 analyzer and 2/2 configuration tests; workflow, backlog, AI context, shell, syntax, and diff validation.
- Commits: `2d4d50f`, `7d846f1`, `48b696a`, `817f0f4`, `d15ee29`, `26b13b3`, `4fef08f`, `f3d8f36`, and review remediation `244fc54` before the closure commit.
- Residual risks: hosted Linux execution remains unauthorized and unverified; real full mode remains excluded because its advisory helper may inspect product tests; runner parity parsing intentionally depends on a documented literal call format. Bootstrap commit `2d4d50f` lacks the current workflow-stage body and is retained as a historical exception rather than rewriting all subsequent hashes.
