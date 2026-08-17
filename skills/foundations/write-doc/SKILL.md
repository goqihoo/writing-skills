---
name: write-doc
description: "Plan, draft, revise, or review one clear human-readable document. Use directly when no artifact skill fits, and as the shared writing and natural-prose foundation for every Scribe deliverable: reader outcome, factual grounding, concrete language, reader flow, boundaries, and completion."
disable-model-invocation: true
---

# Write Doc

Make the document help one primary reader understand, decide, act, verify, or find an answer.

## Workflow

1. **Set the outcome.** Name the primary reader, the question, and the action reading should enable. Infer the relationship, medium, and level of formality; treat a supplied writing sample as the strongest voice guide.
2. **Respect the artifact.** Follow its owning skill and healthy local conventions. Preserve verified facts, links, decisions, and scope.
3. **Lock the artifact plan.** Let the owning skill fix the artifact type, core question, reasoning path, outline, section responsibilities, and required material before prose work. When the owning skill selects an explicit output template, treat the template as the structure owner: preserve its heading names, order, hierarchy, and permitted branches, and apply only the omissions or additions that the template or owning skill authorizes. Without an owning template, let the owning skill derive a subject-specific outline instead of imposing a generic heading set. When revising an existing document, treat its healthy title, outline, and section responsibilities as locked unless the user explicitly asks for restructuring. Do not add, remove, rename, or reorder locked sections, change a section's job, or promote an example into the document's organizing spine for stylistic reasons.
4. **Build within the plan.** Place facts, reasoning, and examples in the sections that own them. Treat a template as a coverage contract, not as a prose voice: satisfy its responsibilities without echoing its labels, symmetry, or field order in every paragraph. Give each paragraph one clear job and use examples or formatting only when they help this reader.
5. **Route visual questions.** During the artifact plan, identify central relationships that prose would force readers to reconstruct. Treat it as a visual candidate when a model would otherwise require repeated arrows or indentation, four or more linked objects or relationships, three or more dependent stateful stages, branching or convergence, a cycle, bidirectional correspondence, hierarchy, ownership, timing, or failure paths. When the user explicitly included `$draw-diagrams`, let it decide whether the final form should be no visual, a table, Mermaid, SVG, a chart, or another format. Without that explicit invocation, preserve the smallest sufficient prose or table and return a complete invocation when the requested result materially requires a visual.
6. **Support each claim.** Separate facts, interpretations, choices, assumptions, and open questions. Connect important claims to evidence, reasoning, or an example.
7. **State boundaries.** Expose prerequisites, non-goals, exceptions, failure modes, uncertainty, and conditions that would change the conclusion.
8. **Write concretely.** Name actors, actions, conditions, and observable results. Introduce an abstract term only after the reader has a familiar object, event, decision, or result to attach it to; then reuse one stable name.
9. **Run the shared reader-flow pass after the artifact logic and substance are stable.** Revise every reader-facing passage against the shared prose contract below. Make the prose sound like one informed writer leading this reader through the subject, even when the headings come from a strict template. Improve openings, causal movement, definitions, transitions, sentence rhythm, emphasis, and formatting without changing the outline, reasoning sequence, section ownership, or artifact boundary.
10. **Recheck structure and substance.** Compare the final heading sequence and section responsibilities with the locked artifact plan and, for a revision, with the source. Restore structural drift and any changed name, date, number, term, citation, qualification, uncertainty, requirement, acceptance criterion, decision, constraint, domain distinction, premise, or conclusion. Flag substantive ambiguity instead of silently resolving it. When expression and precision conflict, preserve precision and revise the sentence around it.
11. **Compress and verify.** Remove wording or formatting that does not change understanding, use, or judgment. Do not remove a required premise, reasoning step, boundary, or conclusion merely to make the prose shorter or smoother. Test the result against the reader action and the owning skill's completion criteria.

## Shared prose contract

Apply this contract to every human-readable Scribe artifact. Keep the artifact's genre, structure, facts, and precision; share the same standard of natural reader flow rather than forcing every artifact into one tone.

- **Point first.** Open a section or paragraph with the fact, action, judgment, or consequence the reader needs. Use document narration such as “this section explains” only when it changes how the reader should use the material.
- **Concrete before abstract.** Let the reader encounter a recognizable object, event, decision, or result before naming the model that explains it. Explain each new term once in plain language, then reuse the stable term.
- **Causal movement.** Make adjacent sentences move by cause, consequence, contrast, condition, or sequence. Prefer a transition that names that relationship over one that merely announces the next topic.
- **Human syntax.** Name actors and use ordinary, exact verbs. Unpack noun chains and sentences carrying several independent relationships. Let short conclusions and longer explanations alternate as the thought requires.
- **Selective structure.** Preserve required headings and fields, but expose only the scaffolding the reader needs. Use prose for explanation, lists for genuine sets or actions, and tables for compact repeated fields or comparison. Move a full argument out of a table cell and into prose.
- **Proportionate emphasis.** Give more space to consequential or difficult ideas. Keep useful repetition, but do not manufacture equal-length sections, mirrored paragraphs, three-part lists, or a uniform sentence pattern.
- **Grounded examples.** Use examples to clarify the claim owned by a section. Carry one example across sections only when the artifact plan gives it that job.
- **Honest qualification.** Keep material uncertainty, exceptions, assumptions, and limits close to the claim they constrain without interrupting every sentence with method commentary.
- **Consistent voice.** Treat a supplied writing sample as the strongest voice guide. Otherwise preserve the writer's apparent relationship to the reader and level of formality without inventing anecdotes, emotions, opinions, quotations, or deliberate imperfections.
- **Clean delivery.** Cut canned openings, generic claims of importance, vague authority, promotional gloss, exposed template instructions, redundant summaries, and conversational handoffs the genre does not need.

Before delivery, scan for reader-flow failures: an opening that talks about the document before the subject; several unexplained abstract nouns arriving together; consecutive paragraphs with the same sentence pattern; repeated template labels used as prose; transitions that announce sections instead of relationships; and table cells carrying multi-step reasoning. Rewrite each failure inside the locked artifact plan.

Keep code, commands, formulas, schemas, diagram syntax, structured data, quotations, and exact-format text outside these prose rules. Let the owning skill continue to control the artifact type, outline, reasoning path, section responsibilities, facts, technical meaning, decisions, requirements, constraints, and completion criteria.

## Shared completion check

- One primary reader task is resolved through a clear path.
- Facts, interpretations, choices, assumptions, and open questions remain distinct.
- Important conclusions state their evidence and boundary in concrete language.
- No fact, agreement, or material decision is invented or hidden.
- The heading sequence, section responsibilities, and reasoning path match the locked artifact plan.
- Within that plan, the prose satisfies the shared prose contract: the point arrives early, abstractions have concrete anchors, sentences move through explicit relationships, and formatting serves the content instead of exposing the template.
- Every central relationship that is expensive to reconstruct is clear in prose or a table, or has been routed through an explicitly invoked `$draw-diagrams`; retained visuals add information rather than decoration.
- Readers can tell when to act and when the document needs revision.
