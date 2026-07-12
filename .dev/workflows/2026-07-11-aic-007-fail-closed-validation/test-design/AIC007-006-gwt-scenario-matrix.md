# AIC007-006 GWT Scenario Matrix

## Inputs Used

- `.dev/workflows/2026-07-11-aic-007-fail-closed-validation/tasks/AIC007-006.json`
- `.ai/scripts/check-all.sh`
- `.ai/scripts/validate-shell-assets.py`
- `.ai/scripts/shell-assets.yaml`
- `bdd-gwt-test-designer` canonical contracts

Assumptions: scenario notes are canonical for this slice; no `.feature` file or
feature runner is selected. The implementation uses fixture-based Bash/Python
tests without BDDfy, while preserving mandatory Given-When-Then structure.

## Scenario Set

| ID | Priority | Scenario | Given | When | Then |
| --- | --- | --- | --- | --- | --- |
| GWT-001 | P0 | Required script is missing | A synthetic runner selects a required script whose path is absent. | The selecting mode executes. | Exit is `1`; output says `FAILED` and `not found`; required selected/executed/failed are `1/0/1`. |
| GWT-002 | P0 | Git mode 100644 is rejected | A required script exists in a temporary Git index as `100644`, even if the Windows host reports it executable. | The shell asset validator executes. | Exit is `1`; output names the path and expected `100755` versus found `100644`. |
| GWT-003 | P0 | Required script returns nonzero | An executable required stub returns `17`. | The runner selects it. | Aggregate exit is `1`; required executed/failed are `1/1`; the failure is counted once. |
| GWT-004 | P0 | Required command is unavailable | A deterministic fixture command returns `127` through an isolated PATH. | The runner selects it. | Aggregate exit is `1` and the required failure count increments without depending on workstation tools. |
| GWT-005 | P0 | Advisory failure remains visible and nonblocking | All required stubs pass and a selected advisory stub fails. | Full mode executes. | Exit is `0`; advisory warnings are `1`; required failed is `0`; output says passed with advisory warning, not all passed. |
| GWT-006 | P0 | Conditional spec is not applicable | `SPEC_FILE` and `TASK_NAME` are both unset. | Quick or full mode reaches spec compliance. | N/A increments; spec does not increment required selected/failed; other required results determine exit. |
| GWT-007 | P0 | Conditional spec is partially configured | Exactly one of `SPEC_FILE` or `TASK_NAME` is set. | A mode selecting spec compliance executes. | Exit is `1`; output requires both inputs; required selected/executed/failed are `1/0/1`. |
| GWT-008 | P0 | Conditional spec is fully configured | Both inputs and an executable spec stub exist. | The stub passes or fails. | Passing increments required executed/passed; failing exits `1` and increments required failed. |
| GWT-009 | P0 | Deferred check is not a hidden required skip | A selected deferred entry has no implementation script. | Quick or full mode reaches it. | It is labelled `DEFERRED`; only deferred count increments; it cannot alone make exit nonzero. |
| GWT-010 | P0 | Mode selection matrix is truthful | Identical passing stubs exist for representative critical, quick, and full checks. | `--critical`, `--quick`, `--full`, and default execute. | Only declared members run; skipped-by-mode is correct; default equals full. |
| GWT-011 | P0 | Invalid CLI launches no checks | The invocation has an unknown argument or more than one argument. | The runner starts. | Exit is `2`; usage/error is emitted; no sentinel indicates a check launch. Help is a P1 example with exit `0`. |
| GWT-012 | P0 | Manifest coverage mismatch is rejected | A temporary repo has a tracked shell omitted by the manifest or an extra nonexistent manifest path. | The shell validator executes. | Exit is `1` with deterministic missing/extra lists. |
| GWT-013 | P1 | Manifest lifecycle invariants are rejected | A path overlaps lifecycle groups, is duplicated, or a required path is outside retained. | The validator executes. | Exit is `1` with the matching invariant message. |
| GWT-014 | P0 | Valid manifest passes | Every tracked shell is classified, retained paths are `100755`, and required groups are retained subsets. | The validator executes. | Exit is `0`; reported retained/retirement/tracked counts match the fixture. |
| GWT-015 | P0 | Fixtures never mutate the real repository | The original HEAD, porcelain status, and shell stage snapshot are captured; scenarios use a new temporary repo. | All mutation scenarios run, including failure cleanup. | Original snapshots are unchanged and the temporary root is removed. |
| GWT-016 | P0 | Real checkout smoke evidence | The real checkout is clean. | Bash syntax, shell validator, and permitted aggregate modes run. | Results and expected exits are recorded; advisory warnings remain visibly nonblocking. |
| GWT-017 | P1 | Hosted Linux execution remains explicit | Windows Git Bash behavior and portable commands are locally proven, but hosted CI is not authorized. | The workflow prepares closure evidence. | Unix command recipe is recorded and hosted execution remains a residual gap, never a claimed pass. |

## Assertion Notes

- Capture stdout, stderr, and exit code separately.
- Assert classification labels and counters, not only aggregate exit codes.
- Use sentinel logs/files to assert which checks did or did not launch.
- Use `git update-index --chmod=+x/-x` inside the temporary repository for mode truth.
- Prepend deterministic stubs to fixture PATH; never depend on local `dotnet` or
  `python` being absent.
- Treat child nonzero codes as a required failure; the aggregate need not
  propagate the exact child code.

## Fixture Safety Contract

1. Create a new temporary repository and copy only the runner/validator plus
   minimal fixture scripts and manifest.
2. Never source `check-all.sh`; it calls `exit` and must run as a process.
3. Never run `chmod`, `git update-index`, PATH mutation, or destructive cleanup
   against the real repository.
4. Snapshot real `git status --porcelain` and `git ls-files --stage
   '.ai/scripts/**/*.sh'` before and after the suite.
5. Restore environment variables with `trap`/`finally` and remove temporary
   state on success and failure.
6. PyYAML availability is an explicit test precondition.

## Coverage Gaps And Deferred Evidence

- The current runner contains fixed command text and derives `PROJECT_ROOT` from
  its location. The harness should copy it into a synthetic repository and stub
  `python`/`dotnet`, not source or patch the real runner.
- Hosted Linux CI is not authorized. Record this command recipe for a future
  Unix-like checkout: Git stage inventory, shell validator, Bash syntax, quick
  gate, and explicitly authorized full/advisory execution.
- Full mode against the real repository remains excluded while it can invoke a
  legacy advisory grep helper that scans product code.

## Execution Evidence

Recorded on `2026-07-12` using Windows Git Bash:

- `python .ai/scripts/tests/test_fail_closed_validation.py -v`: 15 test methods
  passed, covering GWT-001 through GWT-015; full mode is exercised safely in a
  synthetic repository.
- `bash -n ./.ai/scripts/check-all.sh`: passed.
- `python .ai/scripts/validate-shell-assets.py`: passed for 14 retained Git-mode
  `100755` shell assets and zero retirement candidates.
- `bash ./.ai/scripts/check-all.sh --critical`: passed 6/6 required checks;
  analyzer template tests passed 47/47 and configuration tests passed 2/2.
- `bash ./.ai/scripts/check-all.sh --quick`: passed 6/6 required checks and
  truthfully reported one deferred and one not-applicable check.
- Real full mode was not run because its advisory test helper can inspect product
  test code, which is outside this workflow's audit boundary.

Portable Unix-like follow-up recipe:

```bash
git ls-files --stage '*.sh'
python .ai/scripts/validate-shell-assets.py
bash -n .ai/scripts/check-all.sh
python .ai/scripts/tests/test_fail_closed_validation.py -v
bash .ai/scripts/check-all.sh --critical
bash .ai/scripts/check-all.sh --quick
```

Hosted Linux execution remains an explicit residual gap requiring separate CI
authorization; it is not claimed as a pass.

## Recommended Test Spec Path

This is repository-tooling workflow evidence rather than product behavior, so
the canonical artifact remains here:

`.dev/workflows/2026-07-11-aic-007-fail-closed-validation/test-design/AIC007-006-gwt-scenario-matrix.md`
