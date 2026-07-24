# v0.6.0 Terra Model-In-The-Loop Evaluation Report

## Result

The approved model-in-the-loop threshold passed.

| Measure | Required | Observed |
| --- | ---: | ---: |
| Critical safety | 8/8 | 8/8 |
| Full rubric | at least 7/8 | 8/8 |
| Candidate repetitions | 2 | 2 |
| Independent judgments | 1 | 1 |

The judge recommends activation. This result clears only the EVAL-001 model
gate; SKILL-001 must still activate both identifiers atomically and validate
the compatibility contract.

## Configuration

- Evaluation ID: `EVAL-001-terra-v0.6.0`
- Candidate model: `gpt-5.6-terra`
- Candidate reasoning: medium
- Candidate repetitions: 2 fresh runs
- Judge model: `gpt-5.6-terra`
- Judge reasoning: high
- Judge repetitions: 1 fresh independent run
- Cases: empty repository initialization, customization-aware upgrade,
  software-development orchestration, and identifier compatibility
- Candidate isolation: deterministic expected outputs, baselines, mutants, and
  the other candidate output were unavailable to candidates
- Generated-output ceiling: 4,000 tokens per call, 12,000 tokens aggregate
- Failure disposition: keep both candidate identifiers inactive and retain
  failed evidence for a later approved rerun

## Retained Evidence

| Artifact | SHA-256 | Bytes | Whitespace-delimited words |
| --- | --- | ---: | ---: |
| `evidence/terra-candidate-a.yaml` | `7b5a952fcdd38b104ecbebd8018b0acbc7c31db85a10ef4f6a179304c0d9fd8a` | 8,623 | 574 |
| `evidence/terra-candidate-b.yaml` | `78c81bbdb124a380b7c5243c6398e28081cc87a28fc55a82df12020e093459d5` | 8,672 | 592 |
| `evidence/terra-judge.yaml` | `863bbe93af16fca2674366ab5aa078182035bca632c41d6bd5111236b8538dd3` | 4,968 | 535 |

Provider-reported prompt and completion token telemetry was unavailable. The
recorded byte and word counts prove the retained artifact envelope only; they
are not represented as token counts. Each model call received the approved
4,000-generated-token ceiling in its evaluation instruction and returned one
complete bounded YAML result.

## Judgment Summary

Both candidates:

- selected the currently active `repo-structure-sync` and `dev-workflow`
  identifiers while the transition remained inactive;
- identified the future `ai-context-init` and
  `software-development-orchestrator` routes after atomic activation;
- preserved explicit approval pauses, target-owned enterprise test policy,
  blocked integration-test status, and historical identifiers;
- required governance reconciliation and validation before provenance writes;
- retained deprecated compatibility entries without inventing a removal date.

The independent judge found no critical or full-rubric failure across the eight
run/case records.

## Residual Risk And Handoff

- Stochastic evaluation does not replace deterministic regression; both gates
  remain required.
- Activation must not expose only one new identifier or rewrite historical
  workflow, task, assessment, release, provenance, `initialized_by`, or
  `generatedBy` values.
- Legacy identifiers remain thin deprecated compatibility entries with no
  scheduled removal release.

The next authorized action is the governed atomic SKILL-001 activation.
