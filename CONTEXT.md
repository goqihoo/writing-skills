# Scribe

Scribe is a collection of composable skills for producing and organizing professional documentation. Its language distinguishes general knowledge that is not tied to one company from documentation whose authority belongs to a particular company or project, while treating coordination as a skill role rather than a content class.

## Language

**Knowledge**:
A reusable explanation, model, method, pattern, case, or reference whose applicability is not tied to one company, product implementation, technical estate, or project. Its subject may be a domain, product practice, technology, architecture, or another field.
_Avoid_: Company Documentation, Project Documentation

**Domain Knowledge**:
General knowledge that explains the language, participants, rules, mechanisms, cases, and practices of a business or problem domain without binding them to one company.
_Avoid_: Company-specific policy or operating documentation

**Product Knowledge**:
General knowledge about product concepts, methods, models, practices, and recurring cases that remains useful across companies and products.
_Avoid_: Product Documentation

**Technical Knowledge**:
General knowledge about technologies, architecture, engineering methods, mechanisms, patterns, and recurring cases that remains useful across companies and systems.
_Avoid_: Technical Documentation

**Company Documentation**:
The records and standards whose truth, authority, and currency belong to one particular company.
_Avoid_: Knowledge, Project Documentation

**Company Documentation Set**:
The governed company-level collection that contains Product Documentation and Technical Documentation under one named organizational scope.
_Avoid_: Knowledge Set, Project Documentation Set

**Product Documentation**:
Company Documentation for how one company defines, organizes, governs, evolves, measures, and operates its commercial products.
_Avoid_: Product Knowledge

**Technical Documentation**:
Company Documentation for how one company structures, governs, evolves, secures, and operates its technical capabilities and systems.
_Avoid_: Technical Knowledge

**Project Documentation**:
The customer-, contract-, initiative-, or engagement-specific records that govern scope, plan, delivery state, and acceptance for one project.
_Avoid_: Product Documentation, Technical Documentation

**Knowledge Set**:
A governed collection of general Knowledge organized for continued use across companies, products, systems, or projects.
_Avoid_: Product Documentation Set, Technical Documentation Set, Project Documentation Set

**Product Documentation Set**:
The governed collection of Product Documentation for one company and its commercial products.
_Avoid_: Product Knowledge Set

**Product Portfolio**:
The products and product lines that one company governs together as investments, including their relationships, ownership, lifecycle, and shared constraints.
_Avoid_: Treating the company itself as one product

**Technical Documentation Set**:
The governed collection of Technical Documentation for one company's technical capabilities and systems.
_Avoid_: Technical Knowledge Set

**Technical Landscape**:
The company-specific view of technical capabilities, platforms, systems, ownership, dependencies, and lifecycle across the organization.
_Avoid_: Technical Knowledge, one system's implementation documentation

**Company Product Core**:
The default stable responsibilities `Portfolio/`, `Governance/`, and `Products/` within one company's `Product/` documentation root. Each accepted product receives `Definition/`, `Capabilities/`, `Planning/`, and `Measurement/` beneath `Products/{Product}/`.
_Avoid_: Pre-creating event or type-extension directories

**Company Technical Core**:
The default stable responsibilities `Strategy/`, `Architecture/`, `Systems/`, and `Governance/` within one company's `Technical/` documentation root.
_Avoid_: Treating a code repository's documentation layout as the company technical structure

**Project Documentation Set**:
The governed collection of Project Documentation for one customer, contract, initiative, or engagement.
_Avoid_: Product Documentation Set, Technical Documentation Set

**Coordination Skill**:
A skill that resolves boundaries, readiness, coverage, placement, or workflow without owning the target artifact body.
_Avoid_: Delivery Skill

**Artifact Skill**:
A user-invoked skill that owns either one high-frequency reader-facing artifact boundary or one coherent document family, together with its routing workflow and completion tests.
_Avoid_: Coordinator, Foundation

**Public Skill**:
An explicit user-invoked interface justified by a recurring task, distinct reasoning or workflow, and a checkable completion contract. A directory responsibility, document title, or template does not by itself justify a Public Skill.
_Avoid_: One skill per document type

**Skill ID**:
The canonical lower-case hyphenated name shared by a Public Skill's directory and `SKILL.md` frontmatter. It remains stable in paths, manifests, code, and machine-facing references and is also a valid invocation name.
_Avoid_: Skill Display Name, translated name, temporary alias

**Skill Display Name**:
The exact, unique user-facing name declared by `agents/openai.yaml` `interface.display_name`. It is the preferred invocation name in prompts, guides, and catalogs while the Skill ID remains the machine identifier.
_Avoid_: Fuzzy label, localized variant, duplicate display name

**Invocation Name**:
Either the exact Skill ID or the exact Skill Display Name accepted to invoke one Public Skill. Client syntax adds `$` for Agent Skills clients or `/` for Claude Code.
_Avoid_: Directory path, approximate spelling

**Dual-name Invocation**:
The Public Skill contract in which one stable Skill ID and one exact Skill Display Name are equivalent Invocation Names. It guarantees configured spelling, capitalization, and spacing only; previous display names and fuzzy normalization are not compatibility interfaces.
_Avoid_: Alias collection, case-insensitive matching, automatic normalization

**High-Frequency Documentation Task**:
A documentation task that recurs across multiple companies or multiple products and repeatedly requires the same distinct reasoning, workflow, and completion contract. Frequency describes cross-scope recurrence, not how many times the document is edited in a month.
_Avoid_: Treating importance, a directory, or a standard template alone as frequency

**Internal Document Type**:
A named artifact branch, template, or completion profile owned by a broader Artifact Skill rather than exposed as a separate invocation. Promote it to a Public Skill only after repeated use proves independent reasoning, workflow, and completion needs.
_Avoid_: Treating every standard company document as a separate skill

**Common Writer**:
A Public Artifact Skill that routes one coherent company-document family to Internal Document Types. `write-product-doc` owns common Product Documentation types and `write-technical-doc` owns common Technical Documentation types while routing independently owned high-frequency artifacts to their Public Skills.
_Avoid_: Hidden invocation of another Public Skill, unbounded miscellaneous writer

**Explicit Skill Composition**:
A workflow in which the user explicitly names every required coordination, structure, and artifact Public Skill plus any optional writing or visual workflow they want. Every Public Skill disables model invocation and implicit invocation. A skill that detects a missing required dependency stops, explains the gap, and returns a complete ready-to-type invocation; it never invokes the missing skill itself. Selecting an Internal Document Type already owned by the invoked Common Writer is routing within that skill, not another skill invocation.
_Avoid_: Implicit skill chaining

**Stable Responsibility**:
A documentation responsibility that exists continuously for the accepted company, product, or technical scope and therefore receives a default home.
_Avoid_: Creating an event collection merely because its events are common

**Type Extension**:
A documentation responsibility materialized only when the company's product or technical model proves that the responsibility has independent ownership, governance, or navigation needs.
_Avoid_: Optional directory created without evidence

**Event Collection**:
A collection whose entries exist only after decisions, initiatives, releases, incidents, exceptions, or other events occur; create it with the first real entry rather than during the default scaffold.
_Avoid_: Stable Responsibility

**Responsibility README**:
A concise navigation and ownership map for one materialized documentation responsibility. It states what belongs there, what remains authoritative elsewhere, and which real documents currently exist without inventing placeholder facts.
_Avoid_: Empty directory marker, duplicated document body

**Assessment Record**:
A persisted Product Assessment or Technical Assessment used when a disputed boundary, type extension, or migration decision needs durable traceability. Simple scaffolding may keep the assessment within the execution instead of creating a permanent file.
_Avoid_: Readiness document, lifecycle event, mandatory scaffold artifact

**Architecture Knowledge**:
Reusable knowledge about architectural boundaries, ownership, contracts, controls, failure, validation, alternatives, and evolution without committing one concrete system to an implementation.
_Avoid_: Study Architecture, Technical Architecture

**Technical Architecture**:
The company-specific account of the accepted structure, principles, boundaries, relationships, constraints, and evolution of its technical landscape.
_Avoid_: Delivery Architecture, Architecture Knowledge, one repository's implementation design

**System Architecture**:
The detailed architectural account of one concrete system. Company Technical Documentation may link to it while retaining only the company-level system profile, ownership, lifecycle, and cross-system relationships.
_Avoid_: Technical Architecture, System Profile

**System Profile**:
The company-level record of one system's purpose, ownership, lifecycle, critical relationships, governance state, and authoritative downstream links without copying implementation detail.
_Avoid_: System Architecture, code or configuration inventory

**Technical Design**:
A bounded project or downstream-system proposal for how one technical change should alter a concrete system. It is outside the current company Technical Documentation skill scope.
_Avoid_: Technical Architecture, System Profile

**Knowledge Adoption**:
An explicit `Adopt`, `Adapt`, or `Reject` decision that determines how general Knowledge influences Company or Project Documentation without becoming an automatic commitment.
_Avoid_: Copying Knowledge into company or project documentation without recording applicability

**Knowledge Candidate**:
A scoped lesson proposed for later extraction, decontextualization, and validation as reusable Knowledge.
_Avoid_: Treating a product review, incident review, or ADR as reusable Knowledge by default

**Machine Authority**:
An executable artifact such as a schema, migration, configuration definition, test, or codebase that owns a field- or behavior-level fact more reliably than duplicated prose.
_Avoid_: Repeating the full executable definition in documentation
