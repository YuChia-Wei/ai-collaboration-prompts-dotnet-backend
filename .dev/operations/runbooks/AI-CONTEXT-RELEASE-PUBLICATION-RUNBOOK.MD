# AI Context Release Publication Runbook

## Trigger

當已核准的 governed framework release 已完成實作，需要從冷啟動環境建立候選、合併、由 owner 建立 immutable annotated tag、GitHub Actions 發布，並完成本機 registry 收尾時使用本文件。

不要用於補改既有 published tag、搬移 tag 或複製舊 release 目錄。任何 tag 的建立、移動、重建與刪除都不屬於 automation 或 agent 的權限。

## Scope And Source Of Truth

- 新版本一律從 [canonical release-publication templates](../../../.ai/assets/skills/ai-context-governance/templates/release-publication/) instantiate；不得複製 `.dev/releases/v*` instance。
- `release.yaml`、`release-notes.md`、`migration-guide.md` 是 candidate 的 source of truth。`release-notes.md` 不得包含 renderer 的 automation marker 或 provenance block。
- [`release-phase-checks.yaml`](../../releases/release-phase-checks.yaml) 的 command 是 handoff 可比對的 sanctioned command；不可包進 shell substitution 或任意 command。
- 本 runbook 固定適用本次 `v0.5.0` release contract。下一個版本必須新增其 own phase contract，而不是修改本次已記錄的 command。

## Cold-Start Candidate

1. Instantiate the five template artifacts into the active workflow and `.dev/releases/v0.5.0/`; resolve every `<...>` placeholder with current observed values: release record, authored notes, migration guide, workflow locator, and release task.

2. Run:

   ```powershell
   python .ai/scripts/validate-ai-context-release-state.py --phase candidate --version v0.5.0
   ```

   Expected result: exit `0`, a governed `validated` candidate, complete authored artifacts, and no stale copied values.

   Fail action: do not merge, tag, or publish. Correct only the candidate artifact or its validation evidence, then rerun the same command.

3. Run the repository critical gate and record its exact output in the workflow evidence:

   ```powershell
   bash .ai/scripts/check-all.sh --critical
   ```

   Expected result: exit `0` and no required failed check.

   Fail action: remain on the owning remediation task. Do not mark the release record `validated`.

## Merge And Pre-Tag Gate

1. Merge the release workflow into `main` with the approved strategy. Re-open the merged checkout; do not create a tag from a workflow branch.

2. Run:

   ```powershell
   python .ai/scripts/prepare-ai-context-release.py --version v0.5.0
   ```

   Expected result: exit `0`, clean worktree, exact validated candidate identity, and the critical gate evidence required for user tag creation.

   Fail action: do not request a tag. Repair the indicated registry, candidate, branch, or gate problem; make a new reviewed checkpoint and repeat from the candidate phase.

## Owner-Created Annotated Tag

The repository owner—not an agent, script, or GitHub workflow—creates and pushes
the annotated `v0.5.0` tag only after the pre-tag preparation command passes.
Use the complete command printed by `prepare-ai-context-release.py`; it pins the
validated commit, summarizes compatibility, and takes the `AI-Model` value from
the latest registered handoff checkpoint.

After the owner has created and pushed the tag, first run:

```powershell
python .ai/scripts/validate-ai-context-release-state.py --phase tag --version v0.5.0
```

Expected result: exit `0`; the tag is annotated, peels to the current validated
commit, and the tagged tree contains the `validated` registry skeleton.

Fail action: do not move, recreate, delete, or replace the tag. Preserve
evidence and escalate the mismatch to the owner.

Then run:

```powershell
python .ai/scripts/validate-ai-context-release-state.py --phase publication --version v0.5.0 --hosted
```

Expected result: exit `0`; the public release, exact rendered body, four governed
assets, and successful tag-triggered workflow match the immutable tag.

Fail action: do not move, recreate, delete, or replace the tag. Preserve evidence and escalate the mismatch to the owner.

## Hosted Publication

The tag push triggers `.github/workflows/publish-release.yml`. That workflow validates the tag, renders the public body, builds deterministic archives, and creates or resumes only its owned draft release. It never creates, selects, or moves a tag.

Expected result: the hosted workflow completes successfully; the GitHub Release is stable/non-draft with exactly the ZIP, tar.gz, and adjacent checksum assets produced from the tagged tree.

Fail action: retain the GitHub Actions run URL and logs, then repair the source workflow on a new branch. Do not mutate an unowned draft or a published release merely to hide a failure.

## Local Registry Finalization

After hosted publication evidence is available, record only observed tag, commit, timestamp, run, asset, and release URL facts in the governed release record. Keep generated marker/provenance material out of authored notes.

Run:

```powershell
python .ai/scripts/validate-ai-context-release-state.py --phase finalization --version v0.5.0 --hosted
```

Expected result: exit `0`; the published registry record equals the immutable tag peel, authored notes remain renderer-free, and required terminal evidence is present.

Fail action: do not alter the tag. Correct a factual registry omission through the governed finalization workflow, retain the publication evidence, and rerun the command.

## Terminal Checks

Run these read-only checks before declaring the release closed:

```powershell
python .ai/scripts/validate-ai-context-release-state.py --phase finalization --version v0.5.0 --hosted
python .ai/scripts/validate-ai-context-versions.py
git status --short
```

Expected result: both Python commands exit `0`; `git status --short` is empty after the finalization checkpoint is committed.

Fail action: the release is not closed. Record the failed command and output in the workflow, then resume only the task that owns the failed condition.
