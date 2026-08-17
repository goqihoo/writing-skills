---
name: write-technical-architecture
description: Create, revise, or review one company's Technical Architecture across its Technical Landscape, principles, structure, boundaries, relationships, constraints, decisions, and evolution.
disable-model-invocation: true
---

# Write Tech Arch

Produce the company Technical Architecture that governs how its Technical Landscape is structured and evolves.

## Workflow

1. Apply `$Reason Tech Docs` and `$Reason Arch`.
2. Read the Technical Assessment when persisted, Technical navigation, strategy, system landscape and profiles, governance, accepted architecture decisions, and authoritative downstream links.
3. Read `references/technical-architecture-method.md` completely.
4. Establish company scope, current state, target concerns, principles, constraints, decision authority, and material evidence.
5. Separate company facts, accepted architecture decisions, principles, constraints, proposals, downstream System Architecture, Project Documentation, and Machine Authority.
6. Model only the Domain, Application, Governance, and Runtime views needed at company-landscape level. Define boundaries, ownership, critical relationships, controls, failure domains, and evolution.
7. Compare material alternatives against the same drivers. Record accepted costs, rejected options, validation, and review triggers.
8. Use `assets/technical-architecture-template.md`. Link System Profiles and detailed System Architecture rather than copying their design.
9. When `$Draw Diagram` was explicitly invoked by the user, provide the accepted architecture meaning and let it own visual form. Otherwise retain sufficient prose or a table.
10. Update Technical and Architecture navigation, then verify scope, authority, traceability, downstream links, evolution, and explicit unresolved decisions.

## Boundaries

- Own company Technical Architecture across the Technical Landscape.
- Let `$Write Arch Knowledge` own reusable Architecture Knowledge.
- Let detailed System Architecture own one concrete system's design.
- Exclude project delivery architecture, Technical Design, implementation tasks, field schemas, configuration, code, and runbook procedures.

## Completion

The work is complete when principles and constraints shape an explicit company-level structure, boundaries and owners are visible, critical relationships and failure domains are traceable, accepted decisions and costs are recorded, downstream authority links replace copied detail, evolution is governed, and unresolved material choices remain explicit.
