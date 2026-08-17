# Domain Knowledge Skill Architecture

Status: Accepted

## Purpose

This architecture separates three independently valuable user results: assess a domain boundary, structure a Domain Knowledge set, and create one common domain document. It keeps the reusable domain reasoning method in one internal location without making that implementation step a user-facing dependency.

## Public skills

| Skill | Independently owned result |
| --- | --- |
| **Reason Domain** (`reason-domain`) | A Domain Assessment for a disputed candidate, boundary, relationship, or ownership question. |
| **Structure Domain Docs** (`structure-domain-docs`) | A proposed, audited, scaffolded, or migrated Domain Knowledge structure with real navigation. |
| **Write Domain Doc** (`write-domain-doc`) | One complete common Domain Knowledge document. |

Each skill applies `skills/methods/domain-reasoning.md` internally when its result needs admission, boundaries, relationships, maturity, or content ownership. Structure work also applies `skills/methods/documentation-structure.md`. Every human-readable result applies `skills/methods/prose-quality.md`, and visual production applies `skills/methods/visual-production.md` when requested or materially useful.

## Domain Assessment

A `Domain Assessment` records:

- `Accept`, `Do not accept`, or `Needs evidence`;
- minimum purpose and core objects or activities;
- shared language and constraints;
- change authority and reusability;
- included knowledge, exclusions, and destinations;
- parent-or-child, related, and handoff relationships;
- subdomain decisions;
- one primary content class for each assessed material;
- maturity, review triggers, and unresolved questions.

`Reason Domain` always owns this standalone result. Another Public Skill may create a supporting assessment internally when durable traceability is needed. Routine reasoning can remain inside the execution. A real evidence, approval, or ownership gap may stop unsafe work; an absent `$Reason Domain` invocation may not.

## Structure outputs

`Structure Domain Docs` produces the structure artifacts and navigation requirements needed to complete its request. `Write Domain Doc` retains ownership of Domain README bodies:

- `Domain Knowledge Inventory` accounts for material by reader question, change authority, lifetime, content class, document type, state, home, and structural issue.
- `Domain Structure Plan` records topology, proposed tree, path responsibilities, materialization, README navigation, migration mapping, unresolved choices, and verification.

Every knowledge responsibility uses one state: `Existing`, `Create now`, `Planned`, or `Unresolved`. Planned content appears in a README without a link. An empty directory requires an explicit full-scaffold request.

## Document branches

`skills/knowledge/write-domain-doc/references/domain-document-types.md` owns the ten common artifact responsibilities and structure strengths. `Structure Domain Docs` reads them as a coverage model; `Write Domain Doc` selects exactly one branch.

Domain README, essence, terminology, object lifecycle, participants and rules, mechanism, capability and solution space, method and practice, case and failure, and reference remain Internal Document Types. Promote one only when it gains a recurring independent task, workflow, and completion boundary.

Do not split the ten document types into separate Public Skills merely because their templates differ.

## Invocation

Use one skill for one result:

```text
$Reason Domain
```

```text
$Structure Domain Docs
```

```text
$Write Domain Doc
```

Multiple skills mean the user requested multiple independently owned results. `$Write Doc`, `$Structure Docs`, and `$Draw Diagram` remain standalone skills for standalone goals, not prerequisites.

## Repository layout

```text
skills/methods/
├── domain-reasoning.md
├── documentation-structure.md
├── prose-quality.md
└── visual-production.md

skills/foundations/reason-domain/
├── SKILL.md
├── agents/openai.yaml
└── assets/domain-assessment-template.md

skills/knowledge/structure-domain-docs/
├── SKILL.md
├── agents/openai.yaml
├── references/domain-structure-model.md
└── assets/
    ├── domain-inventory-template.md
    └── domain-structure-plan-template.md

skills/knowledge/write-domain-doc/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── domain-document-types.md
│   └── essence-document-module.md
└── assets/[ten artifact templates]
```

## Verification

Contract tests verify that all three Public Skills remain independently invoked; all reuse one domain method; no skill requires another invocation; the ten Internal Document Types and templates remain present; each default prompt invokes only its own display name; and the full suite, shell syntax checks, JSON validation, and diff checks pass.

## Completion

The architecture is satisfied when the domain method has one internal owner, each Public Skill completes its own result, supporting assessments remain traceable when needed, and users never have to expose an implementation dependency in their invocation.
