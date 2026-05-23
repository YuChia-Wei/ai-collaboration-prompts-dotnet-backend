---
name: ai-context-governance
description: Govern AI collaboration context boundaries, documentation language policy, skill routing, runtime wrapper sync, and AI context migration. Use when Codex needs to organize `.ai`, `.dev`, `.agents`, or `.claude` context, split universal versus tech-stack-specific prompts, define context governance policies, or avoid routing AI documentation cleanup to unrelated BDD or code implementation skills.
---

# AI Context Governance

This is a thin current-runtime wrapper.

## Canonical Source

- Registry: `.ai/assets/skills/README.MD`
- Spec: `.ai/assets/skills/ai-context-governance/skill.yaml`
- Human Guide: `.dev/guides/ai-collaboration-guides/AI-CONTEXT-GOVERNANCE-SKILL-GUIDE.md`
- References:
  - `.ai/assets/skills/ai-context-governance/references/context-boundary-playbook.md`
  - `.ai/assets/skills/ai-context-governance/references/language-policy-playbook.md`
  - `.ai/assets/skills/ai-context-governance/references/workflow-and-commit-playbook.md`
  - `.ai/assets/skills/ai-context-governance/references/output-contract.md`

## Wrapper Rules

Use this wrapper only as the current runtime entry.
Keep runtime-specific metadata in this wrapper directory only when the runtime requires it.
If wrapper text and canonical spec differ, follow `.ai/assets/skills/ai-context-governance/skill.yaml`.
