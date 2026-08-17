# Technical Documentation Skill Architecture

## Scope

Technical Documentation is Company Documentation for how one company structures, governs, evolves, protects, and operates its technical capabilities and systems. It is distinct from reusable Technical or Architecture Knowledge, Project Documentation, detailed System Architecture, and Machine Authority.

## Structure

The Stable Responsibilities are:

```text
Technical/
├── Strategy/
├── Architecture/
├── Systems/
└── Governance/
```

`Platforms/`, `Engineering/`, `Data/`, `Security/`, `Quality/`, and `Operations/` are Type Extensions created only for proven independent ownership, governance, or navigation. `Architecture/Decisions/`, `Governance/Exceptions/`, and `Operations/Incidents/` are Event Collections created with the first real event and only beneath an existing parent responsibility.

## Public skills

| Skill | Ownership |
| --- | --- |
| **Reason Tech Docs** (`reason-technical`) | Company technical scope, Technical Landscape, ownership, authority, materialization admission, and Technical Assessment decisions. |
| **Structure Tech Docs** (`structure-technical-docs`) | Technical topology, navigation, materialization, scaffolding, audits, and approved migration. |
| **Write Tech Doc** (`write-technical-doc`) | Technical Common Writer and its Internal Document Types. |
| **Write Tech Arch** (`write-technical-architecture`) | Company Technical Architecture across principles, boundaries, relationships, constraints, decisions, and evolution. |

## Common Writer boundary

`write-technical-doc` owns Technical navigation, Strategy, Roadmap, System Landscape, System Profile, Operating Model, Governance, Standards, extension documents, Architecture Decisions, Governance Exceptions, and Incident Records or Reviews. Company Technical Architecture retains its independent public skill.

## Architecture boundaries

`write-architecture-knowledge` owns reusable Architecture Knowledge without a company commitment. `write-technical-architecture` owns company Technical Architecture across the Technical Landscape. Detailed System Architecture owns one concrete system. Project Technical Design remains outside this release.

A System Profile retains company purpose, ownership, lifecycle, critical relationships, governance state, and authoritative links. It does not copy interface definitions, deployment, configuration, schemas, code, tests, or runbook procedures.

## Explicit Skill Composition

Technical artifacts explicitly include `$Reason Tech Docs`. Company Technical Architecture also explicitly includes `$Reason Arch`. Add `$Write Doc` for a dedicated prose-quality pass or `$Draw Diagram` when the user requests one visual. Internal Document Type selection stays inside `write-technical-doc`.

## Completion contract

The Technical system is coherent when the four Stable Responsibilities remain distinct, every Type Extension and Event Collection has its required evidence, every standard document has one Internal Document Type completion profile, architecture authority is unambiguous, and Machine Authority is linked rather than copied.
