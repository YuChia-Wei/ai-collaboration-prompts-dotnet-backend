# v0.5.0 Pre-Tag Portability Hotfix

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-22T08:46:21+08:00`
- `updated_at`: `2026-07-22T09:13:38+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-22-v0-5-0-pretag-portability-hotfix`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-22-v0-5-0-pretag-portability-hotfix`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `in_progress`
- `current_phase`: `post-audit`
- `artifact_root`: `.dev/workflows/2026-07-22-v0-5-0-pretag-portability-hotfix`
- `created_at`: `2026-07-22T08:46:21+08:00`
- `updated_at`: `2026-07-22T09:13:38+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: after the validated v0.5.0 candidate was merged to
  `main@3c3a66c`, the sanctioned pre-tag command reached the critical gate but
  crashed while Python decoded localized output from the Windows WSL `bash`
  launcher as UTF-8. The reader-thread failure then produced a misleading
  `None.strip()` exception and concealed that Git Bash was not selected.
- Authorized remediation scope: make the allowlisted critical-gate runner
  select Git Bash and supply its `usr/bin` tools on Windows, decode arbitrary subprocess bytes
  deterministically, retain useful failure output, and add fail-closed
  regression coverage.
- Exclusions: do not change the command allowlist, critical-gate contents,
  release compatibility, tag ownership, or publication state. v0.4.2 remains
  a required exact automatic upgrade source.
- Completion criteria: focused regression tests and repository gates pass;
  the hotfix is merged; the actual pre-tag command passes on updated `main`;
  lifecycle records are closed on a continuation branch; no tag is created.

## Artifact Contract

- Release blocker: `.dev/backlog/items/REL-002.yaml`
- Remediation report: `.dev/workflows/2026-07-22-v0-5-0-pretag-portability-hotfix/reports/remediation-report.md`
- Task: `.dev/workflows/2026-07-22-v0-5-0-pretag-portability-hotfix/tasks/PRETAG-001.json`
- Regression surfaces: `.ai/scripts/prepare-ai-context-release.py`,
  `.ai/scripts/tests/test_prepare_ai_context_release.py`

## Finding Triage

| Finding | Severity | Owner | Disposition | Task | Validation |
| --- | --- | --- | --- | --- | --- |
| `PTP-001` | HIGH / P0 | `ai-context-governance` | fix in v0.5.0 | `PRETAG-001` | byte-level fixtures, critical gate, merged-main pre-tag |

## Stages And Checkpoints

1. Register the unexpected release blocker and reopen v0.5.0 execution state.
2. Resolve Git Bash without accepting the Windows WSL launcher, prepend its
   `usr/bin` only to the child process, then implement deterministic
   replacement-safe decoding and robust empty-output handling.
3. Run focused, workflow, critical, and hosted validation; obtain a bounded
   independent review of the frozen hotfix candidate.
4. Merge the implementation branch, run the real pre-tag command on `main`,
   and record evidence on a dedicated continuation branch.
5. Merge the closeout branch and run the pre-tag command once more on final
   `main`. Keep tag creation separately owner-authorized.

## Resume Checkpoint

- Last completed action: the repaired pre-tag runner completed the unrestricted
  critical gate at `958da6e`: 33/33 passed, 0 failed, 0 deferred, and all 56
  .NET tests passed. Nine focused portability tests also pass.
- Current task: `PRETAG-001`.
- Exact next action: commit this local-gate evidence, rerun the complete gate on
  the final clean candidate commit, validate the workflow commit range, then
  push for hosted verification.
- Validation already completed: the parent candidate passed critical 33/33 and
  hosted package, governance, and Ubuntu gates before merge; the failing
  merged-main pre-tag invocation is retained as incident evidence here.
- Git state: clean implementation branch based on `main@3c3a66c` before these
  workflow artifacts.
- Blockers or unresolved decisions: no product or SemVer decision is open;
  publication and tag creation remain unauthorized.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-22-v0-5-0-pretag-portability-hotfix` | `main@3c3a66c` | validated implementation | `958da6e` | local | `2026-07-22T09:13:38+08:00` | Repair the proven merged-main release blocker. | Freeze final candidate docs, rerun exact critical and commit-range gates, then push. |
