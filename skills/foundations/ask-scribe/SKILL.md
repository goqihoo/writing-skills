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
5. Explain the smallest suitable skill or sequence. Name every required coordination, structure, and artifact skill plus any optional writing or visual skill that serves the request.
6. Return ready-to-type display-name invocations such as `$Ask Scribe` or `/Ask Scribe` when useful. Mention the canonical Skill ID as the compatible alternative when introducing a skill.
7. Do not invoke another skill, perform its workflow, modify files, or produce an artifact owned by another skill.

## Materialization and interface language

- **Stable Responsibility:** default home for a continuing accepted responsibility.
- **Type Extension:** materialize only when independent ownership, governance, or navigation is proven.
- **Event Collection:** materialize with the first real event document.
- **Internal Document Type:** a standard artifact branch inside `write-product-doc` or `write-technical-doc`.
- **Explicit Skill Composition:** the user names every required Public Skill; a missing dependency causes the invoked skill to stop and return the complete invocation.
- **Skill ID:** the canonical machine name used by the directory, frontmatter, manifests, and code.
- **Skill Display Name:** the exact user-facing invocation name from `agents/openai.yaml`; it is unique and equivalent to the Skill ID.

## Skill guide

| Result | Skill | Boundary |
| --- | --- | --- |
| Understand Scribe or choose a workflow | **Ask Scribe** (`ask-scribe`) | Explain only; do not execute. |
| Place files, define directory responsibilities, or plan a migration | **Structure Docs** (`structure-docs`) | Own information architecture, not artifact meaning. |
| Run a dedicated reader-flow and prose-quality pass | **Write Doc** (`write-doc`) | Optional; own presentation, not genre meaning. |
| Apply four-view architecture reasoning | **Reason Arch** (`reason-architecture`) | Own the method, not an artifact. |
| Admit and bound reusable Domain Knowledge | **Reason Domain** (`reason-domain`) | Own the Domain Assessment. |
| Resolve a company portfolio, product line, product, capability, or extension | **Reason Product** (`reason-product`) | Own Product Assessment decisions. |
| Resolve company technical scope, ownership, authority, or extension | **Reason Tech Docs** (`reason-technical`) | Own Technical Assessment decisions. |
| Structure an accepted Domain Knowledge set | **Structure Domain Docs** (`structure-domain-docs`) | Own domain topology and navigation. |
| Write a common Domain Knowledge document | **Write Domain Doc** (`write-domain-doc`) | Own its internal domain document types. |
| Write general reusable Knowledge | **Write Knowledge** (`write-knowledge`) | Own concepts, mechanisms, methods, patterns, cases, and references. |
| Write reusable Architecture Knowledge | **Write Arch Knowledge** (`write-architecture-knowledge`) | Do not make one company's implementation commitment. |
| Assess a product decision and artifact coverage | **Assess Product Lifecycle** (`assess-product-lifecycle`) | Own the Product Lifecycle Assessment, not missing artifacts. |
| Structure company Product Documentation | **Structure Product Docs** (`structure-product-docs`) | Own Product topology and materialization. |
| Write a standard Product document | **Write Product Doc** (`write-product-doc`) | Own its listed Internal Document Types and route public artifacts. |
| Define product direction | **Write Product Strategy** (`write-product-strategy`) | Own durable strategy. |
| Model product capabilities | **Map Product Capabilities** (`map-product-capabilities`) | Own capability responsibility and relationships. |
| Sequence product outcomes and decisions | **Write Product Roadmap** (`write-product-roadmap`) | Own product sequence, not tasks. |
| Define one product change | **Write PRD** (`write-prd`) | Own observable behavior and acceptance. |
| Define the product metric system | **Design Product Metrics** (`design-product-metrics`) | Own measure semantics and governance. |
| Structure company Technical Documentation | **Structure Tech Docs** (`structure-technical-docs`) | Own Technical topology and materialization. |
| Write a standard Technical document | **Write Tech Doc** (`write-technical-doc`) | Own its listed Internal Document Types. |
| Define company Technical Architecture | **Write Tech Arch** (`write-technical-architecture`) | Own Technical Landscape structure, not detailed System Architecture. |
| Create one technical visual | **Draw Diagram** (`draw-diagram`) | Own visual form; the source skill owns meaning. |

## Common complete invocations

- Domain Knowledge structure: `$Structure Domain Docs $Reason Domain $Structure Docs`
- Domain Knowledge document: `$Write Domain Doc $Reason Domain`
- Architecture Knowledge: `$Write Arch Knowledge $Reason Arch`
- Product Documentation structure: `$Structure Product Docs $Reason Product $Structure Docs`; add `$Write Product Doc` when navigation or Responsibility README bodies are requested.
- Product Internal Document Type: `$Write Product Doc $Reason Product`
- Product lifecycle assessment: `$Assess Product Lifecycle $Reason Product`
- Technical Documentation structure: `$Structure Tech Docs $Reason Tech Docs $Structure Docs`; add `$Write Tech Doc` when navigation or Responsibility README bodies are requested.
- Technical Internal Document Type: `$Write Tech Doc $Reason Tech Docs`
- Company Technical Architecture: `$Write Tech Arch $Reason Tech Docs $Reason Arch`
- Visual inside another artifact: add `$Draw Diagram` explicitly to the complete document invocation.
- Dedicated prose-quality pass: add `$Write Doc` explicitly to any composition when wanted.

Product Strategy, Capability Map, Product Roadmap, PRD, and Product Metric System retain their named public skills. Product Solution, Product Release Plan, and Product Review are Internal Document Types of `write-product-doc`. Technical Strategy, Roadmap, System Landscape, System Profile, governance documents, standards, extension documents, and event records are Internal Document Types of `write-technical-doc`.

## Completion

The answer is complete when the user can distinguish the authority scope, understands the recommended skill boundaries, and receives a complete explicit invocation without another workflow having been executed.
