# V050-010 Hosted Candidate Evidence

- Workflow: `2026-07-21-v0-5-0-development`
- Task: `V050-010`
- Candidate head before correction: `073829ff5c947084fc2625893d43fb8d1fd8825f`
- Evidence updated: `2026-07-22T08:09:41+08:00`

## Initial hosted result

Draft PR `#1` started package-candidate run `29878332021`. Checkout, Python
setup, dependency installation, release-body rendering, and release-registry
validation passed. The exact candidate-state step then failed with:

```text
AI context release-state validation failed: candidate validation requires a clean source worktree
```

The failure was workflow-generated. The preceding render step wrote
`dist/release-body.md` inside the checked-out source tree, so the workflow made
its own worktree dirty before enforcing the clean-source invariant.

## Correction

The candidate workflow now renders the release body to
`${RUNNER_TEMP}/release-body.md` and uploads that exact temporary artifact.
The validator remains strict; no dirty-state exception or ignored path was
introduced. `ReleaseWorkflowContractGwtTests.test_gwt_007` asserts both the
temporary output route and absence of the prior `dist` render destination.

## Corrected hosted result

Candidate `ef148472bb2e47b058693a1ab5e28dcb99e5ba32` passed all three draft PR
checks after the correction:

- package candidate run `29878635973` passed in 27 seconds;
- governance run `29878635862` passed in 10 seconds;
- Ubuntu quick-gate run `29878635890` passed in 1 minute 35 seconds.

Independent assessment `ASM-20260722-001` confirms the runtime and package
mechanics but blocks release-readiness on stale discovery, resume/handoff, and
backlog lifecycle wording. V050-010 owns remediation and successor verification.
