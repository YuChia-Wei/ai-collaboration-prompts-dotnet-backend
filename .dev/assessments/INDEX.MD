# Assessment Index

This index catalogs durable assessments. Each assessment's `assessment.yaml`
owns its identity, current lifecycle state, subject revision, and relationships.

## Draft Assessments

| Assessment | Title | Type | Owner | Status | Subject Commit | Updated | Report |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Final Assessments

| Assessment | Title | Type | Owner | Status | Subject Commit | Updated | Report |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`ASM-20260722-002`](ASM-20260722-002/assessment.yaml) | v0.5.0 Candidate Remediation Successor Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `d83f395e5a399f944cb53b87c1f95cd299a4c386` | `2026-07-22T08:29:59+08:00` | [report](ASM-20260722-002/report.md) |
| [`ASM-20260722-001`](ASM-20260722-001/assessment.yaml) | v0.5.0 Four-Source Release Candidate Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `ef148472bb2e47b058693a1ab5e28dcb99e5ba32` | `2026-07-22T08:04:18+08:00` | [report](ASM-20260722-001/report.md) |
| [`ASM-20260720-002`](ASM-20260720-002/assessment.yaml) | v0.4.2 Release Finalization Hotfix Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `895ce060b2287e6c6be6a5327496f6e763145891` | `2026-07-20T22:43:57+08:00` | [report](ASM-20260720-002/report.md) |
| [`ASM-20260720-001`](ASM-20260720-001/assessment.yaml) | v0.4.2 Publication Incident External Review Intake | `ai-context-audit` | `ai-context-auditor` | `final` | `71c41dbd9c4f2b65105a616d15b7f1cc9db2a338` | `2026-07-20T22:43:57+08:00` | [report](ASM-20260720-001/report.md) |
| [`ASM-20260719-001`](ASM-20260719-001/assessment.yaml) | v0.4.2 AI Context Remediation Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `51be197a9a46caf23438c98065fcca58c723ce99` | `2026-07-19T15:45:00+08:00` | [report](ASM-20260719-001/report.md) |
| [`ASM-20260718-001`](ASM-20260718-001/assessment.yaml) | v0.4.1 Package Upgrade And Downstream Gate Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `962919bfa15e7dba1f56e4a9741538d9caf1d7e6` | `2026-07-18T23:11:56+08:00` | [report](ASM-20260718-001/report.md) |
| [`ASM-20260717-004`](ASM-20260717-004/assessment.yaml) | AI context self-audit of v0.3.0 with verification of the 2026-07-07 informal review findings | `ai-context-audit` | `ai-context-auditor` | `final` | `82b88b7287deb7a64e0311fde6b1b53ea0d194b1` | `2026-07-18T14:53:16+08:00` | [report](ASM-20260717-004/report.md) |
| [`ASM-20260717-003`](ASM-20260717-003/assessment.yaml) | v0.4.0 AI Context Closeout Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `a13adec9bbc789c954ddd480cf3e115966eb963f` | `2026-07-17T07:39:43+08:00` | [report](ASM-20260717-003/report.md) |
| [`ASM-20260717-002`](ASM-20260717-002/assessment.yaml) | v0.4.0 AI Context Final Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `36c0add48129eff6bfa503b2244a45c4a802b5c5` | `2026-07-17T07:28:50+08:00` | [report](ASM-20260717-002/report.md) |
| [`ASM-20260717-001`](ASM-20260717-001/assessment.yaml) | v0.4.0 AI Context Successor Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `26c958069510f56818752368bec4bd7ad83e5038` | `2026-07-17T07:16:38+08:00` | [report](ASM-20260717-001/report.md) |
| [`ASM-20260716-001`](ASM-20260716-001/assessment.yaml) | v0.4.0 AI Context Remediation Verification | `ai-context-verification` | `ai-context-auditor` | `final` | `e7ca51a7f03c114d5ce5826a15eeb15338efea76` | `2026-07-16T23:10:20+08:00` | [report](ASM-20260716-001/report.md) |
| [`ASM-20260715-002`](ASM-20260715-002/assessment.yaml) | v0.4.0 Standards Lineage And Downstream Adoption Reassessment | `ai-context-audit` | `ai-context-auditor` | `final` | `82b88b7287deb7a64e0311fde6b1b53ea0d194b1` | `2026-07-15T23:43:06+08:00` | [report](ASM-20260715-002/report.md) |

## Superseded Or Withdrawn Assessments

| Assessment | Title | Type | Owner | Status | Subject Commit | Updated | Report |
| --- | --- | --- | --- | --- | --- | --- | --- |

| [`ASM-20260715-001`](ASM-20260715-001/assessment.yaml) | v0.4.0 Standards, Examples, And Script Usage Assessment | `ai-context-audit` | `ai-context-auditor` | `superseded` | `82b88b7287deb7a64e0311fde6b1b53ea0d194b1` | `2026-07-15T23:43:06+08:00` | [report](ASM-20260715-001/report.md) |

## Related Policies

- [Assessment artifact policy](../standards/ASSESSMENT-ARTIFACT-POLICY.md)
- [Workflow gate policy](../standards/WORKFLOW-GATE-POLICY.md)
- [Git commit policy](../standards/GIT-COMMIT-POLICY.md)
- [Durable backlog](../backlog/INDEX.MD)

## External Review Sources

External review packages retain the reviewer's original structure and wording.
They are evidence inputs, not repository-native assessments or normative truth.
Material findings become durable only after a repo-native assessment reproduces
them and assigns stable finding IDs. The normalized assessment keeps the raw
package under its `evidence/` directory so external reviewers do not need to
follow repository-owned assessment templates.

| Input | Source | Received | Normalized By | Status |
| --- | --- | --- | --- | --- |
| [`fable5-v0.4.2`](ASM-20260720-001/evidence/fable5-v0.4.2/README.md) | Claude Fable 5 | 2026-07-20 | [`ASM-20260720-001`](ASM-20260720-001/assessment.yaml) | `normalized` |
