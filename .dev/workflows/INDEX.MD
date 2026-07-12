# Workflow Index

This index is the discovery view for workflow records. Each workflow's
`workflow.yaml` remains the lifecycle source of truth; this file must not repeat
task-level progress.

## Active Workflows

| Workflow | Title | Owner | Status | Updated | Entry Point |
| --- | --- | --- | --- | --- | --- |
| [`2026-07-11-aic-007-fail-closed-validation`](2026-07-11-aic-007-fail-closed-validation/workflow.yaml) | AIC-007 Fail-Closed Validation And Executable Modes | `dev-workflow` | `active` | `2026-07-12T08:19:41+08:00` | [plan](2026-07-11-aic-007-fail-closed-validation/workflow-plan.md) |

## Completed Post-Adoption Workflows

| Workflow | Title | Owner | Status | Updated | Entry Point |
| --- | --- | --- | --- | --- | --- |
| [`2026-07-11-workflow-branch-lifecycle-policy`](2026-07-11-workflow-branch-lifecycle-policy/workflow.yaml) | Workflow Branch Lifecycle Policy | `ai-context-governance` | `completed` | `2026-07-11T00:23:58+08:00` | [plan](2026-07-11-workflow-branch-lifecycle-policy/workflow-plan.md) |
| [`2026-07-10-ai-context-self-audit`](2026-07-10-ai-context-self-audit/workflow.yaml) | 2026-07-10 AI Context Self-Audit And Remediation | `ai-context-governance` | `completed` | `2026-07-11T23:30:00+08:00` | [plan](2026-07-10-ai-context-self-audit/workflow-plan.md) |
| [`2026-07-10-ai-context-workflow-governance`](2026-07-10-ai-context-workflow-governance/workflow.yaml) | AI Context Workflow Governance | `ai-context-governance` | `completed` | `2026-07-10T23:41:46+08:00` | [plan](2026-07-10-ai-context-workflow-governance/workflow-plan.md) |

## Legacy Workflow Records

Directories without a post-adoption `workflow.yaml` are listed without inferred
lifecycle states. Add a locator only when a legacy workflow is formally resumed.

| Legacy Workflow | State |
| --- | --- |
| [`2026-04-14-legacy-decision-portability-consolidation`](2026-04-14-legacy-decision-portability-consolidation/) | legacy / no locator |
| [`2026-04-14-legacy-script-rename`](2026-04-14-legacy-script-rename/) | legacy / no locator |
| [`2026-04-15-problem-frame-validator-pilot`](2026-04-15-problem-frame-validator-pilot/) | legacy / no locator |
| [`2026-05-ai-context-boundary-and-governance`](2026-05-ai-context-boundary-and-governance/) | legacy / no locator |
| [`2026-05-ai-context-skill-and-doc-cleanup`](2026-05-ai-context-skill-and-doc-cleanup/) | legacy / no locator |
| [`2026-05-dotnet-script-to-analyzer-transition`](2026-05-dotnet-script-to-analyzer-transition/) | legacy / no locator |
| [`2026-05-repo-identity-and-init-template`](2026-05-repo-identity-and-init-template/) | legacy / no locator |
| [`2026-06-dev-workflow-core-profile`](2026-06-dev-workflow-core-profile/) | legacy / no locator |
| [`2026-06-dev-workflow-skill`](2026-06-dev-workflow-skill/) | legacy / no locator |
| [`2026-06-implementer-taxonomy-domain-language`](2026-06-implementer-taxonomy-domain-language/) | legacy / no locator |
| [`2026-06-requirements-skill-naming-domain-language`](2026-06-requirements-skill-naming-domain-language/) | legacy / no locator |
| [`2026-07-agent-execution-principles`](2026-07-agent-execution-principles/) | legacy / no locator |
| [`2026-07-ai-context-audit-report-translation`](2026-07-ai-context-audit-report-translation/) | legacy / no locator |
| [`2026-07-ai-context-auditor-skill`](2026-07-ai-context-auditor-skill/) | legacy / no locator |
| [`2026-07-ai-context-relationship-audit`](2026-07-ai-context-relationship-audit/) | legacy / no locator |
| [`2026-07-dotnet-validator-phase-2`](2026-07-dotnet-validator-phase-2/) | legacy / no locator |
| [`2026-07-dotnet-validator-phase-3`](2026-07-dotnet-validator-phase-3/) | legacy / no locator |
| [`2026-07-historical-context-normalization`](2026-07-historical-context-normalization/) | legacy / no locator |
| [`2026-07-repository-pattern-standards-alignment`](2026-07-repository-pattern-standards-alignment/) | legacy / no locator |
| [`2026-07-usecase-command-handler-boundary`](2026-07-usecase-command-handler-boundary/) | legacy / no locator |

## Templates

| Path | Purpose |
| --- | --- |
| [`templates/`](templates/) | Legacy shared workflow templates retained for historical consumers; new workflows use their owner skill's templates. |

## Related Discovery

- [Workflow artifact policy](../standards/WORKFLOW-ARTIFACT-POLICY.md)
- [Durable backlog](../backlog/INDEX.MD)
- [Workflow README](README.MD)
