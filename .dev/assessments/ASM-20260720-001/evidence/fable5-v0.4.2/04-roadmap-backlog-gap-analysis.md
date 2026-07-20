# 04 — Roadmap / Backlog Gap Analysis + Proposed Items

## Coverage matrix

| Finding / risk | Existing coverage | Gap? |
| --- | --- | --- |
| F1 critical gate red on main | none | YES — no item owns fixing current broken state |
| F2 release.yaml stuck `validated` (blocks v0.5.0) | none | YES |
| F3/F4 notes polluted, migration guide empty | none | YES |
| F5 fabricated evidence | none | YES |
| F6 roadmap/backlog not reconciled | none | YES |
| Gate exists but not enforced in CI | `ENF-001` (v0.5.0) partial | Partial — helps future, not now |
| Tag-timing / pre-tag precondition gate | none | YES |
| Render output pollution prevention | none | YES |
| Evidence authenticity (run IDs, hashes) | none | YES |
| Model-handoff state-alignment gate | none | YES |
| Portability, wrapper semantics, translation debt | `TOOL-001`, `ENF-001`, `LANG-001` | Covered |
| v0.5.0 activation "v0.4.2 evidence reconciled" precondition | ROADMAP states it | Blocked by F2/F6, and roadmap does not know why |

Conclusion: the entire class of "release publication finalization + release
automation hardening + model-handoff safety" is uncovered. Three new items
proposed below.

## Proposed item 1 — R042-005 (immediate hotfix, target v0.4.2)

Draft (reconcile against repo backlog schema before committing):
```yaml
schema_version: "1.0"
backlog_id: "R042-005"
title: "v0.4.2 Publication Finalization Hotfix"
category: "release-finalization"
status: "planned"
priority: "HIGH"
summary: "Repair the broken v0.4.2 publication finalization: fix the workflow locator, flip release.yaml to published, rewrite polluted release notes and empty migration guide, correct fabricated evidence, and reconcile roadmap/backlog."
release:
  target: "v0.4.2"
  completed_in: null
  published_in: null
  target_scope: "publication-finalization-only"
  gate: "release-blocker"
origin_refs:
  - "external: ai-context-review-report-by-fable5-v0.4.2/03-current-state-findings.md"
recommended_owner_skill: "ai-context-governance"
handoff_condition: "Finalize-only; do not change published package contracts or move the immutable v0.4.2 tag."
ground_truth:  # confirmed from hosted runs 2026-07-20; use verbatim
  published_commit: "f474c3b058cb9f89f93929e0732fc1f276422dd9"
  published_run: "29679273269"   # run #5, success, 2026-07-19 08:07 UTC
  failed_run: "29678934006"      # run #4, failure at validate step, tag at 1c13d799a8cd
  invalid_public_provenance_sha: "1c13d7966b937004f12be6dd70d58c8ecb5afbe7"  # not a real object
decision_needed: "None on facts (confirmed). Decide only whether to regenerate the public GitHub Release body to clear the invalid provenance SHA."
acceptance:
  - "validate-workflow-artifacts.py passes on main (F1/F7)."
  - "release.yaml status=published, commit=f474c3b058cb9f89f93929e0732fc1f276422dd9; exactly one governed candidate remains discoverable (F2)."
  - "release-notes.md is a single authored source with no automation markers or render provenance; migration-guide.md has real content (F3/F4)."
  - "In-repo evidence uses run 29679273269 and commit f474c3b; the copied 29650583394 is removed (F5)."
  - "The published GitHub Release body no longer shows the invalid provenance commit 1c13d7966b93... (regenerate from corrected source) (F3)."
  - "ROADMAP marks v0.4.2 published; R042-001..005 published_in set; Next Action advanced (F6)."
constraints:
  - "Do not move, recreate, or delete the immutable v0.4.2 tag."
  - "Patch-compatible; introduces no new schema or published-path removal."
```

## Proposed item 2 — REL-001 (release automation hardening, target v0.5.0)

Addresses RC-1, RC-2, RC-3. Could also be folded into `ENF-001`'s
acceptance; keeping it separate makes the release surface explicit.
```yaml
schema_version: "1.0"
backlog_id: "REL-001"
title: "Release Publication Runbook, Templates, and Mechanical Gates"
category: "release-governance"
status: "planned"
priority: "HIGH"
release:
  target: "v0.5.0"
  gate: "release-blocker"
summary: "Make release publication cold-start-safe: a step-by-step runbook, placeholder templates with stale-value rejection, a pre-tag precondition gate, and a post-publication terminal-state validator."
acceptance:
  - "ai-context-governance publishes a release-publication runbook: each step names the command to run and its expected output; copying the previous release's instance is prohibited."
  - "release.yaml / workflow.yaml / task.json are instantiated from placeholder templates; a validator rejects stale values (created_at earlier than workflow creation, run ID equal to any prior release, backlog_refs unrelated to the workflow)."
  - "A prepare-release-tag script is the only sanctioned way to create the tag: it verifies registry skeleton present, status=validated, notes/migration non-empty and free of automation markers, and check-all --critical green, before creating the annotated tag."
  - "A terminal-state validator asserts: if tag vX exists then release.yaml status=published and commit == vX^{}; and release-notes.md contains no render output."
  - "governance validation route runs in pull-request CI (aligns with ENF-001)."
decision_needed: "Approve the runbook, the new validators/scripts, and whether REL-001 stands alone or merges into ENF-001."
```

## Proposed item 3 — HANDOFF-001 (model-handoff gate, target v0.5.0)

Addresses RC-4 and the evidence-discipline contributing factor.
```yaml
schema_version: "1.0"
backlog_id: "HANDOFF-001"
title: "Model / Session Handoff State-Alignment Gate"
category: "governance-process"
status: "planned"
priority: "MEDIUM"
release:
  target: "v0.5.0"
  gate: "disposition-gate"
summary: "Require a mechanical state-alignment step whenever work is handed to a different model or fresh session mid-workflow, so process quality does not depend on context continuity."
acceptance:
  - "AGENTS.md / TEAM-GIT-FLOW-RULES defines a handoff checkpoint: the receiving agent runs check-all --critical and records the result in the resume checkpoint before continuing."
  - "A red critical gate blocks continuation until fixed."
  - "Validation-claim sections in commit/task artifacts require a runnable command and its output, not a free-text assertion (reduces fabricated verification)."
  - "The design-for-weakest-executor principle is stated in the root collaboration guide."
decision_needed: "Whether the handoff gate is advisory guidance or a hard release-blocker; how strictly to enforce the evidence-command requirement."
```

## Roadmap edits implied

- Add v0.4.2 → `published` transition only after R042-005 closes.
- Record the real reason v0.5.0 is currently blocked (F2), replacing the
  implicit "evidence reconciled" wording with the concrete finalization
  dependency.
- Slot REL-001 and HANDOFF-001 into the v0.5.0 gate table; decide the
  ENF-001 relationship.
