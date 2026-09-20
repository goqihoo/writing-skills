# Essence document module

This is an internal module used only by `Write Domain Doc`. It is not a standalone skill, has no invocation metadata, and must not appear in the plugin skill list.

Use it after `Write Domain Doc` has classified the requested artifact as a domain essence document. Treat `../assets/essence-article-template.md` as the fixed public schema.

## Derivation workflow

1. **Set the boundary and reader outcome.** Name the domain, what is inside and outside it, the class of new problems readers must judge, and the concrete question the document answers. The reader must be able to derive a judgment from domain realities rather than recall a framework definition.
2. **Choose the anchor example before drafting.** Pick one concrete situation that exposes the domain's objects, participants, state changes, desired result, and a meaningful failure. Use it as a thread throughout the document. It anchors observation but does not prove the essence by itself.
3. **Classify the domain and define its minimum purpose.** Select the primary type and state the smallest result that justifies the domain's existence:
   - an **output domain** must produce a dependable output under specified conditions;
   - a **control or governance domain** must keep actions or states within an acceptable boundary and make that control accountable or provable;
   - a **knowledge or practice domain** must make judgment or action repeatable and improvable across practitioners or situations.
4. **Record unavoidable realities.** Identify pre-solution facts that remain true across at least three materially different situations. Number them `R1`, `R2`, and so on. A reality describes the world before a response is chosen; it is not a framework principle, desired outcome, control, or product feature.
5. **Identify the core objects.** Keep only the domain objects needed to understand the essence. Introduce how they relate, order them by the reader's natural questions, and summarize each object's meaning, role in the domain's main line, and necessary recognition boundary in one or two sentences. Explain how the objects connect and why they are not interchangeable. Defer detailed states and change conditions to Core Objects and Lifecycle, and defer who may confirm or change them to Participants, Responsibilities, and Rules or the relevant mechanism artifact. Prefer short paragraphs; use a table only for genuine horizontal comparison.
6. **Map participants and interests.** Identify who acts, decides, benefits, bears cost or harm, supplies evidence, and can block or override action. State conflicting incentives and information asymmetries that make the domain non-trivial.
7. **Stress-test the candidate essence.** Use the realities, objects, participants, anchor, and additional cases to revise the candidate claim:
   - **Domain-uniqueness test.** Replace the domain nouns with those of the closest adjacent domain. If the claim remains equally explanatory, it is too generic.
   - **Coverage stress test.** Require the same causal spine to explain at least three materially different situations that vary in actors, objects, harm mechanisms, or timescales.
   - **Case-independence test.** Remove the anchor example. The realities and central relationship must still exist across the domain.
   - **Solution-stack test.** Reject a claim that only lists controls, lifecycle stages, outcomes, framework functions, or product capabilities. Restate the problem that makes those responses necessary.
   - **Adjacent-domain subtraction test.** Remove responsibilities owned by law, risk management, operations, resilience, architecture, or another neighboring domain. The remainder must still explain why this domain exists.
8. **Compress the essence.** Write the core essence sentence as a cognitive handle rather than the whole argument. Make it as concise and easy to understand as possible. Add a plain-language explanation immediately after it when needed, and let the following causal explanation carry the supporting argument.
9. **Derive necessary constraints.** For each constraint, cite the reality or object that makes it necessary, state what must remain true, and give a concrete failure case when it is absent. Number constraints `C1`, `C2`, and so on. A regulation, framework, or familiar good practice becomes a necessary constraint only when the causal link is shown.
10. **Map the solution or capability space.** Derive families of response from the constraints. Separate capabilities the domain must provide from optional frameworks, tools, organizations, and technologies. Ground each family with real-system coordinates: an actual system, protocol, product, institution, or operating model that shows where the response appears in practice.
11. **Expose the core tensions.** Name goals that cannot all be maximized, who benefits or pays under each tradeoff, the boundary that must not be crossed, and the minimum acceptable result. A tension is not a generic advantages-and-disadvantages list.
12. **Turn the reasoning into a reusable analysis framework.** Write a short ordered set of questions that starts from scope and objects, moves through realities, participants, constraints, evidence, failures, capability choices, and tensions, and ends with boundaries and remaining uncertainty.
13. **State boundaries, sources, and revision triggers.** Separate enduring domain facts from interpretation and implementation choices. Identify adjacent domains, assumptions, authoritative sources, and observable changes that would require the article to be reconsidered.
14. **Draft and verify the fixed structure.** Preserve every top-level heading and its exact order from `../assets/essence-article-template.md`. Use subject-specific third-level headings only inside the fixed sections. Remove every template instruction and placeholder before delivery.

## Artifact boundary

The essence document is the domain's cognition anchor, not the whole domain knowledge set. Give it enough detail to establish and test the causal spine, then link to separate artifacts for exhaustive terminology and concept relationships, object states and lifecycles, participant rules, mechanism explanations, methods and practices, solution comparisons, cases and failures, and reference material.

Keep failure cases and counterexamples with the constraints or claims they test. Keep real-system examples with the capability family they make concrete. Use tables for stable mapping and comparison; use prose and numbered steps for causal reasoning and analysis questions.

## Completion test

The essence document is complete only when:

- all twelve fixed sections are present in order and each performs its assigned reasoning job;
- the anchor case is concrete enough to follow through the article but the same causal spine still holds without it;
- the primary domain type and minimum purpose are explicit;
- unavoidable realities are pre-solution facts supported across at least three materially different situations;
- core objects answer distinct reader questions, show their roles and recognition boundaries, and explain their relationships without absorbing lifecycle, authority, or mechanism detail owned by sibling artifacts;
- participants' authority, interests, costs, and conflicts explain why the problem is non-trivial;
- the core essence sentence is a concise, understandable cognitive handle rather than the whole argument; a plain-language explanation follows immediately when needed, and the following reasoning passes every stress test;
- each necessary constraint traces to a reality or object and includes an observable failure case;
- the capability space separates necessary capability families from replaceable implementations and includes proportionate real-system coordinates;
- core tensions state what cannot be maximized together and what minimum result must be preserved;
- the ordered analysis questions work for a new situation not used in the article;
- adjacent-domain responsibilities, assumptions, evidence limits, and revision triggers are explicit;
- factual claims have proportionate support and every foundational reference supports a claim the article uses;
- no template instruction or placeholder remains.
