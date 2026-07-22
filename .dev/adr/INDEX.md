# ADR Index

This directory retains governance documents and proposed or accepted structural decisions.

## Decision Records

| ADR | Title | Status | Date | Related Work |
| --- | --- | --- | --- | --- |
| [ADR-001](ADR-001-separate-source-config-from-downstream-templates.md) | Separate Source Repository Configuration From Downstream Templates | Proposed | 2026-07-23 | [`CFG-001`](../backlog/items/CFG-001.yaml) |

## Current Contents

| File | Role |
| --- | --- |
| `README.md` | ADR governance guidance |
| `ADR-TEMPLATE.md` | Template for a new ADR |
| `WHEN-TO-CREATE-ADR.MD` | Criteria for creating an ADR |

## Status Rule

- Add `ADR-###-<topic>.md` for a new significant structural decision.
- When a decision is fully incorporated into `.dev/standards/`, `.dev/guides/`, or `.ai/`, this index may mark it as retired/landed.
- When there is no active decision record to retain, `INDEX.md` may remain a catalog of governance documents only.

## Naming Rule

- Filename format: `ADR-###-<topic>.md`
- Use a three-digit sequence number for `###`.
- Use English kebab-case for `<topic>`.
