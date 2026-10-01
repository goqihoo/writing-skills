# Concrete architecture adaptation

Apply this profile to shared architecture templates for a named company, System, Subsystem, Component or Project design. Keep the owning Writer's authority and completion contract. Read only the selected template; use `templates.yaml` for a supporting topic justified by the request. Treat topic scaffolds as structural resources, not new registered types or separate skill invocations.

## Establish the baseline

Use the real object's title and the document set's language. Record known owner/decision authority, evidence date or version, current/target design state, proposal/acceptance status and planned/implemented state without inventing approval. Replace illustrative prerequisites with established constraints or bounded assumptions. Compare the observed baseline with the intended change and its exclusions; preserve current-state work when that is the request.

## Adapt the common sections

- Turn problem and applicability into the named scope, baseline, requirements, stakeholders and constraints, with sources and priorities. Keep missing quality budgets explicit.
- Turn the model and mechanisms into the selected or proposed realization: modules, technologies, identities, transactions, contract completion and errors, concurrency, recovery and operating ownership. Apply the implementation-depth checks in `../architecture-documents.md`.
- Use scenarios to demonstrate the actual proposed design, including a consequential failure. Label illustrative walkthroughs and observed evidence separately.
- Turn variants into evaluated alternatives and the adopted or proposed choice, its cost, authority and review trigger. Explain rationale beside the affected mechanism rather than leaving a menu of options.
- Turn adaptation and evolution into compatibility, state transition, rollout, rollback limits and recovery after irreversible change. Link a migration design only when it exists and owns the detail.
- Turn validation into requirement-to-mechanism-to-check traceability, sourced pass criteria, observed or planned evidence and residual risks. Name which commitment an unresolved gap prevents and what closes it. Keep acceptance explicit and evidence-backed.

Apply the template-structure rules in `../architecture-documents.md`; adapt the content to the named design without replacing the selected outline with the source material's taxonomy. Include deployment, security and governance consequences in the main design even when detailed topics are separate. Keep parent allocations, local choices and changes requiring parent coordination distinct. Link executable schemas, complete APIs, configuration and procedures to Machine Authority while retaining architecture-significant semantics.

## Apply the authority scope

For a company Technical Landscape, use product, service and capability definitions as evidence for scope, drivers and coverage. Explain their architecture-significant consequences within the selected template, and link governing System designs. Include or link a Product-System Map when the requested reader task needs that view; do not require a product-to-system derivation section or diagram for every overall architecture. For stable System or Subsystem design, realize inherited commitments and record only locally owned refinements. Let Component Architecture inherit parent authority. For Project delivery, apply the Writer's delivery method for bounded scope, reference adoption, cutover and acceptance. Keep proposals linked to stable authorities until their promotion is authorized.

Complete when readers can identify what to build or govern, follow its interfaces and state changes through failure, and distinguish proven guarantees from proposed checks and open commitments. Apply the cross-document scenario check to any substantive set.
