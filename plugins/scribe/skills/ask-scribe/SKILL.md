---
name: ask-scribe
description: Explain Scribe's skills, authority boundaries, composition rules, and complete explicit invocation choices without executing another skill or producing its artifact.
---

# Ask Scribe

Explain and recommend. Leave every subsequent invocation and execution to the user.

## Guidance

1. Answer the user's question about Scribe, its skills, boundaries, or composition.
2. Inspect the installed `SKILL.md` files before describing current behavior.
3. Identify the intended result, authority scope, reader decision, artifact lifetime, and requested output.
4. Distinguish reusable **Knowledge**, company-owned **Product Documentation** or **Technical Documentation**, and engagement-owned **Project Documentation**.
5. Recommend the single Public Skill that owns the requested result. Recommend multiple Public Skills only when the user explicitly asks for multiple independently owned results.
6. Return ready-to-type display-name invocations such as `$Ask Scribe` or `/Ask Scribe` when useful. Mention the canonical Skill ID as the compatible alternative when introducing a skill.
7. Read `../../methods/prose-quality.md`, then explain the choice. Read `../../methods/visual-production.md` only when the user asks for a visual explanation of Scribe or the catalog relationships are materially clearer as one. Do not invoke another skill, perform its workflow, modify files, or produce an artifact owned by another skill.

For architecture purpose, viewpoints, document types, template structure or design rationale, follow **Architecture design choices** below before recommending a Writer.

## Materialization and interface language

- **Stable Responsibility:** default home for a continuing accepted responsibility.
- **Type Extension:** materialize only when independent ownership, governance, or navigation is proven.
- **Event Collection:** materialize with the first real event document.
- **Internal Document Type:** a registered frequent or audit-sensitive artifact branch inside one Writer.
- **Freeform Artifact:** a compatible occasional document owned by a Writer without creating a new registered type or forcing a template.
- **Shared Method:** an internal rule set a Public Skill applies directly; it has no invocation name and never appears in the catalog.
- **Explicit Skill Composition:** the user names one Public Skill for each independently requested result; internal reasoning, structure, prose, and visual methods add no invocation.
- **Skill ID:** the canonical machine name used by the directory, frontmatter, manifests, and code.
- **Skill Display Name:** the exact user-facing invocation name from `agents/openai.yaml`; it is unique and equivalent to the Skill ID.

## Skill guide

| Result | Skill | Boundary |
| --- | --- | --- |
| Understand Scribe or choose a workflow | **Ask Scribe** (`ask-scribe`) | Explain only; do not execute. |
| Place files, define directory responsibilities, or plan a migration | **Structure Docs** (`structure-docs`) | Own information architecture, not artifact meaning. |
| Write a general linear document or run a dedicated prose-quality pass | **Write Doc** (`write-doc`) | Own linear document expression, not a presentation manuscript or another artifact's meaning. |
| Write an audience-facing presentation manuscript in Markdown | **Write Deck** (`write-deck`) | Own the narrative and slide sequence; preserve source authority and do not create a rendered presentation file. |
| Apply four-view architecture reasoning | **Reason Arch** (`reason-architecture`) | Own the method, not an artifact. |
| Admit and bound reusable Domain Knowledge | **Reason Domain** (`reason-domain`) | Own the Domain Assessment. |
| Resolve a company portfolio, product line, product, capability, or extension | **Reason Product** (`reason-product`) | Own Product Assessment decisions. |
| Resolve company technical scope, ownership, authority, or extension | **Reason Tech Docs** (`reason-technical`) | Own Technical Assessment decisions. |
| Structure an accepted Domain Knowledge set | **Structure Domain Docs** (`structure-domain-docs`) | Own domain topology and navigation. |
| Write a common Domain Knowledge document | **Write Domain Doc** (`write-domain-doc`) | Own its internal domain document types. |
| Write general reusable Knowledge | **Write Knowledge** (`write-knowledge`) | Own concepts, mechanisms, methods, patterns, cases, and references. |
| Create or organize reusable Architecture Knowledge systems and documents | **Write Arch Knowledge** (`write-architecture-knowledge`) | Own reusable designs and knowledge-set organization using shared primary templates; do not make project commitments. |
| Assess a product decision and artifact coverage | **Assess Product Lifecycle** (`assess-product-lifecycle`) | Own the Product Lifecycle Assessment, not missing artifacts. |
| Structure company Product Documentation | **Structure Product Docs** (`structure-product-docs`) | Own Product topology and materialization. |
| Write a standard or occasional Product document | **Write Product Doc** (`write-product-doc`) | Own registered types and compatible Freeform Artifacts; route public artifacts. |
| Define product direction | **Write Product Strategy** (`write-product-strategy`) | Own durable strategy. |
| Model product capabilities | **Map Product Capabilities** (`map-product-capabilities`) | Own capability responsibility and relationships. |
| Sequence product outcomes and decisions | **Write Product Roadmap** (`write-product-roadmap`) | Own product sequence, not tasks. |
| Define one product change | **Write PRD** (`write-prd`) | Own observable behavior and acceptance. |
| Define the product metric system | **Design Product Metrics** (`design-product-metrics`) | Own measure semantics and governance. |
| Structure company Technical Documentation | **Structure Tech Docs** (`structure-technical-docs`) | Own Technical topology and materialization. |
| Write a standard or occasional Technical document, including stable System or Subsystem Architecture, Module Design and Component Architecture | **Write Tech Doc** (`write-technical-doc`) | Own registered Technical types at their declared levels and compatible Freeform Artifacts; route company-level architecture. |
| Define company overall architecture, a Product-System Map, a cross-System topic, or Project delivery architecture | **Write Tech Arch** (`write-technical-architecture`) | Own company-level Technical Landscape structure and concrete Project delivery architecture. |
| Change a Technical directory, navigation, scaffold, audit, or migration | **Structure Tech Docs** (`structure-technical-docs`) | Own Technical topology and navigation, not document meaning. |
| Create one architecture, data, process, planning, or quantitative visual | **Draw Diagram** (`draw-diagram`) | Own one of 39 Diagram Design visual forms; the source skill owns meaning. |

## Architecture design choices

Read `../../methods/architecture-documents.md` for purpose, document responsibilities and template adaptation, and `../../methods/architecture-reasoning.md` for viewpoint definitions and their entry into design. Use these Shared Methods as the authorities; explain their rules without executing a Writer. When asked to show an outline, resolve its template through `../../methods/architecture-templates/templates.yaml` and inspect the actual asset rather than reconstructing headings from memory.

Explain the design principle: **purpose determines how content develops; document responsibility determines the template; four viewpoints guide design reasoning and completeness checks.** Keep purpose, authority, document granularity and viewpoint separate so a change in intended use does not automatically create another template or document set.

- Explain **Architecture Knowledge** through reusable problems, assumptions, reference mechanisms, alternatives, evidence and applicability limits. Explain evolution through variants and adaptation; require an actual migration question before describing a concrete cutover.
- Explain **Concrete Design** through the named object, actual constraints, selected or proposed mechanisms, acceptance evidence and applicable transition arrangements. Distinguish continuing Company/System authority from named Project delivery when selecting the Writer; purpose alone does not settle ownership.
- Explain that both purposes use the same template for the same document responsibility. Change the content's specificity and claims, while retaining the questions that make the design understandable.

Use the four primary responsibilities to explain when a separate document earns its place:

| Document | Explain its responsibility | Explain its depth boundary |
| --- | --- | --- |
| Overall Architecture | Show how the whole system's parts combine to satisfy its goals and constraints. | Allocate responsibilities and explain cross-part collaboration, state ownership and overall operation; leave complete API specifications to their owner. |
| Subsystem Architecture | Show how a justified responsibility group realizes the guarantees allocated by its parent. | Connect external commitments to internal organization, mechanisms and local operation. |
| Module Design | Show how one cohesive function implements its operations, rules and processing flow. | Explain functional decisions, state changes, transactions and dependency coordination. |
| Component Architecture (component design) | Show how an encapsulated implementation mechanism realizes its usage contract. | Explain internal structure, algorithms, concurrency, lifecycle and resource guarantees. |

Explain that these are optional design granularities, not a compulsory four-level hierarchy. A simple system may contain modules directly; a component may be private to a module or shared by several. Justify a separate document by its independent reader task and maintenance value. Keep topic and supporting documents tied to their actual questions rather than expanding this primary family by default.

Explain the four viewpoints through the questions they contribute: **Domain** checks concepts, rules, state and invariants; **Application** checks behavior and state owners, contracts and collaboration; **Governance** checks authority, permitted actions, controls and evidence; **Runtime** checks deployment conditions, resources, load, failures and recovery. Describe their three entry points: identify drivers before choosing a design, reason through success and failure scenarios while making choices, and check claims and evidence after drafting. Locate the resulting explanation beside the design it supports. Use separate viewpoint documents only when an independent reader task warrants them, for either purpose.

When asked why the templates have matching chapter counts, inspect the current assets and distinguish the default outline from a fixed-count requirement. Explain the reading progression from goals and boundaries through structure, state and behavior to operation, validation and evolution. Apply the Shared Method's adaptation criteria; assess relevant responsibility coverage rather than equal chapter counts, section lengths or document counts.

For a concrete usage question, identify the purpose and authority, select the independently useful document responsibility, then recommend its owning Writer with the relevant scope in the invocation. Explain that the Writer applies viewpoint reasoning internally; a separate `$Reason Arch` invocation is only for an independently requested reasoning result. Complete the explanation when the user can say why this template fits, how purpose changes its content and where viewpoints affect the design.

## Complete invocations

- Domain Knowledge structure: `$Structure Domain Docs`
- Domain Knowledge document: `$Write Domain Doc`
- Architecture Knowledge systems and individual documents: `$Write Arch Knowledge`
- Product Documentation structure: `$Structure Product Docs`
- Product Internal Document Type: `$Write Product Doc`
- Product lifecycle assessment: `$Assess Product Lifecycle`
- Technical Documentation structure: `$Structure Tech Docs`
- Technical Internal Document Type: `$Write Tech Doc`
- Company Technical Architecture or Project architecture delivery: `$Write Tech Arch`
- Dedicated prose revision or review: `$Write Doc`
- Presentation manuscript: `$Write Deck`
- Standalone visual creation or revision: `$Draw Diagram`

Architecture Writers share structural templates while retaining distinct Knowledge, Company and Project responsibilities. Recommend by the requested result, without asking the user to invoke another Writer to obtain a template.

Each Public Skill applies the reasoning, structure, prose-quality, and visual-production Shared Methods its own workflow needs. Do not present the former required multi-skill combinations as compatible alternatives.

Product Strategy, Capability Map, Product Roadmap, PRD, and Product Metric System retain their named public skills. Product Release Plan and Product Review remain registered Internal Document Types of `write-product-doc`; compatible removed or occasional Product artifacts use its Freeform fallback. Technical Strategy, Roadmap, System Landscape, System Profile, System and Subsystem Architecture, Module Design, Component Architecture, governance documents, standards, and event records are registered Internal Document Types of `write-technical-doc`; compatible occasional Technical artifacts use its Freeform fallback.

Route natural requests without requiring the user to know a type name:

- Route a presentation, slide-sequenced talk, course deck, business presentation, product introduction, technical explanation, or proposal manuscript to `$Write Deck` when the requested result is the audience-facing deck source rather than an authoritative document or rendered presentation file.
- Route company overall architecture, Product-System Map, or a cross-System concern to `$Write Tech Arch`.
- Route stable System or Subsystem Architecture, Module Design and Component Architecture to `$Write Tech Doc`.
- Route concrete Project architecture delivery, including its necessary detailed design, migration and validation artifacts, to `$Write Tech Arch`.
- Route an architecture knowledge system, view overview, overall/subsystem/module/component reference, governance/runtime topic, strategy or mechanism to `$Write Arch Knowledge`.
- Route a compatible occasional Product or Technical document to its owning Writer as a Freeform Artifact.
- Route a Product directory, navigation, scaffold, audit, or migration to `$Structure Product Docs`.
- Route a Technical directory, navigation, scaffold, audit, or migration to `$Structure Tech Docs`.

## Completion

The answer is complete when the user can distinguish the authority scope, understands the recommended skill boundaries, and receives a complete explicit invocation without another workflow having been executed.
