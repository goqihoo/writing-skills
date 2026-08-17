---
name: ask-scribe
description: Explain Scribe's skills, authority boundaries, composition rules, and complete explicit invocation choices without executing another skill or producing its artifact.
disable-model-invocation: true
---

# Ask Scribe

Explain and recommend. Leave every subsequent invocation and execution to the user.

## Guidance

1. Answer the user's question about Scribe, its skills, boundaries, or composition.
2. Inspect the installed `SKILL.md` files before describing current behavior.
3. Identify the intended result, authority scope, reader decision, artifact lifetime, and requested output.
4. Distinguish reusable **Knowledge**, company-owned **Product Documentation** or **Technical Documentation**, and engagement-owned **Project Documentation**.
5. Explain the smallest suitable skill or sequence. Name every coordination, structure, artifact, shared-writing, and optional visual skill required.
6. Return ready-to-type `$skill-name` or `/skill-name` invocations when useful.
7. Do not invoke another skill, perform its workflow, modify files, or produce an artifact owned by another skill.

## Materialization and interface language

- **Stable Responsibility:** default home for a continuing accepted responsibility.
- **Type Extension:** materialize only when independent ownership, governance, or navigation is proven.
- **Event Collection:** materialize with the first real event document.
- **Internal Document Type:** a standard artifact branch inside `write-product-doc` or `write-technical-doc`.
- **Explicit Skill Composition:** the user names every required Public Skill; a missing dependency causes the invoked skill to stop and return the complete invocation.

## Skill guide

| Result | Skill | Boundary |
| --- | --- | --- |
| Understand Scribe or choose a workflow | `ask-scribe` | Explain only; do not execute. |
| Place files, define directory responsibilities, or plan a migration | `structure-docs` | Own information architecture, not artifact meaning. |
| Apply the shared prose contract | `write-doc` | Own reader flow and presentation, not genre meaning. |
| Apply four-view architecture reasoning | `reason-architecture` | Own the method, not an artifact. |
| Admit and bound reusable Domain Knowledge | `reason-domain` | Own the Domain Assessment. |
| Resolve a company portfolio, product line, product, capability, or extension | `reason-product` | Own Product Assessment decisions. |
| Resolve company technical scope, ownership, authority, or extension | `reason-technical` | Own Technical Assessment decisions. |
| Structure an accepted Domain Knowledge set | `structure-domain-docs` | Own domain topology and navigation. |
| Write a common Domain Knowledge document | `write-domain-doc` | Own its internal domain document types. |
| Write general reusable Knowledge | `write-knowledge` | Own concepts, mechanisms, methods, patterns, cases, and references. |
| Write reusable Architecture Knowledge | `write-architecture-knowledge` | Do not make one company's implementation commitment. |
| Assess a product decision and artifact coverage | `assess-product-lifecycle` | Own the Product Lifecycle Assessment, not missing artifacts. |
| Structure company Product Documentation | `structure-product-docs` | Own Product topology and materialization. |
| Write a standard Product document | `write-product-doc` | Own its listed Internal Document Types and route public artifacts. |
| Define product direction | `write-product-strategy` | Own durable strategy. |
| Model product capabilities | `map-product-capabilities` | Own capability responsibility and relationships. |
| Sequence product outcomes and decisions | `write-product-roadmap` | Own product sequence, not tasks. |
| Define one product change | `write-prd` | Own observable behavior and acceptance. |
| Define the product metric system | `design-product-metrics` | Own measure semantics and governance. |
| Structure company Technical Documentation | `structure-technical-docs` | Own Technical topology and materialization. |
| Write a standard Technical document | `write-technical-doc` | Own its listed Internal Document Types. |
| Define company Technical Architecture | `write-technical-architecture` | Own Technical Landscape structure, not detailed System Architecture. |
| Create a technical visual | `draw-diagrams` | Own visual form; the source skill owns meaning. |

## Common complete invocations

- Domain Knowledge structure: `$structure-domain-docs $reason-domain $structure-docs $write-doc`
- Domain Knowledge document: `$write-domain-doc $reason-domain $write-doc`
- Architecture Knowledge: `$write-architecture-knowledge $reason-architecture $write-doc`
- Product Documentation structure: `$structure-product-docs $reason-product $structure-docs $write-doc`; add `$write-product-doc` when navigation or Responsibility README bodies are requested.
- Product Internal Document Type: `$write-product-doc $reason-product $write-doc`
- Product lifecycle assessment: `$assess-product-lifecycle $reason-product $write-doc`
- Technical Documentation structure: `$structure-technical-docs $reason-technical $structure-docs $write-doc`; add `$write-technical-doc` when navigation or Responsibility README bodies are requested.
- Technical Internal Document Type: `$write-technical-doc $reason-technical $write-doc`
- Company Technical Architecture: `$write-technical-architecture $reason-technical $reason-architecture $write-doc`
- Visual inside another artifact: add `$draw-diagrams` explicitly to the complete document invocation.

Product Strategy, Capability Map, Product Roadmap, PRD, and Product Metric System retain their named public skills. Product Solution, Product Release Plan, and Product Review are Internal Document Types of `write-product-doc`. Technical Strategy, Roadmap, System Landscape, System Profile, governance documents, standards, extension documents, and event records are Internal Document Types of `write-technical-doc`.

## Completion

The answer is complete when the user can distinguish the authority scope, understands the recommended skill boundaries, and receives a complete explicit invocation without another workflow having been executed.
