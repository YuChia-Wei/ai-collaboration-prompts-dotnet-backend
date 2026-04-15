---
name: problem-frame-author
description: Draft a first problem frame for this repository from existing requirements, specs, ADRs, code, or tests. Use when Codex needs to create validator-ready CBF or SWF inputs, reverse-engineer a problem frame from code, or turn requirement/spec truth into structured problem-frame files without yet claiming spec compliance.
---

# Problem Frame Author

## Overview

Use this skill to draft a first problem frame for one use case.
Prefer `CBF` for the first pass unless `SWF` is clearly a better fit.

## Quick Start

1. Read `.dev/ARCHITECTURE.MD` and `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`.
2. Read `.dev/problem-frames/README.MD` to confirm the expected directory structure.
3. Read [references/authoring-playbook.md](references/authoring-playbook.md).
4. Read [references/source-mapping.md](references/source-mapping.md).
5. Read [references/output-contract.md](references/output-contract.md) before returning results.

## Workflow

### 1. Choose one use case

Draft only one use case at a time.
Do not model an entire bounded context in one pass.

### 2. Identify the highest-priority source of truth

Prefer these inputs in order:

- `.dev/requirement/`
- `.dev/specs/`
- ADR or architecture rules
- existing code and tests for gap filling

### 3. Build the extraction sheet

Extract:

- actor and trigger
- input fields
- preconditions
- success and failure outcomes
- domain events
- external systems
- authority boundaries
- timeout / retry / duplicate rules
- acceptance scenarios

### 4. Draft the file set

Draft:

- `frame.yaml`
- `machine/machine.yaml`
- `machine/use-case.yaml`
- `controlled-domain/aggregate.yaml` or `workpiece/aggregate.yaml`
- `acceptance.yaml` or `requirements/*.yaml`

### 5. Mark inferred items

If a fact comes from code or a best-effort inference instead of explicit requirement/spec truth, label it as inferred.

### 6. Stop before validator claims

Do not claim 100% compliance.
If code and tests do not yet exist, recommend the next handoff rather than pretending validation is complete.

## Output Expectations

Return:

1. source inputs used
2. use case selection and `CBF` / `SWF` decision
3. extraction sheet
4. draft file set
5. inferred items
6. open questions
7. recommended next skill

## References

- [references/authoring-playbook.md](references/authoring-playbook.md)
- [references/source-mapping.md](references/source-mapping.md)
- [references/output-contract.md](references/output-contract.md)
