# Technical architecture and Internal Document Type registry

Status: ready-for-agent

## Objective

Revise Scribe's Product and Technical document writers so architecture ownership is complete, architecture levels remain distinct from architecture views, and Internal Document Types are governed by small per-Writer registries with optional templates. Preserve all Public Skill IDs and Display Names.

Work only in the Scribe source repository. Treat `plugins/scribe/` as generated output and rebuild it from canonical sources; never edit an installed Codex or Claude cache.

## Current problems

1. `System Architecture` has a glossary definition but no writing owner, registered type, or completion contract.
2. Company, System, and Subsystem architecture levels are not represented consistently in Technical structure and writing skills.
3. Domain, Application, Governance, and Runtime views are a Shared Method but some templates turn them into fixed output headings.
4. Product and Technical type tables infer configuration from Markdown and require one template per type.
5. Product and Technical registries enumerate many speculative or overlapping types.
6. Product and Technical navigation types overlap their Structure Skills.
7. Type entries lack a required description and explicit Freeform or template policy.

## Confirmed architecture model

### Objects

- A Product is a company value offering and may span several Systems.
- A System owns a stable technical responsibility and independently governed lifecycle. State ownership, external contracts, release, and failure boundaries are evidence, not individually mandatory conditions.
- An Application is a runnable or audience-specific entry within a System.
- A Subsystem is a stable logical responsibility boundary inside a System.
- A Module or Component is an implementation unit inside a Subsystem.
- A Codebase and Runtime Unit realize architecture but do not define Product, System, or Subsystem boundaries by themselves.
- Preserve many-to-many Product-to-System relationships. Never derive directories from a one-to-one Product, System, Application, Subsystem, Codebase, or Runtime Unit mapping.

### Architecture levels and views

- Treat company, System, and Subsystem as Architecture Levels.
- Treat Domain, Application, Governance, and Runtime as orthogonal Architecture Views that may be applied at every level.
- Use the four views as internal coverage checks. Do not require four directories, four documents, or four fixed parallel headings.
- Organize architecture output around the reader's questions, the selected level, evidence, decisions, and local healthy conventions.

### Ownership

- `write-technical-architecture` owns company-level Technical Architecture, Product-System Map, and compatible cross-system Architecture Topics.
- `write-technical-doc` owns System Architecture and Subsystem Architecture as registered Internal Document Types.
- Keep Architecture Topic as an unregistered Freeform Artifact of `write-technical-architecture` until repeated use proves a stable type contract.
- Keep `write-technical-architecture` as the company-level public skill and `write-technical-doc` as the system/common Technical writer. Add no Public Skill.
- Keep Project Technical Design, Machine Authority, code-local implementation guidance, configuration, schemas, tests, and runbook procedures in their existing authority scopes and link them.

### Technical structure

- Treat Strategy, Architecture, Systems, and Governance as logical Stable Responsibilities rather than mandatory English directory names.
- Reuse the documentation set's language. For a new set, follow the user's language; for an existing set, map equivalent responsibilities without renaming only for language consistency.
- Register a System only after its stable name, responsibility boundary, owner, and lifecycle status are supported by evidence.
- Give every Registered System a System Responsibility README and System Architecture.
- Make the System Profile type own the Registered System README. Let `structure-technical-docs` own the Technical root and responsibility README bodies.
- Materialize a Subsystem directory and Subsystem Architecture only when its boundary, complexity, and continuing maintenance value justify independent documentation.
- Keep Architecture Decisions at the narrowest Architecture Level that governs their consequences. Higher levels link or summarize them.
- Create Product-System Map only when accepted Products and their many-to-many System relationships need independent maintenance.
- Create an Architecture Topics collection only with the first accepted cross-system concern. Do not create one per Product.
- Keep company responsibility extensions such as Platform, Data, Security, Quality, and Operations separate from concrete Systems. A concrete platform that satisfies the System test is also registered under Systems; responsibility documents link it.

## Internal Document Type contract

### Three artifact levels

1. A Public Skill owns a frequent independent result and invocation.
2. An Internal Document Type is registered when repeated use or audit-critical consistency justifies a stable identity, description, authority boundary, and completion profile.
3. A compatible occasional document remains a Freeform Artifact of its owning Writer until real use justifies registration.

Do not reject a compatible request because no registered type matches. Apply the Writer's general authority, evidence, prose, navigation, and completion rules to the Freeform Artifact. Do not create a new type automatically.

### Configuration layout

Create:

```text
methods/internal-document-types.md
docs/internal-document-types.md
skills/write-product-doc/references/internal-document-types.yaml
skills/write-technical-doc/references/internal-document-types.yaml
skills/write-technical-architecture/references/internal-document-types.yaml
```

- Make each YAML file the sole configuration authority for its owning Writer.
- Make `methods/internal-document-types.md` the shared execution contract read internally by all three Writers.
- Generate `docs/internal-document-types.md` from YAML. Do not maintain a second hand-written catalog of the same fields.
- Add a generator with a `--check` mode and run it in tests.
- Leave Domain's current Markdown type model and templates unchanged.
- Leave Knowledge Types outside the Internal Document Type registry.

Use a versioned per-Writer schema equivalent to:

```yaml
schema_version: 1
owner_skill: write-technical-doc
model: Technical Documentation
types:
  - id: system-architecture
    name: System Architecture
    description: Describe one registered System's stable architecture.
    reader_question: How does this System divide responsibility and behave?
    authority: One registered System's architecture, excluding Machine Authority and Project Technical Design.
    completion: The System's boundaries, ownership, contracts, failure, validation, and evolution are decision-ready.
    template:
      path: ../assets/example-template.md
      policy: adaptive
```

Required top-level fields:

- `schema_version`
- `owner_skill`
- `model`
- `types`

Required type fields:

- stable lower-case hyphenated `id`
- unique `name`
- `description`
- `reader_question`
- `authority`
- `completion`

Template behavior:

- Omit `template` for Freeform Structure.
- Require a real bundled asset path and `policy` when `template` exists.
- Accept only `fixed`, `sequence`, or `adaptive` policy.
- `fixed` preserves exact headings, order, and fields.
- `sequence` preserves reasoning or action order and permits subject-specific headings.
- `adaptive` preserves content responsibilities and permits merging, reordering, layout changes, and visible omission.
- Treat template absence as a normal Freeform mode, not an error or a reason to interview the user about routine headings.
- Keep `assets/` equal to the set of configured active templates. Remove unreferenced and dormant templates.

Do not implement company- or project-level template override discovery in this change.

## Product registry

Keep exactly these ten Product types:

| ID | Name | Description | Mode |
| --- | --- | --- | --- |
| `product-portfolio` | Product Portfolio | Govern the company's accepted Products and investment relationships. | `templated/adaptive` |
| `products-registry` | Products Registry | Register accepted Products, owners, lifecycle, and navigation. | `templated/adaptive` |
| `product-governance` | Product Governance | Define Product decision rights, policies, evidence, and exceptions. | `templated/adaptive` |
| `product-definition` | Product Overview/Definition | Define one Product's boundary, users, value, behavior, exclusions, and relationships. | `templated/adaptive` |
| `capability-detail` | Capability Detail | Explain one Product capability's responsibility, behavior, rules, evidence, and evolution. | `templated/adaptive` |
| `evidence-record` | Evidence Record | Separate observations, method, limits, interpretation, and decision implications. | `templated/adaptive` |
| `product-decision` | Product Decision | Preserve an accepted Product choice, alternatives, rationale, costs, and review triggers. | `templated/adaptive` |
| `product-release-plan` | Product Release Plan | Define release availability, evidence gates, dependencies, and stop conditions. | `templated/sequence` |
| `release-notes` | Release Notes | Record released current state and link changed authorities. | `templated/adaptive` |
| `product-review` | Product Review | Compare expectations with evidence and record conclusions, decisions, and follow-up. | `templated/sequence` |

Keep only the corresponding ten existing templates. Remove these registered types and templates:

- Product Navigation
- Product Operating Model
- Users and Roles
- Product Terminology
- Lifecycle Map
- Journey/Product Behavior
- Product Solution
- Initiative Record

Route Product root and responsibility navigation to `structure-product-docs`. Treat compatible requests for removed types as Freeform Artifacts of `write-product-doc` when they remain Product Documentation.

Keep Product Strategy, Capability Map, Product Roadmap, PRD, and Product Metric System routed to their existing Public Skills.

## Technical registries

### `write-technical-architecture`

Register exactly two types:

| ID | Name | Description | Mode |
| --- | --- | --- | --- |
| `technical-architecture` | Technical Architecture | Describe company-level Technical Landscape structure, principles, boundaries, relationships, failure domains, and evolution. The artifact title need not contain the word “company.” | `freeform` |
| `product-system-map` | Product-System Map | Maintain many-to-many Product, System, and capability relationships without redefining Product or System authorities. | `templated/adaptive` |

- Remove `technical-architecture-template.md`; Technical Architecture becomes reader-driven Freeform Structure with an explicit completion profile.
- Add one adaptive Product-System Map template.
- Let the skill handle a cross-system Architecture Topic as a Freeform Artifact, not a registered type.

### `write-technical-doc`

Register exactly eleven types:

| ID | Name | Description | Mode |
| --- | --- | --- | --- |
| `technical-strategy` | Technical Strategy | Define durable Technical direction, choices, constraints, outcomes, and review triggers. | `freeform` |
| `technical-roadmap` | Technical Roadmap | Sequence Technical outcomes, dependencies, decisions, and review triggers. | `templated/sequence` |
| `system-landscape` | System Landscape | Register Systems, owners, lifecycle, critical relationships, and authoritative links. | `templated/adaptive` |
| `system-profile` | System Profile | Provide one Registered System's identity, responsibility, lifecycle, relationships, and navigation through its README. | `templated/adaptive` |
| `system-architecture` | System Architecture | Describe one Registered System's stable internal architecture and evolution. | `freeform` |
| `subsystem-architecture` | Subsystem Architecture | Describe one justified Subsystem's stable responsibility and internal architecture. | `freeform` |
| `technical-governance` | Technical Governance | Define company Technical decision rights, policies, evidence, exceptions, and review. | `freeform` |
| `technical-standard` | Technical Standard | State normative rules, applicability, rationale, verification, exceptions, and evolution. | `templated/adaptive` |
| `architecture-decision` | Architecture Decision | Preserve a choice, alternatives, rationale, accepted cost, authority, validation, Architecture Level, and supersession. | `templated/adaptive` |
| `governance-exception` | Governance Exception | Preserve an approved deviation, authority, scope, risk, controls, expiry, and remediation. | `templated/adaptive` |
| `incident-record-review` | Incident Record/Review | Separate impact, timeline, evidence, contributing conditions, response, learning, and actions. | `templated/sequence` |

Keep only templates referenced by the seven templated types. Remove these registered types and their templates:

- Technical Navigation
- Technical Operating Model
- Platform Definition
- Engineering Practice
- Data Governance
- Security Governance
- Quality Model
- Operations Model

Also remove the current Technical Strategy and Technical Governance templates because their retained types become Freeform.

Route Technical root and responsibility navigation to `structure-technical-docs`. Treat compatible requests for removed types as Freeform Artifacts of `write-technical-doc` when they remain Technical Documentation.

## System Architecture completion contract

Do not create a fixed System Architecture template. Make the type description, completion profile, Technical Reasoning Method, and Architecture Reasoning Method require the selected document family to address relevant evidence for:

- purpose, scope, responsibilities, and non-goals;
- external actors, context, and boundaries;
- Applications, Subsystems, and internal responsibility boundaries;
- authoritative state, data ownership, and consistency boundaries;
- interfaces, commands, events, queries, and cross-boundary contracts;
- normal flows and failure semantics including duplicate, timeout, ordering, partial, and unknown outcomes;
- permissions, controlled commands, control points, and durable evidence;
- deployment responsibilities, runtime dependencies, failure domains, degradation, recovery, and observability;
- principles, constraints, material decisions, alternatives, and accepted costs;
- validation, operating evidence, fitness checks, and review triggers;
- current facts, accepted target direction, evaluated proposals, compatibility, migration, and evolution boundaries;
- downstream Subsystem Architecture, interface definitions, runbooks, code repositories, and Machine Authority links.

Permit supporting files when they have an independent reader task, authority, change cycle, and navigation value. Require the main System Architecture document to remain the coherent entry point. One invocation may update the main document and directly affected supporting files; it must not rewrite unrelated files.

Apply the same principles proportionally to Subsystem Architecture at the narrower level.

## Required source updates

Re-read and update every authority that currently treats detailed System Architecture as outside company Technical Documentation. At minimum inspect and update:

- `AGENTS.md`
- `CONTEXT.md`
- `methods/architecture-reasoning.md`
- `methods/technical-reasoning.md`
- `skills/reason-technical/SKILL.md`
- `skills/reason-technical/assets/technical-assessment-template.md`
- `skills/structure-technical-docs/SKILL.md`
- `skills/structure-technical-docs/references/technical-structure-model.md`
- `skills/structure-technical-docs/assets/technical-inventory-template.md`
- `skills/structure-technical-docs/assets/technical-structure-plan-template.md`
- `skills/structure-product-docs/SKILL.md`
- `skills/write-product-doc/SKILL.md`
- `skills/write-technical-doc/SKILL.md`
- `skills/write-technical-architecture/SKILL.md`
- `skills/write-technical-architecture/references/technical-architecture-method.md`
- `skills/ask-scribe/SKILL.md`
- `README.md`
- `docs/scribe-skill-architecture.md`
- `docs/product-documentation-skill-architecture.md`
- `docs/technical-documentation-skill-architecture.md`

Update only files whose authority or routing actually changes. Keep branch-specific detail behind direct one-level reference pointers and keep `SKILL.md` workflows concise and imperative.

Update Ask Scribe so natural requests route without requiring the user to know Internal Document Type names:

- company overall architecture or Product-System mapping → `$Write Tech Arch`;
- one System or Subsystem architecture → `$Write Tech Doc`;
- compatible occasional Product or Technical document → its owning Writer as a Freeform Artifact;
- directory, navigation, scaffold, audit, or migration → the applicable Structure Skill.

Do not add required Public Skill composition.

## Tests

Add a generic registry contract test that parses canonical YAML and verifies:

1. schema version and owner/model fields are present;
2. IDs are unique lower-case hyphenated values;
3. names are unique within the registry;
4. description, reader question, authority, and completion are non-empty;
5. absent template means Freeform;
6. present template has an allowed policy and resolves to a real asset;
7. every active template is referenced exactly once unless an explicitly documented shared-template rule is added;
8. every bundled Writer template is active and no dormant template remains;
9. the generated Markdown catalog exactly matches YAML;
10. Product has exactly 10 registered types;
11. `write-technical-architecture` has exactly 2 registered types;
12. `write-technical-doc` has exactly 11 registered types;
13. removed Product and Technical type names are absent from registries;
14. Domain's current type contract remains unchanged;
15. Knowledge Types remain outside the registry.

Update Technical contract tests to verify:

- System Architecture and Subsystem Architecture belong to `write-technical-doc`;
- Technical Architecture remains company-level and belongs to `write-technical-architecture`;
- Product-System Map belongs to `write-technical-architecture`;
- System Profile owns a Registered System README and does not replace System Architecture;
- each Registered System requires README and System Architecture, not a central implementation/codebase document;
- Architecture Levels and Architecture Views remain distinct;
- four views are coverage checks, not required documents, directories, or fixed headings;
- System Architecture remains separate from Machine Authority and Project Technical Design;
- Architecture Decisions carry a level and live at the narrowest governing scope;
- Structure Skills own root and responsibility navigation types;
- natural Ask Scribe routes distinguish company, System, Subsystem, and structure requests;
- public skill count, IDs, Display Names, explicit invocation, manifest, and flat-layout contracts remain unchanged.

Update Product tests to verify the exact 10-type registry, template set, removed-type fallback language, and Structure Product Docs navigation ownership.

## Generated plugin and release

- Rebuild the Codex package with `scripts/build-codex-plugin.sh` after canonical changes.
- Run `scripts/build-codex-plugin.sh --check` and verify no generated drift.
- Keep exactly the existing 23 Public Skills.
- Preserve Public Skill IDs and Display Names.
- Bump plugin/release metadata consistently for this material contract change and add concise release notes.

## Out of scope

- New Public Skills or invocation names.
- Domain type migration or pruning.
- Knowledge Type migration.
- Company- or project-level custom template override discovery.
- A central implementation/codebase mapping document.
- Project Technical Design.
- Copying schemas, configuration, code, tests, deployment manifests, or runbook procedures into company Technical Documentation.
- Compatibility aliases for removed Internal Document Type names; compatible natural-language requests use Freeform fallback instead.

## Validation

Run every repository-required check:

- complete Python test suite;
- canonical Claude plugin validation;
- generated Codex plugin and skill validation;
- Internal Document Type catalog generation in `--check` mode;
- Codex package build in `--check` mode;
- `bash -n scripts/*.sh`;
- `git diff --check`.

## Completion

The change is complete when Product and Technical Writers read validated per-Writer YAML registries, the generated catalog describes every registered type and mode, only active templates remain, compatible unregistered documents use Freeform fallback, architecture ownership is complete across company/System/Subsystem levels, four views remain internal checks, Structure Skills own responsibility navigation, all 23 Public Skill interfaces remain unchanged, generated plugin content matches canonical sources, and every required validation passes.
