# D1-D12 Decision Difference Analysis

## Metadata

- Workflow: `2026-07-usecase-command-handler-boundary`
- Stage: `S1 - Resolve architecture decisions`
- Status: resolved
- Compared sources:
  - user decisions supplied on `2026-07-06`;
  - attached discussion, `.NET 專案中 API Controller、Command Handler、Use Case 分工準則`;
  - current proposals in [workflow-plan.md](./workflow-plan.md).

## Decision Classification

| Decision | Classification | Analysis |
| --- | --- | --- |
| D1 | Conflict | The new decision makes a dedicated Use Case input the default, permits a genuinely input-free operation, mandates `ExecuteAsync`, and mandates a `CancellationToken`. The attachment's primary code examples pass `Guid` directly and do not make dedicated input universal, although its project structure and Rule 7 support a distinct Use Case input. The attachment is internally mixed on this point. |
| D2 | Aligned | Both directions separate HTTP request DTOs and message Commands from a transport-neutral Use Case input. The attachment's early primitive-argument examples are inconsistent examples, not its final Rule 7. |
| D3 | Aligned | The attachment says a Web API does not need a Command/Handler unless a real dispatch or message-driven entry exists. This matches option 1. |
| D4 | Conflict | The attachment prohibits Controller repository operations and says a Controller calls one Use Case. The new decision permits direct query repository or query service calls as an explicit, discouraged exception. |
| D5 | Conflict by extension | The attachment does not establish a query-specific exception and its general Controller rule excludes repository access. The new decision deliberately allows the same discouraged direct-query exception on the query side. |
| D6 | Incomplete / placement ambiguity | The attachment clearly defines a Command Handler as an inbound adapter and places an example Handler under `Application/Commands`. It does not resolve where a Wolverine-specific, MQ consumer, or other framework-coupled Handler belongs. The workflow proposal distinguishes package-neutral Application handlers from framework/transport adapters. |
| D7 | Aligned with wording constraint | Both directions reject HTTP/MQ response contracts from Use Cases. The new wording should mean: return only a transport-neutral output produced by the completed operation; use `Task` when no output object exists. It should not force an artificial output object for every operation. |
| D8 | Aligned | The attachment assigns orchestration, persistence, transaction control, and event publication to the Use Case rather than the Handler. |
| D9 | Aligned for naming; existing terminology remains | `*UseCase` is the selected implementation suffix. The attachment and the current relationship standard already mention Application Service as a possible supporting abstraction. This workflow should not expand or redefine that term; removal or redesign is outside D9 unless separately requested. |
| D10 | User-deferred | Migration mechanics will not be standardized in this stage. Concrete migration direction belongs to a later product refactor task. |
| D11 | Aligned by absence | The attachment contains no analyzer plan, so the workflow recommendation applies: deterministic boundary violations are errors; naming and migration advisories remain warnings where reliable target evidence is unavailable. |
| D12 | Conflict | The attachment puts `IIntegrationEventPublisher` behind an outbound port and describes Wolverine/message bus primarily as delivery or dispatch infrastructure. The new decision permits a Use Case to depend directly on Wolverine `IMessageBus` to publish events, while strictly prohibiting command publication and Use Case-to-Use Case invocation. |

## Material Tradeoffs Requiring Redecision

### R1 — D1 input shape

Candidate A — apply the new decision:

- `ExecuteAsync` is mandatory;
- a dedicated, transport-neutral input type is the default;
- a genuinely input-free Use Case may omit the input parameter;
- every asynchronous signature includes a non-optional `CancellationToken`
  parameter;
- primitive arguments shown in the attachment become non-canonical examples.

Candidate B — retain the attachment's looser examples:

- dedicated input types are recommended when mapping or boundary separation needs
  them;
- simple primitive arguments remain canonical for small Use Cases.

Architecture recommendation: Candidate A. It gives analyzers and generators one
deterministic boundary and prevents transport contracts from gradually becoming
Use Case parameters.

### R2 — D4/D5 direct query exception

Candidate A — apply the new decision:

- command-style Controllers depend on Use Cases;
- query Controllers should also depend on query Use Cases;
- direct `IQueryRepository` or query service injection is allowed only as a
  documented, discouraged exception;
- the exception accepts tighter Controller/read-model coupling, inconsistent
  inbound-port enforcement, and possible future migration cost.

Candidate B — retain the attachment's strict adapter rule:

- every Controller calls a Use Case;
- repositories and query services are never Controller dependencies.

Architecture recommendation: Candidate A only if the repository intentionally
values low-ceremony read endpoints over strict inbound-port symmetry. The
exception must be explicit enough that analyzers do not silently normalize it.

### R3 — D6 framework-specific Handler placement

Candidate A — use the workflow proposal:

- package-neutral convention handlers may remain in Application;
- Wolverine/MediatR-specific handlers, MQ consumers, and transport-coupled
  handlers belong to an inbound adapter or composition boundary;
- a Handler that references only an Application contract may be hosted beside the
  adapter without moving Use Case orchestration out of Application.

Candidate B — use the attachment's sample structure for all Command Handlers:

- place Handlers under `Application/Commands`, including framework-discovered
  handlers;
- accept framework convention or package coupling in Application.

Architecture recommendation: Candidate A. It preserves the attachment's
Handler-as-adapter role without making a runtime package part of the portable Use
Case boundary.

### R4 — D12 direct Wolverine event publication

Candidate A — apply the new decision:

- Use Cases may inject Wolverine `IMessageBus`;
- event publication APIs are allowed;
- sending, invoking, or publishing Commands is prohibited;
- injecting another Use Case is prohibited;
- Wolverine becomes an intentional Application-layer package dependency;
- analyzer and review rules must distinguish events from Commands and verify
  transaction/outbox semantics.

Candidate B — retain the attachment's outbound-port model:

- Use Cases inject a project-owned event publisher port;
- Infrastructure adapts that port to Wolverine;
- Application remains portable and command/event API misuse is harder.

Architecture recommendation: Candidate A is coherent with the stated decision not
to maintain a project-owned event-bus abstraction, but it is a deliberate
exception to the package-neutral Application rule. Domain events should still be
raised by Domain objects; the Use Case may coordinate their dispatch after the
Domain operation. Integration event publication must remain consistent with the
selected transaction/outbox policy.

## Non-conflicting Decisions Ready to Record

The following can be recorded after the material conflicts are resolved:

- D2: dedicated transport-neutral Use Case input, separate from HTTP and command
  contracts;
- D3: Handler exists only for an actual dispatch/message entry;
- D7: transport-neutral output only, with no artificial output required;
- D8: Use Case owns transaction and event lifecycle coordination;
- D9: concrete implementation uses the `*UseCase` suffix, without redefining
  Application Service;
- D10: migration guidance deferred to product refactor work;
- D11: recommended analyzer severity model applies.

## Gate

R1-R4 received explicit user decisions on `2026-07-07`:

- R1: Candidate A, with the additional exception that exactly one standard-type
  scalar input value may be passed directly; collections, tuples, custom input
  types, and multiple values still require a dedicated input object;
- R2: Candidate A, restricted to explicitly selected pure-query endpoints; all
  other endpoints use a Use Case by default;
- R3: Candidate A;
- R4: Candidate B.

The architecture decision gate is passed. Canonical standards, prompts, examples,
and analyzers may proceed in later workflow stages.
