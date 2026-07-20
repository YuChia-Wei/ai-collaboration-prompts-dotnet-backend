# SAG-001 Runtime Adapter Contract Evidence

## Evidence Metadata

- Workflow: `2026-07-21-v0-5-0-development`
- Task: `V050-004`
- Backlog item: `SAG-001`
- Subject commit: `6aed5786033d404fdfe9eaa8961f51a071321b5f`
- Verified at: `2026-07-21T01:22:48+08:00`

## Decision

Dynamic canonical loading is the default. A role is promoted only when a
concrete runtime-specific model, tool, permission, or invocation need exists.
Role symmetry is not evidence for promotion.

The complete inventory contains 18 roles: 17 remain dynamic and only
`context-translator` is runtime-native. The promoted role maps exact paths for
Codex, Claude, and GitHub Copilot through canonical `adapter_metadata`.

## Current Runtime Schema Evidence

| Target | Current source and local evidence | Validated repository contract | Executability statement |
| --- | --- | --- | --- |
| Codex | [Official sub-agent documentation](https://developers.openai.com/codex/subagents) requires standalone project TOML under `.codex/agents/` with `name`, `description`, and `developer_instructions`; local `codex-cli 0.144.3` reports `multi_agent` stable. | TOML parses; required identity fields, exact canonical citation, `gpt-5.6-terra`, and `low` reasoning metadata are present. | The local client and format are available. A read-only ephemeral invocation was attempted, but the managed environment prohibited sending repository instructions to the external service. Named-agent execution is therefore not claimed by this evidence. |
| Claude | [Official Claude Code sub-agent documentation](https://code.claude.com/docs/en/sub-agents) requires Markdown with YAML frontmatter under `.claude/agents/`; `name` and `description` are required. Local Claude Code is `2.1.201` and exposes `--agent` and `--agents`. | Frontmatter parses; required identity fields, `haiku`, bounded tools, and the exact canonical citation are present. | The local client and documented project format are available. No paid model invocation was executed, so runtime execution is not claimed. |
| GitHub Copilot | [Official custom-agent reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration) requires `description`, supports `.md` or `.agent.md`, and retires `infer` in favor of `disable-model-invocation` and `user-invocable`. | Frontmatter parses; exact identity, canonical citation, supported tools, manual invocation, and current invocation flags are present; retired `infer` is rejected. | No local Copilot CLI is installed. The configuration is schema-valid, but local execution is not claimed. |

Schema conformance, local client presence, and successful model invocation are
separate evidence classes. The adapter contract must not convert the first two
into a claim about the third.

## Role Dispositions

| Canonical role | Disposition | Native targets | Rationale |
| --- | --- | --- | --- |
| `aggregate-code-review-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `aggregate-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `aggregate-test-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `code-review-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `command-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `context-translator` | promote native | Codex, Claude, Copilot | A bounded lower-cost model, restricted tools, and explicit post-finalization invocation are runtime-specific. |
| `controller-code-review-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `controller-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `controller-test-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `mutation-testing-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `outbox-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `problem-frame-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `profile-config-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `query-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `reactor-code-review-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `reactor-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `reactor-test-sub-agent` | keep dynamic | none | No runtime-specific requirement. |
| `usecase-test-sub-agent` | keep dynamic | none | No runtime-specific requirement. |

## Deterministic Validation

- `python .ai/scripts/tests/test_ai_context_wrapper_metadata.py -q`: 9 passed.
- `python .ai/scripts/tests/test_ai_context_sub_agent_adapters.py -q`: 18 passed.
- The negative fixtures reject missing and extra target metadata, duplicate
  targets and paths, placeholder/glob, repository escape, nonexistent and
  wrong-case paths, wrong runtime root or format, missing canonical citation,
  retired Copilot metadata, package omission, target remapping, and exclusion.
- `python .ai/scripts/validate-ai-context.py`: passed with 32 canonical
  manifests; the role-inventory fixture proves 18 total, 17 dynamic, and one
  promoted role with three exact targets.
- The authoritative source-side `collect_payload()` GWT proves that all three
  adapters retain their exact target paths.

## Immutable Package Evidence

The package builder produced ZIP and tar.gz candidates from subject commit
`6aed5786033d404fdfe9eaa8961f51a071321b5f`.

- `validate-ai-context-package.py` passed both archives and their parity checks.
- The extracted payload and `metadata/files.yaml` contain:
  - `.codex/agents/context-translator.toml`
  - `.claude/agents/context-translator.md`
  - `.github/agents/context-translator.agent.md`
- The packaged adapter validator returned no errors without
  `.ai/distribution/`, confirming that source-only package-profile validation
  is not imposed on initialized consumers.

The raw payload is a template seed, not an initialized repository; unrelated
root bilingual projections are finalized by repository initialization. This
evidence therefore asserts archive integrity and the focused adapter contract,
not full validation of an uninitialized payload directory.

## Boundary

SAG-001 owns deterministic identity, schema marker, canonical citation,
target/path, and package inclusion checks. General prose semantic equivalence
between runtime projections and canonical assets remains assigned to
`ENF-001`.
