# v0.5.0 Development Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-21T03:32:43+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-21-v0-5-0-development`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-21-v0-5-0-development`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `active`
- `current_phase`: `verification`
- `artifact_root`: `.dev/workflows/2026-07-21-v0-5-0-development`
- `created_at`: `2026-07-21T00:19:22+08:00`
- `updated_at`: `2026-07-22T08:26:17+08:00`
- `template_source`: `.ai/assets/skills/ai-context-governance/templates/ai-context-maintenance-workflow-plan-template.md`
- `template_version`: `1.2.0`

## Objective And Scope

- Problem statement: v0.5.0 has seven release blockers and three disposition
  gates spanning package migration, runtime adapters, governance enforcement,
  portable tooling, language parity, release publication, and cross-session
  handoff. The work must remain resumable under limited AI quota and cannot
  depend on hidden session state.
- Authorized remediation scope: inventory, decide, implement, validate, and
  checkpoint all work assigned to v0.5.0 until the repository has a
  release-ready candidate with independent verification and exact publication
  preconditions.
- Execution posture: continue from the current branch ancestry without merging
  every item to `main`; create coherent validated commits at task or stage
  boundaries; use sub-agents only for bounded work while the main agent owns
  integration and review.
- Exclusions: do not publish or create the immutable `v0.5.0` tag without a
  separate publication authorization; do not pull `STD-001`, `OBS-001`,
  `SIMPL-001`, `EVAL-001`, or `SKILL-001` into v0.5.0; do not imply unexecuted
  macOS evidence.
- Completion criteria: every v0.5.0 release blocker is resolved with executable
  evidence; every disposition gate has an explicit retained decision; all
  required local and hosted gates pass; an independent assessment confirms
  release readiness; release artifacts can be built deterministically from an
  immutable candidate commit.

## Artifact Contract

- Baseline assessments: `.dev/assessments/ASM-20260717-004/assessment.yaml`,
  `.dev/assessments/ASM-20260720-001/assessment.yaml`
- Backlog and roadmap: `.dev/backlog/ROADMAP.md`,
  `.dev/backlog/items/{PKG-003,SAG-001,ENF-001,TOOL-001,LANG-001,REL-001,HANDOFF-001,GOV-001,CAP-001,VAL-001}.yaml`
- Remediation report: `.dev/workflows/2026-07-21-v0-5-0-development/reports/remediation-report.md`
- Tasks: `.dev/workflows/2026-07-21-v0-5-0-development/tasks/`
- Verification assessment: pending stable assessment ID after implementation
  freezes a subject revision

## Frozen Decision Matrix

The repository owner's directive to execute all v0.5.0 work authorizes the
smallest evidence-backed contract within the existing roadmap scope. It does
not authorize later-horizon work or publication. The detailed evidence and
decision rationale are retained in
[`evidence/v050-decision-matrix.md`](evidence/v050-decision-matrix.md).

| Item | Frozen v0.5.0 direction | Execution task |
| --- | --- | --- |
| `GOV-001` | Reconcile only; mark satisfied or superseded markers without retrofitting legacy locators. | `V050-002` |
| `CAP-001` | Do not create a terminology skill; retain the domain-language document pattern until repeatable action evidence exists. | `V050-002` |
| `VAL-001` | Treat repository validation as superseded by later analyzers; implement deterministic dependency/version consistency and retire the permanent deferred placeholder. | `V050-006` |
| `PKG-003` | Introduce migration schema 2.0 with exact multi-source selection; retain schema 1.0 read compatibility and the v0.0.1-to-v0.3.0 provenance route. The owner's 2026-07-22 amendment adds v0.4.2 as a required fourth exact automatic source. | `V050-003` core plus `V050-009` expansion |
| `SAG-001` | Keep dynamic loading as default; retain only `context-translator` as native for Codex, Claude, and Copilot unless live runtime evidence requires another adapter. | `V050-004` |
| `ENF-001` | Add a separate governance PR workflow and deterministic semantic/path-disposition enforcement; do not merge general governance ownership into package candidate CI. | `V050-005` |
| `TOOL-001` | Retain the current runner for v0.5.0, strengthen manifest/format tests and execute the same declared gate set on Windows Git Bash and hosted Ubuntu; macOS remains unverified. | `V050-006` |
| `LANG-001` | Refresh the historical inventory to current truth, remediate the bounded active-language defect set, and use a hybrid deterministic plus retained semantic-review gate. | `V050-007` |
| `HANDOFF-001` | Add a machine-readable receiving checkpoint and compatible attribution evidence union; never rewrite provider-native metadata and do not encode a provider without a real fixture. | `V050-008` |
| `REL-001` | Add canonical placeholder templates, runbook, pre-tag validation, and local plus hosted terminal-state checks while keeping tag creation user-owned. | `V050-009` |

## Execution Stage Model

| Stage | Scope | Primary Owner | Status | Checkpoint |
| --- | --- | --- | --- | --- |
| 1 | Inventory, dependency graph, decision freeze, executable task creation | `ai-context-governance` with `dev-workflow` coordination | completed | `62e721e` bootstrap plus `95df89d` inventory commit |
| 2 | Disposition gates and prerequisite governance decisions | owning skill per item | completed | disposition commit |
| 3 | Package migration and runtime adapter contracts | `ai-context-governance` | completed | `49a2086`, `a87bddf`, and `6aed578` |
| 4 | Enforcement, tooling, handoff, and language parity | `ai-context-governance` / `dev-workflow` | completed | task-level commits through the V050-008 checkpoint |
| 5 | Cold-start release mechanics and integrated candidate validation | `ai-context-governance` | completed | `2ecf832` mechanics plus validated-candidate state commit |
| 6 | Independent assessment and release-candidate closure | `ai-context-auditor` plus main-agent reconciliation | in progress | assessment and closure commits |

Execution order is `V050-002`, then the independent foundation lanes
`V050-003`, `V050-004`, `V050-006`, and `V050-007`. `V050-005` consumes their
declared validators and CI commands. `V050-008` and `V050-009` integrate against
the enforcement route. `V050-010` freezes and independently verifies the
candidate. Tasks may be reordered only when their recorded dependencies and
acceptance evidence remain satisfied.

## Validation Strategy

- Run focused GWT or schema tests with every implementation slice.
- Run workflow, backlog, AI-context, version, and structured-data validation
  before every governance checkpoint.
- Run `check-all.sh --critical` at receiving-agent checkpoints and
  `check-all.sh --quick` at coherent implementation checkpoints.
- Exercise package upgrades from real immutable source packages and preserve
  target-owned truth.
- Retain Windows Git Bash and hosted Ubuntu evidence for the same declared gate
  set; macOS remains explicitly unverified unless an environment becomes
  available.
- Run commit-range validation before push, merge, or release-candidate closure.
- Freeze a subject commit and obtain a separate read-only verification
  assessment before claiming release readiness.

## Resume Checkpoint

- Last completed action: committed and repository-verified the V050-010 release
  checkpoint at `de7805b`. A read-only successor preflight confirmed AIC-001
  and AIC-003 resolved and found only that this plan/task still named the
  already completed checkpoint commit; this containing refresh removes that
  final AIC-002 resume lag.
- Current task: `V050-010`
- Exact next action: run and persist the independent successor assessment
  against this refreshed checkpoint commit, then perform final workflow and
  release-readiness reconciliation without tagging or publishing.
- Validation already completed: four real extracted upgrades, exact candidate
  state, two deterministic package builds, Windows critical 33/33, and all
  three same-revision hosted PR gates pass at `ef14847`.
- Git state: `de7805b` is clean, pushed, and passes exact candidate, repository
  handoff, registry, lifecycle, and all three hosted PR gates. This checkpoint
  refresh is pending its containing commit.
- Branch history and checkpoint handoffs: draft PR `#1` remains the hosted
  evidence surface. V050-008 is retained as historical HANDOFF implementation
  evidence and must be superseded by a current V050-010 release checkpoint.
- Blockers or unresolved decisions: persisted successor verification and final
  workflow reconciliation still block release-readiness. macOS and real
  Copilot CLI/cloud-agent and Claude attribution fixtures remain explicitly
  unverified; no identity or platform result may be invented.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-21-v0-5-0-development` | `main@b3eb2af31fbeffe773967ca805fd78600901c03b` plus `6813cf257fc3191b210e01dba483b50b184bb675` | started | `6813cf257fc3191b210e01dba483b50b184bb675` | local | `2026-07-21T00:19:22+08:00` | Continue from the approved HANDOFF planning ancestry without another main merge. | Complete and commit `V050-001`; remain on this branch. |
