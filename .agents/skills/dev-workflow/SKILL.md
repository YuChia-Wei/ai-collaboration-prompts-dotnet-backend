---
name: dev-workflow
description: Coordinate multi-stage development, documentation, refactoring, and AI collaboration work by deciding direct mode versus workflow mode, creating workflow artifacts, routing stages to other skills, and managing validation and commit checkpoints.
---

# Dev Workflow

This is a thin current-runtime wrapper.

## Canonical Source

- Registry: `.ai/assets/skills/README.MD`
- Spec: `.ai/assets/skills/dev-workflow/skill.yaml`
- Human Guide: `.dev/guides/ai-collaboration-guides/DEV-WORKFLOW-SKILL-GUIDE.md`
- References:
  - `.ai/assets/skills/dev-workflow/references/routing-playbook.md`
  - `.ai/assets/skills/dev-workflow/references/skill-discovery-playbook.md`
  - `.ai/assets/skills/dev-workflow/references/capability-profile.md`
  - `.ai/assets/skills/dev-workflow/references/fallback-playbooks.md`
  - `.ai/assets/skills/dev-workflow/references/workflow-artifact-playbook.md`
  - `.ai/assets/skills/dev-workflow/references/output-contract.md`

## Wrapper Rules

Use this wrapper only as the current runtime entry.
Keep runtime-specific metadata in this wrapper directory only when the runtime requires it.
If wrapper text and canonical spec differ, follow `.ai/assets/skills/dev-workflow/skill.yaml`.
