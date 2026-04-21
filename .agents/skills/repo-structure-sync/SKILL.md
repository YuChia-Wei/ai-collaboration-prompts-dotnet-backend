---
name: repo-structure-sync
description: Scan a freshly copied target git repository and refresh repo-specific architecture sections in `.dev/`, `.ai/`, and `agents.md`. Use when Codex needs to adapt this template to a new .NET repo by inventorying solution structure, projects, stack facts, and documentation truth without rewriting framework-level collaboration rules.
---

# Repo Structure Sync

## Overview

Use this skill after the collaboration template has been copied into a different repository.
Its job is to rebuild repo-specific architecture truth from the target repo's current files and then update the architecture-facing sections of `.dev/`, `.ai/`, and `agents.md`.

## Quick Start

1. Read `.dev/PORTABLE-PACKAGING-GUIDE.MD`.
2. Read `.dev/PORTABLE-TRANSFER-CHECKLIST.MD`.
3. Read [references/scan-playbook.md](references/scan-playbook.md).
4. Read [references/escalation-checklist.md](references/escalation-checklist.md).
5. Read [references/delegation-rules.md](references/delegation-rules.md).
6. Read [references/document-targets.md](references/document-targets.md).
7. Read [references/output-contract.md](references/output-contract.md) before returning results.

## Workflow

### 1. Run a low-cost inventory pass first

Default to a lower-cost model for the first pass.
The first pass should focus on file-backed discovery, not high-creativity rewriting.

Use the first pass to:

- scan the repo tree and project files
- extract confirmed stack and structure facts
- identify stale copied docs
- classify complexity before choosing the writing strategy
- produce the phase-1 output shape from [references/output-contract.md](references/output-contract.md)

### 2. Build the repo inventory

Collect evidence from the current repository before editing docs:

- git-visible top-level structure
- solution files and `*.csproj`
- `Directory.Packages.props`, `global.json`, `NuGet.config`
- `src/`, `tests/`, `docker-compose/`, deployment, and infra folders
- package references, target frameworks, and messaging/database libraries
- existing README and architecture docs

Prefer facts from the actual repo structure and project files over stale prose in copied template documents.

### 3. Extract architecture truth

Summarize only confirmed repo facts such as:

- bounded contexts or modules
- application hosts and executable entry points
- shared libraries and contracts
- testing project layout
- persistence, messaging, and hosting choices
- major runtime folders and operational assets

If a fact is not directly supported by files, label it as inferred.

### 4. Check whether escalation is needed

Stay on the low-cost model when the repo is structurally clear and the required edits are mostly direct substitutions.

Use [references/escalation-checklist.md](references/escalation-checklist.md) as the decision gate.
Escalate to a stronger model or sub-agent when the checklist produces:

- any `P0` trigger
- two or more `P1` triggers
- one `P1` trigger plus a user request for architecture-grade rewriting

If escalation is needed, keep the first-pass inventory as the source packet for the next step rather than rescanning everything from scratch.

### 5. Separate portable rules from repo truth

Keep framework-level collaboration rules, workflow rules, and reusable guidance.
Only rewrite the parts that describe what this specific repository looks like now.

### 6. Update the document set

Update only the relevant repo-truth sections called out in [references/document-targets.md](references/document-targets.md).
Preserve stable framework guidance unless the new repo clearly invalidates it.
Use [references/delegation-rules.md](references/delegation-rules.md) to decide which files can be updated directly and which should be handed off.

### 7. Return a migration-quality summary

Report:

1. evidence used
2. confirmed architecture facts
3. inferred or missing items
4. documents updated
5. follow-up docs that still need human confirmation

## Guardrails

- Do not spend a strong model on the first pass unless the user explicitly requests it.
- Do not pretend the new repo still matches the source template's sample bounded contexts, services, or folders.
- Do not bulk-rewrite `.dev/specs/` or `.dev/operations/` unless the user explicitly asks for those artifacts too.
- If the target repo is not primarily .NET, narrow the update scope and state the mismatch clearly.
- If the repo contains multiple solutions or mixed stacks, describe the partitioning rather than flattening it into one fake architecture.
- When README text conflicts with `*.csproj`, package references, or folder structure, trust the codebase and note the conflict.

## References

- [references/scan-playbook.md](references/scan-playbook.md)
- [references/escalation-checklist.md](references/escalation-checklist.md)
- [references/delegation-rules.md](references/delegation-rules.md)
- [references/document-targets.md](references/document-targets.md)
- [references/output-contract.md](references/output-contract.md)
