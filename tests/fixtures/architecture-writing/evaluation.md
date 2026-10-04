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

## Completion

Complete the evaluation when both requested outcomes have an observed artifact or recorded limit, each available full artifact has been reviewed against the criteria, findings cite concrete evidence, and the report distinguishes routing, expression and technical correctness. State sample limitations and any untested modes; do not generalize a single run into a measured overall quality improvement.
