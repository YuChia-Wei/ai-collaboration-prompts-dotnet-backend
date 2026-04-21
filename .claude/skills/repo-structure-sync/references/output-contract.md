# Output Contract

## Phase 1 Output

The low-cost inventory pass should return these sections in order:

1. `Evidence Used`
   - key files or folders inspected
2. `Confirmed Repo Facts`
   - only file-backed architecture facts
3. `P0 Hits`
   - list each `P0` trigger or state `none`
4. `P1 Hits`
   - list each `P1` trigger or state `none`
5. `Complexity Verdict`
   - `stay-low-cost` or `escalate`
   - include the reason using the checklist rule
6. `Safe Direct Updates`
   - files that can be updated now without stronger synthesis
7. `Escalation Targets`
   - files or tasks that should be handed off
8. `Source Packet`
   - the compact handoff bundle for the next model or agent

## Phase 2 or Final Output

After edits are made, return:

1. `Docs Updated`
   - list of files changed
2. `Inferred or Missing Truth`
   - assumptions, stale docs, or unresolved areas
3. `Recommended Next Step`
   - such as requirement/spec regeneration or architecture review

## Source Packet Minimum Shape

When escalation is required, the `Source Packet` should include:

- top-level folder inventory
- solution and project list
- package-reference summary
- confirmed host types
- stale-doc conflicts
- exact target files for rewrite

If no edits were made, explain what blocked the sync and which file-backed evidence was insufficient.
