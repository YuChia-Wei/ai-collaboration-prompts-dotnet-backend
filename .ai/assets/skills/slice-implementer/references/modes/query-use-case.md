# Query Use Case Mode

Use this mode when the slice implements one bounded query-side use case.

## Mandatory References

- `.dev/ARCHITECTURE.MD`
- `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`
- `.ai/assets/sub-agent-role-prompts/query-sub-agent/sub-agent.yaml`
- `.ai/assets/sub-agent-role-prompts/query-sub-agent/references/implementation-playbook.md`
- `.dev/standards/USECASE-COMMAND-HANDLER-RELATIONSHIP.MD`

## Rules

- Use WolverineFx query handlers.
- Queries must not modify domain state.
- Return DTOs, not domain entities.
- Prefer projections or read-side storage patterns already established by the repo.
- Keep read model shape, filter normalization, and client-facing state mapping explicit.

## Expected Output

- bounded implementation for the target query use case;
- touched files or intended output paths;
- DTO/read-model notes;
- validation notes;
- explicit follow-up handoff when test design, review, or architecture work remains.
