# Deterministic AI Behavior Evaluation

This directory owns the model-free behavioral regression corpus used by the
aggregate repository gate. The corpus consumes structured, preclassified facts;
it does not interpret natural language and it never calls a model, judge, or
network service.

Run the complete corpus and exact oracle:

```text
python .ai/scripts/validate-ai-behavior-evaluation.py validate
```

Write a normalized candidate result and compare it with the checked-in
baseline:

```text
python .ai/scripts/validate-ai-behavior-evaluation.py run --output candidate.yaml
python .ai/scripts/validate-ai-behavior-evaluation.py compare \
  --baseline .ai/evaluation/baselines/v1.yaml \
  --candidate candidate.yaml
```

The six fixture families cover empty, existing, and copied-template repository
initialization; software-development orchestration; customization-aware
upgrades; and identifier compatibility. Exact outputs are checked in under
`expected/`. Tests mutate the structured inputs to prove that missing routes,
unauthorized implementation, false test success, source-truth leakage, dual
provenance, and silent compatibility removal fail closed.

Package-facing references use placeholders such as
`.dev/workflows/<workflow-id>/workflow.yaml`. Source workflow, assessment,
release, and backlog instances are not evaluation inputs and must not be
embedded in distributed corpus files.

Model-in-the-loop evaluation remains a separately approved release-side
activity. Model and judge selection, repetitions, sampling, thresholds, token
budgets, and stochastic result retention are intentionally outside this
deterministic contract.
