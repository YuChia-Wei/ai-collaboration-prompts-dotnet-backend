# .NET Backend Architecture and Coding Standards

This folder owns normative framework and repository standards. Reusable `.ai`
documents load concise projections of these rules for agents; they do not become
independent normative owners.

DDD / Clean Architecture / CQRS boundaries are normative. Database, ORM, event store, message broker, test package, and runtime versions are selected by each target repository from file-backed evidence.

EF Core, Dapper, Npgsql, WolverineFx, RabbitMQ, Kafka, and mocking-library documents are conditional/reference guidance unless target repository configuration explicitly adopts them. Technology choices use the generic target selection mechanism in `TECHNOLOGY-SELECTION-POLICY.md`. For tests, Given-When-Then is the framework-wide minimum and Arrange-Act-Assert is not an allowed substitute. xUnit + BDDfy is the default; a target team may explicitly decline BDDfy, but its C# tests must still preserve GWT structure. NSubstitute is the default mocking selection and may be explicitly replaced. Gherkin `.feature` files and their runners remain optional.

## Navigation

Use [INDEX.MD](INDEX.MD) for the standards catalog. Use this README for
purpose, normative boundaries, and placement guidance.

Operational guides, setup walkthroughs, FAQs, and troubleshooting documents have moved to `.dev/guides/`.

## Belongs Here

- normative documents
- checklist
- anti-pattern / best-practice
- conditional target project structure profiles with clearly separated invariants and examples
- stable standards entry points intended for long-term reference
- AI context governance, commit policy, and workflow gate policy

## Do Not Put Here

- setup guide
- quick start walkthrough
- FAQ
- troubleshooting / solution note
- one-off refactoring proposals or work records
- AI skill/prompt/workflow guide

Place these materials in the appropriate locations:

- `.dev/guides/implementation-guides/`
- `.dev/guides/design-guides/`
- `.dev/guides/learning-guides/`
- `.dev/guides/ai-collaboration-guides/`
- `.dev/workflows/`

## Notes
- ezDDD/ezSpec concepts must be preserved even without direct .NET packages.
- If no .NET equivalent exists, keep the rule and mark TODO rather than deleting it.
- `standards/` should not accumulate setup guides, troubleshooting guides, or FAQ-style documents.
