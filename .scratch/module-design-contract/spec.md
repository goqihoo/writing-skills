# Module Design template and writing contract

Status: complete

Implement the five user-confirmed chapters and all confirmed subsection responsibilities, including the final title 规则与接口. Preserve Overall and Subsystem work and leave Component Architecture for later confirmation. Keep existing skill IDs, registries and authority; do not edit business documents or installed plugin caches.

## Accepted behavior

Explain one cohesive business or technical function, allowing direct System ownership and private/shared components without mandatory extra documents. Keep functional behavior/rules separate from internal realization, state before execution, and verification results separate from planned checks. Name actual key flows rather than fixed generic happy-path, concurrency and recovery chapters.

Require implementation structure and a diagram per independently explained key flow, including flows under compatibility/migration. Require state diagrams for important transitions. Keep caller/context, deployment and validation views optional at Module scope. Explain runtime effects inside flows and real change/migration obligations under extension and compatibility.

## Previous obligation mapping

| Previous content | New owner |
| --- | --- |
| Representative use and result | 1.1 |
| Scope, callers, independent design | 1.2 and 2.4 |
| Parent authority, guarantees, constraints and principles | 1.3 |
| Current facts, change scope and assumptions | Explicit 1.4 plus metadata |
| Supported operations | 2.1 |
| Input/output, preconditions and completion | 2.2 |
| Rules, invalid use, failures and unknown results | 2.3–2.4 |
| Callers, dependencies, sync/async and compatibility | 2.4 |
| Internal responsibilities, private/shared components and dependencies | 3.1 |
| Identity, relations, version, lifecycle, authority and reconstruction | 3.2 |
| Strategies, technology, alternatives, costs and inherited style | 3.3 |
| Extension, change impact, compatibility, transition and rollback limits | 3.4 |
| Normal processing, branches and module handoffs | 4, within actual named flows |
| Atomic changes, consistency, concurrency, waiting, cancellation and control evidence | Model in 3.2; enforcement and execution in 4 |
| Partial/unknown outcomes, retries, recovery and reconciliation | 4 |
| Overload, limits, backpressure, degradation, signals and parent runtime assumptions | 4; relevant assumptions in 1.3 and choices in 3.3 |
| Rules, quality and implementation validation | 5.1 |
| Input boundaries, concurrent/resource/failure and integration checks | 5.2 |
| Observed versus illustrative or planned evidence | Explicit 5.3 |
| Unsupported assumptions, pending decisions and redesign conditions | 5.4 |

## Completion

Review one full synthetic Module artifact and rendered diagrams against the contract. Check stateless technical-function, no-independent-deployment, narrow-edit and unresolved-rule adaptations. Validate source/generated routing, existing tests, available validators, shell syntax and whitespace. Report self-review limits and unavailable dedicated plugin validation without claiming independent testing or production acceptance.
