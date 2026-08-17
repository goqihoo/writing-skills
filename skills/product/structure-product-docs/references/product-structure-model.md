# Product structure model

Use this model after `$reason-product` has accepted the product boundary and `$assess-product-lifecycle` has identified current artifact needs.

## Seven-directory core

Create these high-frequency responsibilities for an explicitly requested product scaffold:

```text
{product}/
├── README.md
├── lifecycle.md
├── definition/
│   └── README.md
├── capabilities/
│   └── README.md
├── planning/
│   └── README.md
├── initiatives/
│   └── README.md
├── evidence/
│   └── README.md
├── measurement/
│   └── README.md
└── releases/
    └── README.md
```

The tree is a responsibility scaffold, not an instruction to create every standard artifact. Create the README bodies only when `$write-product-doc` is explicitly included. List real planned coverage without linking nonexistent files.

### Core responsibilities

| Path | Owns | Excludes |
| --- | --- | --- |
| `definition/` | Product strategy, users and roles, product concepts, stable scope | Initiative requirements and implementation |
| `capabilities/` | Capability map and durable capability details | Features, modules, teams, and delivery sequence |
| `planning/` | Roadmap, product bets, outcome sequence, priority rationale | Current capability truth and task backlogs |
| `initiatives/` | One change's problem, scope, observable behavior, and acceptance | Whole-product definition and technical design |
| `evidence/` | Research, feedback, experiments, and interpreted product evidence | Accepted product commitments and metric definitions |
| `measurement/` | Outcome model, metric definitions, guardrails, and periodic product results | Instrumentation implementation and raw research |
| `releases/` | Product release plans, notes, outcomes, and reviews | Technical runbooks, deployment records, and enduring strategy |

Keep root `README.md` and `lifecycle.md` as maps. They reference the same authoritative files through different reader paths.

## Product-type extensions

Create only supported extensions:

- `solutions/` when a B2B, platform, or partner product has several reusable capability compositions for classes of scenarios;
- `experience/` when cross-capability journeys, product-wide behaviors, or rules require independent maintenance;
- `decisions/` when several cross-initiative decisions need a governed record set and cannot remain with their owning strategy, capability, roadmap, or release artifact.

A single customer solution remains in its project. A single journey can remain inside the owning capability or PRD. A decision stays in its primary artifact until independent lookup or review needs justify a separate record.

## Materialization states

- **Existing** — a current artifact already owns the responsibility.
- **Create now** — the lifecycle decision and available evidence justify a path or artifact now.
- **Planned** — the responsibility is real, but evidence or content is not ready.
- **Unresolved** — boundary, authority, or ownership must be decided first.

The core scaffold is an explicit exception to purely content-driven materialization: its high-frequency directories may be created before every standard artifact, but each created directory must receive a boundary README or be recorded as an authorized empty scaffold.

## Upgrade triggers

Upgrade a file or flat collection to a directory when:

- several independently useful documents exist now;
- different documents have independent owners, validity, or review triggers;
- readers need a stable internal navigation path;
- one file can no longer answer a single primary reader question cleanly.

Keep `evidence/`, `initiatives/`, and `releases/` flat initially. Add `research/`, `feedback/`, `experiments/`, initiative directories, or release directories only when current material requires them.

## Product README contract

Expose:

- the accepted product boundary, users, outcome, exclusions, and related products;
- current linked knowledge and planned unlinked coverage;
- entries by definition, capability, planning, initiative, evidence, measurement, and release;
- product-type extensions when present;
- the lifecycle map and maintenance rules;
- links to externally owned business, company, project, method, and technical material.

The README is a map, not a duplicate strategy or capability summary.

## Lifecycle-map contract

For each decision gate, show the required artifact, authoritative link, structure state, acceptance state, currency state, gate state, owner, evidence gap, and next review. Use the lifecycle assessment as the source. Do not copy artifact bodies.

## Technical material

Technical material remains in its owning directory. Product structure may link a technical dependency or readiness record, but it must not copy architecture, component, interface, data, deployment, reliability, or runbook content into the product tree.

## Migration contract

Before an applied migration, record exact old and new paths, affected Markdown and wiki links, moved assets, external bindings, supersession relationships, and approval. Verify that no old path, duplicate authority, broken link, or orphaned asset remains.
