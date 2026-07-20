# Backlog Index

This index catalogs durable work that must remain visible outside workflow
artifact directories. See [README.MD](README.MD) for ownership and lifecycle.

## Active Release Roadmap

| Roadmap | Current Target | Status | Next Gate | Updated |
| --- | --- | --- | --- | --- |
| [ROADMAP.md](ROADMAP.md) | `v0.5.0` | `active` | Complete the active v0.5.0 inventory and decision freeze, then execute the bounded release tasks with checkpoint commits. | 2026-07-21 |

Source planning records are retained under [`plans/`](plans/); they inform the
roadmap but do not replace it or a governed assessment.

## Planned / Open

| Item | Priority | Target Release | Gate | Summary | Decision / Handoff | Updated |
| --- | --- | --- | --- | --- | --- | --- |
| [REL-001](items/REL-001.yaml) | HIGH | `v0.5.0` | release blocker | Make release publication executable from repository files through a runbook, templates, pre-tag gate, and terminal-state validation. | Coordinate PR CI with ENF-001 without merging ownership. | 2026-07-20 |
| [HANDOFF-001](items/HANDOFF-001.yaml) | HIGH | `v0.5.0` | release blocker | Add a fail-closed receiving-agent checkpoint for model, runtime, host, and fresh-session handoffs. | Approve the evidence shape; a red critical gate blocks continuation except for its explicit repair task. | 2026-07-20 |
| [PKG-003](items/PKG-003.yaml) | HIGH | `v0.5.0` | release blocker | Introduce a governed multi-source direct-upgrade contract and prove v0.3.0, v0.4.0, and v0.4.1 paths. | Start only after v0.4.2 completes; retain dotnet-mq-arch-lab on v0.4.0 as the direct-upgrade target. | 2026-07-19 |
| [SAG-001](items/SAG-001.yaml) | MEDIUM | `v0.5.0` | release blocker | Define selective sub-agent runtime-adapter promotion and deterministic target-to-path parity. | Correct existing translator routing in v0.4.2; implement the adapter contract in v0.5.0. | 2026-07-19 |
| [ENF-001](items/ENF-001.yaml) | HIGH | `v0.5.0` | release blocker | Add semantic wrapper validation and governance CI, then disposition obsolete published paths with migration evidence. | Approve the new enforcement contracts and every retain/deprecate/relocate/remove decision. | 2026-07-19 |
| [TOOL-001](items/TOOL-001.yaml) | MEDIUM | `v0.5.0` | release blocker | Institutionalize hosted portability evidence and resolve the runner design. | Retain or redesign the runner explicitly; do not imply unexecuted macOS coverage. | 2026-07-19 |
| [LANG-001](items/LANG-001.yaml) | MEDIUM | `v0.5.0` | release blocker | Refresh and remediate approved translation debt, then establish semantic parity evidence. | Complete the approved batch and human, automated, or hybrid parity gate before publication. | 2026-07-19 |
| [GOV-001](items/GOV-001.yaml) | MEDIUM | `v0.5.0` | disposition gate | Reconcile legacy workflow follow-ups against later completed work. | Read-only reconciliation first; explicitly retain, promote, or close each current result. | 2026-07-19 |
| [CAP-001](items/CAP-001.yaml) | LOW | `v0.5.0` | disposition gate | Decide the ownership of technical glossary and terminology work. | Choose a skill, extend context guidance, or explicitly defer. | 2026-07-19 |
| [VAL-001](items/VAL-001.yaml) | LOW | `v0.5.0` | disposition gate | Reassess deferred repository and dependency/version validation gaps. | Fresh inventory, then explicitly implement, defer, or close the gap. | 2026-07-19 |
| [EVAL-001](items/EVAL-001.yaml) | HIGH | `v0.6.0` | activation gate | Add deterministic regression plus budgeted release-side model evaluation before taxonomy changes. | Approve the fixture corpus, oracle, model/judge, repetitions, threshold, and token ceiling. | 2026-07-19 |
| [SKILL-001](items/SKILL-001.yaml) | MEDIUM | `v0.6.0` | release blocker | Introduce AI context lifecycle taxonomy and transition `repo-structure-sync` to `ai-context-init` with compatibility. | Complete v0.5.0 and EVAL-001 before changing identifiers or taxonomy. | 2026-07-19 |
| [SIMPL-001](items/SIMPL-001.yaml) | MEDIUM | `v0.6.0` | disposition gate | Measure actual loaded context, disposition simplification candidates, and keep historical archive migration conditional on a separately approved v0.7.0 successor. | Do not equate corpus words with prompt tokens; preserve stable evidence until every archive precondition is proven. | 2026-07-20 |
| [STD-001](items/STD-001.yaml) | HIGH | `unassigned` | independent | Run bounded standards discussions across ChatGPT, Fable 5, and repository agents before assigning implementation to a release. | Normalize external feedback through assessments; permit a dedicated standards release after owner review. | 2026-07-20 |
| [OBS-001](items/OBS-001.yaml) | MEDIUM | `unassigned` | independent | Design the reusable CrossCutting Observability and attribute/AOP boundary. | Open a separate architecture workflow; it is not a hidden release gate. | 2026-07-18 |

## Resolved

| Item | Priority | Completed In | Published In | Resolution | Workflow | Updated |
| --- | --- | --- | --- | --- | --- | --- |
| [R042-005](items/R042-005.yaml) | HIGH / P0 | `v0.4.2` | — | Local finalization and the authorized public Release body correction are verified; the immutable tag and four published assets were unchanged. | [`2026-07-20-v0-4-2-release-finalization-hotfix`](../workflows/2026-07-20-v0-4-2-release-finalization-hotfix/workflow.yaml) | 2026-07-20 |
| [R042-001](items/R042-001.yaml) | HIGH | `v0.4.2` | `v0.4.2` | Existing wrapper identity and routing corrections are independently verified without adding adapter contracts. | [`2026-07-19-v0-4-2-remediation`](../workflows/2026-07-19-v0-4-2-remediation/workflow.yaml) | 2026-07-20 |
| [R042-002](items/R042-002.yaml) | HIGH | `v0.4.2` | `v0.4.2` | Handler, time, naming, and spec examples align with existing canonical doctrine. | [`2026-07-19-v0-4-2-remediation`](../workflows/2026-07-19-v0-4-2-remediation/workflow.yaml) | 2026-07-20 |
| [R042-003](items/R042-003.yaml) | MEDIUM | `v0.4.2` | `v0.4.2` | Navigation and lifecycle facts are corrected while published historical paths remain retained. | [`2026-07-19-v0-4-2-remediation`](../workflows/2026-07-19-v0-4-2-remediation/workflow.yaml) | 2026-07-20 |
| [R042-004](items/R042-004.yaml) | HIGH | `v0.4.2` | `v0.4.2` | Patch-safe interpreter, dependency, root, and test portability corrections pass Windows Git Bash and Codespaces Ubuntu 24.04. | [`2026-07-19-v0-4-2-remediation`](../workflows/2026-07-19-v0-4-2-remediation/workflow.yaml) | 2026-07-20 |
| [PKG-001](items/PKG-001.yaml) | HIGH / P0 | `v0.4.1` | `v0.4.1` | Versioned migration metadata binds the exact v0.3.0 manifest and produces deterministic executable operations. | [`2026-07-18-v0-4-1-downstream-upgrade-remediation`](../workflows/2026-07-18-v0-4-1-downstream-upgrade-remediation/workflow.yaml) | 2026-07-18 |
| [PKG-002](items/PKG-002.yaml) | HIGH / P0 | `v0.4.1` | `v0.4.1` | Source-only suites remain required at source and are excluded/not-applicable in downstream packages; extracted target gate passed 19/19. | [`2026-07-18-v0-4-1-downstream-upgrade-remediation`](../workflows/2026-07-18-v0-4-1-downstream-upgrade-remediation/workflow.yaml) | 2026-07-18 |
| [CTX-003](items/CTX-003.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Remediated and independently verified all five CTX-001 findings with no regression. | [`2026-07-12-ai-context-truth-contract-remediation`](../workflows/2026-07-12-ai-context-truth-contract-remediation/workflow.yaml) | 2026-07-18 |
| [CTX-001](items/CTX-001.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Completed the independent post-AIC-007 audit; five findings were handed to AI context governance. | [`2026-07-12-post-aic-007-ai-context-audit`](../workflows/2026-07-12-post-aic-007-ai-context-audit/workflow.yaml) | 2026-07-18 |
| [CTX-002](items/CTX-002.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Removed the retired generated-script catalog entry and restored AI context validation. | [`2026-07-12-ctx-002-ai-index-repair`](../workflows/2026-07-12-ctx-002-ai-index-repair/workflow.yaml) | 2026-07-18 |
| [AIC-007](items/AIC-007.yaml) | HIGH | `v0.1.0` | `v0.1.0` | Required gates fail closed; Git-index executable modes and runner/manifest parity are validated with GWT fixtures. | [`2026-07-11-aic-007-fail-closed-validation`](../workflows/2026-07-11-aic-007-fail-closed-validation/workflow.yaml) | 2026-07-18 |
