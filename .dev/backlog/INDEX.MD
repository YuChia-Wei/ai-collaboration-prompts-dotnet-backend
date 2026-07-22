# Backlog Index

This index catalogs durable work that must remain visible outside workflow
artifact directories. See [README.MD](README.MD) for ownership and lifecycle.

## Active Release Roadmap

| Roadmap | Current Target | Status | Next Gate | Updated |
| --- | --- | --- | --- | --- |
| [ROADMAP.md](ROADMAP.md) | `v0.5.0` | `release_ready` | Await separate owner authorization for the exact annotated tag; no tag or publication exists yet. | 2026-07-22 |

Source planning records are retained under [`plans/`](plans/); they inform the
roadmap but do not replace it or a governed assessment.

## Planned / Open

| Item | Priority | Target Release | Gate | Summary | Decision / Handoff | Updated |
| --- | --- | --- | --- | --- | --- | --- |
| [EVAL-001](items/EVAL-001.yaml) | HIGH | `v0.6.0` | activation gate | Add deterministic regression plus budgeted release-side model evaluation before taxonomy changes. | Approve the fixture corpus, oracle, model/judge, repetitions, threshold, and token ceiling. | 2026-07-19 |
| [SKILL-001](items/SKILL-001.yaml) | MEDIUM | `v0.6.0` | release blocker | Introduce AI context lifecycle taxonomy and transition `repo-structure-sync` to `ai-context-init` with compatibility. | Complete v0.5.0 and EVAL-001 before changing identifiers or taxonomy. | 2026-07-19 |
| [SIMPL-001](items/SIMPL-001.yaml) | MEDIUM | `v0.6.0` | disposition gate | Measure actual loaded context, disposition simplification candidates, and keep historical archive migration conditional on a separately approved v0.7.0 successor. | Do not equate corpus words with prompt tokens; preserve stable evidence until every archive precondition is proven. | 2026-07-20 |
| [STD-001](items/STD-001.yaml) | HIGH | `unassigned` | independent | Run bounded standards discussions across ChatGPT, Fable 5, and repository agents before assigning implementation to a release. | Normalize external feedback through assessments; permit a dedicated standards release after owner review. | 2026-07-20 |
| [OBS-001](items/OBS-001.yaml) | MEDIUM | `unassigned` | independent | Design the reusable CrossCutting Observability and attribute/AOP boundary. | Open a separate architecture workflow; it is not a hidden release gate. | 2026-07-18 |

## Resolved

| Item | Priority | Completed In | Published In | Resolution | Workflow | Updated |
| --- | --- | --- | --- | --- | --- | --- |
| [REL-002](items/REL-002.yaml) | HIGH / P0 | `v0.5.0` | — | Git Bash selection, child PATH, byte decoding, and complete failure diagnostics pass local and hosted gates; merged-main pre-tag passed without creating a tag. | [`2026-07-22-v0-5-0-pretag-portability-hotfix`](../workflows/2026-07-22-v0-5-0-pretag-portability-hotfix/workflow.yaml) | 2026-07-22 |
| [REL-001](items/REL-001.yaml) | HIGH | `v0.5.0` | — | Release mechanics are implementation-resolved; V050-010 still owns candidate-level discovery, handoff, and independent release-readiness closure. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-22 |
| [HANDOFF-001](items/HANDOFF-001.yaml) | HIGH | `v0.5.0` | — | The registered receiving checkpoint fails closed across model/runtime/host/session boundaries, preserves native attribution, and passes the repository critical gate. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
| [ENF-001](items/ENF-001.yaml) | HIGH | `v0.5.0` | — | Semantic wrapper enforcement, evidence-bound published-path dispositions, source/downstream routing, and the read-only governance PR workflow are verified locally and on hosted Ubuntu. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
| [LANG-001](items/LANG-001.yaml) | MEDIUM | `v0.5.0` | — | The stale 21-item planning count is reconciled; four active defects are fixed, deterministic language/structure fixtures pass, and both root bilingual pairs pass retained semantic review at `2db0636`. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
| [TOOL-001](items/TOOL-001.yaml) | MEDIUM | `v0.5.0` | — | Retain the literal runner with fail-closed format/set parity; Windows Git Bash and hosted Ubuntu pass the same 23/23 quick gate with no deferred checks, while macOS remains unverified. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
| [VAL-001](items/VAL-001.yaml) | LOW | `v0.5.0` | — | Repository validation is superseded; deterministic offline dependency/version consistency is required and online currency/vulnerability checks remain advisory. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
| [SAG-001](items/SAG-001.yaml) | MEDIUM | `v0.5.0` | — | Dynamic loading remains the default for 17 roles; context-translator alone has exact Codex, Claude, and Copilot adapters with deterministic schema, canonical-link, path, and package validation. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
| [PKG-003](items/PKG-003.yaml) | HIGH | `v0.5.0` | — | Multi-source mechanics are implementation-resolved for exact v0.3.0, v0.4.0, v0.4.1, and v0.4.2 routes; publication and release-gate closure remain separate. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-22 |
| [GOV-001](items/GOV-001.yaml) | MEDIUM | `v0.5.0` | — | Legacy follow-ups are reconciled as satisfied, superseded, intentionally retained, or non-requirement suggestions without rewriting historical artifacts. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
| [CAP-001](items/CAP-001.yaml) | LOW | `v0.5.0` | — | Terminology remains a domain-language document pattern; no repeated action evidence justifies a dedicated skill. | [`2026-07-21-v0-5-0-development`](../workflows/2026-07-21-v0-5-0-development/workflow.yaml) | 2026-07-21 |
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
