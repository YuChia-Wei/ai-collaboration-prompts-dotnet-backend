# Deterministic EVAL Baseline Remediation Report

## Outcome

The bounded deterministic portion of `EVAL-001` is complete. The repository now
has a source-owned six-family corpus, exact expected outputs, a normalized
baseline and digest, a model-free runner, baseline/candidate comparison, and
fail-closed mutations for routing, approval, test closeout, copied source truth,
provenance, and identifier compatibility.

## Boundary

The runner consumes structured, preclassified facts and makes zero model or
network calls. `.ai/evaluation/**`, its runner, and its tests are source-only and
were proven absent from immutable ZIP and tar.gz payloads built from `b5137b2`.
The follow-up fix at `9807a77` changes only source-only fixtures and their oracle.

The model-in-the-loop portion remains unexecuted. It still requires owner
approval of the model, judge, repetitions, prompt/context inputs, sampling,
token ceiling, threshold, retention, and failure disposition. Therefore
`EVAL-001` remains planned and `SKILL-001` activation remains gated.

## Verification

- `test_ai_behavior_evaluation.py`: 10 passed.
- Complete deterministic corpus: 6 cases, zero model calls.
- Shell asset parity and AI-context validation: passed.
- Aggregate runner fail-closed regression: 27 passed.
- Immutable ZIP/tar.gz validation: passed; source-only EVAL entries found: 0.
- Independent review identified two coverage-strength gaps; both were addressed
  in `9807a77` by using lifecycle placeholders and explicitly rejecting copied
  source truth.
