# Domain structure model

Use this model only after the current workflow has established a usable domain boundary by applying the Domain Reasoning Shared Method. Persist a supporting Domain Assessment when the decision needs durable traceability. Read `../write-domain-doc/references/domain-document-types.md` from the skill workflow for the canonical domain document types and their responsibilities.

## Topology decision

Default to the smallest structure supported by current content. Complexity triggers a boundary review; it does not by itself justify more directories.

### Flat domain

Keep knowledge forms at the domain root when no independent subdomain has been accepted:

```text
{domain}/
├── README.md
├── {domain}-essence.md
├── terminology-and-concept-relationships.md
├── core-objects-and-lifecycle.md
├── participants-responsibilities-and-rules.md
├── mechanisms/
├── capabilities-and-solutions/
├── methods-and-practices/
├── cases-and-failures/
└── references/
```

Translate names to the local language and preserve established conventions. The tree is a coverage model, not a command to create every path.

### Domain with subdomains

Use subdomain directories only when the Domain Assessment establishes a parent-or-child relationship and current material needs separate navigation:

```text
{domain}/
├── README.md
├── {domain}-essence.md
├── shared-semantics/
├── {subdomain-one}/
│   ├── README.md
│   └── [materialized knowledge forms]
└── {subdomain-two}/
    └── ...
```

At the domain root, siblings represent shared material or accepted subdomains. Inside a subdomain, siblings represent document types. Keep one dimension per directory level.

A subdomain earns its own essence document only when it has an independent minimum purpose, realities, objects or activities, constraints, and boundary. Keep related domains separate and express handoffs through links.

### Peer domains

Create peer first-level domains when each candidate passes admission but the proposed parent owns no common minimum purpose, language, objects, constraints, or continuous state chain. Preserve their relationships through links and handoff descriptions.

### Rejected structural candidates

Keep software modules, controls that cross all subdomains, product features, organization units, projects, and document types in their true owning location. Do not use them as subdomains merely to balance the tree.

## Materialization

Use four states for every knowledge responsibility:

- **Existing** — a current artifact already owns it.
- **Create now** — current evidence and reader need justify a new artifact in this change.
- **Planned** — the responsibility is real, but content or evidence is not ready; list it in the README without a link.
- **Unresolved** — ownership or boundary is disputed; record the decision needed before creating a path.

Create the root `README.md` and essence document first for a new durable domain only when their evidence is ready. Do not invent essence claims to make a scaffold look complete.

Keep a document as a file while it answers one reader question and needs no independent navigation. Upgrade it to a directory after several independently useful documents exist or a stable internal reading path is required.

Create an empty directory only when the user explicitly requests a complete empty scaffold. Mark that exception in the structure plan.

## README map contract

The root README must expose:

- the accepted domain boundary, exclusions, and destinations;
- current linked knowledge and planned unlinked coverage;
- accepted subdomains and valid entries;
- a default learning path;
- task, case, or lookup entry paths where useful;
- maintenance rules and related-domain links.

The default learning order is map, essence, language and objects, participants and rules, mechanisms, capabilities and methods, cases, then references. This is a cognitive route, not a required reading sequence.

The README is a map, not the container for full explanations or reference data. Every link must resolve when delivered.

## Migration contract

Before an applied migration, record:

- each exact old path and new path;
- every Markdown navigation or cross-reference affected;
- assets whose relative location changes;
- application bindings or external configuration that names the path;
- the approval that authorizes the move, rename, merge, deletion, or overwrite.

Apply an approved migration as one coherent change. Verify that no old path, broken link, duplicate authoritative explanation, or orphaned asset remains.
