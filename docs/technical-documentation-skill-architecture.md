# Technical Documentation Skill Architecture

## Scope

Technical Documentation is Company Documentation for how one company structures, governs, evolves, protects, and operates its technical capabilities and Systems. It includes company-, System-, and Subsystem-authority architecture while remaining distinct from reusable Technical or Architecture Knowledge, Project Technical Design, and Machine Authority.

## Architecture model

Every architecture artifact names an **Architecture Object** and **Architecture Scope**. Technical Documentation routes authority through Company, System, and Subsystem **Authority Levels** without using those levels as substitutes for object identity.

Architecture analysis selects the relevant foundational domains:

- **Business** — linked capabilities, actors, value, responsibility, policy, concepts, lifecycle, rules, and invariants;
- **Data** — information meaning, authority, lifecycle, lineage, quality, exchange, retention, residency, and privacy;
- **Application** — Applications, Systems, Subsystems, behavior and state ownership, contracts, orchestration, and dependencies;
- **Technology** — platforms, infrastructure, storage, messaging, networks, environments, and deployment mechanisms.

Security, Governance, and Runtime are cross-cutting **Architecture Viewpoints**. Domain, Application, Governance, and Runtime correctness remain coverage checks rather than directories, documents, or fixed headings.

- Company-level Technical Architecture describes the named Technical Landscape as its Architecture Object and a system of Systems.
- System Architecture describes one Registered System's stable internal architecture and evolution.
- Subsystem Architecture describes one justified stable responsibility inside a System.

Products and Systems have many-to-many relationships. An Application is a runnable or audience-specific entry within a System. Codebases and Runtime Units realize architecture but do not define these objects by themselves. Deployment Architecture describes topology and placement; a Runtime View describes operating, failure, degradation, observability, and recovery behavior.

## Structure

Strategy, Architecture, Systems, and Governance are logical Stable Responsibilities. Reuse the documentation set's language for their directory names. Every Registered System requires this minimum core:

```text
Systems/
└── <System>/
    ├── README.md
    └── System Architecture.md
```

The README is the System Responsibility README and System Profile. Materialize a Subsystem directory only when its responsibility, complexity, independent reader task, and continuing maintenance value justify it.

Platform, Engineering, Data, Security, Quality, and Operations may become Type Extensions for proven cross-System responsibility. A concrete platform that satisfies the System test is also registered under Systems. Architecture Decisions name their object and scope and belong at the narrowest governing Authority Level. Product-System Map and Architecture Topics are conditional rather than default directories.

## Public skills

| Skill | Ownership |
| --- | --- |
| **Reason Tech Docs** (`reason-technical`) | Company technical scope, Technical Landscape, Registered System admission, authority routing, and Technical Assessment decisions. |
| **Structure Tech Docs** (`structure-technical-docs`) | Technical topology, navigation, Registered System core, materialization, audits, and approved migration. |
| **Write Tech Doc** (`write-technical-doc`) | Registered and freeform Technical artifacts, including stable System and Subsystem Architecture, Module Design, Component Architecture, and Database Design. |
| **Write Tech Arch** (`write-technical-architecture`) | Company-level Technical Architecture, Product-System Map, cross-System Architecture Topics, and a separate Project delivery architecture branch. |

## Internal Document Types

Each Technical Writer owns one YAML registry. The generated [Internal Document Type catalog](internal-document-types.md) is the readable inventory. A registered type has a stable identity, description, reader question, authority boundary, and completion profile. A template is optional; absence means Freeform Structure. Compatible occasional work remains a Freeform Artifact and does not create a permanent type automatically.

`write-technical-architecture` registers Technical Architecture and Product-System Map. A cross-System Architecture Topic remains freeform. `write-technical-doc` registers the smaller set of recurring strategy, roadmap, system, governance, standard, decision, exception, and incident artifacts, including System and Subsystem Architecture.

## Authority boundaries

Database Design is a registered supporting design under the owning System or Subsystem authority. Use the shared [database writing contract](../methods/references/database-design-writing.md) for embedded or standalone placement, scope-based detail and verification. Project database delivery uses the same template under Write Tech Arch's separate delivery registry entry. Neither registration creates another Public Skill, architecture granularity or mandatory System-core file.

System and Subsystem Architecture link interface definitions, deployments, configuration, schemas, code, tests, and runbooks in Machine Authority instead of copying them. Project Technical Design owns a bounded proposed change for a delivery effort. Company-level architecture links the governing System Architecture. Higher Authority Levels link or summarize lower-level decisions without duplicating their authoritative records.

Business and Product facts remain in their owning Company Documentation authorities. Technical Architecture records their structural consequences without redefining them.

## Completion contract

The Technical system is coherent when the logical Stable Responsibilities remain distinct in local language, every Registered System has its README and System Architecture, Architecture Objects, Scopes, Domains, Viewpoints, and Authority Levels are not conflated, conditional extensions and collections have evidence, each Writer's YAML remains the sole type configuration authority, active templates exactly match configured assignments, and Machine, Project, Product, and Business authorities remain linked rather than copied.

## Company architecture presentation

Technical Architecture now uses a registered adaptive template: lead with a comprehensible overall structure, explain responsibilities and exchanges, then cover data/runtime boundaries, choices and evolution. Delivery status and decision status are independent. System and Subsystem Architecture remain under Write Tech Doc and now use separately registered adaptive templates, preserving the existing coverage contract while providing a structural overview, concrete behavior, design rationale, and validation. This addresses observed documents that were complete as checklists but did not reveal the overall architecture.

## Project delivery branch

Write Tech Arch owns Project delivery architecture, not the broader project-management artifact system. Its overall, subsystem, module, component and deployment types reuse shared architecture templates with the concrete-design profile. Delivery entry, migration and validation remain specific supplements. All link stable company/System authority. Project proposals do not overwrite stable design by default. Write Tech Doc retains stable architecture ownership; Module Design and Component Architecture inherit their governing System or Subsystem Authority Level. When the user explicitly asks Write Tech Arch to handle such a stable design, apply the shared explicit-adaptation branch and the owning stable registry; preserve the document's authority and avoid inventing a Project identity.
