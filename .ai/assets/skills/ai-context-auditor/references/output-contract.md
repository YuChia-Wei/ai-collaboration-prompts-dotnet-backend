# AI Context Auditor Output Contract

Always create or update a durable Markdown report from:

```text
.ai/assets/skills/ai-context-auditor/templates/ai-context-audit-report-template.md
```

Default destination:

```text
.dev/workflows/<workflow-id>/review-report.md
```

The report must include metadata and scope, explicit code exclusions, methodology and evidence, both audit passes, their comparison, strengths, severity-ranked findings, validation and skipped checks, deferred items and code-review handoffs, and prioritized actions.

Do not mark the report final while high-severity claims lack file-backed evidence.

The final response must return the overall assessment, highest-priority findings, report path, scope exclusions, validation summary, recommended next skill, and whether remediation was intentionally not performed.

If source-code review was requested, return the handoff instead of an AI context finding about unread code.

