# Command Use Case Mode

Use this mode when the slice implements one bounded command-side use case.

## Mandatory References

- `.dev/ARCHITECTURE.MD`
- `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`
- `.ai/assets/sub-agent-role-prompts/command-sub-agent/sub-agent.yaml`
- `.ai/assets/sub-agent-role-prompts/command-sub-agent/references/implementation-playbook.md`
- `.dev/standards/USECASE-COMMAND-HANDLER-RELATIONSHIP.MD`

## Rules

- Use WolverineFx command handlers.
- Commands may change aggregate state.
- Keep aggregate boundary and command responsibility explicit.
- Keep repository access aligned with the current DI model.
- Do not add custom repository interfaces for write-side flows.
- Follow the active storage profile and architecture configuration.
- Keep validation notes explicit when tests or review are still pending.

## Expected Output

- bounded implementation for the target command use case;
- touched files or intended output paths;
- validation notes;
- explicit follow-up handoff when test design, review, or architecture work remains.
