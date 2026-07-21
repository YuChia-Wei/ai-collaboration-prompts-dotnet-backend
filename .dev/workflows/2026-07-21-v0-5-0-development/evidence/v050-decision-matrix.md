# v0.5.0 Decision And Dependency Matrix

## Evidence Boundary

- Subject revision at inventory start:
  `62e721e7764fd99253d445f6e92002b92ceee902`
- Authoritative inputs: roadmap, ten v0.5.0 backlog items, their direct origin
  references, tracked runtime adapters, distribution schemas, shell manifest,
  validators, tests, workflows, and Git history.
- Discovery accelerators: three read-only `gpt-5.6-terra` low-effort
  sub-agents covered dependency ordering, package/release/tooling, and
  governance/runtime/language. The main agent rechecked material conclusions
  against repository files.
- Observed inventory failures: PowerShell lacked `ConvertFrom-Yaml`, and two
  guessed release paths did not exist. Those outputs were rejected and replaced
  with Python/PyYAML or actual tracked-path checks.

## Decision Authority

On `2026-07-21`, the repository owner directed the agent to begin every v0.5.0
development item and continue to release readiness, authorized bounded
sub-agents, required checkpoint commits and progress updates, and permitted
continued work from the current branch ancestry. This authorizes the smallest
evidence-backed choice inside each existing backlog item's acceptance boundary.
It does not authorize a new roadmap item, later release scope, immutable tag,
or publication.

## Frozen Decisions

### `PKG-003`

- Emit migration schema `2.0.0` for v0.5.0.
- Represent clean-install operations separately from an ordered list of
  immutable source entries. Select an upgrade entry only by exact source version
  and source `files.yaml` digest; reject zero or multiple matches.
- Keep schema `1.0.0` read compatibility and deterministic operation rules.
- Support automatic v0.3.0, v0.4.0, and v0.4.1 sources in the original frozen
  matrix. Owner amendment on 2026-07-22 adds v0.4.2 as a required fourth exact
  automatic source; V050-009 owns the added candidate and evidence update.
- Preserve the existing v0.0.1 route: manually establish v0.3.0 provenance,
  then use the automatic v0.3.0-to-v0.5.0 path.

### `SAG-001`

- Dynamic canonical loading is the default.
- Keep `context-translator` as the only runtime-native role for Codex, Claude,
  and Copilot unless live runtime evidence proves another role needs native
  model, tool, permission, or invocation metadata.
- Add exact target-to-path metadata, canonical citation/import checks,
  distribution parity, and negative GWT fixtures.

### `ENF-001`

- Add a dedicated governance pull-request workflow for AI-context paths.
- Keep package candidate and publication workflows separately owned.
- Add deterministic semantic wrapper/adapter validation and a governed
  per-release published-path disposition artifact. No path is removed without
  migration and downstream evidence.

### `TOOL-001` And `VAL-001`

- Retain `check-all.sh` as the v0.5.0 orchestrator. Strengthen its manifest and
  formatting compatibility tests rather than rewriting the runner during a
  release blocker.
- Execute the same declared required set on Windows Git Bash and hosted Ubuntu.
  macOS remains explicitly unverified.
- Treat later Roslyn/configuration work as satisfying the repository-validation
  half of VAL-001.
- Replace the permanent dependency/version deferred placeholder with a
  deterministic consistency validator. Online freshness or vulnerability
  queries remain hosted/advisory because they are not reproducible offline.

### `LANG-001`

- English remains canonical for agent execution contracts and zh-TW remains
  derived for approved bilingual entries.
- The historical count of 21 high-priority candidates is stale. Current direct
  Markdown inventory finds one active English-standard punctuation defect
  (`Commit。`) and one intentional workflow-trigger line containing zh-TW
  examples.
- The v0.5.0 remediation batch is the punctuation defect plus any candidate
  produced by the deterministic refreshed inventory.
- Semantic evidence is hybrid: deterministic structure/path/identifier/code
  checks plus a retained context-translator or human review checklist. No model
  pass alone is an oracle.

### `GOV-001` And `CAP-001`

- Reconcile legacy follow-up markers without adding retrospective locators.
  Close markers already satisfied by later completed workflows and promote only
  genuinely current work.
- Do not create a terminology skill. Keep technical nouns under the existing
  domain-language/document pattern until a repeatable action workflow exists.

### `HANDOFF-001`

- Use one machine-readable `handoff.yaml` per checkpoint, validated against a
  repository-owned schema.
- Record repository, branch, commit, workflow, task, dirty state, exact next
  action, command, exit status, bounded output evidence, and execution
  provenance source.
- Treat provider-native author/signature/session evidence and local AI
  contribution trailers as compatible alternatives. Never rewrite a commit
  solely to normalize attribution.
- Require real Copilot CLI/cloud, Claude, and Codex fixtures before
  provider-specific validation.

### `REL-001`

- Store canonical release templates under a source template area and instantiate
  version records without prior-version values.
- Add an exact-command runbook, local pre-tag validator, and terminal-state
  validator. Public GitHub state is an optional hosted/API layer over
  deterministic local tag/registry/notes truth.
- Tag creation remains user-owned and is outside this development authorization.

## Execution Dependencies

1. `V050-002`: persist disposition gates.
2. Parallel foundation lanes: `V050-003`, `V050-004`, `V050-006`, `V050-007`.
3. `V050-005`: general enforcement and PR CI consumes foundation validators.
4. `V050-008` and `V050-009`: handoff and release mechanics integrate with
   enforcement.
5. `V050-010`: full deterministic gates, real extracted upgrades, hosted
   evidence, frozen subject commit, independent assessment, and release-ready
   reconciliation.

## Commit Checkpoints

- One commit for the bootstrap.
- One commit for inventory and task freeze.
- One commit for disposition gates.
- One or more commits per release blocker only at coherent green boundaries.
- Separate commits for hosted evidence, independent assessment, and final
  release-candidate reconciliation.
- Push or merge does not close the workflow. Publication requires separate user
  authorization.
