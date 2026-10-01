# Architecture document families

Apply this method inside architecture Writers. Keep architecture reasoning in `architecture-reasoning.md` and prose quality in `prose-quality.md`.

## Select purpose and document responsibility

Establish whether the request concerns reusable Knowledge, stable Company/System design, or a named Project delivery. Then select the object or topic and its owning template. Keep a view overview, a substantive architecture document, a component, and an engineering strategy distinct. Use an overview to own aggregate judgments and navigation; use detailed documents to own the underlying explanation.

Read only the selected template and directly relevant references. Use the Writer's manifest as the template-path authority. Preserve the output language and explicit user structure. Retain the template's substantive section responsibilities, tables and figure slots where applicable; fill them with evidence and subject-specific content. Merge or omit irrelevant sections deliberately. Remove unfilled placeholders and unused figure slots from the deliverable. Keep selection instructions and acceptance checklists in references rather than adding them to the document body.

## Knowledge and delivery adaptation

Use Knowledge templates to describe reusable models, mechanisms, variants, applicability, failure limits, validation expectations and project extraction. Select a concrete model and explain it fully; Knowledge can contain detailed internal structure without committing a project to that structure.

Use delivery templates to describe the named object's actual baseline, selected or proposed design, constraints, interfaces, deployment, decisions, migration and acceptance evidence. Record `Adopt`, `Adapt`, or `Reject` for material reference-architecture choices with reasons. Replace illustrative actors and assumptions with established delivery facts or clearly bounded proposals. Keep knowledge-source links instead of copying the full reference article.

Distinguish design state (current or target), decision state (proposed or accepted), and delivery state (planned or implemented). A delivery request authorizes design work, not invented approvals, external deployment, or claimed acceptance. Keep executable schemas, configuration, code and runbook procedures in Machine Authority; summarize their architecture-significant contracts and link them.

## Document-set boundaries

Support view-based Knowledge organization when the knowledge system uses it. Treat Domain, Application, Governance and Runtime as one supported organizational profile, not a mandatory universal taxonomy or one document per concern. Preserve other established healthy structures. A view can contain an overview, topic documents and nested object details; document responsibilities and cross-view links govern placement.

Organize delivery around the real object and review/implementation/acceptance tasks. Integrate relevant view content into its main architecture. Split a detailed document only when it has an independent reader task, sufficient substance, and a clear relationship to the main architecture. Avoid creating every available template, one document per view, or every potential component by default.

## Review before completion

Verify template fit, evidence, current/target distinctions, decision status, and consistency of names, contracts, ownership and views. Confirm the reader can reconstruct the structure and trace important behavior and failure. For Knowledge, verify applicability, variants, transfer and cross-document responsibilities. For delivery, trace requirements through design to observed or planned validation and leave unverified acceptance explicit. Check actual local links and parent/child navigation when writing into a document set; allow standalone results without invented navigation.
