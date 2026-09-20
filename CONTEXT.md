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

**Product**:
A company-governed value offering and commitment to users that may be realized by multiple Systems and may share those Systems with other Products.
_Avoid_: System, Application, one-to-one Product-to-System mapping

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
The logical stable responsibilities Strategy, Architecture, Systems, and Governance within one company's Technical documentation root. Their directory names follow the documentation set's language rather than mandatory English names.
_Avoid_: Treating a code repository's layout or English directory spelling as the company technical structure

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
An explicit user-invoked interface that owns one independently valuable user result, justified by a recurring task, distinct workflow, and a checkable completion contract. It completes its core workflow without requiring the user to invoke implementation methods as additional Public Skills.
_Avoid_: One skill per document type, exposing an implementation step as a required invocation

**Shared Method**:
An internal, non-invocable method that owns reusable reasoning, structure, prose quality, visual production, or another implementation rule set. Public Skills point directly to only the Shared Methods their workflows need while retaining ownership of user-visible results and completion conditions. A Shared Method has no Invocation Name, lives outside the public skill system, and never appears in the public skill catalog.
_Avoid_: Internal Skill, required Public Skill dependency, Internal Document Type

**Prose Quality Method**:
The Shared Method every Public Skill applies proportionally to its human-readable prose. `$Write Doc` is the independent public entry for a dedicated prose revision or review, not a dependency of other skills.
_Avoid_: Mandatory Write Doc composition, changing exact labels, code, commands, or structured data

**Visual Production Method**:
The Shared Method a Public Skill applies when its requested result includes or materially needs a visual. `$Draw Diagram` is the independent public entry for creating or revising one visual, not a dependency of other skills.
_Avoid_: Mandatory Draw Diagram composition, decorative visual

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
A registered artifact branch owned by a broader Artifact Skill rather than exposed as a separate invocation. Register it only when repeated use or audit-critical consistency justifies a stable identity, authority boundary, and completion profile; a template is optional, and a type without one defaults to Freeform Structure. Promote it to a Public Skill only after repeated use proves independent reasoning, workflow, and completion needs.
_Avoid_: Cataloging every possible document, treating every standard company document as a separate skill, assuming every type requires a template

**Internal Document Type Registry**:
The authoritative configuration for an Artifact Skill's Internal Document Types, including stable identity, reader purpose, authority boundary, completion profile, and optional template assignment. Human guidance explains the registry contract without becoming a conflicting second source of configuration truth.
_Avoid_: Inferring types from asset filenames, duplicating configuration across prose and metadata

**Freeform Structure**:
The default structure policy for an Internal Document Type without an assigned template. The Artifact Skill derives an outline from reader needs, evidence, local healthy conventions, authority boundaries, and the completion profile without asking the user to design routine headings.
_Avoid_: Unbounded writing, missing completion contract, mandatory outline interview

**Freeform Artifact**:
An occasional artifact within an Artifact Skill's authority that does not yet justify a registered Internal Document Type. The owning skill uses its general authority and completion contract without refusing the work or inventing a permanent type; repeated use may later justify registration.
_Avoid_: Miscellaneous dumping ground, automatic type creation, document outside the skill's authority

**Templated Structure**:
The structure policy for an Internal Document Type with an explicitly assigned template. The registry states how strongly the template binds the result; the template does not silently become mandatory merely because an asset file exists.
_Avoid_: Inferring template ownership from filename, treating every template as a fixed schema

**Template Policy**:
The explicitly configured strength of a Templated Structure: `fixed` preserves exact headings, order, and fields; `sequence` preserves reasoning or action order while allowing subject-specific headings; `adaptive` preserves content responsibilities while allowing layout, merging, reordering, and visible omission.
_Avoid_: Treating template presence as an exact-schema requirement, using document purpose as a template-strength label

**Common Writer**:
A Public Artifact Skill that routes one coherent company-document family to Internal Document Types. `write-product-doc` owns common Product Documentation types and `write-technical-doc` owns common Technical Documentation types while routing independently owned high-frequency artifacts to their Public Skills.
_Avoid_: Hidden invocation of another Public Skill, unbounded miscellaneous writer

**Explicit Skill Composition**:
A workflow in which the user names a Public Skill for each independently requested artifact or assessment. Every Public Skill disables model invocation and implicit invocation, completes its own core workflow with Shared Methods, and routes requests for a different owned artifact to that artifact's Public Skill. Selecting an Internal Document Type, applying Shared Methods, and creating a supporting Assessment Record required by the invoked workflow are internal behavior, not additional skill invocation.
_Avoid_: Implicit skill chaining, exposing Shared Methods as required invocations

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
A persisted Domain, Product, or Technical Assessment used when a disputed boundary, type extension, or migration decision needs durable traceability. A Public Skill may create the supporting record by applying its Shared Method; routine reasoning remains within the execution.
_Avoid_: Readiness document, lifecycle event, mandatory scaffold artifact, required Reason Skill invocation

**Architecture Knowledge**:
Reusable knowledge about architectural boundaries, ownership, contracts, controls, failure, validation, alternatives, and evolution without committing one concrete system to an implementation.
_Avoid_: Study Architecture, Technical Architecture

**Technical Architecture**:
The company-level account of the accepted structure, principles, boundaries, relationships, constraints, and evolution of one company's Technical Landscape. Its Architecture Object is the named Technical Landscape and its Authority Level is Company even when its title does not include the word “company.”
_Avoid_: Delivery Architecture, Architecture Knowledge, one repository's implementation design

**Product-System Map**:
The company-level Technical Architecture authority for the many-to-many relationships among Products, Systems, and the capabilities they realize. It links Product and System authorities instead of redefining either one.
_Avoid_: System Landscape, Product Portfolio, one-to-one Product-to-System hierarchy

**Architecture Topic**:
A company-level Technical Architecture artifact for an end-to-end concern whose state ownership, failure, recovery, release, or evolution crosses multiple Systems and cannot be owned by one System Architecture.
_Avoid_: mandatory document per Product, System Architecture, Project Technical Design

**Architecture Object**:
The entity whose architecture is being described, such as a company Technical Landscape, Product, Solution, Business Domain, System, or Subsystem. Scribe's company Technical writers directly govern the company Technical Landscape, System, and Subsystem objects within their authority.
_Avoid_: Architecture Domain, Architecture Viewpoint, Authority Level

**Architecture Scope**:
The selected responsibility and environment boundary around one Architecture Object or decision. It states what is included without replacing the object's stable identity.
_Avoid_: Architecture Object, Authority Level, directory path

**Architecture Domain**:
A foundational family of architecture concerns: Business, Data, Application, or Technology. Domains guide analysis and coverage without becoming mandatory directories, documents, or headings.
_Avoid_: Business Domain as an Architecture Object, Architecture Viewpoint, four-view taxonomy

**Architecture Viewpoint**:
A reusable way to examine cross-cutting stakeholder concerns: Security, Governance, or Runtime. A Viewpoint guides analysis; it is not the resulting artifact or an Architecture Domain.
_Avoid_: Architecture View, mandatory document, Architecture Domain

**Architecture View**:
The concrete representation produced for one Architecture Object and Scope using a focused Architecture Domain or Viewpoint. Materialize it independently only when its reader task, authority, and change cycle justify a separate artifact.
_Avoid_: Architecture Viewpoint, fixed coverage heading, directory level

**Authority Level**:
The Company, System, or Subsystem scope that owns a Technical Documentation artifact or Architecture Decision. It is a routing and authority hierarchy, not a substitute for Architecture Object or Scope.
_Avoid_: Architecture Level, Architecture Object, Architecture View

**Architecture Correctness Checks**:
The Domain, Application, Governance, and Runtime questions used to test whether facts and invariants, application ownership, controlled authority, and operating behavior remain coherent. They are completion checks rather than Architecture Domains, Viewpoints, directories, documents, or fixed headings.
_Avoid_: Four Architecture Views, mandatory four-part output structure

**System**:
A stable technical responsibility boundary with an independently governed lifecycle. State ownership, external contracts, independent release, and failure boundaries are evidence for the boundary, but a System need not satisfy all of them; a System may support multiple Products and contain multiple Applications and Subsystems.
_Avoid_: Product, Application, Codebase, Runtime Unit

**Registered System**:
A System admitted to the company System Landscape with a stable name, responsibility boundary, owner, and lifecycle status. It receives a System Responsibility README and System Architecture; candidates without this evidence remain assessments or open questions rather than formal System directories.
_Avoid_: Product entry, repository inventory, unsupported System scaffold

**Application**:
A runnable or audience-specific entry within a System. It participates in the System's architecture without becoming a synonym for the System itself.
_Avoid_: System, Product, Subsystem

**Subsystem**:
A logical boundary within a System that owns a stable group of responsibilities and may warrant independent architecture detail when its complexity and maintenance value justify it.
_Avoid_: System, Application, Module or Component

**Module or Component**:
An implementation unit inside a Subsystem whose existence alone does not establish a System or Subsystem boundary.
_Avoid_: System, Subsystem, Codebase

**Codebase**:
An implementation and version-management carrier that may implement several Modules, Subsystems, or Systems and does not define their architecture boundaries by itself.
_Avoid_: System, Subsystem, Product

**Runtime Unit**:
A deployed or executed process, container, task, or equivalent runtime instance. Runtime Units realize architecture but do not own product or system meaning.
_Avoid_: System, Application, Codebase

**System Architecture**:
The Technical Documentation authority for the stable design of one concrete System Architecture Object, including relevant domains and viewpoints, internal responsibilities, information and state authority, contracts, controls, deployment and runtime behavior, decisions, and evolution. It links Machine Authority and Project Technical Design instead of copying them.
_Avoid_: Technical Architecture, System Profile, Subsystem Architecture, Machine Authority

**Subsystem Architecture**:
The Technical Documentation authority for one justified Subsystem within a System. Materialize it independently only when the Subsystem has a stable responsibility boundary, sufficient complexity, and continuing maintenance value.
_Avoid_: System Architecture, Module or Component, Project Technical Design

**Architecture Decision**:
An accepted architectural choice for an explicit Architecture Object and Scope, owned at the narrowest Authority Level that governs its consequences. Higher levels link or summarize the decision instead of duplicating its authoritative record.
_Avoid_: centralizing every decision at company level, implementation task, unresolved option

**System Profile**:
The concise identity and navigation record for one System, normally carried by that System's Responsibility README. It states purpose, ownership, lifecycle, critical relationships, governance state, and authoritative links without replacing System Architecture.
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
