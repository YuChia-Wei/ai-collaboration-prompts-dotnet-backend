# Skill Responsibility Audit

This audit reviews current top-level AI collaboration skills for responsibility overlap, unclear names, wrapper/spec drift, and routing confusion.

## Evidence Used

- `.ai/assets/skills/*/skill.yaml`
- `.agents/skills/*/SKILL.md`
- `.claude/skills/*/SKILL.md`
- `.dev/guides/ai-collaboration-guides/`
- Sub-agent explorer result for `ai-context-governance` and `bdd-gwt-test-designer`

## Skills Reviewed

| Skill | Primary Responsibility | Verdict |
| --- | --- | --- |
| `ai-context-governance` | AI context boundaries, documentation language policy, skill routing, wrapper sync, and context migration. | Keep. Correctly fills the AI documentation governance gap. |
| `bdd-gwt-test-designer` | BDD/Gherkin-style scenario and assertion design without test code implementation. | Keep. Boundary is mostly clear. |
| `code-reviewer` | Formal .NET code review for DDD, CA, CQRS, Event Sourcing compliance. | Keep. Distinct from refactor implementers. |
| `command-use-case-implementer` | Implement bounded command-side use cases. | Keep. Distinct from query/reactor implementers. |
| `query-use-case-implementer` | Implement bounded query-side use cases. | Keep. Distinct from command/reactor implementers. |
| `reactor-implementer` | Implement event-driven consistency, projection updates, and integration reactions. | Keep. Distinct from command/query implementers. |
| `ddd-ca-hex-architect` | Architecture design and refactor shaping. | Keep. Distinct from implementation and review skills. |
| `problem-frame-author` | Draft validator-ready problem frames from requirements/specs/code/tests. | Keep. Distinct from spec compliance validator. |
| `repo-structure-sync` | Refresh repo-specific architecture docs after template copy. | Keep. Distinct from AI context governance. |
| `requirement-author` | Draft or normalize requirement documents. | Keep. Distinct from spec author. |
| `spec-author` | Draft or normalize production/test specs. | Keep. Distinct from BDD scenario design. |
| `spec-compliance-validator` | Validate code/tests against problem frame specs with 100% gate. | Keep. Distinct from authoring skills. |
| `staged-refactor-implementer` | Execute pre-decided multi-step refactor slices. | Keep. Distinct from tactical refactor. |
| `tactical-refactor-implementer` | Execute local object-centered refactors. | Keep. Distinct from staged refactor. |

## Findings

### No Rename or Merge Required

No current skill requires renaming, merging, or deletion. The skill set is broad, but each skill owns a recognizable top-level capability.

### Main Routing Risk: BDD Design vs Test Generation

`bdd-gwt-test-designer` is correctly scoped to scenario and assertion design. The drift risk appears in surrounding guide language that mentions test generation sub-agents. Those references are valid as downstream handoff guidance, but they can mislead readers if not explicitly framed as separate from the BDD skill itself.

Low-risk fix:

- Tighten `BDD-GWT-TEST-DESIGNER-PAIR-GUIDE.md` so test generation is explicitly downstream and not part of the skill responsibility.
- Add a central note in the taxonomy or workflow guide: use `ai-context-governance` for AI documentation/context cleanup; use `bdd-gwt-test-designer` only for behavior/test scenario design.

### AI Context Governance Boundary Is Correct

`ai-context-governance` has the right negative boundaries:

- no BDD scenario design;
- no production code implementation;
- no domain architecture redesign.

It should remain the primary skill for `.ai`, `.dev`, `.agents`, `.claude`, language policy, wrapper sync, and context migration work.

### Architect vs Implementers

`ddd-ca-hex-architect` overlaps conceptually with command/query/reactor implementers only at handoff boundaries. Current wording keeps the split clear:

- architect defines direction and boundaries;
- implementers execute bounded use case slices without redefining architecture.

No correction needed.

### Requirement, Spec, BDD, Problem Frame, Validator Chain

The authoring chain is coherent:

1. `requirement-author`
2. `spec-author`
3. `bdd-gwt-test-designer` when GWT scenario design is needed
4. `problem-frame-author` when validator-ready problem frames are needed
5. `spec-compliance-validator` for the 100% gate

The only needed improvement is to keep this sequence visible in central routing docs.

## Recommended Low-Risk Corrections

1. Update `SKILL-AND-SUB-AGENT-TAXONOMY-GUIDE.md` with a routing note for `ai-context-governance` versus `bdd-gwt-test-designer`.
2. Update `BDD-GWT-TEST-DESIGNER-PAIR-GUIDE.md` to state that test generation sub-agents run after scenario design and are not part of the BDD designer skill.
3. Update `AI-COLLABORATION-WORKFLOW-GUIDE.md` if needed to distinguish scenario design from implementation.
4. Do not rename or merge skills in this workflow.

## Deferred Items

- A full sub-agent role taxonomy audit is out of scope for this pass.
- Moving `frontend-sub-agent` to a future full-stack template is a context relocation decision, not a skill responsibility fix.
- Stricter automated routing enforcement can be considered later if human guidance is insufficient.
