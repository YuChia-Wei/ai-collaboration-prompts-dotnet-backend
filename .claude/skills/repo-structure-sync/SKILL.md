---
name: repo-structure-sync
description: Initialize a target repository after this AI context framework is copied in by scanning repo facts, refreshing repo-specific context, and atomically creating provenance plus the customization ledger only from credible source evidence.
---

# Repo Structure Sync

This is a thin Claude-compatible wrapper.

## Canonical Source

- Registry: `.ai/assets/skills/README.MD`
- Spec: `.ai/assets/skills/repo-structure-sync/skill.yaml`
- Human Guide: `.dev/guides/ai-collaboration-guides/REPO-STRUCTURE-SYNC-SKILL-GUIDE.md`
- References:
  - `.ai/assets/skills/repo-structure-sync/references/scan-playbook.md`
  - `.ai/assets/skills/repo-structure-sync/references/migration-boundaries.md`
  - `.ai/assets/skills/repo-structure-sync/references/escalation-checklist.md`
  - `.ai/assets/skills/repo-structure-sync/references/delegation-rules.md`
  - `.ai/assets/skills/repo-structure-sync/references/document-targets.md`
  - `.ai/assets/skills/repo-structure-sync/references/output-contract.md`
  - `.ai/assets/skills/ai-context-governance/references/semantic-customization-lifecycle.md`
  - `.ai/assets/skills/ai-context-governance/templates/customizations.schema.yaml`
  - `.ai/assets/skills/repo-structure-sync/templates/project-config.template.yaml`
  - `.ai/assets/skills/repo-structure-sync/templates/technology-selection.schema.yaml`
  - `.ai/assets/skills/repo-structure-sync/templates/public-template-manifest.yaml`
  - `.ai/assets/sub-agent-role-prompts/context-translator/sub-agent.yaml`
  - `.ai/assets/skills/ai-context-upgrader/templates/provenance-template.yaml`
  - `.ai/assets/skills/ai-context-upgrader/templates/customizations-template.yaml`

## Wrapper Rules

Use this wrapper only as a compatibility entry.
Keep runtime-specific metadata in this wrapper directory only when the runtime requires it.
If wrapper text and canonical spec differ, follow `.ai/assets/skills/repo-structure-sync/skill.yaml`.
