# Post-AIC-007 AI Context Health Audit Report

## Template Metadata

- `template_id`: `ai-context-auditor-report`
- `template_version`: `1.0.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-10T18:22:49+08:00`

## Metadata

- `report_id`: `audit-report-2026-07-12-post-aic-007-ai-context-audit`
- `report_type`: `baseline`
- `owner_skill`: `ai-context-auditor`
- `workflow_id`: `2026-07-12-post-aic-007-ai-context-audit`
- `related_plan_id`: `2026-07-12-post-aic-007-ai-context-audit`
- `status`: `final`
- `audit_date`: `2026-07-12`
- `created_at`: `2026-07-12T14:38:13+08:00`
- `updated_at`: `2026-07-12T14:38:13+08:00`
- `template_source`: `.ai/assets/skills/ai-context-auditor/templates/ai-context-audit-report-template.md`
- `template_version`: `1.0.0`
- `repository`: `ai-collaboration-prompts-dotnet-backend`
- `branch`: `codex/2026-07-12-post-aic-007-ai-context-audit`
- `previous_report`: `.dev/workflows/2026-07-10-ai-context-self-audit/reports/03-post-remediation-audit-report.md`

## Executive Summary

- Overall assessment: Tooling integrity, workflow discovery, wrapper inventory, skill routing, and context validation are materially healthier after AIC-007 and CTX-002. All required quick gates execute, shell assets are tracked as `100755`, and the canonical/runtime inventories agree. The repository is not yet healthy because active standards and guides still route historical product topology and source-project defaults as current framework truth, including unsafe production-password guidance. Two schema/process inconsistencies and one local backlog-format typo add maintenance risk.
- Overall score: `7.9/10`.
- Decision: `remediation-recommended`.
- Primary strengths: deterministic fail-closed gates; explicit repository identity; README/INDEX separation; canonical skill ownership; thin runtime wrappers; durable workflow/backlog discovery; coherent GWT/BDDfy contract.
- Primary risks: historical product facts remain active through normative standards and indexed guides; wrapper metadata has an unvalidated nested-key split; transient sub-agent workflow routing is phrased inconsistently.

## Scope

### Included AI Context Surfaces

- Root collaboration and identity entries: `README.md`, `README.en.md`, `agents.md`, `agents.zh-tw.md`, and AI-facing `.github/**`.
- `.ai/**` canonical assets, indexes, manifests, context scripts, and routing documents.
- `.dev/**` governance, standards, guides, requirements, workflow discovery, backlog, and retained workflow evidence.
- `.agents/**` and `.claude/**` runtime skill wrappers.
- Context validator entrypoints, shell manifest, and Git metadata required to verify declared context contracts.

### Default Exclusions

- `src/**`.
- `tests/**`, `test/**`.
- Product implementation trees under `app/**` or `apps/**`.
- Generated and dependency trees.

### Additional Exclusions

- Tool implementation and tool-test source bodies; aggregate gates were executed as existing validation evidence without reviewing their implementation adequacy.
- `bin/**`, `obj/**`, `dist/**`, `build/**`, package/vendor trees, and `.git/**` contents.
- Historical workflow claims were treated as evidence records, not active truth, unless an active locator/index or current document referenced them.

### Code Review Handoff

- Requested: `no`.
- Paths not scanned: all product source/test paths and tool implementation/test bodies listed above.
- Recommended skill: `code-reviewer` only if a separate .NET implementation review is authorized.

## Methodology And Evidence

### Pass A: Independent Baseline

- Evidence used: root identity entries; directory indexes/readmes; canonical skill registry; wrapper indexes; active standards/guides; workflow/backlog discovery; file counts and path relationships.
- Checks performed: repository identity and truth boundary; information architecture; canonical ownership and duplication; instruction clarity; active versus historical labeling; lifecycle discoverability; cognitive load; portability.
- Repository-specific policy was not used as the initial scoring rubric.

### Pass B: Repository-Aware Skill Review

- Policies and skills used: `ai-context-auditor`; `AI-CONTEXT-BOUNDARY`; `AI-CONTEXT-LANGUAGE-POLICY`; ownership registry; workflow artifact/gate and commit policies; runtime wrapper/canonical precedence; README-versus-INDEX contract.
- Checks performed: policy-to-active-content comparison; wrapper/canonical inventory parity; nested metadata comparison; workflow/backlog lifecycle validation; language/structural parity; required/advisory/deferred gate classification; Git executable modes.

### Delegation

- Sub-agents used: three bounded read-only reviewers.
- Assigned surfaces: independent structure/navigation baseline; content/truth/language/governance; runtime wrappers/schemas/scripts/validation.
- Main-agent reconciliation: re-read every HIGH candidate, verified active index/consumer routes, downgraded historical-only evidence, and overturned the requirement-lifecycle candidate after confirming its implementation-outcome banner.

## Repository Context Inventory

| Surface | Files / Size | Audience | Scope | State | Notes |
| --- | ---: | --- | --- | --- | --- |
| Root entries | 3 primary counted entries plus bilingual companions | human / agent | repo identity | active | identity and framework-not-product boundary are clear |
| `.ai/**` | 172 allowlisted files | agent | universal and dotnet-backend reusable context | active | 13 canonical skills, 30 manifests, 6 owned rules |
| `.dev/**` | 440 allowlisted files | human / both | governance, standards, guides, retained records | mixed active/historical | strong indexes; active truth leakage remains in selected standards/guides |
| Runtime wrappers | 31 files across `.agents` and `.claude` | agent/runtime | runtime projections | active | both inventories contain the same 13 skills |
| Workflow discovery | 26 indexed directories | human / agent | lifecycle evidence | active index plus legacy records | 6 post-adoption workflows validate; legacy records are explicitly separated |
| Backlog | 8 machine-readable items | human / agent | durable future work | active | lifecycle validates; README has one extension typo |

## Strengths

1. Repository identity explicitly states that this is a reusable AI collaboration framework rather than a product repository.
2. `.ai` agent assets, `.dev` human/project governance, canonical specs, and runtime wrappers have clear ownership and precedence.
3. README files explain purpose while INDEX files own catalogs, substantially reducing navigation duplication.
4. Workflow locators, full-date IDs, timestamps, branch metadata, backlog handoff, and legacy separation make current lifecycle state discoverable.
5. AIC-007 is resolved: 14 tracked shell assets are `100755`, required runner children are manifest-validated, and the quick gate reports 6/6 required checks executed with no failure.
6. AIC-002 remains resolved: GWT is invariant, BDDfy is the default with explicit opt-out, 3A is not a substitute, and `.feature` support is conditional.
7. Canonical and runtime skill inventories agree at 13 skills, with thin wrappers declaring canonical precedence.
8. Validators provide continuous evidence for indexes, paths, manifests, language ownership, capability routing, workflow artifacts, backlog references, shell classification, and Git modes.

## Findings

| ID | Severity | Finding | Evidence | Impact | Recommendation | Owner / Next Skill |
| --- | --- | --- | --- | --- | --- | --- |
| CTX-H-001 | HIGH | Active normative project-structure guidance presents a fixed historical multi-bounded-context topology as current project truth. | `.dev/standards/project-structure.md` says “This project uses” and prescribes `src`, `tests`, `docker-compose`, `Lab.*`, DomainCore/Presentation topology; its AI responsibility table uses wrong `./ai` and omits `.agents`. `.dev/standards/README.md` calls it the single source of truth; architect `source-map.md` routes shared project boundaries to it. | Architect and implementation agents can impose source-project structure on this framework or a copied target without file-backed adoption. | Reclassify it as a conditional dotnet-backend target template/profile, or rewrite it to separate this framework repository's actual structure from optional target topology; update active consumers. | `ai-context-governance`, with `ddd-ca-hex-architect` only for architecture semantics |
| CTX-H-002 | HIGH | Active indexed guides retain source-project facts and unsafe defaults as current guidance. | `CORS-SETUP.md` says implemented in this project; `PROFILE-BASED-TESTING-GUIDE.md` says this project uses fixed profiles; `VERSION-PLACEHOLDER-GUIDE.md` maps MyScrum names and recommends `root` for test, production, and AI database passwords. These files are listed by active guide indexes/readmes. | Target repos may inherit historical names, frontend/profile assumptions, or insecure credential defaults; current framework identity is contradicted. | Label valid material as parameterized examples, remove source-project names and credential recommendations, require target evidence/project config, and retire guides that cannot be made portable. | `ai-context-governance` |
| CTX-M-001 | MEDIUM | Canonical skill `wrapper_metadata.codex` uses two incompatible keys that the schema/validator does not define or validate. | 10 skill specs use `runtime_wrapper_path`; `ai-context-auditor`, `ai-context-governance`, and `repo-structure-sync` use `wrapper_path`. `CANONICAL-SCHEMA.MD` and the skill template do not define the nested contract; validation still passes. | A future exporter or wrapper consumer can silently miss three or ten skills depending on the assumed key. | Select one canonical key, document it in schema/template, migrate all 13 manifests, and validate target/key/path shape. | `ai-context-governance` |
| CTX-M-002 | MEDIUM | Active sub-agent artifact routing omits the transient read-only exception defined by workflow policy. | `WORKFLOW-GATE-POLICY.md` allows conversation-only multi-pass/sub-agent analysis in direct mode; `.ai/SUB-AGENT-SYSTEM.MD` says use durable workflow artifacts whenever work crosses skills, stages, or sub-agents. | Agents following the shorter router can create unauthorized or unnecessary workflow artifacts for transient analysis. | Qualify artifact routing by persistence/mutation and link the transient exception directly. | `ai-context-governance` |
| CTX-L-001 | LOW | Backlog ownership documentation names the wrong item extension. | `.dev/backlog/README.MD` says `items/<item-id>.md`, then correctly requires machine-readable YAML; all items and validation use `.yaml`. | A future agent may create a wrong-format item that fails discovery/validation. | Change the ownership example to `items/<item-id>.yaml`. | `ai-context-governance` |

## Baseline And Skill Comparison

### Confirmed

- Pass A and Pass B both confirm the two historical-truth findings and wrapper metadata drift.
- Repository-aware boundary rules increase CTX-H-001 and CTX-H-002 confidence because the affected files are active, indexed, and consumed by agent routing rather than archived examples.
- AIC-007 and CTX-002 are confirmed resolved by current machine evidence.

### Added By Repository-Aware Review

- CTX-M-002 becomes actionable because the repository has an explicit persistence/mutation decision boundary that `.ai/SUB-AGENT-SYSTEM.MD` fails to project.
- CTX-L-001 is a direct contradiction with the repository's machine-readable backlog contract.

### Downgraded Or Deferred

- The 9 coding-standards warnings remain maintenance signals: eight missing back references and one possible duplication. They do not overturn a required child check or any prior finding.
- Hosted Linux execution and manifest-driven runner simplification remain `TOOL-001`, not a new audit defect; Windows Git Bash plus synthetic tests currently provide the validated baseline.
- Wrapper semantic equivalence and bilingual semantic parity are residual human-review limitations, not defects claimed by current structural validators.
- Historical workflow volume is a discoverability cost already tracked by `GOV-001`; the active index correctly labels legacy/no-locator records.
- Shell shebang inconsistency is portability hygiene and may be considered inside `TOOL-001`; no observed gate failure supports a stronger finding.

### Overturned

- The candidate that implemented requirements still look unresolved was overturned. `SKILL-IMPLEMENTER-NAMING-REQUIREMENTS.MD` and `DOMAIN-UBIQUITOUS-LANGUAGE-REQUIREMENTS.MD` contain prominent implementation outcomes and explain that future-tense text is preserved decision history.
- The prior AIC-003 onboarding fixes remain valid for their exact files. CTX-H-001 and CTX-H-002 show that the earlier report's broader “no stale active truth” conclusion was incomplete, not that the repaired onboarding files regressed.
- The `.codex/config.toml` approval-policy candidate was not promoted because its runtime semantics and repository applicability were not established within this audit's verified context contract.

## Validation

| Check | Result | Evidence / Notes |
| --- | --- | --- |
| Git state | PASS | Audit branch was clean after bootstrap commit before report-only edits. |
| Registry and wrapper parity | PASS WITH SCHEMA GAP | 13 canonical skills and both 13-skill runtime inventories agree; CTX-M-001 concerns unvalidated nested metadata keys. |
| Path and reference checks | PASS | `validate-ai-context.py` reports 8 active indexes and valid canonical/consumer paths; CTX-H findings concern truth, not missing paths. |
| Schema / structured file parse | PASS WITH GAP | 30 canonical manifests parse; wrapper metadata nested contract is not defined or checked. |
| Workflow / backlog | PASS | 6 post-adoption workflows, 26 indexed directories, and 8 backlog items validate. |
| Shell assets | PASS | 14 retained/tracked assets, 0 retirement candidates, all Git index modes `100755`; Bash syntax passes. |
| Repository context quick gate | PASS WITH SIGNALS | 6 required checks selected/executed/passed; 47/47 analyzer and 2/2 configuration tests pass; dependency/version validation remains explicitly deferred; coding standards emits 9 maintenance warnings. |
| Active generated-script references | PASS | No active contract expects `.ai/scripts/generated/`; remaining mentions are historical/remediation evidence. |
| Diff whitespace check | PASS | No whitespace errors; Windows line-ending conversion notices are nonblocking. |

### Skipped Validation

- Product source and test implementation were not read, reviewed, or scored.
- Tool implementation and tool-test source bodies were not inspected; existing aggregate tests were executed only as gate evidence.
- Product build quality, security, performance, test adequacy, and architecture compliance were not assessed.
- Real full mode was not used because an advisory helper can inspect product tests; critical/quick and synthetic AIC-007 evidence cover context gate semantics.
- Hosted Linux was not executed; this remains explicitly tracked by `TOOL-001`.
- Semantic equivalence of bilingual documents and runtime-wrapper prose was not inferred from structural parity.
- No internet research was required.

## Recommended Action Order

1. Use `ai-context-governance` to triage CTX-H-001 and CTX-H-002 into a bounded historical-product-truth remediation workflow.
2. In the same governance planning pass, decide whether CTX-M-001 and CTX-M-002 fit the same workflow or should be separate low-radius tasks.
3. Fix CTX-L-001 opportunistically within the governance batch, not as a separate workflow.
4. Request an independent post-remediation audit before changing the overall decision to `healthy` or `healthy-with-followups`.
5. Keep `TOOL-001`, `LANG-001`, `GOV-001`, `CAP-001`, and `VAL-001` prioritized independently; none blocks this report's completion.

## Deferred Items

- Product-code review: outside AI-context scope; route to `code-reviewer` only on explicit request.
- Hosted Linux and manifest-driven runner design: `TOOL-001`.
- Translation inventory and semantic parity strategy: `LANG-001`.
- Legacy workflow reconciliation: `GOV-001`.
- Terminology capability decision: `CAP-001`.
- Repository and dependency/version validation reassessment: `VAL-001`.

## Appendix

### Commands Run

```text
rg --files -uu <allowlisted roots> with explicit product/generated/dependency exclusions
python .ai/scripts/validate-ai-context.py
python .ai/scripts/validate-workflow-artifacts.py
python .ai/scripts/validate-shell-assets.py
C:\Program Files\Git\bin\bash.exe ./.ai/scripts/check-all.sh --quick
git ls-files -s .ai/scripts/*.sh
git ls-files --eol .ai/scripts/*.sh
bash -n .ai/scripts/*.sh
rg -n -uu <targeted active truth, routing, wrapper metadata, and reference patterns>
git diff --check
```

### Notes

- One delegated attempt referenced a nonexistent `validate-sub-agent-assets.py`; this was a command-discovery mistake, not a failed repository gate. The repository exposes three active `validate-*.py` context validators, all of which passed.
- The quick gate executed analyzer/configuration tests but this audit did not inspect their source or claim product implementation coverage.

## Lifecycle Handoff

- Baseline report path: `.dev/workflows/2026-07-12-post-aic-007-ai-context-audit/reports/01-audit-report.md`
- Remediation owner: `ai-context-governance`
- Remediation report path: future governance-owned workflow artifact
- Post-remediation report path: future auditor-owned verification requested by governance
- Remediation intentionally not performed by this skill: `yes`
