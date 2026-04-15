---
name: requirement-author
description: Draft or normalize requirement documents for this repository from rough notes, existing requirement files, architecture references, or codebase facts. Use when Codex needs to turn unstructured problem statements into `.dev/requirement/`-aligned markdown without yet expanding into use-case specs.
---

# Requirement Author

## Overview

Use this skill to produce requirement-quality markdown that matches `.dev/requirement/REQUIREMENT-GUIDE.MD`.

## Quick Start

1. Read `.dev/ARCHITECTURE.MD` and `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`.
2. Read `.dev/requirement/REQUIREMENT-GUIDE.MD`.
3. Read [references/authoring-playbook.md](references/authoring-playbook.md).
4. Read [references/output-contract.md](references/output-contract.md).

## Workflow

### 1. Define the topic and scope

Clarify what problem or bounded-context area the requirement should cover.

### 2. Build the requirement draft

Populate:

- Metadata
- Context & Goals
- Personas
- Functional Requirements
- Non-Functional Requirements
- Constraints & Assumptions
- Domain / Business Rules
- Acceptance Criteria
- References

### 3. Mark assumptions and missing truth

If the source inputs do not fully confirm a fact, mark it as an assumption or open question.

### 4. Stop before spec drafting

Do not jump straight into use-case JSON specs.
Recommend `spec-author` when the requirement is stable enough to expand.

## References

- [references/authoring-playbook.md](references/authoring-playbook.md)
- [references/output-contract.md](references/output-contract.md)
- [references/source-truth-rules.md](references/source-truth-rules.md)
