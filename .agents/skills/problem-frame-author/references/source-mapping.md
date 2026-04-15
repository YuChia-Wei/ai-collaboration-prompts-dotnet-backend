# Source Mapping

Use requirement/spec files as the primary truth.
Use code/tests only to recover missing details or expose mismatches.

Map sources into:

- `frame.yaml`: business boundary, external facts, frame concerns
- `machine/machine.yaml`: processing steps, error mapping, constraint enforcement
- `machine/use-case.yaml`: inputs, preconditions, postconditions, outputs
- `aggregate.yaml`: contracts, invariants, events, semantics
- `acceptance.yaml`: scenarios, traces, test anchors
