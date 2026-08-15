---
name: write-doc
description: "Plan, draft, revise, or review one clear human-readable document. Use directly when no artifact skill fits, and as the shared writing foundation for every Scribe deliverable: reader outcome, factual grounding, concrete language, boundaries, and completion."
---

# Write Doc

Make the document help one primary reader understand, decide, act, verify, or find an answer.

## Workflow

1. **Set the outcome.** Name the primary reader, the question, and the action reading should enable. Infer the relationship, medium, and level of formality; treat a supplied writing sample as the strongest voice guide.
2. **Respect the artifact.** Follow its owning skill and healthy local conventions. Preserve verified facts, links, decisions, and scope.
3. **Lock the artifact plan.** Let the owning skill fix the artifact type, core question, reasoning path, outline, section responsibilities, and required material before prose work. When the owning skill selects an explicit output template, treat the template as the structure owner: preserve its heading names, order, hierarchy, and permitted branches, and apply only the omissions or additions that the template or owning skill authorizes. Without an owning template, let the owning skill derive a subject-specific outline instead of imposing a generic heading set. When revising an existing document, treat its healthy title, outline, and section responsibilities as locked unless the user explicitly asks for restructuring. Do not add, remove, rename, or reorder locked sections, change a section's job, or promote an example into the document's organizing spine for stylistic reasons.
4. **Build within the plan.** Place facts, reasoning, and examples in the sections that own them. Improve the reader path by ordering the explanation within each section, not by replacing the artifact's logic. Give each paragraph one clear job and use examples or formatting only when they help this reader.
5. **Route visual questions.** During the artifact plan, identify central relationships that prose would force readers to reconstruct. Invoke `$draw-diagrams` when a model would otherwise require repeated arrows or indentation, four or more linked objects or relationships, three or more dependent stateful stages, branching or convergence, a cycle, bidirectional correspondence, hierarchy, ownership, timing, or failure paths. Let `$draw-diagrams` decide whether the final form should be no visual, a table, Mermaid, SVG, a chart, or another format.
6. **Support each claim.** Separate facts, interpretations, choices, assumptions, and open questions. Connect important claims to evidence, reasoning, or an example.
7. **State boundaries.** Expose prerequisites, non-goals, exceptions, failure modes, uncertainty, and conditions that would change the conclusion.
8. **Write concretely.** Name actors, actions, conditions, and observable results. Explain each new key term with its purpose and one example.
9. **Apply the natural writing guidance only after the artifact logic and substance are stable.** Revise reader-facing prose inside the established sections: improve openings, topic sentences, definitions, examples, transitions, sentence rhythm, and useful repetition. Do not use prose quality as a reason to change the outline, reasoning sequence, section ownership, or artifact boundary.
10. **Recheck structure and substance.** Compare the final heading sequence and section responsibilities with the locked artifact plan and, for a revision, with the source. Restore structural drift and any changed name, date, number, term, citation, qualification, uncertainty, requirement, acceptance criterion, decision, constraint, domain distinction, premise, or conclusion. Flag substantive ambiguity instead of silently resolving it. When expression and precision conflict, preserve precision and revise the sentence around it.
11. **Compress and verify.** Remove wording or formatting that does not change understanding, use, or judgment. Do not remove a required premise, reasoning step, boundary, or conclusion merely to make the prose shorter or smoother. Test the result against the reader action and the owning skill's completion criteria.

## Natural writing guidance

- State each section's real point early. Build from specific facts, actions, judgments, and examples instead of generic claims about importance or impact.
- Prefer ordinary, exact verbs and stable terms. Let sentence length follow the thought, keep useful repetition, and add a transition only when the relationship is not already clear.
- Keep genuine qualifications and uncertainty. Give more space to what matters; do not manufacture balance, symmetry, or a three-part structure.
- Preserve established headings, section order, and section responsibilities. Improve a heading only when the user or owning skill leaves its wording open; do not convert the document into a question-driven, chronological, or case-led narrative by default.
- Use examples to clarify the claim owned by a section. Do not turn one example into a running narrative unless the user or owning skill assigns it that role.
- Use lists for action and tables for real comparison, not as default containers for ordinary explanation.
- Cut canned openings, vague authority, promotional gloss, unsupported significance, and conclusions that only repeat the outline.
- Preserve the writer's apparent voice without inventing anecdotes, emotions, opinions, quotations, sources, or deliberate imperfections. Never frame the work as defeating authorship detection.
- Return the requested artifact without conversational preamble, a redundant summary, or a generic offer to continue unless the genre calls for one.

Keep code, commands, formulas, schemas, diagram syntax, structured data, quotations, and exact-format text outside these prose rules. Let the owning skill continue to control the artifact type, outline, reasoning path, section responsibilities, facts, technical meaning, decisions, requirements, constraints, and completion criteria.

## Shared completion check

- One primary reader task is resolved through a clear path.
- Facts, interpretations, choices, assumptions, and open questions remain distinct.
- Important conclusions state their evidence and boundary in concrete language.
- No fact, agreement, or material decision is invented or hidden.
- The heading sequence, section responsibilities, and reasoning path match the locked artifact plan.
- Within that plan, the prose sounds like one writer addressing this reader; its formatting serves the content instead of a template.
- Every central relationship that is expensive to reconstruct from prose has been routed through `$draw-diagrams`; retained visuals add information rather than decoration.
- Readers can tell when to act and when the document needs revision.
