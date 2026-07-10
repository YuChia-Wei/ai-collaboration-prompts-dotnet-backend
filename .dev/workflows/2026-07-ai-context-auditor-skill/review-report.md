# AI Context Audit Report

## Metadata

- `report_id`: `review-report-2026-07-10-ai-context-self-audit`
- `owner_skill`: `ai-context-auditor`
- `related_plan_id`: `workflow-plan-2026-07-ai-context-auditor-skill`
- `status`: `final`
- `audit_date`: `2026-07-10`
- `repository`: `ai-collaboration-prompts-dotnet-backend`
- `branch`: `main`
- `previous_report`: `none`

This report captures the repository state assessed before `ai-context-auditor` was added. The skill-creation changes in the related workflow are not treated as evidence that the original findings were already remediated.

## Executive Summary

- Overall assessment: The repository has mature AI context governance concepts, but active rules, canonical ownership, schemas, runtime declarations, and validation gates do not yet form a reliable machine-verifiable closed loop.
- Overall score: `6.5/10`
- Decision: `remediation-recommended`
- Primary strengths: clear repository identity, intentional context layering, evidence-first truth handling, bounded delegation, thin runtime wrappers, and explicit validation migration direction.
- Primary risks: dual normative surfaces, stale active onboarding truth, incompatible testing rules, canonical schema drift, workflow authorization gaps, and fail-open script behavior.

### Score Breakdown

| Dimension | Score |
| --- | ---: |
| Context architecture and governance design | 8.0/10 |
| Navigation and discoverability | 7.0/10 |
| Rule consistency | 5.0/10 |
| Runtime and machine-validation closure | 5.5/10 |
| Portability and target-repository safety | 6.0/10 |

## Scope

### Included AI Context Surfaces

- Root README and agent instruction files.
- `.ai/**` canonical assets, skill registries, sub-agent prompts, references, templates, and context scripts.
- `.dev/**` governance, standards, guides, requirements, specs, operations, and workflow records.
- `.agents/**` and `.claude/**` runtime wrappers.
- AI-assistant declarations under `.github/**`.
- Git metadata and context-validation commands needed to verify the findings.

### Default Exclusions

- `src/**` implementation content.
- `tests/**` and `test/**` implementation content.
- Product feature, domain, application, infrastructure, API, and test code.
- Generated output and dependency trees.

The repository inventory exposed product and tooling paths, but their implementation content was not reviewed. No conclusion in this report is a product-code finding.

### Additional Exclusions

- Remediation of findings.
- Production architecture redesign.
- BDD scenario design.
- Broad documentation translation.
- Gemini or Copilot wrapper implementation.

### Code Review Handoff

- Requested: `no`
- Paths not scanned: `src/**`, `tests/**`, product implementation and test code.
- Recommended skill if later requested: `code-reviewer`.

## Methodology And Evidence

### Pass A: Independent Baseline

- Used general AI context engineering, knowledge-base, documentation architecture, runtime adapter, validation-integrity, and portability principles.
- Did not read or apply repository skill specifications during this pass.
- Parallel read-only audits covered structure/navigation, content/truth quality, and runtime/schema/script relationships.
- Verified high-severity evidence from root entries, indexes, active standards, onboarding guides, context rules, wrapper inventories, and scripts.

### Pass B: Repository-Aware Skill Review

- Applied `dev-workflow` for workflow, artifact, routing, and validation boundaries.
- Applied `ai-context-governance` for audience, scope, language, placement, canonical ownership, and wrapper sync.
- Compared findings against `AI-CONTEXT-BOUNDARY.md`, `AI-CONTEXT-LANGUAGE-POLICY.md`, the canonical skill registry, wrapper indexes, workflow gate, and commit policy.
- Reclassified broad or historical concerns when the skill boundary required deferral.

### Delegation

- Sub-agents used: `yes`, three bounded audit surfaces.
- Assigned surfaces: structure/navigation; content/truth/language; runtime/wrappers/schema/scripts.
- Main-agent responsibilities: scope enforcement, evidence verification, duplicate resolution, severity ranking, skill comparison, and final synthesis.

## Repository Context Inventory

| Surface | Files / Size At Audit Time | Audience | Scope | State | Notes |
| --- | ---: | --- | --- | --- | --- |
| Repository total | 612 files | mixed | framework repo | active | 347 Markdown, 43 YAML, 94 JSON |
| `.ai/**` | 155 files, about 59K tokens | agent | universal and dotnet-backend | active/transitional | Strong structure; language, schema, and script drift remain |
| `.dev/**` | 390 files, about 242K tokens | both | governance, reusable standards, project/workflow truth | active/historical | Largest cognitive-load and ownership hotspot |
| Canonical skills | 12 | agent | canonical skills | active | Matched both runtime wrapper sets at audit time |
| Codex wrappers | 12 | agent | runtime wrapper | active | Thin and synchronized at audit time |
| Claude wrappers | 12 | agent | runtime wrapper | active | Thin and synchronized at audit time |
| Workflow records | 18 non-template directories | both | workflow and historical state | mixed lifecycle | Missing active/completed/superseded/archive registry |

## Strengths

1. Repository identity explicitly states that this is a portable AI collaboration framework rather than a product repository.
2. `.ai`, `.dev`, canonical skills, sub-agent prompts, and runtime wrappers have intentional conceptual boundaries.
3. README and INDEX responsibilities are separated into purpose/boundary versus catalog/navigation.
4. Root agent rules emphasize file-backed truth, smallest coherent change, and verifiable completion.
5. Sub-agent delegation is bounded and keeps synthesis and validation with the main agent.
6. Canonical, Codex, and Claude skill sets were `12 / 12 / 12`, and sampled wrappers were thin.
7. The repository explicitly recognizes that grep-based C# validation should migrate to Roslyn, tests, or other .NET-native mechanisms.
8. Git hygiene was clean at audit time, with no tracked `bin/` or `obj/` output.

## Findings

| ID | Severity | Finding | Evidence | Impact | Recommendation | Owner / Next Skill |
| --- | --- | --- | --- | --- | --- | --- |
| AIC-001 | HIGH | Reusable .NET agent rules have two normative surfaces: `.ai/assets/tech-stacks/dotnet-backend/**` and `.dev/standards/**`. | `.dev/standards/README.md` calls its content reusable standards while `.ai` files declare mandatory agent rules. | Agents can receive conflicting active truth without a defined precedence. | Create a per-rule ownership matrix and keep one normative owner. | `ai-context-governance`, then architecture/testing owner for domain decisions |
| AIC-002 | HIGH | Testing rules are mutually incompatible. | `common-rules.md` and `testing-strategy.md` require BDDfy only and prohibit `.feature`; `GHERKIN-FEATURE-STORAGE-GUIDE.MD` requires formal `.feature` assets under `tests/Features/`. | A compliant agent cannot satisfy both active contracts. | Decide whether feature files are forbidden, optional by profile, or formally supported, then synchronize every consumer. | Testing decision owner, coordinated by `dev-workflow` |
| AIC-003 | HIGH | Active onboarding contains stale product truth and retired topology. | `coding-guide.md` describes a Todo List application and fixed Wolverine/EF/Event Sourcing choices; `NEW-PROJECT-GUIDE.md` creates old `.ai` and `.dev` roots and installs fixed packages; learning docs reference missing `CLAUDE.md`. | Target repositories can inherit unsupported technology and directory decisions. | Retire or rewrite the active onboarding entries before they are reused. | `ai-context-governance` with `ddd-ca-hex-architect` for technical choices |
| AIC-004 | HIGH | The canonical asset schema is not followed by canonical assets. | All 12 skill specs used `asset_id` rather than required `id`; 8 lacked part of the declared mandatory metadata; 17 sub-agent manifests had the same identifier mismatch; duplicate template families used incompatible formats. | Machine validation or export cannot rely on the declared schema. | Version the schema, choose `id` or `asset_id`, define stable types/enums, migrate assets, and add a validator. | `ai-context-governance` |
| AIC-005 | HIGH | `dev-workflow` discovery and profile contracts are incomplete. | Discovery prefers `capability_slots`, but no audited skill declared them; capability profile mapped `local-change-implementer` under `implementation` and lacked a `local-change` row. | Portable discovery degrades to name inference, and local routing can select an ambiguous implementer. | Add capability metadata and validate profile-to-skill consistency. | `dev-workflow` / `ai-context-governance` |
| AIC-006 | HIGH | Workflow policy lacks a read-only audit/report-only exception. | Two stages, sub-agent use, or review requires workflow artifacts, while commit policy requires commits at workflow and inventory boundaries. | A read-only analysis can be forced to modify and commit repository state without explicit remediation intent. | Add audit-only mode that preserves routing and reporting but allows explicitly skipped mutation artifacts. | `dev-workflow` governance |
| AIC-007 | HIGH | Context script gates can pass when important checks are skipped. | Tracked shell files were mode `100644`; `check-all.sh` converts non-executable scripts to warnings and exits `0` with warnings; Windows Git Bash masked the mode issue. | CI or users can receive false confidence from a successful exit code. | Make required checks fail closed, validate Git executable mode, and distinguish warning-only preflight from a gate. | Tooling workflow; not a context-audit remediation |
| AIC-008 | MEDIUM | Gemini and Copilot support is documented as current although the entry roots do not exist. | Root entries and runtime guide reference `.gemini/`, `.github/prompts/`, and `.github/copilot-instructions.md`; all were absent. | Users and agents overestimate the supported runtime matrix. | Label support as planned or create and validate the promised entries. | `ai-context-governance` |
| AIC-009 | MEDIUM | Navigation, language, audience, and lifecycle policies are not continuously validated. | `.dev/INDEX.md` contained three literal ``|`n|`` corruptions; active indexes were incomplete; agent-facing Chinese tutorial content remained in `.ai`; workflows lacked lifecycle navigation. | Drift accumulates despite well-written governance policies. | Add context lint for paths, tables, language exceptions, bilingual parity, wrapper parity, and workflow lifecycle. | `ai-context-governance` |

## Baseline And Skill Comparison

### Confirmed

- Conditional versus mandatory rule conflicts.
- Stale onboarding and missing paths.
- Language-policy drift and incomplete index relationships.
- Workflow cognitive load and missing lifecycle.
- Script and schema/template migration debt.

### Added By Repository-Aware Review

- The rule conflicts originate in dual canonical ownership between `.ai` and `.dev/standards`.
- Active `coding-guide.md` is product-truth leakage, not merely an old example.
- Schema drift covers all top-level skills and all sub-agent manifests.
- `dev-workflow` has capability-profile and audit-only authorization gaps.
- `.dev/specs/tests` has both placement and language ambiguity.

### Downgraded Or Deferred

- Stable bilingual root entries are allowed; they need ownership/parity checks rather than removal.
- Runtime wrapper duplication is expected and was healthy at audit time; the residual problem is the lack of an automated drift gate.
- Historical workflow records are correctly placed; the problem is lifecycle navigation, not their mere existence.
- Broad translation, script retirement, and product architecture decisions require separate workflows.

### Overturned

- No evidence showed that the audited Codex and Claude wrappers had already drifted from each other in skill inventory or canonical references.
- README casing and empty placeholder directories were not retained as primary governance findings.

## Validation

| Check | Result | Evidence / Notes |
| --- | --- | --- |
| Git state at audit completion | PASS | Worktree was clean before the skill-creation workflow began |
| Registry and wrapper parity | PASS | Canonical / Codex / Claude skill sets were `12 / 12 / 12` |
| Path and reference checks | FINDINGS | Gemini and Copilot entries absent; `.dev/INDEX.md` table corruption confirmed |
| Schema / structured-file audit | FAIL | Canonical schema and asset fields were inconsistent |
| Prompt portability check | PASS | `.ai/scripts/check-prompt-portability.sh` passed under Git Bash |
| Coding standards integrity check | PASS WITH WARNINGS | Completed with 14 warnings, including missing back-references and possible duplication |
| Script gate semantics | FAIL | Required-script skip behavior and warning-only exit `0` confirmed |

### Skipped Validation

- Product build and tests were not run because product source and test code were outside the audit scope.
- No `code-reviewer` workflow was run.
- No remediation validation was run because the audit was read-only.
- No internet research was needed.

## Recommended Action Order

1. Stop active wrong guidance: resolve the `.feature` decision, retire or rewrite stale onboarding, repair index corruption, correct runtime support declarations, and add an audit-only workflow exception.
2. Establish canonical ownership and a shared rule-strength vocabulary: `invariant`, `profile-default`, `conditional-if-selected`, `example`, and `historical`.
3. Repair machine governance: version the asset schema, align templates, add capability metadata, validate routing profiles, and add wrapper/path drift checks.
4. Make context/tooling validation fail closed where it is presented as a gate.
5. Add workflow lifecycle and targeted language/audience cleanup without starting a broad translation migration.

## Deferred Items

- Selecting the final BDD/test artifact strategy.
- Selecting mandatory versus conditional .NET packages and architecture conventions.
- Implementing or retiring Roslyn, shell, and generated validators.
- Product source and test code review.
- Broad translation and historical workflow archival.
- Remediation of all findings in this report.

## Appendix

### Representative Commands Run

```text
rg --files --hidden -g '!**/.git/**' ...
rg -n --hidden ...
git status --short
git ls-files -s .ai/scripts/*.sh
Git Bash ./.ai/scripts/check-prompt-portability.sh
Git Bash ./.ai/scripts/check-coding-standards.sh
path-existence and canonical/wrapper set comparisons with PowerShell
```

### Notes

- The report intentionally distinguishes audit truth from the subsequent creation of `ai-context-auditor`.
- Future audits should compare against this report and record resolved, recurring, and newly introduced findings.

