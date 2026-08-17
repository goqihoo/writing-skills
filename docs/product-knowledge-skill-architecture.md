# Product Knowledge Skill Architecture

Status: Accepted

## Purpose

This architecture turns product-boundary reasoning, lifecycle readiness, documentation structure, and standard product artifacts into explicit Scribe interfaces. It keeps one authoritative product knowledge set while allowing two navigation views: a responsibility map for finding durable product truth and a lifecycle map for deciding what evidence and artifact is needed next.

The runtime plugin must carry the method itself. It must not depend on a maintainer vault, a particular product repository, or a technical-documentation layout.

## Decision

Use three coordination interfaces, one common document writer, and eight standard artifact interfaces:

| Skill | Owns | Excludes |
| --- | --- | --- |
| `reason-product` | Product admission, boundary, hierarchy, relationships, change and release authority, content ownership, and the Product Assessment handoff | Directory topology and document bodies |
| `assess-product-lifecycle` | Decision readiness, evidence sufficiency, artifact coverage, three independently assigned state groups, and the Product Lifecycle Assessment | Creating another skill's artifact or treating stages as directories |
| `structure-product-docs` | Product inventory, the Seven-directory core, Product-type extensions, materialization, navigation, scaffolding, and migration | Product admission and artifact bodies |
| `write-product-doc` | Common current-state product documents selected through internal branches | Standard lifecycle artifacts with independent decision boundaries |
| `write-product-strategy` | Product direction, target users, value, strategic choices, non-goals, and review triggers | Capability decomposition, roadmap sequencing, and one initiative's requirements |
| `map-product-capabilities` | Stable product capabilities, relationships, ownership, external authority, and reusable composition | Feature lists, system modules, team structure, and delivery timing |
| `write-solution-definition` | A reusable capability composition for one class of customer or partner scenario | One customer's delivery agreement and technical design |
| `write-product-roadmap` | Outcome sequencing, product bets, dependencies, confidence, commitments, and review points | Product capability truth and task backlogs |
| `write-prd` | One product change's problem, scope, observable behavior, rules, and acceptance | Whole-product strategy and implementation structure |
| `design-product-metrics` | Product outcome model, metric hierarchy, definitions, guardrails, governance, and evidence gaps | Instrumentation implementation and dashboard construction |
| `write-release-plan` | Product release intent, readiness, coordination, communication, success signals, and decision criteria | Technical deployment and rollback procedures |
| `write-product-review` | Evidence-based evaluation of a release, period, experiment, or product decision and the next accepted actions | Team retrospectives and technical incident reviews |

Existing foundations remain explicit dependencies:

- `write-doc` owns the shared prose contract.
- `structure-docs` owns repository-wide taxonomy and cross-class placement.
- `draw-diagrams` owns visual form when a capability or lifecycle model needs a diagram.
- Technical skills and directories own implementation, architecture, operations, and engineering records. Product artifacts link to them when a product decision depends on them.

## Three views

The system separates three reader actions:

1. **Product method knowledge** explains how to perform product work and can survive any one product.
2. **Lifecycle navigation** shows the current decision, required evidence, authoritative artifact, status, owner, and next review.
3. **Product-instance knowledge** records what one product is, what it is changing, why decisions were made, and what happened.

Only the third view forms the product knowledge set. The first belongs in reusable knowledge. The second is a map over the third, not another owner of its content.

## Product Assessment

`reason-product` produces the handoff consumed by downstream product skills. It records:

- `Accept`, `Route as product area or capability`, `Route to another content class`, or `Needs evidence`;
- the minimum user outcome, target users, context, value, and offered capability boundary;
- product-line, subproduct, product-area, capability, peer, dependency, and handoff relationships;
- change authority, release boundary, lifecycle stage, and review triggers;
- included and excluded product knowledge with one primary destination for each assessed material;
- known evidence, hypotheses, decisions, and unresolved questions.

Structure and common-document skills require an accepted assessment. A standard artifact may refine an accepted boundary, but it must not silently invent a product around a feature, project, team, customer, or software component.

## Product Lifecycle Assessment

`assess-product-lifecycle` treats lifecycle stages as a decision view. It records:

- the decision currently being prepared;
- required evidence and authoritative artifacts;
- sufficiency, staleness, ownership, and open decisions;
- a ready-to-type explicit invocation for each missing artifact;
- three independently assigned state groups.

The state groups are:

| State group | Fields and states |
| --- | --- |
| Structure | `Structure state`: `Existing`, `Create now`, `Planned`, `Unresolved` |
| Artifact validity | `Acceptance state`: `Draft`, `Accepted`; `Currency state`: `Current`, `Needs review`, `Superseded` |
| Decision gate | `Gate state`: `Not applicable`, `Collecting evidence`, `Ready for decision`, `Go`, `Hold`, `Recycle`, `Stop` |

A file can exist without being accepted, an accepted artifact can become stale, and a gate can pass without making every source permanently current. Templates therefore record artifact validity through separate acceptance and currency fields while keeping both inside the one artifact-validity dimension.

## Seven-directory core

The default product scaffold creates the high-frequency responsibilities that recur across most products:

```text
{product}/
├── README.md
├── lifecycle.md
├── definition/
├── capabilities/
├── planning/
├── initiatives/
├── evidence/
├── measurement/
└── releases/
```

Each directory receives a README when the scaffold includes `$write-product-doc`; the README defines current and planned coverage so the directory is not an unexplained empty container. Standard artifacts are created only when their owning skill is explicitly invoked.

### Product-type extensions

Create extensions only when the product model supports them:

- `solutions/` for a B2B, platform, or partner product with several reusable scenario compositions;
- `experience/` for a product with cross-capability journeys or behavior rules that need independent maintenance;
- `decisions/` after several cross-initiative product decisions need one governed record set.

Keep evidence, initiatives, and releases flat initially. Add their internal subdirectories only after several independently useful documents or a stable navigation path exists.

## One file, two maps

The product `README.md` maps knowledge by responsibility. `lifecycle.md` maps the same authoritative files by decision sequence. Neither map duplicates product strategy, capability, roadmap, PRD, evidence, metric, or release content.

This separation lets one capability map support strategy, solution design, roadmap planning, and iteration without moving between stage directories. It also lets research collected after launch live beside discovery evidence while appearing at the correct lifecycle decision point.

## Common documents and standard artifacts

`write-product-doc` keeps ten common branches behind one public interface:

- product map and README;
- lifecycle map;
- collection README;
- users and roles;
- concepts and language;
- capability detail;
- journey and behavior;
- evidence record;
- product decision record;
- release notes.

The standard artifacts remain public skills because each has a different reader decision, input authority, reasoning sequence, approval boundary, and completion test. Do not fold product strategy, capability mapping, solution definition, roadmap, PRD, metrics, release planning, or product review into the common writer.

## Explicit invocation

Every Scribe skill is user-invoked. Recommended compositions name all required foundations and artifact owners:

```text
$reason-product $write-doc
```

```text
$assess-product-lifecycle $reason-product $write-doc
```

```text
$structure-product-docs $reason-product $assess-product-lifecycle $structure-docs $write-doc
```

Add `$write-product-doc` when the same authorized request must create the root map, lifecycle map, or collection README bodies.

```text
$write-product-strategy $reason-product $write-doc
$map-product-capabilities $reason-product $write-doc
$write-solution-definition $reason-product $write-doc
$write-product-roadmap $reason-product $write-doc
$write-prd $write-doc
$design-product-metrics $reason-product $write-doc
$write-release-plan $reason-product $write-doc
$write-product-review $reason-product $write-doc
```

A skill never silently invokes another user-invoked Scribe skill. When a required artifact or foundation is missing, it returns a ready-to-type invocation and stops before performing the missing workflow.

## Repository layout

```text
skills/foundations/reason-product/
├── SKILL.md
├── agents/openai.yaml
├── references/product-reasoning-method.md
└── assets/product-assessment-template.md

skills/product/assess-product-lifecycle/
├── SKILL.md
├── agents/openai.yaml
├── references/product-lifecycle-model.md
└── assets/product-lifecycle-assessment-template.md

skills/product/structure-product-docs/
├── SKILL.md
├── agents/openai.yaml
├── references/product-structure-model.md
└── assets/
    ├── product-inventory-template.md
    └── product-structure-plan-template.md

skills/product/write-product-doc/
├── SKILL.md
├── agents/openai.yaml
├── references/product-document-types.md
└── assets/[common product templates]

skills/product/[standard-artifact-skill]/
├── SKILL.md
├── agents/openai.yaml
└── assets/[owned template]
```

## Verification

Contract tests verify:

- every product skill remains explicitly invoked and composes `$write-doc`;
- Product Assessment remains the boundary handoff;
- lifecycle assessment keeps the three state groups and their fields separate;
- the Seven-directory core and Product-type extensions remain distinct;
- common documents stay behind `write-product-doc` while standard artifacts retain their public owners;
- every standard artifact skill owns exactly one output template;
- README, Ask Scribe, plugin manifests, and default prompts expose complete compositions;
- the complete test suite, skill validation, shell syntax checks, JSON parsing, and `git diff --check` pass.

The architecture is complete when a product can be assessed, its next decision can be identified, its authoritative files can receive stable homes, and each standard artifact can be created without duplicating another skill's responsibility or placing technical material inside the product system.
