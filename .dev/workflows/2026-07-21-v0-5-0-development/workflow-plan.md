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
- `current_phase`: `planning`
- `artifact_root`: `.dev/workflows/2026-07-21-v0-5-0-development`
- `created_at`: `2026-07-21T00:19:22+08:00`
- `updated_at`: `2026-07-21T00:19:22+08:00`
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

## Initial Stage Model

| Stage | Scope | Primary Owner | Status | Checkpoint |
| --- | --- | --- | --- | --- |
| 1 | Inventory, dependency graph, decision freeze, executable task creation | `ai-context-governance` with `dev-workflow` coordination | in progress | bootstrap and inventory commits |
| 2 | Disposition gates and prerequisite governance decisions | owning skill per item | pending | disposition commit |
| 3 | Package migration and runtime adapter contracts | `ai-context-governance` | pending | one commit per validated coherent slice |
| 4 | Enforcement, tooling, handoff, and language parity | `ai-context-governance` / `dev-workflow` | pending | task-level commits |
| 5 | Cold-start release mechanics and integrated candidate validation | `ai-context-governance` | pending | release-readiness commit |
| 6 | Independent assessment and release-candidate closure | `ai-context-auditor` plus main-agent reconciliation | pending | assessment and closure commits |

The dependency and parallelization matrix is intentionally not frozen in this
bootstrap. `V050-001` owns repository-native inventory, sub-agent comparison,
decision recommendations, and creation of the bounded execution tasks.

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

- Last completed action: created the dedicated v0.5.0 branch and bootstrapped
  the master workflow.
- Current task: `V050-001`
- Exact next action: complete the evidence inventory and freeze the dependency,
  decision, task, validation, and checkpoint matrix.
- Validation already completed: predecessor HANDOFF planning passed the Git for
  Windows quick gate at 21/21; this bootstrap still requires its own focused
  artifact validation before commit.
- Git state: branch starts from
  `6813cf257fc3191b210e01dba483b50b184bb675`, including the unpushed roadmap
  and HANDOFF planning ancestry.
- Branch history and checkpoint handoffs: no v0.5.0 checkpoint has been pushed
  or merged.
- Blockers or unresolved decisions: exact multi-source schema, adapter promotion
  set, published-path dispositions, runner design, language remediation batch,
  parity evidence form, release template interface, and final attribution
  evidence union remain subject to `V050-001` evidence and decision freeze.

## Branch Lifecycle

| Segment | Branch | Base | Checkpoint Type | Commit | Remote / Target | Recorded At | Reason | Resume Branch / Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `codex/2026-07-21-v0-5-0-development` | `main@b3eb2af31fbeffe773967ca805fd78600901c03b` plus `6813cf257fc3191b210e01dba483b50b184bb675` | started | `6813cf257fc3191b210e01dba483b50b184bb675` | local | `2026-07-21T00:19:22+08:00` | Continue from the approved HANDOFF planning ancestry without another main merge. | Complete and commit `V050-001`; remain on this branch. |
