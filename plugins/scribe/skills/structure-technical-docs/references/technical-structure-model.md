# Technical Documentation structure model

Technical Documentation belongs to one named company. Treat the names below as logical Stable Responsibilities. Reuse the documentation set's language for directories and navigation rather than imposing English names or capitalization.

## Logical Stable Responsibilities

- **Strategy** — technical direction, roadmap, investment choices, and constraints.
- **Architecture** — company-level Technical Architecture, Product-System Map, cross-System Architecture Topics, and evolution.
- **Systems** — the registry of real Systems and each System's authoritative Technical Documentation.
- **Governance** — decision rights, standards, architecture decisions, and exceptions.

Give the Technical root and each materialized root responsibility a Responsibility README.

## Registered Systems

Register a System only when evidence supports its stable name, technical responsibility boundary, owner, and lifecycle status. Authoritative state, external contracts, independent release, failure boundaries, repositories, deployments, interfaces, and operations are supporting evidence; no one of them is an additional mandatory condition.

Every Registered System has this minimum core:

```text
Systems/
└── <System>/
    ├── README.md
    └── System Architecture.md
```

- `README.md` is the System Responsibility README and System Profile. It records responsibility, boundary, owner, lifecycle, real navigation, and links to Machine Authority and Project Documentation.
- `System Architecture.md` owns the named System Architecture Object and Scope, relevant architecture domains and viewpoints, Applications, Subsystems, information and state authority, contracts, controls, deployment and Runtime behavior, validation, and evolution. It links implementation and operational facts instead of copying them.

Materialize a Subsystem directory only when the Subsystem has a stable independent responsibility, reader question, authority, change cadence, and navigation need. Do not create a central implementation-and-codebase document; repositories and executable facts normally remain with Machine Authority.

## Conditional Architecture material

- Create a Product-System Map only when the company needs a maintained many-to-many view among products, Systems, and capabilities.
- Create an Architecture Topics collection with its first accepted cross-System concern. A product does not automatically receive a topic. Use one only when state ownership, contracts, recovery, joint release, or evolution spans multiple Systems and cannot be governed by one System Architecture.

## Type Extensions

Create only when a cross-System responsibility has independent ownership, governance, or navigation:

- Platform
- Engineering
- Data
- Security
- Quality
- Operations

A concrete platform that satisfies the Registered System test belongs in Systems. “Platform” as a Type Extension is for cross-System policy, capability, or governance, not a substitute for registering a real System.

## Event Collections

Create only with the first real event and when the parent responsibility exists:

- Architecture Decisions — name the Architecture Object and Scope, then place each decision at the narrowest Authority Level that governs it: Company, System, or Subsystem.
- Governance Exceptions — approved deviations from technical governance.
- Operations Incidents — incident records and reviews; materialize only when Operations is justified.

The first real event creates the Event Collection; a default scaffold never creates one. An event cannot justify a missing parent responsibility by itself.

## Migration contract

Before an approved migration, record exact old and new paths, links, assets, external bindings, supersession, and approval. Preserve each material's Architecture Object, Scope, and Authority Level, move decisions to the narrowest governing Authority Level, and verify that no duplicate authority, broken link, orphaned asset, or stale old path remains.
