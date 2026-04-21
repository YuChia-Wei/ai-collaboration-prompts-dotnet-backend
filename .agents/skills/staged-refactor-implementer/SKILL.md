---
name: staged-refactor-implementer
description: Execute incremental refactoring stages in this repository using existing architecture decisions and review findings. Use when Codex needs to turn a bounded, pre-decided refactoring slice into concrete code changes, tests, and validation steps without redefining the overall architecture direction.
---

# Staged Refactor Implementer

This is a thin runtime wrapper.

## Canonical Source

- Registry: `.ai/assets/skills/README.MD`
- Spec: `.ai/assets/skills/staged-refactor-implementer/skill.yaml`
- References:
  - `.ai/assets/skills/staged-refactor-implementer/references/skill-boundaries.md`
  - `.ai/assets/skills/staged-refactor-implementer/references/execution-playbook.md`
  - `.ai/assets/skills/staged-refactor-implementer/references/input-contract.md`

## Runtime Notes

Use this wrapper only as the current runtime entry.
Preserve runtime metadata such as `agents/openai.yaml`.
If wrapper text and canonical spec differ, follow `.ai/assets/skills/staged-refactor-implementer/skill.yaml`.
