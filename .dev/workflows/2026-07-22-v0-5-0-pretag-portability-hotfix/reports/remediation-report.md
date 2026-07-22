# v0.5.0 Pre-Tag Portability Remediation Report

## Report Metadata

- `report_id`: `remediation-report-2026-07-22-v0-5-0-pretag-portability-hotfix`
- `workflow_id`: `2026-07-22-v0-5-0-pretag-portability-hotfix`
- `owner_skill`: `ai-context-governance`
- `status`: `final`
- `created_at`: `2026-07-22T08:46:21+08:00`
- `updated_at`: `2026-07-22T09:58:38+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-remediation-report-template.md`
- `template_version`: `2.0.0`

## Remediation Summary

- Authorized scope: repair the proven Windows Bash-selection, child PATH, and
  subprocess-output portability defects in the v0.5.0 pre-tag path.
- Completed scope: incident registered; bounded Git Bash resolver, decoder fix,
  child-only Git `usr/bin` environment, combined-stream failure reporting, and
  six regression scenarios implemented.
- Validation summary: 10 focused pre-tag tests, live Windows resolution to
  `C:\Program Files\Git\bin\bash.exe`, 15 adjacent release-state tests,
  6 backlog lifecycle tests, workflow validation, and AI-context validation
  pass. After a sandbox attempt correctly reported three `NU1301` network
  denials, the unrestricted runner completed 33/33 critical checks with 0
  failed and 0 deferred at `958da6e`; all 56 .NET tests passed. Exact candidate
  `c53e1bf` repeated 33/33. Independent review found no implementation blocker;
  its one low-severity roadmap summary omission is corrected in this checkpoint.
  Final candidate `47aa1cc` repeated 33/33 and passed hosted runs
  `29883289326`, `29883289335`, and `29883289321`. PR #2 merged it as
  `main@540cd029`, where the unrestricted sanctioned pre-tag command passed,
  reported all four exact automatic sources, and created no tag. PR #3 then
  merged lifecycle closeout as `main@03f86ccc`; preparation was rerun there,
  superseded the older output, and exposed the need for the durable
  current-main invalidation rule now covered by focused test 10.
- Closure decision: `ready`.

## Finding Resolution Matrix

| Finding | Before Severity | Status | Changed Files | Validation | Commit | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `PTP-001` | HIGH / P0 | `resolved` | pre-tag script, tests, backlog, roadmap, and workflow records | final critical 33/33; hosted triad green; merged-main pre-tag passed | `47aa1cc`, merge `540cd029` | sandboxed NuGet restore still requires approved network access; tag remains owner-authorized |

## Closure Evidence

- Required validations: ten focused portability fixtures; adjacent release and
  backlog suites; final candidate critical 33/33; workflow commit range 7/7;
  independent no-blocker audit; hosted package, governance, and Ubuntu gates;
  unrestricted merged-main pre-tag all pass.
- Commit status: implementation `47aa1cc` merged through PR #2 as `540cd029`;
  lifecycle closeout `0f864d5` merged through PR #3 as `03f86ccc`; durable
  current-main invalidation is the instruction commit containing this update.
- Workflow/task status: completed.
- Final next action: await separate owner authorization before annotated tag
  creation. If authorized, rerun pre-tag on the then-current clean `main`,
  discard every older printed command, and use only the newly printed command
  before proceeding through governed tag, publication, and finalization phases.
  Do not tag or publish before that authorization.
