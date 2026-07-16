# v0.4.0 AI Context Remediation Report

## Template Metadata

- `template_id`: `ai-context-governance-remediation-report`
- `template_version`: `2.0.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Report Metadata

- `report_id`: `remediation-report-2026-07-16-v0-4-0-ai-context-remediation`
- `workflow_id`: `2026-07-16-v0-4-0-ai-context-remediation`
- `owner_skill`: `ai-context-governance`
- `status`: `draft`
- `created_at`: `2026-07-16T07:22:13+08:00`
- `updated_at`: `2026-07-16T21:12:11+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-remediation-report-template.md`
- `template_version`: `2.0.0`
- `baseline_assessment`: `ASM-20260715-002`
- `historical_assessment`: `ASM-20260715-001` (superseded)
- `verification_assessment`: pending

## Remediation Summary

- Authorized scope: all review gates and the first active-truth remediation slice are approved with recorded conditions.
- Completed scope: assessment intake, decision register, repository lineage, reconstruction contract, task-order correction, file-disposition manifest prerequisite, and the first active-truth remediation slice.
- Validation summary: workflow, assessment, and AI-context validators pass; nine task JSON files parse; `git diff --check` passes.
- Closure decision: `not-ready`

## Finding Resolution Matrix

| Assessment Finding | Before Severity | Status | Task | Residual Risk |
| --- | --- | --- | --- | --- |
| `ASM-20260715-002#AIC-001` | HIGH | `not-addressed` | `RULE-001` | Conflicting profile selectors remain active. |
| `#AIC-002` | HIGH | `not-addressed` | `RULE-001` | Applicability decision remains open. |
| `#AIC-003` | HIGH | `not-addressed` | `EXAMPLE-001` | Verification claims remain stronger than evidence. |
| `#AIC-004` | HIGH | `resolved` | `TRUTH-001` | DBA1001/build guidance replaces the removed script and active script references now fail closed when missing; independent verification remains pending. |
| `#AIC-005` | HIGH | `not-addressed` | `BUILD-001` | Placeholder APIs remain unresolved. |
| `#AIC-006` | MEDIUM | `not-addressed` | `EXAMPLE-001` | Duplicate maintenance remains. |
| `#AIC-007` | MEDIUM | `not-addressed` | `ROUTE-001` | Audience/placement drift remains. |
| `#AIC-008` | MEDIUM | `not-addressed` | `VALIDATE-001` | Structural gate can still be over-read. |
| `#AIC-009` | MEDIUM | `not-addressed` | `VALIDATE-001` | Retention still conflates lifecycle meanings. |
| `#AIC-010` | MEDIUM | `not-addressed` | `TRUTH-001` | Synchronous controller example remains. |
| `#AIC-011` | LOW | `not-addressed` | `ROUTE-001` | Weakly routed material remains undecided. |
| `#AIC-012` | MEDIUM | `resolved` | `TRUTH-001` | Active canonical guidance now uses the portable BoundedContextContracts placeholder; independent verification remains pending. |
| `#AIC-013` | HIGH | `not-addressed` | `RULE-001` | User selected NSubstitute; docs and downstream evidence still disagree. |
| `#AIC-014` | MEDIUM | `not-addressed` | `BUILD-001`, `ARCH-001` | Canonical architecture lacks a compact verified reference. |

## Supplemental Architecture Decisions

- `V040-DEC-001`: NSubstitute is the framework profile default; a target may replace it through one explicit technology-selection override.
- `V040-DEC-002`: soft delete is a default profile with explicit target opt-out; physical purge is an explicit restricted capability.
- `V040-DEC-003`: the minimal common logical solution-folder grammar is approved; detailed physical layout and cross-profile migration design are excluded.
- `V040-DEC-004`: full Observability design is moved out of this workflow; only the bounded CrossCutting/Domain dependency statement may remain as input.
- `V040-DEC-005`: BuildingBlocks defaults to contracts/interfaces; optional `EsAggregateRoot<TId>` option B is approved with executable tests, an independent behavior contract, and source-copy/upgrader ownership rules.
- `V040-DEC-006`: example evidence tiers are machine-readable; structure-validated names its validator; unclassified legacy defaults downward.
- `V040-DEC-007`: mocking, ORM, broker, and similar choices share one generic technology-selection override shape.
- `V040-DEC-008`: every changed framework path receives a file disposition for upgrader and migration-guide consumption.
- Provenance: `ai-coding-exercise` Java origin -> initial .NET standards -> `dotnet-mq-arch-lab` adoption/refinement -> implementation removal and continued evolution in this standalone AI context repository. Historical names are classification evidence, not current truth.

## Deferred Work

| Item | Reason | Owner | Next Action |
| --- | --- | --- | --- |
| NuGet packages for analyzers/BuildingBlocks | Explicitly not now | user / future workflow | Reconsider only if reusable binaries become a separate product goal. |
| Distributable `dotnet new` template | Outside the current knowledge-first repository scope | architecture + governance | Evaluate separately if deterministic source reproduction becomes a product goal. |
| Executable clean-room reconstruction exercise | Useful but not required for the planning MVP | independent verifier / future authorization | Run outside the committed context surface and retain only assessment evidence if later approved. |
| Full CrossCutting Observability design | Does not map to an assessment finding and would broaden verification scope | future architecture workflow | Retain only the minimal dependency-boundary candidate in this workflow. |
| Product remediation in either lab | Outside this framework workflow | target repository owners | Use target-owned workflow if authorized. |
| Remote assessment branch cleanup | No authorization | user | Decide separately; do not delete implicitly. |

## Closure Evidence

- Required validations: workflow bootstrap validations passed; remediation and closure gates remain pending.
- Commit status: gate-decision checkpoint `ed5f8fb` and first-remediation checkpoint `4b6ea28` are committed and pushed for review.
- Workflow/task status: `PLAN-001` and `TRUTH-001` completed; `RULE-001` in progress; later remediation tasks remain pending.
- Final next action: publish the first remediation checkpoint, then inventory generic technology-selection and soft-delete projections for `RULE-001`.
