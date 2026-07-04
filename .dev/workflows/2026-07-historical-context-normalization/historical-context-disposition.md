# Historical Context Disposition

## Remove

These files describe a source product and are already covered by canonical guides, schemas, or templates:

- `.dev/requirement/distributed-commerce-bounded-context-overview.md`
- `.dev/specs/domains/`
- product-specific test specs under `.dev/specs/tests/product/`, `.dev/specs/tests/order/`, and `.dev/specs/tests/inventory-item/`
- `.dev/problem-frames/orders/`
- `.dev/problem-frames/payments/`
- `.dev/operations/context-map.md`
- `.dev/operations/event-catalog.md`
- `.dev/operations/mq-topology.md`
- `.dev/operations/runbooks/inventory-reservation-failure.md`
- `.dev/BUILDING-BLOCKS-CLASS-INDEX.MD`
- source-product `.dev/project-config.yaml`
- duplicate `.dev/standards/templates/project-config-template.yaml`

## Neutralize

Reusable guides and examples remain, but fixed credentials, ports, namespaces, project names, and source-product assumptions must become placeholders:

- `.dev/guides/implementation-guides/`
- `.dev/guides/learning-guides/`
- `.dev/guides/design-guides/`
- `.dev/standards/`
- `.ai/assets/tech-stacks/dotnet-backend/`

## Retain As Explicit Future Planning

- React / Vite is retained only in `.dev/guides/design-guides/MULTI-STACK-CONTEXT-PLACEMENT-NOTES.md`.
- No frontend runtime profile, implementation skill, or support commitment is created.

## Historical Workflow Exception

Completed workflow artifacts remain unchanged when old names are required for traceability. They are not active project truth.
