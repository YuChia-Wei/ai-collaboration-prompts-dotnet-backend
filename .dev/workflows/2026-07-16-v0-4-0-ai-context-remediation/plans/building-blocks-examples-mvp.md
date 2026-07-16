# BuildingBlocks And Examples Reconstruction Contract MVP

## Purpose

Demonstrate that v0.4.0 preserves enough architecture and software-engineering knowledge to reconstruct an equivalent .NET backend structure without turning this AI context repository into a product implementation, source template, or BuildingBlocks package.

The six review gates were approved on 2026-07-16 with the conditions recorded below. The first remediation slice is authorized; later slices remain governed by their task boundaries and validation gates.

## Repository Identity Decision

Do not add a complete BuildingBlocks plus SampleProduct solution under `tools/` or another framework-owned directory.

This repository owns:

- architecture invariants, rationale, terminology, and technology-selection boundaries;
- project-structure and dependency-direction blueprints;
- portable port and contract semantics;
- focused illustrative snippets whose evidence tier is explicit;
- analyzers, validators, and their minimal test inputs under `tools/**`;
- skills and routing that select the smallest relevant knowledge set.

This repository does not currently own:

- a production-ready BuildingBlocks implementation;
- a complete reference product or golden application;
- persistence, broker, observability, or other target adapter implementations;
- byte-for-byte reconstruction of one historical lab;
- a distributable `dotnet new` template or NuGet package.

The reconstruction goal is architectural equivalence, not identical source code. A target is equivalent when it preserves the documented bounded-context grammar, dependency direction, ports/adapters ownership, Aggregate and Repository semantics, deletion policy, CQRS/MQ boundaries, and selected technology profile.

## Provenance And Interpretation

The user supplied the following repository lineage:

1. `ai-coding-exercise` was the original source, with commit `f7ed0b9b5b23822ec012c375261df44f6f03a97f` representing the earliest Java version.
2. Initial .NET standards were extracted from that source and applied to `dotnet-mq-arch-lab`.
3. `dotnet-mq-arch-lab` was then used to refine the desired .NET architecture and standards.
4. This AI context repository was created from that refined knowledge, after removing the product implementation, and has since evolved independently.

Consequences for v0.4.0:

- Java, EzDDD, and `Lab.*` literals are migration-provenance signals, not automatic deletion evidence.
- A historical name may remain only when it is explicitly classified as historical/reference material or replaced by a portable placeholder in active canonical guidance.
- `dotnet-mq-arch-lab` is useful adoption and architecture evidence, but its source code is not canonical truth for this repository.
- Current standards must express the surviving concept without requiring access to either historical repository.

## Minimal BuildingBlocks Contract

BuildingBlocks should default to interfaces and semantic contracts rather than shared inheritance:

- `IDomainEntity<TId>` only if entity identity needs a reusable contract;
- `IAggregateRoot<TId>`;
- `IDomainEvent`;
- `IAggregateRepository<TAggregate,TId>` with `FindByIdAsync` and `SaveAsync`;
- read-only query port semantics, without a public generic writable CRUD repository;
- integration-event and publisher port semantics when the selected profile uses integration messaging.

Product Domain and Application own product behavior. Product Infrastructure owns persistence, broker, observability, and other outbound adapter implementations.

### Base-Class Minimization

The default reconstruction contract must not require `DomainEntity<TId>`, `AggregateRoot<TId>`, or `ValueObject` base classes:

- entities may implement identity directly;
- normal Aggregate roots may implement `IAggregateRoot<TId>` directly;
- value objects should prefer immutable C# records and product-owned equality semantics;
- shared test base classes remain prohibited.

`EsAggregateRoot<TId>` is the only approved optional abstract base class because event replay, pending-event tracking, `Apply/When`, and committed-version handling are stable mechanical behavior that is costly to reimplement incorrectly.

The approved option B has three conditions:

1. The abstraction is `executable-tested` with focused pure-logic tests for replay, pending events, transition dispatch, and committed-version behavior.
2. The behavior contract is documented independently so a target may reimplement it instead of copying the supplied abstraction.
3. Until a package distribution path is approved, a source-included copy becomes target-owned. Upgrade reconciliation uses `ai-context-upgrader` three-way comparison and the v0.4.0 file-disposition manifest.

No other abstract base class enters the v0.4.0 default profile without separate evidence and user approval.

Standards, examples, and `DBA1009` must recognize the same `EsAggregateRoot` shape. A rule that cannot recognize the documented descendant type is not considered enforced.

## Reconstruction Evidence Matrix

Each architecture capability selected for v0.4.0 must have all applicable evidence columns completed. Every equivalence criterion maps to either a deterministic check or an explicit review checklist item:

| Capability | Normative rule | Rationale | Minimal illustration | Validator/analyzer | Downstream evidence |
| --- | --- | --- | --- | --- | --- |
| Project/layer grammar | required | required | optional | structural check plus profile checklist | compare both lab profiles |
| Aggregate and Repository | required | required | focused snippet | analyzer plus review checklist | compare `dotnet-mq-arch-lab` |
| Soft delete and purge | required | required | focused use-case flow | ownership/projection check plus target opt-out evidence | target-specific review |
| CQRS and MQ boundaries | required | required | focused flow | dependency/routing checks plus review checklist | compare adopted repositories |
| Technology selection | required | required | profile example | generic selection/override schema validation | target override evidence |
| BuildingBlocks contracts | required | required | signatures only | API-name/relationship checks plus ES behavior tests | downstream implementations |

A capability is not considered reconstructable merely because a class name appears in an index. The rule, ownership boundary, and navigation path must be sufficient for an agent working without the historical repositories.

## Example And Test Contract

| Tier | Contains implementation | Test requirement | Allowed claim |
| --- | --- | --- | --- |
| `executable-tested` | yes | build plus focused tests required | verified executable reference |
| `structure-validated` | partial/configuration | deterministic structural validator required | structure validated only |
| `illustrative` | optional snippets | no test required | illustrative; not copy-ready |
| `reference-only` | no required implementation | no test required | conceptual/reference guidance |
| `historical` | legacy provenance | no test required | history/migration only |

Do not create an executable architecture fixture solely to populate the first tier. Existing code examples may be promoted individually only when they have a real build/test route. Analyzer and validator tests may use minimal inline C# inputs to prove one rule without becoming a reference product.

Tier declarations must be machine-readable through frontmatter or a manifest:

- `structure-validated` names the exact validator that supplies its evidence;
- `executable-tested` names its build/test route;
- unclassified legacy material defaults to `historical` or `illustrative`;
- no validator or migration may promote an unclassified item by inference.

## Proposed MVP Work

1. Create an EzDDD/Java/lab-to-current-concept disposition matrix.
2. Reduce the conceptual BuildingBlocks index to interfaces, semantic contracts, conditional target technologies, and clearly labeled historical references.
3. Document and executable-test the optional `EsAggregateRoot<TId>` abstraction under the approved conditions; reject implicit base-class requirements elsewhere.
4. Create a compact reconstruction blueprint for micro-system and mono-system project profiles.
5. Define the five evidence tiers and reclassify existing examples before deleting or promoting them.
6. Add or strengthen analyzers/validators only for deterministic rules; keep their test inputs minimal and focused.
7. Compare the resulting knowledge against `dotnet-mq-arch-lab` and `dotnet-webapi-lab` as read-only downstream evidence.
8. Maintain the workflow file-disposition manifest with `kept`, `moved-to`, `merged-into`, and `retired` outcomes for upgrader and migration-guide consumption.
9. Use the independent verification assessment to judge whether an agent can navigate and reconstruct the architecture without copying either lab.

## Approved Review Gates

1. Approved: remove the committed architecture-fixture proposal.
2. Approved: contracts/interfaces are the default BuildingBlocks form.
3. Approved: optional `EsAggregateRoot<TId>` option B with executable tests, an independent behavior contract, and source-copy/upgrader ownership rules.
4. Approved: architectural equivalence is the reconstruction target, with one deterministic check or review checklist item per criterion.
5. Approved: use five machine-readable evidence tiers with explicit validator identity and default-downward legacy classification.
6. Approved: begin with `AIC-004` and `AIC-012`; create the file-disposition manifest before remediation and complete release/migration integration before `ROUTE-001`.

## Deferred

- executable clean-room reconstruction exercise;
- `dotnet new` template packaging;
- BuildingBlocks or analyzer NuGet packaging/versioning;
- production-ready EF Core, Dapper, Wolverine, broker, or observability adapters;
- full example portfolio conversion;
- product remediation in either downstream lab.
