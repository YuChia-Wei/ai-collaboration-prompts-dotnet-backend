---
name: tactical-refactor-implementer
description: Execute local, object-centered refactoring in this repository. Use when Codex needs to improve one target class, object, or symbol through bounded structural changes such as extract method or safe local rename, without redesigning architecture, introducing new types, or planning a larger refactoring stage.
---

# Tactical Refactor Implementer

This is a thin runtime wrapper.

## Canonical Source

- Registry: `.ai/assets/skills/README.MD`
- Spec: `.ai/assets/skills/tactical-refactor-implementer/skill.yaml`
- References:
  - `.ai/assets/skills/tactical-refactor-implementer/references/skill-boundaries.md`
  - `.ai/assets/skills/tactical-refactor-implementer/references/allowed-operations.md`
  - `.ai/assets/skills/tactical-refactor-implementer/references/execution-rules.md`

## Runtime Notes

Use this wrapper only as the current runtime entry.
Preserve runtime metadata such as `agents/openai.yaml`.
If wrapper text and canonical spec differ, follow `.ai/assets/skills/tactical-refactor-implementer/skill.yaml`.
