# Domain Knowledge Skill Architecture

Status: Accepted

## Purpose

This architecture turns the method in the maintainer knowledge note `Domain/领域知识体系搭建方法.md` into explicit Scribe interfaces. The source method distinguishes four jobs that previously overlapped: proving that a domain exists, organizing a domain knowledge set, writing one domain artifact, and routing material that belongs to another content class.

The runtime plugin must carry the required method itself. It must not depend on the maintainer's local vault path, and it must not copy the complete method into several skills.

## Decision

Use three domain-specific modules behind three explicit skill interfaces:

| Skill | Interface | Owns | Excludes |
| --- | --- | --- | --- |
| **Reason Domain** (`reason-domain`) | Assess one candidate domain or disputed knowledge boundary | Admission, boundary, relationships, subdomain validity, high-level content ownership, maturity, review triggers, and the `Domain Assessment` handoff | Directory topology, file operations, and document bodies |
| **Structure Domain Docs** (`structure-domain-docs`) | Plan, audit, scaffold, or migrate one accepted domain knowledge set | Material inventory, topology, materialization, coverage, navigation requirements, scaffolding, migration mapping, and structural verification | Re-running domain admission and drafting artifact bodies |
| **Write Domain Doc** (`write-domain-doc`) | Create, revise, or review one common domain document | Artifact classification, one internal document contract, evidence, content, canonical sibling links, and artifact verification | Domain admission and whole-set restructuring |

Existing shared modules retain separate responsibilities:

- **Write Doc** (`write-doc`) offers an optional dedicated reader-flow and prose-quality pass.
- **Structure Docs** (`structure-docs`) owns repository-wide taxonomy and cross-class placement.
- **Write Knowledge** (`write-knowledge`) owns durable knowledge outside the common domain artifact set.
- Architecture, product, company, and project skills own material whose primary truth changes with those contexts.

## Why this seam

The three interfaces align with three independently testable outcomes:

1. A supported domain decision.
2. A coherent knowledge-set structure.
3. One complete document with one reader question.

Deleting `reason-domain` would spread admission and ownership tests across structure and writing. Deleting `structure-domain-docs` would spread topology and migration decisions across every artifact writer. Deleting `write-domain-doc` would expose ten templates and repeated evidence rules to users. Each module therefore hides substantial behavior behind a small interface and concentrates future change in one owner.

Do not split the ten document types into public skills. Domain README, essence, terminology, object lifecycle, participants and rules, mechanism, capability and solution space, method and practice, case and failure, and reference are internal branches of `write-domain-doc`. Their stable schemas remain assets and their conditional reasoning remains one-level references.

## Domain Assessment

`Domain Assessment` is the handoff from reasoning to structure and writing. It records:

- `Accept`, `Do not accept`, or `Needs evidence`;
- minimum purpose and core objects or activities;
- shared language and constraints;
- change authority and reusability;
- included knowledge, exclusions, and destinations;
- parent-or-child, related, and handoff relationships;
- subdomain decisions;
- one primary content class for each assessed material;
- maturity, review triggers, and unresolved questions.

`structure-domain-docs` must not propose a domain tree without an `Accept` assessment. `write-domain-doc` must not draft against `Do not accept`, `Needs evidence`, or a materially stale boundary. Missing assessment work produces a ready-to-type explicit invocation rather than an automatic skill call.

## Structure handoffs

The structure workflow produces two stable artifacts:

- `Domain Knowledge Inventory` accounts for every existing and requested material by reader question, change authority, lifetime, content class, domain document type, state, primary home, and structural issue.
- `Domain Structure Plan` records the topology decision, proposed tree, path responsibilities, materialization state, README map contract, migration mapping, unresolved choices, and verification.

Every knowledge responsibility uses one state: `Existing`, `Create now`, `Planned`, or `Unresolved`. Planned content appears in the README without a link. An empty directory requires an explicit full-scaffold request.

## Document branches

`write-domain-doc/references/domain-document-types.md` is the single source of truth for the ten common artifact responsibilities and structure strengths. `structure-domain-docs` reads it as a coverage model; `write-domain-doc` reads it to select exactly one branch.

The essence branch remains an internal module because it has a demanding derivation and fixed schema but no separate user interface. The same rule applies to the other templates: expose a new public skill only when a new independent user task and completion boundary appear, not when an internal branch becomes detailed.

## Explicit invocation

Every Scribe skill is user-invoked. Recommended compositions must name every required skill:

```text
$Reason Domain
```

Use this to assess a candidate domain or disputed ownership boundary.

```text
$Structure Domain Docs $Reason Domain $Structure Docs
```

Use this to propose or audit a domain knowledge structure.

```text
$Write Domain Doc $Reason Domain
```

Use this to create or revise one accepted domain artifact.

Add `$Write Domain Doc` to the structure composition when the same authorized request must also produce the README or other document bodies. A skill never silently invokes another Scribe skill; it returns the complete next invocation when a required interface is missing.

Add `$Write Doc` to any composition when a dedicated reader-flow and prose-quality pass is wanted.

## Repository layout

```text
skills/foundations/reason-domain/
├── SKILL.md
├── agents/openai.yaml
├── references/domain-reasoning-method.md
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

Contract tests must verify:

- all three public skills remain explicitly invoked;
- the plugin, README, and Ask Scribe expose `reason-domain` and complete compositions;
- all six admission criteria, three relationship types, and four maturity states remain in the reasoning method;
- the Domain Assessment keeps its required handoff sections;
- structure consumes domain reasoning and does not automatically invoke the writer;
- the ten artifact types remain internal to one writer and every template remains present;
- default prompts include all required explicit skills;
- the full test suite, shell syntax checks, JSON validation, and `git diff --check` pass.

Forward tests should cover a technology mistaken for a domain, a valid small domain, false subdomains, peer domains with handoffs, a sparse scaffold, a mixed existing directory, a README with planned content, an essence document that avoids becoming a knowledge container, and mechanism-versus-method routing.

## Consequences and review triggers

The design adds one public skill and one explicit dependency to domain workflows. In return, admission logic has one owner, structure no longer legitimizes a weak domain by drawing a tree, and document writers receive a stable boundary instead of inferring one independently.

Review this architecture when domain assessment cannot be reused by both downstream skills, a new artifact has an independent user task rather than an internal branch, individual-skill distribution cannot carry required references, or explicit invocation creates repeated user errors that Ask Scribe and default prompts cannot prevent.
