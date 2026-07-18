# Backlog Index

This index catalogs durable work that must remain visible outside workflow
artifact directories. See [README.MD](README.MD) for ownership and lifecycle.

## Active Release Roadmap

| Roadmap | Current Target | Status | Next Gate | Updated |
| --- | --- | --- | --- | --- |
| [ROADMAP.md](ROADMAP.md) | `v0.4.1` | `active` | Validate and publish focused `PKG-001`/`PKG-002`; activate the complete deferred correction set in required v0.4.2. | 2026-07-18 |

Source planning records are retained under [`plans/`](plans/); they inform the
roadmap but do not replace it or a governed assessment.

## Planned / Open

| Item | Priority | Target Release | Summary | Decision / Handoff | Updated |
| --- | --- | --- | --- | --- | --- |
| [PKG-003](items/PKG-003.yaml) | HIGH | `v0.5.0` | Introduce a governed multi-source direct-upgrade contract and prove v0.3.0, v0.4.0, and v0.4.1 paths. | Design a new migration contract; retain dotnet-mq-arch-lab on v0.4.0 as the direct-upgrade acceptance target. | 2026-07-18 |
| [SAG-001](items/SAG-001.yaml) | MEDIUM | `v0.5.0` | Define selective sub-agent runtime-adapter promotion and deterministic target-to-path parity. | Correct existing translator routing in v0.4.2; add the governance and validator contract in v0.5.0 before v0.6.0 taxonomy work. | 2026-07-18 |
| [SKILL-001](items/SKILL-001.yaml) | MEDIUM | `v0.6.0` | Introduce AI context lifecycle taxonomy and transition `repo-structure-sync` to `ai-context-init` with compatibility. | Stabilize v0.5.0 governance, then design deprecation metadata and validation before renaming. | 2026-07-18 |
| [OBS-001](items/OBS-001.yaml) | MEDIUM | `unassigned` | Design the reusable CrossCutting Observability and attribute/AOP boundary. | Open a separate architecture workflow; keep it outside the current assessment-remediation verification baseline. | 2026-07-18 |
| [TOOL-001](items/TOOL-001.yaml) | MEDIUM | `v0.5.0` | Verify hosted Linux behavior and consider manifest-driven runner execution. | Decide Linux verification, runner redesign, both, or defer. | 2026-07-18 |
| [LANG-001](items/LANG-001.yaml) | MEDIUM | `v0.5.0` | Refresh and reduce translation debt before strengthening semantic parity gates. | Decide priority after a refreshed candidate inventory. | 2026-07-18 |
| [GOV-001](items/GOV-001.yaml) | MEDIUM | `v0.5.0` | Reconcile legacy workflow follow-ups against later completed work. | Read-only reconciliation first; promote only current work. | 2026-07-18 |
| [CAP-001](items/CAP-001.yaml) | LOW | `v0.5.0` | Decide the ownership of technical glossary and terminology work. | Choose a skill, extend context guidance, or defer. | 2026-07-18 |
| [VAL-001](items/VAL-001.yaml) | LOW | `v0.5.0` | Reassess deferred repository and dependency/version validation gaps. | Fresh development-tooling inventory required before planning. | 2026-07-18 |

## In Progress

No backlog items are currently in progress.

## Resolved

| Item | Priority | Completed In | Published In | Resolution | Workflow | Updated |
| --- | --- | --- | --- | --- | --- | --- |
| [PKG-001](items/PKG-001.yaml) | HIGH / P0 | `v0.4.1` | pending | Versioned migration metadata binds the exact v0.3.0 manifest and produces deterministic executable operations. | [`2026-07-18-v0-4-1-downstream-upgrade-remediation`](../workflows/2026-07-18-v0-4-1-downstream-upgrade-remediation/workflow.yaml) | 2026-07-18 |
| [PKG-002](items/PKG-002.yaml) | HIGH / P0 | `v0.4.1` | pending | Source-only suites remain required at source and are excluded/not-applicable in downstream packages; extracted target gate passed 19/19. | [`2026-07-18-v0-4-1-downstream-upgrade-remediation`](../workflows/2026-07-18-v0-4-1-downstream-upgrade-remediation/workflow.yaml) | 2026-07-18 |
| [CTX-003](items/CTX-003.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Remediated and independently verified all five CTX-001 findings with no regression. | [`2026-07-12-ai-context-truth-contract-remediation`](../workflows/2026-07-12-ai-context-truth-contract-remediation/workflow.yaml) | 2026-07-18 |
| [CTX-001](items/CTX-001.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Completed the independent post-AIC-007 audit; five findings were handed to AI context governance. | [`2026-07-12-post-aic-007-ai-context-audit`](../workflows/2026-07-12-post-aic-007-ai-context-audit/workflow.yaml) | 2026-07-18 |
| [CTX-002](items/CTX-002.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Removed the retired generated-script catalog entry and restored AI context validation. | [`2026-07-12-ctx-002-ai-index-repair`](../workflows/2026-07-12-ctx-002-ai-index-repair/workflow.yaml) | 2026-07-18 |
| [AIC-007](items/AIC-007.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Required gates fail closed; Git-index executable modes and runner/manifest parity are validated with GWT fixtures. | [`2026-07-11-aic-007-fail-closed-validation`](../workflows/2026-07-11-aic-007-fail-closed-validation/workflow.yaml) | 2026-07-18 |
