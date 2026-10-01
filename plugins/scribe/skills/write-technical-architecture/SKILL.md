---
name: write-technical-architecture
description: Create, revise, or review company Technical Architecture or a concrete project architecture delivery, including its necessary subsystem, component, deployment, migration, and validation documents.
---

# Write Tech Arch

Produce company Technical Architecture for a Technical Landscape or a coherent Project delivery architecture at the requested scope.

## Workflow

1. Read `../../methods/architecture-reasoning.md`, `../../methods/architecture-documents.md`, and `../../methods/internal-document-types.md`.
2. Establish whether the result is company-level architecture or Project delivery architecture. Use the user's intended authority and lifetime, not the word "architecture" alone. Read the target, actual sources, existing navigation and governing decisions.
3. For company work, read `../../methods/technical-reasoning.md` and `references/technical-architecture-method.md`; identify the named Technical Landscape and Company Authority Level. For project work, read `references/delivery-architecture-method.md`; establish the delivery object, baseline, requirements and acceptance boundary.
4. Read `references/internal-document-types.yaml`. Select the registered type and its actual template. Treat a compatible cross-System Architecture Topic or occasional Project architectural artifact as a Freeform Artifact. For a Project delivery set, choose its main artifact and only necessary supporting types.
5. Read the selected assets. Develop structure, responsibilities, state, contracts, key flows, controls, deployment, material alternatives and validation at the requested level. Use the template fields and figure slots to express the architecture; preserve explicit user structure and output format.
6. Keep observed facts, proposals, accepted decisions and implementation state distinct. For Project delivery, record material reference-knowledge adoption and compatibility/migration constraints. For company work, link governing System Architecture instead of copying internal design.
7. Read `../../methods/visual-production.md` when a visual is requested or materially improves understanding, and `../../methods/prose-quality.md` before delivery. Use a principal view and responsibility explanation for a multi-System architecture.
8. Update directly affected real navigation for document-set work; allow standalone documents without invented navigation. Verify the selected completion profile, the architecture-document reader checks and the relevant branch's completion conditions. Remove unfilled placeholders and unused figure slots.

## Boundaries

- Own company-level Technical Architecture, Product-System Map, cross-System Architecture Topics, and Project delivery architecture with its directly required supporting documents.
- Let `$Write Arch Knowledge` own reusable Architecture Knowledge and its document system.
- Let `$Write Tech Doc` own stable System Architecture, Subsystem Architecture and Component Architecture. Keep Project proposals linked to those authorities rather than overwriting them.
- Exclude implementation tasks, executable field schemas, configuration, code and runbook procedures; summarize architecture-significant contracts and link Machine Authority.

## Completion

Complete when the named company or Project scope has an intelligible principal structure, consistent ownership and contracts, traceable choices and evidence, and explicit current/target, proposal/acceptance and unresolved-risk distinctions. For multi-file delivery, verify its main entry and supporting artifacts form one coherent reviewable set. Keep unverified acceptance and unsupported commitments explicit.
