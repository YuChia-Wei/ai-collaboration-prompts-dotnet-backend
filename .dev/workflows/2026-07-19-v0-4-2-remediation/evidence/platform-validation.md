# v0.4.2 Platform Validation Evidence

## Evidence Contract

- Candidate implementation revision:
  `e76d89ca7927152cd993af7d53c3f0eb8a322384`
- Evidence must name the executed platform, command, revision, and result.
- A passing result is not transferred to an unexecuted platform.

## Windows Git Bash

- Status: `passed`
- Executed at: `2026-07-19T13:27:03+08:00` through
  `2026-07-19T13:28:55+08:00`
- Revision:
  `e76d89ca7927152cd993af7d53c3f0eb8a322384`
- Worktree before execution: clean
- Host: `Microsoft Windows NT 10.0.26200.0`
- Shell: `GNU bash 5.3.9(1)-release (x86_64-pc-cygwin)` from Git for Windows
- Python: `3.13.14`
- .NET SDK: `10.0.302`
- Command:

  ```powershell
  & 'C:\Program Files\Git\bin\bash.exe' .ai/scripts/check-all.sh --quick
  ```

- Result: exit `0`; 21 required checks selected, 21 executed, 21 passed,
  0 failed, 0 advisory warnings, 1 declared deferred check, and 2
  not-applicable checks.
- .NET evidence inside the gate: 49 analyzer tests, 2 configuration-validation
  tests, and 5 BuildingBlocks behavior tests passed.
- Expected platform-specific limitation: the package-apply symlink fixture
  reported one unittest skip because Windows did not grant symlink creation;
  the required package-apply suite and aggregate gate still passed.

## Hosted Ubuntu

- Status: `pending`
- Revision: must use
  `e76d89ca7927152cd993af7d53c3f0eb8a322384` or an explicitly superseding
  candidate revision.
- Required command:

  ```text
  .ai/scripts/check-all.sh --quick
  ```

- Constraint: v0.4.2 must not add a new required CI route. The current
  repository workflows do not execute this aggregate gate, so hosted execution
  requires an owner-approved external environment or an already-authorized
  remote checkpoint.

## macOS

- Status: `unverified`
- Owner decision: environment will be arranged separately.
- No v0.4.2 artifact may imply macOS execution or support evidence.
