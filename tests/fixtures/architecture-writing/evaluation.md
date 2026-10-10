# Architecture writing evaluation

Use `source.md` and `request.md` as a complete-document behavioral fixture. The case is synthetic: it tests writing and routing under known evidence, not a real system's correctness or delivery readiness.

## Run

1. Freeze the skill and Shared Method trees for the baseline and candidate revisions. Record commit IDs or diffs, model and reasoning settings when known, and the source/request hashes.
2. Give independent fresh runs the identical request, source and execution settings, substituting only the skill snapshot and output paths. Keep evaluators unaware of the desired difference; keep outputs and working notes outside production documentation. Save limits and routing responses as observed results rather than making a refused task silently use a different skill.
3. Read each complete output against the source before comparing versions. Separate stable and Project results; classify any missing output as a routing result, not a prose score. An additional run through the default owner may serve as a labeled control, but is not the same-request comparison.
4. Record concrete passages for findings, their effect on the reader and any lost or invented conditions. Compare like scopes; do not treat shorter prose, fewer tables or matching chapter counts as success.
5. Apply targeted repairs justified by the results. Rerun only affected cases when a behavioral correction changes the candidate; keep earlier outputs as evidence. Run registry, generated-package and skill validation separately from these reader checks.

## Review criteria

- Preserve stable subsystem authority in stable.md. Preserve the named delivery scope and unverified rollout state in project.md. Distinguish existing facts from the designs the source asks the Writer to propose.
- Let a developer identify business-state ownership, subscription authorization, event/recipient delivery records, participant responsibilities and the meaning of acknowledgment. Explain a full successful delivery and a timeout or worker failure without inventing a missing cross-boundary mechanism.
- Retain at-least-once/duplicate and out-of-order delivery, unknown timeout results, lease expiry and stale-worker result protection, tenant authorization, audit without payload, and unresolved retry/retention/quality values. Treat unprovided recipient update algorithms and exact performance numbers as unknown or explicit proposals.
- For the Project case, account for a single active sender per tenant, in-flight tasks and both queue/table backlog, subscription revocation, irreversible external notifications, reconciliation and conditional rollback. Preserve acceptance as planned verification rather than a passed test.
- Check the reader progression against the selected template: establish the object's purpose, normal use and structure before detailed failure mechanisms. Verify that data, state, recovery and compatibility remain explained after merging sections. Treat forced equal chapter counts or generic taxonomy blocks as failures when they interrupt that progression; do not score a particular count as a quality result.
- Ask a fresh reader to explain the main operation, responsibility boundaries, reason for a major choice, its accepted cost and a meaningful failure. Record which passages support those answers and where the reader must reconstruct missing links. A full set of technical keywords is insufficient evidence of understanding.
- Give sections distinct contributions; keep useful local context while consolidating repeated responsibility lists and global status disclaimers. Keep real permission and audit controls in the design.
- Make consequential Chinese passages clear about actors, actions, objects, conditions and consequences. Preserve necessary technical terminology and qualify algorithmic guarantees.

## Design-argument regression checks

Evaluate the reasoning in the artifact independently from preservation of implementation constraints. Locate actual passages, not just headings or keywords:

- Identify which source obligations are binding and which architecture characteristics are prioritized. Require a concrete scenario and observable response for each consequential quality claim; preserve unknown numeric targets.
- Identify inherited or proposed principles and a consequential design choice they guide. Reject restatements of one tool or mechanism as a principle.
- For the subsystem, explain its organizing style or precise structural form using the source's boundaries, interactions and deployment assumptions. Distinguish a local notification pattern from the whole architecture's style; do not infer distributed deployment from a queue.
- Trace the recovery/delivery strategy through its problem, mechanism, cost, competing option and validation. Verify the rationale remains visible after expression editing, not only in a separate plan or rubric.
- Distinguish inherited decisions from inferred labels and new proposals. In a module/component variant, inherit the parent style and explain local consequences rather than inventing an independent architecture or deployment.
- Countercheck missing dimensions: a mechanism-rich output with no priority/choice rationale fails; a generic list of characteristics, principles and style names with no causal link also fails. Preserve existing technical and authority criteria above in both cases.

When adapting this case to a real user document, keep proprietary sources and generated outputs outside the repository. Record the template-obligation mapping and findings using sanitized descriptions. Treat a single full-document run as case evidence, not measured reliability across all four levels and purposes.

## Section-judgment regression cases

Use these additional synthetic cases when changing section review or overall-architecture guidance. Supply the facts and task to a fresh run; keep the expected judgments with the evaluator. Request complete documents for generation tests and affected sections for scoped repair tests. Keep results outside production documentation and distinguish a manual walkthrough from an observed generation run.

| Case facts and task | Expected reader judgment |
| --- | --- |
| A service accepts independent checks A and B and a combined request. Both consume the same frozen input; B does not consume A's result. Each result is saved independently. The combined request completes after both required results are saved. Review a draft whose selection prose allows independent execution but whose main figure serializes A then B and whose state view marks the first saved result as request completion. | Find the contradiction across selection, flow and state. Preserve legitimate concurrency and distinguish operation completion from request completion. Include a validation condition in which A waits while ready B proceeds; a correct paragraph cannot excuse the misleading views. |
| A worker uses a database and an artifact store. A draft says only “start the worker; back up both stores; maintain compatibility; roll back on failure.” Review its operations and release sections. No actual startup or recovery procedure, numerical target or test evidence is supplied. | Identify missing readiness, in-flight shutdown, joint recovery checks, release continuation and rollback conditions. Distinguish missing expression from unresolved design; any supplied mechanism is a proposal. Keep operational readiness qualified and do not invent passed checks or precise budgets. |
| A staged replacement has old-only, coexistence and new-only diagrams, but no stage exit conditions. External effects cannot be undone; only one implementation may issue them for an account at a time. Revise the transition design. | Explain viable intermediate ownership/routing, progress checks and failure handling on each side of irreversible effects. Tie retirement to explicit evidence. A stage diagram alone cannot justify advancement or unconditional rollback. |
| A small stateless formatter is one cohesive module with one caller and no independent internal responsibilities or migration. Write its module design. | Explain the single unit, responsibility and meaningful interaction without manufacturing layers, worker state, multiple execution modes or a migration program. Apply the module contract rather than overall operating detail. |
| A module's internal structure and sequence views show its caller, a peer storage module and three internal parts. All nodes have equally saturated category paint. Its private calculator also has a component view showing the parent as its caller. Adjust visual emphasis without changing the design. | Use neutral surfaces and lighter borders for external nodes relative to each view: storage and caller are external to the module, while the parent is external to the calculator. Keep the calculator internal in the module view. Preserve readable labels, relationship semantics, topology and meaningful status; bright alternate category colors or global opacity do not satisfy the hierarchy. |

Record the passages and views supporting each judgment and any gaps left unresolved. Treat these as behavioral cases, not keyword assertions or evidence that a run has occurred.

## Database-field regression case

Request a database design for a PostgreSQL application with two related tables, an application-generated UUID, a nullable foreign key, a composite business unique key, a timestamp default, a numeric precision/scale and a filtered unique index. Supply the implemented schema as evidence in one run; supply no implementation and authorize a proposed design in another. Require the relevant Writer to produce the complete document, not a key-field inventory.

Parse the produced physical dictionaries with a Markdown table parser and reconstruct the tables, named constraints and indexes in an empty temporary database. Verify all common/audit fields are explicit rows, nullability does not imply a default, composite key members retain their order, optional foreign keys preserve their matching behavior, and the exact index predicate survives parsing. Compare implemented definitions to the supplied schema; distinguish visibly proposed decisions in the new-design run. Test one accepted row and one rejected row for each supplied invariant. Reject generation-readiness claims for omitted or unresolved definitions; distinguish construction evidence from migrations and business tests. Record actual outputs and results before claiming this case passed.

## Completion

Complete the evaluation when both requested outcomes have an observed artifact or recorded limit, each available full artifact has been reviewed against the criteria, findings cite concrete evidence, and the report distinguishes routing, expression and technical correctness. State sample limitations and any untested modes; do not generalize a single run into a measured overall quality improvement.
