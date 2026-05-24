# Migration Boundaries

Use these rules when this collaboration framework has been copied into a target repository and the target repo's local truth must replace copied template truth.

This is a repo init boundary. `repo-structure-sync` should normally be the first skill run after the framework is copied into an existing repo or an empty new repo.

## Keep Framework-Level Materials

Usually keep these areas as reusable collaboration structure:

- `.ai/` canonical agent assets, scripts, shared rules, sub-agent definitions, and templates
- `.dev/guides/` human-facing guides and skill usage guides
- `.dev/standards/` structure rules, code review checklist, examples, and organization principles
- `.dev/adr/` governance files: `README.md`, `INDEX.md`, `ADR-TEMPLATE.md`, and `WHEN-TO-CREATE-ADR.MD`
- `.dev/workflows/README.MD` workflow artifact contract
- `agents.md` collaboration baseline
- root README template shape, while rewriting repository identity and product-specific sections

## Rewrite From Target Repo Evidence

Do not carry these over as project truth. Rebuild them from the target repository's file tree, solution files, project files, package references, infrastructure config, and confirmed local docs:

- `.dev/ARCHITECTURE.MD`
- `.dev/project-config.yaml`
- `.dev/requirement/TECH-STACK-REQUIREMENTS.MD`
- bounded-context requirements and project-specific non-functional requirements
- `.dev/specs/domains/`
- `.dev/specs/tests/`
- `.dev/operations/context-map.md`
- `.dev/operations/event-catalog.md`
- `.dev/operations/mq-topology.md`
- `.dev/operations/runbooks/*.md`
- project-specific ADR files such as `ADR-*.md`
- root `README.md` and `README.en.md` sections that describe product identity, runtime services, API endpoints, setup commands, or repository layout

## Clean Up Copied Artifacts

Remove copied artifacts that describe old work rather than reusable process:

- completed `.dev/workflows/<workflow-id>/` plans, task files, and review reports
- files tied directly to the source repo's bounded contexts, event names, queue names, service names, routes, aggregates, or deployment reality
- script wrappers or validation rules that no longer match the target repo structure
- root README content tied to the source repository's product, domains, hosts, endpoints, package versions, or setup commands

## Empty Repository Rule

When the target repo is empty or near-empty:

- keep framework-level AI collaboration rules;
- keep `agents.md` as a minimal collaboration entry;
- do not create fake architecture, bounded-context, package, broker, database, or endpoint facts;
- mark `.dev/ARCHITECTURE.MD` and tech-stack requirements as awaiting project initialization if those files are present;
- ask for product and stack direction before invoking requirement or architecture design skills.

## Directory-Specific Rules

### `.dev/requirement/`

Keep authoring guides. Rewrite tech stack, bounded-context overview, project-specific NFR, and entries tied to a broker, database, deployment model, or other target-specific reality.

### `.dev/specs/`

Keep taxonomy, naming rules, `SPEC-GUIDE.MD`, `SPEC-ORGANIZATION-GUIDE.MD`, `tests/README.MD`, and `tests/TEST-SPEC-GUIDE.MD`. Rewrite bounded contexts, aggregates, use cases, scenarios, assertions, cross-domain specs, and E2E specs.

### `.dev/operations/`

Keep document-type guides and README files. Rewrite producer, consumer, queue, topic, retry, DLQ, incident, context map, event catalog, MQ topology, and runbook truth.

### `.dev/workflows/`

Keep only the workflow artifact contract unless the target repo is intentionally continuing the same unfinished workflow. Completed source-repo workflow artifacts should not be copied forward.

### `.dev/adr/`

Keep the governance layer, not old decisions. Delete or rewrite `ADR-*.md` files unless they are valid decisions for the target repo.

## Verification Checks

Before finishing a sync:

- confirm root README files describe the target repo rather than the source template repo
- confirm `agents.md` stack and directory rules match the target repo
- confirm `.dev/ARCHITECTURE.MD` and `.dev/requirement/TECH-STACK-REQUIREMENTS.MD` are rebuilt from target facts
- confirm `.ai/scripts/README.md` lists only scripts that still apply
- search `.dev/specs/` and `.dev/operations/` for source-repo names, routes, services, event names, queues, and topics
- confirm `.dev/adr/` is governance only unless target-specific ADRs were intentionally authored

## Judgement Rule

If a document describes how the collaboration framework works, it is usually reusable. If it describes what the current project is, it must be verified and usually rewritten. If it mixes both, split framework guidance from project truth during the sync.
