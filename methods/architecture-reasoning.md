# Architecture reasoning method

Use this method inside any Public Skill that must reason about architectural scope, ownership, controls, failure, options, evolution, or validation.

## Architecture model

Keep the design object, viewpoint and document structure separate:

| Axis | Meaning | Examples |
| --- | --- | --- |
| Architecture Object | The entity being designed | Company Technical Landscape, System, Subsystem, Component |
| Architecture Scope | The selected responsibility and environment boundary | One service and its dependencies, one company landscape |
| Architecture Viewpoint | One of Scribe's four organizing and review perspectives | Domain, Application, Governance, Runtime |
| Architecture View | A concrete explanation of an object through a viewpoint | A service's application structure, its runtime behavior |
| Authority Level | The scope owning a decision or technical artifact | Company, System, Subsystem |

Use Domain, Application, Governance and Runtime as the shared framework for organization and coverage review. It is Scribe's working framework, not a claim that every architecture discipline uses the same taxonomy. Do not infer the viewpoint or template from a directory name, repository count or object size.

## Four viewpoints

| Viewpoint | Reader question and review responsibility |
| --- | --- |
| Domain | What concepts, facts, rules, lifecycle states and invariants define the problem? |
| Application | Which systems and modules own behavior and state, and how do their contracts and dependencies realize it? |
| Governance | Who may decide or act, under which constraints, with what review and evidence? |
| Runtime | How does the design operate under deployment conditions, load, failures and recovery? |

Link company Business and Product facts to their owning authorities. Explain their technical consequences without redefining their product meaning.

Do not introduce Data, Integration, Deployment or Security as additional peer viewpoints, predefined subcategories or recommended standalone documents. Their organization is deferred. Address necessary facts and mechanisms in the relevant explanation, allowing them to affect more than one viewpoint without imposing a fixed placement scheme. Preserve existing specialist templates as resources; use them for an explicitly requested specialist artifact, not to expand an ordinary architecture request.

## Correctness checks

Check domain validity, application ownership, governed authority and runtime behavior through the four viewpoints. An important action must remain authorized and traceable through failure and recovery; information must have clear meaning and ownership. These are coverage checks, not mandatory headings or a requirement for four files.

Use the selected template for the document sequence. A main architecture may combine all four viewpoints. Materialize a separate view only when the requested reader task and maintained content warrant it; do not split merely to complete a taxonomy. Keep object decomposition, viewpoints and document boundaries independent.

## Reasoning loop

Apply this loop across the relevant viewpoints:

```text
Context → Drivers → Scenarios and flows → Risks → Decisions → Validation
```

| Step | Required result |
| --- | --- |
| Context | Object, scope, authority, facts, stakeholders, unknowns, and change assumptions |
| Drivers | Invariants, information authority, ownership needs, constraints, control obligations, runtime conditions, and ranked qualities |
| Scenarios and flows | Concrete success, failure, duplicate, delayed, partial, unknown, replay, recovery, and evolution paths |
| Risks | Unsafe assumptions, bypasses, inconsistency, overload, unrecoverable states, and evidence gaps |
| Decisions | Boundaries, ownership, contracts, controls, deployment structure, patterns, and accepted costs |
| Validation | Tests, reviews, drills, operating evidence, and signals that prove or challenge each judgment |

Revisit an earlier judgment only when new evidence invalidates it, then trace the consequence forward again.

## Architecture judgment

Distinguish:

- **Constraint:** cannot be violated in the stated context.
- **Quality:** can improve or degrade and must be prioritized.
- **Principle:** guides later choices.
- **Pattern:** a reusable structural response.
- **Decision:** binds the current object and scope and records accepted cost.
- **Validation:** evidence that tests a named judgment.

Pressure-test each choice for **fit**, **simplicity**, and **evolution**.

## Control trace

For every material control, trace:

```text
objective and unsafe outcome
→ protected value and capability
→ policy, decision, information, state, and execution owners
→ last responsible control point
→ allow, reject, hold, limit, degrade, repair, or fail-closed behavior
→ durable evidence
→ design and operating validation
```

Test missing, stale, conflicting, duplicate, delayed, partially applied, and unknown outcomes. “Log and continue” is not a safe default.

## Turn reasoning into an architecture document

For a full architecture artifact, establish a concrete structural model before expanding the prose. Name the participants, responsibility boundaries, authoritative information or state, and meaningful relationships at the requested scope. Explain why the important boundaries exist. Use a principal view when it materially helps the reader; keep its names and relationships consistent with the text through the shared visual production method.

Demonstrate the model with a representative scenario: follow an input or decision through the participating owners, state changes, observable result, and a consequential failure or exception. For a static structural question, trace a concrete dependency or change impact instead. State the mechanism that preserves or restores the relevant invariant; naming a quality such as reliability is not an explanation. Keep illustrative scenarios visibly distinct from observed behavior.

Connect each material recommendation to a driver, a structural consequence, an accepted cost, and evidence that could challenge it. Compare plausible alternatives on the same scenario and criteria. Report missing evidence at the affected claim; preserve a useful proposed model when the user requests design, labeling assumptions and unaccepted decisions explicitly.

Use coverage checks to find omissions after drafting. Express the result through subject-specific explanations, views, and comparisons that let the reader reconstruct the architecture. Apply this process only to affected content for narrow edits and reviews.

## Reader verification

Before delivery, verify that the artifact lets its intended reader:

- reconstruct the relevant structure, owners, and relationships without interpreting a taxonomy checklist;
- follow the representative scenario or change impact and explain a material failure or exception;
- understand why the proposed structure fits its drivers, what it costs, and what evidence would invalidate it;
- distinguish established facts, illustrative examples, proposals, and accepted decisions.

Revise the model or explanation when any relevant answer depends on an unexplained slogan, an empty section, or contradictory views. Use the owning Writer's template for the artifact-specific expression of these checks.

## Completion

Architecture reasoning is complete when the object and scope are explicit, the four viewpoints have been reviewed for relevant concerns, authoritative facts and state have one owner, material controls trace authority through evidence, failure and recovery behavior preserve invariants, and every accepted tradeoff names its cost and review trigger.
