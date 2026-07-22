# v0.5.0 Pre-Tag Portability Hotfix

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-22T08:46:21+08:00`
- `updated_at`: `2026-07-22T09:58:38+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-22-v0-5-0-pretag-portability-hotfix`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-22-v0-5-0-current-main-pretag-instruction`
- `base_branch`: `main`
- `branch_segment`: `3`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-22-v0-5-0-pretag-portability-hotfix`
- `created_at`: `2026-07-22T08:46:21+08:00`
- `updated_at`: `2026-07-22T09:58:38+08:00`
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

- Last completed action: PR #3 merged closeout as `main@03f86ccc`; sanctioned
  pre-tag was rerun successfully there and superseded the output printed before
  that merge. The current instruction makes this invalidation rule durable.
- Current task: none; `PRETAG-001` and this workflow are completed.
- Exact next action: await separate owner authorization before annotated tag
  creation. If authorized, rerun pre-tag on the then-current clean `main`,
  discard every older printed command, and use only the newly printed command
  to resume the governed tag phase.
- Validation already completed: final candidate critical 33/33 and commit range
  7/7; independent audit with no implementation blocker; hosted runs
  `29883289326`, `29883289335`, and `29883289321`; unrestricted pre-tag after
  the PR #2 and PR #3 main merges; ten focused portability tests.
- Git state: instruction-correction branch from clean `main@03f86ccc`; no
  `v0.5.0` tag exists.
- Blockers or unresolved decisions: no product or SemVer decision is open;
  publication and tag creation remain unauthorized.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-22-v0-5-0-pretag-portability-hotfix` | `main@3c3a66c` | independently reviewed candidate | `c53e1bf` | local | `2026-07-22T09:21:46+08:00` | Repair the proven merged-main release blocker. | Commit the only documentation reconciliation, rerun exact critical and commit-range gates, then push. |
| 1 | `codex/2026-07-22-v0-5-0-pretag-portability-hotfix` | `main@3c3a66c` | merged checkpoint | `47aa1cc` | PR #2 / `main@540cd029` | `2026-07-22T09:33:19+08:00` | All local, independent, and hosted gates passed. | Run sanctioned pre-tag on updated `main`, then continue on a dedicated closeout branch. |
| 2 | `codex/2026-07-22-v0-5-0-pretag-portability-closeout` | `main@540cd029` | merged closure | `0f864d5` | PR #3 / `main@03f86ccc` | `2026-07-22T09:51:52+08:00` | Record merged-main pre-tag success without mutating the tag lifecycle. | Rerun pre-tag because the closeout merge changed main HEAD. |
| 3 | `codex/2026-07-22-v0-5-0-current-main-pretag-instruction` | `main@03f86ccc` | handoff correction | instruction commit containing this update | local | `2026-07-22T09:58:38+08:00` | Prevent reuse of a tag command whose SHA became stale after a later main merge. | Validate, merge, then rerun pre-tag on current clean main; retain only the newest output. |
