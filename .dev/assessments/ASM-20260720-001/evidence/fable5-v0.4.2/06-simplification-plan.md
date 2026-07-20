# 06 — Simplification / Token-Reduction Plan

Applies once the roadmap/backlog are complete. Guiding rule and priorities.

## Guiding rule

For every prose rule, ask: **is it backed by a validator?**
- Yes → shrink the prose to a one-line pointer to the check.
- No → either write the validator, or keep the prose (it is the only
  enforcement).

Enforcement in a script costs zero tokens per session; enforcement in context
is paid every session. The v0.4.2 incident is the proof: 1.8k words of policy
did not stop process drift after a model switch — the only things that
actually caught defects were fail-closed scripts.

## Measured baseline (word counts; tokens ≈ ×1.3–2)

| Surface | Words | Note |
| --- | --- | --- |
| `.dev/workflows` | 129,729 | historical run records; ~half of repo text |
| `.dev/standards` | 43,295 | normative + long .NET examples |
| `.ai/assets/skills` | 24,895 | 14 skills |
| `.dev/assessments` | 24,492 | completed audits |
| `.dev/guides` | 23,458 | human-facing |
| `.ai/assets/tech-stacks` | 6,249 | |
| `.ai/assets/sub-agent-role-prompts` | 6,467 | |
| `AGENTS.md` / `AGENTS.zh-TW.md` | 1,803 / 1,230 | always-loaded, per session |

## Priorities (by token saved)

1. **Archive historical run records (~154k words).** Completed
   workflow/assessment artifacts (311 files) have near-zero value to daily
   agents. Policy change: at closeout, compress to a one-page summary + INDEX
   row; move full artifacts to an archive branch / rely on git history.
   Policy and validators unchanged; enforcement unchanged.
2. **Converge bilingual mirror (after LANG-001).** Single English source for
   agent-facing docs; reduce `AGENTS.zh-TW.md` to a thin pointer or drop it;
   keep zh-TW for README and human guides only. Removes a permanent sync
   burden and the parity-gate cost, not just words.
3. **Generate wrappers.** Generate `.agents` / `.claude` / `.codex` /
   `.github` adapters from the canonical skill spec; forbid hand edits;
   validator checks byte-parity only. Structurally eliminates the wrapper
   identity drift that R042-001 had to fix — cheaper and stronger than
   ENF-001's planned semantic validation.
4. **Merge skills (with SKILL-001 taxonomy).** `requirement-author` /
   `spec-author` / `problem-frame-author` / `bdd-gwt-test-designer` are one
   authoring pipeline — collapse into modes of one skill sharing references;
   fold `local-change-implementer` into `slice-implementer` via a scope
   parameter. 14 → ~8 skills; routing table halves; misroute probability
   drops.
5. **Slim standards (43k words).** Extract MUST/MUST NOT normative rules into
   short always-loaded rule files; move .NET examples and long explanations
   to `examples/` read on demand. Tabulate checklists pointing at examples.
   Est. ~50% reduction.
6. **Reduce template metadata.** Replace the 5–6 line template-metadata block
   on every task JSON / workflow yaml with a single
   `template: <id>@<version>` line; schema validation moves to the validator.
   Multiplied across hundreds of files.
7. **Trim AGENTS.md to ~800–1000 words.** It is fixed per-session cost. Keep:
   identity declaration, gate triggers, routing table, pointers. Move the
   File & Directory Index and Mandatory-Workflow detail into `.dev/standards`
   (already there) and reference them.

## Sequencing note

Items 2, 3, 4 depend on their owning backlog items (LANG-001, ENF-001/
wrapper decision, SKILL-001). Items 1, 5, 6, 7 are independent and can run
as a dedicated `ai-context-governance` simplification workflow once the
roadmap is clear. Always pair a prose deletion with the validator that now
carries its enforcement — never drop a rule that has no mechanical backstop.
