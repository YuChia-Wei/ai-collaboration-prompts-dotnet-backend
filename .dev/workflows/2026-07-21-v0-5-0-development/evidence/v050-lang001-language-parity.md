# LANG-001 Language And Semantic Parity Evidence

## Evidence Metadata

- Workflow: `2026-07-21-v0-5-0-development`
- Task: `V050-007`
- Backlog item: `LANG-001`
- Subject commit: `2db0636be79c3f3d65f90c2557856a8969ac8ab5`
- Verified at: `2026-07-21T02:10:06+08:00`

## Inventory Reconciliation

The historical remediation report recorded 21 high-priority and several
medium-priority `.dev/standards` / `.dev/specs` translation candidates. That
was a prospective translation inventory, not a list of active mixed-language
defects. It predates the current language policy, later file moves, five
translation waves, and the explicit decision not to create bilingual variants
for every standard or guide.

The subject revision contains 57 active standards/specs language surfaces:
48 under `.dev/standards` and 9 under `.dev/specs`. The deterministic language
validator reports zero violations across those surfaces. One exact,
path-scoped mixed-language exception remains in
`.dev/standards/WORKFLOW-GATE-POLICY.md`; it preserves literal user trigger
phrases and is covered by a passing exception fixture.

The 16 historical Han-commented C# files under
`.dev/standards/examples/usecase/` are reference-only examples. They remain
outside the active Markdown/YAML/JSON execution-language surface by policy and
are covered by a path-classification fixture.

## Bounded Remediation

The refreshed inventory found four active defects:

| Path | Defect | Resolution |
| --- | --- | --- |
| `.dev/standards/coding-standards.md` | Two fullwidth colons in English prose | Replaced with ASCII colons. |
| `.dev/standards/coding-standards/repository-standards.md` | One ideographic full stop in an English ordered list | Replaced with an ASCII full stop. |
| `AGENTS.md` | Canonical prose omitted the exact ``automatic-candidate`` identifier retained by the zh-TW translation | Restored the exact inline-code identifier without changing the rule's force. |

No standard/spec translation file was created. Agent execution contracts
remain English-only unless the language policy or repository owner explicitly
approves a stable bilingual entry.

## Deterministic Gate

`validate-ai-context.py` now:

- rejects Han prose and selected non-ASCII punctuation (`：`, `。`) on active
  agent-facing language surfaces, except for exact path-and-line exceptions;
- checks approved root bilingual pairs for reciprocal ownership links, heading
  levels, normalized link targets, code-fence markers, inline-code identifier
  multisets, table-column shapes, list-marker shapes, and ordered table paths;
- continues to state explicitly that these structural checks do not assert
  semantic equivalence.

Ten synthetic GWT cases prove ASCII acceptance, both punctuation failures, the
exact routing exception, example exclusion, a valid pair, and fail-closed
identifier, list, table, and fence drift. The suite is a required quick-gate
command and its literal runner/registry membership is validated.

At the subject commit both approved pairs have matching deterministic
structure:

| Pair | Headings | Links | Fences | Inline identifiers | Table rows | List items |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `README.md` / `README.en.md` | 10 / 10 | 1 / 1 | 0 / 0 | 37 / 37 | 13 / 13 | 42 / 42 |
| `AGENTS.md` / `AGENTS.zh-TW.md` | 23 / 23 | 1 / 1 | 0 / 0 | 116 / 116 | 58 / 58 | 81 / 81 |

Reciprocal entry filenames are normalized only for link and inline-code parity;
all other identifiers remain exact.

## Retained Semantic Review

Structural equality is not semantic proof. Two read-only reviews therefore
compared every section of the four files at the subject commit.

| Pair | Main-agent review | Independent bounded review | Disposition |
| --- | --- | --- | --- |
| zh-TW-canonical `README.md` and translated `README.en.md` | Identity, goals, context layers, directories, skills, language policy, target-repo use, and cleanup direction preserve the same meaning and normative force. | `gpt-5.6-terra` low-reasoning reviewer reported no missing, added, weakened, or materially reordered meaning in the same sections. | pass |
| English-canonical `AGENTS.md` and translated `AGENTS.zh-TW.md` | Scope/precedence, execution principles, all workflow gates, upgrade rules, skill routing, indexes, and language rules preserve the same obligations and prohibitions. | The independent reviewer reported complete parity across all mandatory workflow subsections and no normative mismatch. | pass |

Both reviews confirmed the intentional ownership direction:

- `README.md` is the human-facing zh-TW canonical source and
  `README.en.md` is its English translation.
- `AGENTS.md` is the agent-facing English canonical source and
  `AGENTS.zh-TW.md` is its zh-TW translation.

The independent reviewer made no repository changes. Agreement between the two
reviews is retained evidence, not a claim that either model is an oracle.

## Validation

- `python .ai/scripts/tests/test_ai_context_language_policy.py -v`: 10/10
  passed.
- `python .ai/scripts/validate-ai-context.py`: passed for 294 active
  language-policy files and both root structural-parity contracts.
- `python .ai/scripts/validate-shell-assets.py`: passed for all 14 governed
  shell assets and the exact required-command set.
- `python .ai/scripts/tests/test_fail_closed_validation.py -v`: 24/24 passed.
- Windows Git Bash
  `C:\Program Files\Git\bin\bash.exe .ai/scripts/check-all.sh --quick`:
  24 required selected, executed, and passed; 0 failed, warnings, or deferred;
  2 not applicable. Completed at `2026-07-21T02:07:04+08:00`.
- Hosted Ubuntu `Portable AI Context Gates` run
  [29766507514](https://github.com/YuChia-Wei/ai-collaboration-prompts-dotnet-backend/actions/runs/29766507514)
  executed the same quick entrypoint at exact head
  `2db0636be79c3f3d65f90c2557856a8969ac8ab5`: 24 required selected,
  executed, and passed; 0 failed or deferred. The environment used Python
  `3.12.13` and .NET SDK `10.0.302`.

## Residual Boundary

- The semantic review covers only the two approved root bilingual pairs at the
  pinned subject revision.
- It does not prove referenced-file correctness, Markdown rendering, or any
  unapproved translation surface.
- A later material edit to either pair requires a fresh retained semantic
  review even when deterministic structure remains green.
- The historical 21-candidate count is closed as stale planning input, not
  silently reclassified as 21 completed translations.
