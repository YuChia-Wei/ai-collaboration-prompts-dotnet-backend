# Canonical Asset Schema

This document defines the minimum canonical schema for portable AI assets.

## Common Fields

Every asset spec must include at least:

- `id`
- `asset_type`
- `title`
- `purpose`
- `portability`
- `audience`
- `wrapper_targets`
- `source_of_truth`
- `inputs`
- `outputs`
- `constraints`
- `references`
- `examples`
- `status`

## `skill` Spec

Recommended additional fields:

- `triggers`
- `handoff_rules`
- `runtime_notes`

## `command` Spec

Recommended additional fields:

- `invocation_style`
- `prompt_packages`
- `command_outputs`

## `prompt-package` Spec

Recommended additional fields:

- `base_prompt`
- `shared_fragments`
- `validation_rules`

## `shared-rule` Spec

Recommended additional fields:

- `consumers`
- `rule_scope`

## Portability Values

- `portable`
- `repo-portable`
- `wrapper-specific`

## Audience Values

- `agent-facing`
- `human-facing`
- `mixed`

## Source Of Truth Values

- `canonical`
- `wrapper`
- `generated`

## Wrapper Targets

Supported by default:

- `claude`
- `codex`
- `copilot`
