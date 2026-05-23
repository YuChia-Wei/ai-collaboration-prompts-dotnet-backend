# Repo Identity and Init Template Workflow

Status: active

## Goal

Reframe this repository as an AI collaboration knowledge base and reusable context framework, not as the original sample product repository.

## Context

The repository is intended to:

- extract software development knowledge, including software engineering, .NET development, and architecture design;
- maintain AI Agents Context, Skills, Sub-Agent prompts, and AI collaboration workflows;
- separate universal software architecture and engineering context from non-universal .NET C# backend Web API context;
- remove or isolate historical project-specific facts that came from the original source project;
- make `repo-structure-sync` the first-use skill when this AI context framework is copied into an existing or empty target repository.

## Stages

1. Bootstrap workflow artifacts.
2. Rewrite root README files as repo-specific identity documents.
3. Rewrite `agents.md` as this repository's agent operating guide.
4. Promote `repo-structure-sync` to repo-init/template adaptation responsibility.
5. Sync indexes and validate stale references.

## Commit Policy

Use `.dev/standards/GIT-COMMIT-POLICY.md`.

No issue number is currently assigned, so commits use:

```text
<type>(<scope>): <summary>
```

Workflow-stage commits include `Why`, `What`, `Validation`, and `Workflow` body sections.

## Completion Criteria

- Root `README.md` describes this repo's current purpose in Traditional Chinese.
- Root `README.en.md` describes the same purpose in English.
- `agents.md` no longer describes this repo as the copied target product.
- `repo-structure-sync` is explicitly framed as the repo init / template adaptation skill.
- Stale references to the original sample product are removed from root README and agent entry docs.
- Markdown whitespace validation passes.
