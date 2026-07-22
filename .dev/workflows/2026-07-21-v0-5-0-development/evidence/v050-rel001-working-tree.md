# REL-001 Working-Tree Validation Evidence

## Evidence Metadata

- Workflow: `2026-07-21-v0-5-0-development`
- Task: `V050-009`
- Backlog item: `REL-001`
- Mechanics commit: `2ecf832637558020a1d792ceb64c5cc15add29e8`
- Evidence state: mechanics committed; validated-candidate state pending commit
- Verified at: `2026-07-22T07:41:44+08:00`

## Implemented Contract

The working tree contains:

- placeholder-only release publication templates;
- four exact sanctioned phase commands;
- a fail-closed local and hosted release-state validator whose hosted commands
  are read-only;
- an owner-only pre-tag preparation interface;
- a cold-start publication runbook;
- migration schema 2.0 multi-source release-body rendering;
- source, candidate, tag-publication, and finalization CI routing;
- a planned v0.5.0 record, authored release notes, and migration guide.

The candidate source intentionally keeps tag, commit, run, URL, and publication
timestamps null. Generated provenance belongs only to rendered output. By the
owner's 2026-07-22 amendment, the exact automatic migration sources are v0.3.0,
v0.4.0, v0.4.1, and v0.4.2. The real four-source fixture passes, including a
v0.4.2-to-v0.5.0 dry-run/apply from the immutable tagged inventory.

## Local Validation

Environment:

- Git for Windows `2.54.0.windows.1`;
- Git Bash `5.3.9(1)-release`;
- Python `3.13.14`;
- .NET SDK `10.0.302`.

Passed commands:

- `python .ai/scripts/tests/test_ai_context_release_state.py -v` — 15/15;
- `python .ai/scripts/tests/test_prepare_ai_context_release.py -v` — 4/4;
- `python .ai/scripts/tests/test_release_notes_renderer.py -v` — 3/3;
- `python .ai/scripts/tests/test_ai_context_packaging.py -v VersionedMigrationPackagingGwtTests.test_gwt_017_given_four_real_supported_sources_when_one_v050_candidate_is_built_then_each_upgrades_without_overwriting_target_truth` — 1/1 in 240.554 seconds;
- `python .ai/scripts/tests/test_governance_workflow_contract.py -v` — 6/6;
- `python .ai/scripts/validate-ai-context-versions.py` — 8 records;
- `python .ai/scripts/validate-workflow-artifacts.py --workflow-id 2026-07-21-v0-5-0-development`;
- `python .ai/scripts/validate-ai-context.py`;
- `C:\Program Files\Git\bin\bash.exe ./.ai/scripts/check-all.sh --critical` — 33/33 required checks passed, 0 failed, 0 deferred;
- `git diff --check`.

The critical gate includes the complete AI-context packaging GWT suite, .NET
tests, governance enforcement, dependency/version consistency, handoff
registry, shell assets, and the three new release test suites.

Four-source candidate-mode rendering completed to a temporary file with
SHA-256 `A2FDD00E121BC741AEF823128A94B1D84595E3D0DB13EC80505F3BA1AE5D52B0`.
The authored candidate directory contains no generated automation marker,
rendered provenance heading, placeholder token, `TODO`, or `TBD`.

## Non-Claims And Resume Boundary

The mechanics and expanded planned sources are committed at `2ecf832`. Two
independent builds from that immutable commit produced byte-identical ZIP,
tar.gz, and sidecars and both archive pairs passed validation. The containing
validated-candidate state commit still requires its exact clean-state gate,
deterministic rebuild, hosted PR gates, and independent release-readiness
assessment.

Resume in this order:

1. review and commit the REL mechanics and planned candidate checkpoints;
2. build twice from the immutable candidate commit and compare artifacts;
3. run the exact clean-state candidate command and retain its evidence;
4. push and require green hosted governance, portable, and candidate jobs;
5. freeze the verified subject for `V050-010` independent assessment;
6. change the release record to `validated` only when those gates pass.
