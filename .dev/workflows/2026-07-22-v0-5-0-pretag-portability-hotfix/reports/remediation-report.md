# v0.5.0 Pre-Tag Portability Remediation Report

## Report Metadata

- `report_id`: `remediation-report-2026-07-22-v0-5-0-pretag-portability-hotfix`
- `workflow_id`: `2026-07-22-v0-5-0-pretag-portability-hotfix`
- `owner_skill`: `ai-context-governance`
- `status`: `draft`
- `created_at`: `2026-07-22T08:46:21+08:00`
- `updated_at`: `2026-07-22T09:05:56+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-remediation-report-template.md`
- `template_version`: `2.0.0`

## Remediation Summary

- Authorized scope: repair the proven Windows Bash-selection, child PATH, and
  subprocess-output portability defects in the v0.5.0 pre-tag path.
- Completed scope: incident registered; bounded Git Bash resolver, decoder fix,
  child-only Git `usr/bin` environment, combined-stream failure reporting, and
  five regression scenarios implemented.
- Validation summary: 9 focused pre-tag tests, live Windows resolution to
  `C:\Program Files\Git\bin\bash.exe`, 15 adjacent release-state tests,
  6 backlog lifecycle tests, workflow validation, and AI-context validation
  pass. A full sandbox attempt reached all checks without shell/decoder failure
  but three .NET restores were denied network access with `NU1301`; unrestricted
  critical, hosted, and merged-main evidence remains pending.
- Closure decision: `not-ready`.

## Finding Resolution Matrix

| Finding | Before Severity | Status | Changed Files | Validation | Commit | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `PTP-001` | HIGH / P0 | `partially-resolved` | pre-tag script and tests | 30 focused/adjacent tests pass; sandbox full gate reached .NET restore boundary | pending | unrestricted critical, merged-main pre-tag, and hosted evidence remain pending |

## Closure Evidence

- Required validations: focused portability fixtures pass; unrestricted local
  critical, hosted gates, and real pre-tag preparation on merged `main` remain
  pending.
- Commit status: pending.
- Workflow/task status: in progress.
- Final next action: commit combined-stream diagnostics, rerun the critical
  gate outside the network-restricted sandbox, and push for hosted
  verification; do not tag or publish.
