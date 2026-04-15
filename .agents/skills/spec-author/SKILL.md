---
name: spec-author
description: Draft or normalize production specs and test specs for this repository from requirements, existing specs, or codebase facts. Use when Codex needs to turn requirement truth into `.dev/specs/`-aligned JSON or markdown without yet claiming code or test completion.
---

# Spec Author

## Overview

Use this skill to produce repository-aligned specs under `.dev/specs/`.

## Quick Start

1. Read `.dev/ARCHITECTURE.MD` and `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`.
2. Read `.dev/specs/SPEC-GUIDE.MD`.
3. Read `.dev/specs/SPEC-ORGANIZATION-GUIDE.MD`.
4. Read [references/authoring-playbook.md](references/authoring-playbook.md).
5. Read [references/output-contract.md](references/output-contract.md).

## Workflow

### 1. Choose the spec type

Pick one:

- use case spec
- entity/value-object spec
- adapter/controller spec
- test spec

### 2. Identify the target aggregate or use case

If aggregate ownership is unclear, stop and hand off to `ddd-ca-hex-architect`.

### 3. Draft the spec

Follow the required keys, naming rules, and file placement rules from `.dev/specs/`.

### 4. Keep production specs and test specs separate

If the user needs scenario design in Given-When-Then form, recommend `bdd-gwt-test-designer`.

## References

- [references/authoring-playbook.md](references/authoring-playbook.md)
- [references/output-contract.md](references/output-contract.md)
- [references/type-selection.md](references/type-selection.md)
