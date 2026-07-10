# Dev Workflow Capability Profile

This profile maps generic `dev-workflow` capability slots to this repository's concrete skills and local conventions.

The core `dev-workflow` skill should stay publishable. Repository-specific skill names belong in this profile.

## Profile Identity

- Profile name: `ai-collaboration-prompts-dotnet-backend`
- Repository role: AI collaboration knowledge base and .NET backend context framework
- Workflow artifact root: `.dev/workflows/<workflow-id>/`
- Commit policy: `.dev/standards/GIT-COMMIT-POLICY.md`
- Workflow gate policy: `.dev/standards/WORKFLOW-GATE-POLICY.md`

## Capability Mapping

| Capability slot | Local skill | Use when |
| --- | --- | --- |
| `workflow-orchestration` | `dev-workflow` | The task needs stage planning, workflow artifacts, skill routing, validation checkpoints, or commit checkpoints. |
| `context-audit` | `ai-context-auditor` | The task needs a read-only AI context health or drift audit, an independent-versus-policy comparison, and a durable report without product-code review. |
| `context-governance` | `ai-context-governance` | Work changes `.ai`, `.dev`, `.agents`, `.claude`, language policy, context boundaries, wrapper sync, or skill routing. |
| `repo-initialization` | `repo-structure-sync` | This framework has been copied into a target repository and repo-specific entry docs must be refreshed from file-backed facts. |
| `requirements` | `requirement-author` | Rough notes, stakeholder inputs, or code facts need to become `.dev/requirement/`-aligned requirement docs. |
| `specification` | `spec-author` | Requirement truth needs to become retained specs under `.dev/specs/`. |
| `problem-framing` | `problem-frame-author` | Requirement, spec, code, or tests need a first problem-frame draft. |
| `architecture` | `ddd-ca-hex-architect` | The task needs DDD, Clean Architecture, CQRS, ports/adapters, bounded context, aggregate, or .NET backend architecture direction. |
| `test-design` | `bdd-gwt-test-designer` | The task needs Given-When-Then scenarios, assertion points, or test design notes. |
| `implementation` | `slice-implementer` | A bounded implementation slice is ready, using command, query, reactor, generic, remediation, or refactor mode as needed. |
| `implementation` | `local-change-implementer` | A local class, object, method, symbol, SQL/ORM, or direct-call-site technical change is ready. |
| `refactoring` | `slice-implementer` | A behavior-preserving refactor slice is already decided and needs execution. |
| `refactoring` | `local-change-implementer` | One local refactor around a class, object, method, symbol, or direct call sites is needed. |
| `review` | `code-reviewer` | .NET backend code or dotnet-backend implementation guidance needs review. |
| `compliance-validation` | `spec-compliance-validator` | Problem-frame workflows need a 100% coverage gate. |

## Quality Boundary

- Full local workflow quality depends on the mapped downstream skills and repository standards.
- If a mapped skill is unavailable, `dev-workflow` should switch that stage to fallback-mode instead of pretending the specialist review, design, or implementation was performed.
- Fallback-mode output is suitable for planning, handoff, and minimum viable checklist coverage. It is not equivalent to a specialist skill result.

## Profile Update Rules

- Add or change mappings here before changing runtime wrappers or root routing tables.
- Keep capability names generic.
- Keep local skill names in this profile or root routing docs, not in the portable core contract.
- If a downstream skill is renamed, update this profile and run reference searches.
