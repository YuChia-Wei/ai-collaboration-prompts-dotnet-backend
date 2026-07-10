# AI Context Audit Playbook

## 1. Intake And Evidence Boundary

Record the repository identity, branch, audit reason, requested focus, included context roots, excluded code/generated surfaces, previous report, and whether bounded sub-agent delegation is useful.

Read deeper `AGENTS.*` files before auditing a governed subtree. Keep the work read-only unless remediation is separately authorized.

## 2. Pass A: Independent Baseline

Assess the repository using general knowledge before treating its own governance policies as the rubric. Review:

- repository identity and truth boundaries;
- information architecture and navigation;
- canonical ownership and duplication;
- instruction clarity, precedence, and actionability;
- active versus example, historical, generated, and planned content;
- runtime wrapper and registry relationships;
- schema and template consistency;
- language and audience consistency;
- validation integrity and fail-open behavior;
- scale, cognitive load, lifecycle, and portability.

Capture strengths as well as defects. Do not read product code to validate architecture or coding claims.

## 3. Pass B: Repository-Aware Assessment

After the baseline is recorded, apply repository-specific policies and relevant skills. For this repository, normally use `ai-context-governance` for audience, scope, language, placement, routing, and wrapper rules, and `dev-workflow` for workflow mode, artifact, validation, and handoff rules.

Check whether the repository follows its own declared contracts. Do not allow a policy assertion to erase contradictory file-backed evidence.

## 4. Parallel Audit Pattern

When the context is large and sub-agents are available, use bounded read-only tasks for structure/navigation, content truth/rule strength/language, and runtime wrappers/schemas/scripts/validation. Tell each worker the same exclusions. The main agent verifies high-severity evidence, resolves duplicates, compares both passes, and owns the final report.

## 5. Finding Rules

| Severity | Meaning |
| --- | --- |
| `CRITICAL` | The context can directly cause unsafe, destructive, or broadly incorrect agent behavior. |
| `HIGH` | Active rules conflict, canonical truth is ambiguous, or validation can materially mislead execution. |
| `MEDIUM` | Navigation, maintenance, lifecycle, portability, or policy drift increases recurring error risk. |
| `LOW` | Local clarity, consistency, or hygiene issue with limited behavioral impact. |

Each finding must contain evidence, impact, recommendation, and an appropriate owner or next skill. Separate active defects from historical references, accepted exceptions, and items needing a domain decision.

## 6. Validation

Prefer deterministic read-only checks: explicit `rg --files --hidden` include/exclude globs, path existence, registry comparison, structured-file parsing, Markdown/reference checks, wrapper-to-canonical checks, targeted context validation scripts, and Git state checks.

Record exact commands and results. A warning-only or skipped gate is not equivalent to a passing semantic validation.

## 7. Comparison And Persistence

Compare confirmed findings, findings added by repo policies, downgraded or deferred findings, overturned findings, and residual uncertainty.

Create the report from the canonical template. Default path:

```text
.dev/workflows/<YYYY-MM-DD>-ai-context-audit/review-report.md
```

When an active workflow owns the audit, use that workflow's `review-report.md`. If the default id exists, append a concise topic or sequence suffix instead of overwriting an unrelated report.
