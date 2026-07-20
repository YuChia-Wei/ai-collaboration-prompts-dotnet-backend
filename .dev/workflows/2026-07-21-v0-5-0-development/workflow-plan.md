# v0.5.0 Development Workflow

## Template Metadata

- `template_id`: `ai-context-governance-maintenance-workflow-plan`
- `template_version`: `1.2.0`
- `created_at`: `2026-07-10T18:22:49+08:00`
- `updated_at`: `2026-07-13T23:11:56+08:00`

## Workflow Metadata

- `workflow_id`: `2026-07-21-v0-5-0-development`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-21-v0-5-0-development`
- `base_branch`: `main`
- `branch_segment`: `1`
- `status`: `active`
- `current_phase`: `implementation`
- `artifact_root`: `.dev/workflows/2026-07-21-v0-5-0-development`
- `created_at`: `2026-07-21T00:19:22+08:00`
- `updated_at`: `2026-07-21T02:10:06+08:00`
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
| `PKG-003` | Introduce migration schema 2.0 with exact multi-source selection; retain schema 1.0 read compatibility and the v0.0.1-to-v0.3.0 provenance route. | `V050-003` |
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
| 4 | Enforcement, tooling, handoff, and language parity | `ai-context-governance` / `dev-workflow` | in progress | task-level commits |
| 5 | Cold-start release mechanics and integrated candidate validation | `ai-context-governance` | pending | release-readiness commit |
| 6 | Independent assessment and release-candidate closure | `ai-context-auditor` plus main-agent reconciliation | pending | assessment and closure commits |

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

- Last completed action: completed `V050-005` at `83a0c1c`; Windows Git Bash
  and hosted Ubuntu run `29770661564` pass 28/28, dedicated governance run
  `29770662383` passes, and the package-candidate failure is confined to the
  intentionally absent REL-001 v0.5.0 release record.
- Current task: `V050-008`
- Exact next action: define the generic receiving-checkpoint schema,
  executable validation-evidence shape, and REL phase-check interface; keep
  unavailable provider fixtures explicitly blocked and avoid provider-specific
  identity rules without captured evidence.
- Validation already completed: ENF-001 focused suites, affected package
  upgrade cases 16 and 17, Windows Git Bash 28/28, hosted Ubuntu 28/28, and
  the separate read-only governance workflow all pass at `83a0c1c`.
- Git state: `83a0c1c` is committed and pushed; ENF completion evidence and
  V050-008 activation are pending this closeout checkpoint commit.
- Branch history and checkpoint handoffs: the branch is pushed through
  `d5d74ea`; draft PR `#1` is the hosted evidence and continuing CI surface.
- Blockers or unresolved decisions: package-candidate run `29770662983`
  correctly fails closed until `V050-009` creates a governed v0.5.0 release
  record. Real Copilot CLI/cloud-agent and Claude attribution fixtures are not
  present; V050-008 must retain that absence explicitly rather than inventing
  identities. Public terminal-state API evidence belongs to V050-009; macOS
  remains unverified.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-21-v0-5-0-development` | `main@b3eb2af31fbeffe773967ca805fd78600901c03b` plus `6813cf257fc3191b210e01dba483b50b184bb675` | started | `6813cf257fc3191b210e01dba483b50b184bb675` | local | `2026-07-21T00:19:22+08:00` | Continue from the approved HANDOFF planning ancestry without another main merge. | Complete and commit `V050-001`; remain on this branch. |
