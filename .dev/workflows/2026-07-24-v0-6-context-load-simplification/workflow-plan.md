# v0.6.0 Active Context Measurement And Simplification

## Workflow Metadata

- `workflow_id`: `2026-07-24-v0-6-context-load-simplification`
- `workflow_kind`: `ai-context-maintenance`
- `owner_skill`: `ai-context-governance`
- `branch`: `codex/2026-07-24-v0-6-context-load-simplification`
- `base_branch`: `codex/2026-07-24-v0-6-ci-lifecycle`
- `status`: `completed`
- `current_phase`: `completed`
- `artifact_root`: `.dev/workflows/2026-07-24-v0-6-context-load-simplification`
- `created_at`: `2026-07-24T10:20:00+08:00`
- `updated_at`: `2026-07-24T10:50:34+08:00`

## Objective And Scope

- Measure repository context actually loaded by controlled runtime,
  skill-routing, release, handoff, and development sessions.
- Keep repository corpus, repository-loaded bytes/words, and provider-reported
  total prompt tokens as three separate measurements.
- Disposition all seven Fable 5 simplification candidates.
- Implement only a mechanically safe reduction whose retained routing and
  validation remain explicit.
- Do not move or delete workflow, assessment, standards, skill, or bilingual
  evidence merely because the repository corpus is large.

## Completion Criteria

- A clean full commit pins every trace and every loaded file digest.
- Five required session families report exact repository load events.
- The measurement gate fails closed on dirty/unpinned subjects, unsafe paths,
  missing families, digest drift, duplicates, and corpus-as-prompt claims.
- Every Fable candidate has one explicit disposition and owning horizon.
- English and Traditional Chinese root entries retain structural and semantic
  parity after the bounded directory-table trim.
- `SIMPL-001` closes without authorizing a historical archive migration.

## Closure Checkpoint

- Current task: none; `SIMPL-001` is complete.
- Last completed action: independently verified the exact corpus, 38 load
  events, five families, seven dispositions, root-entry trim, bilingual
  structure, and absence of historical evidence deletion.
- Validation: 10 measurement fail-closed tests, 10 language/structure tests,
  AI-context, workflow, shell-asset, and diff checks passed.
- Residual boundary: provider total prompt tokens were unavailable and remain
  `null`; historical archive migration still requires a separately approved
  v0.7.0 successor.
- Git state: completed local stacked branch; no push or merge requested.
