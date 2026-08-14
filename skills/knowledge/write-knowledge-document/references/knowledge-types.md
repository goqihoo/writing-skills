# Knowledge document types

Choose the primary type by the action readers need to perform after reading. A document may contain supporting material from other types, but its primary use controls the main structure.

## Contents

- [Selection](#selection)
- [Domain cognition](#domain-cognition)
- [Mechanism explanation](#mechanism-explanation)
- [Methodology](#methodology)
- [Pattern decision](#pattern-decision)
- [Mental model](#mental-model)
- [Case study](#case-study)
- [Reference](#reference)

## Selection

| Reader action | Primary type |
|---|---|
| Derive judgments from a domain's goals and realities | Domain cognition |
| Explain how objects, state, and rules produce a result | Mechanism explanation |
| Complete a repeatable task | Methodology |
| Choose among recurring solution families | Pattern decision |
| Analyze a problem through a stable set of questions | Mental model |
| Test understanding against one real situation | Case study |
| Find an exact fact, rule, field, or record | Reference |

## Domain cognition

Use this type to help readers continue reasoning inside one domain.

| Part | Question |
|---|---|
| Scope and key objects | Which problems, actors, and objects are included? |
| Minimum goal | What must this domain make possible? |
| Unavoidable realities | Which facts, conflicts, failures, and state changes cannot be removed? |
| Core transformation | What input or state becomes what result? |
| Necessary constraints | Which conditions must hold for the goal to remain possible? |
| Core conflicts | Which goals cannot be maximized together? |
| Solution space | Which structures, rules, and processes can satisfy the constraints? |
| Analysis framework | Which questions should guide a new problem? |
| Cases and counterexamples | Where does the reasoning hold or fail? |

Complete when readers can apply the same reasoning chain to a new problem not covered in the document.

## Mechanism explanation

Use this type to explain how one mechanism produces behavior. Compare alternative mechanisms in a pattern-decision document.

| Part | Question |
|---|---|
| Intended result | What must the mechanism make true? |
| Objects, states, invariants | What participates, how can it change, and what must remain true? |
| Preconditions | What must already exist? |
| Trigger | Which event starts the mechanism? |
| State changes and causes | Who changes what, and why does each change cause the next? |
| Observable result | What can callers, users, or operators observe? |
| Failure | Where can contention, timeout, partial completion, or invalid state occur? |
| Dependencies and alternatives | Which mechanisms does this one require, replace, or constrain? |

Complete when readers can trace success and failure from precondition through observable result.

## Methodology

Use this type when readers need to perform a repeatable task while making context-dependent judgments.

| Part | Question |
|---|---|
| Outcome and success | What problem does the method solve, and what result counts as success? |
| Applicability | When should or should not it be used? |
| Inputs and prerequisites | What information, resources, authority, or prior output is required? |
| Principles | Which stable rules guide tradeoffs? |
| Steps | What does each step receive, do, and produce? |
| Decision points and variants | When should the path change, skip, or branch? |
| Stage outputs | What inspectable result must each major stage leave? |
| Acceptance | How does the user know the result works, not merely that steps ran? |
| Failure and adaptation | Which signals show failure, and how should the method change? |

Complete when a qualified reader can execute the method, navigate its branches, and judge the result.

## Pattern decision

Use this type to compare recurring solution families. Explain one selected pattern's internal behavior in a mechanism document.

| Part | Question |
|---|---|
| Recurring problem and conflicting demands | Why does the problem recur, and which goals conflict? |
| Candidate patterns | Which stable approaches exist, and how does each address the problem? |
| Shared comparison dimensions | Which identical dimensions will compare every option? |
| Selection conditions | Which goals, constraints, or environments change the choice? |
| Benefits and costs | What does each option strengthen and sacrifice? |
| Failure and boundaries | When does each option fail, stop fitting, or create side effects? |
| Examples and counterexamples | Which cases demonstrate fit or expose limits? |

Complete when readers can compare options on common dimensions and defend a choice and its cost.

## Mental model

Use this type to give readers a reusable way to inspect a class of problems. It supplies questions, not an automatic answer.

| Part | Question |
|---|---|
| Problem | Which class of questions does the model help analyze? |
| Objects and relationships | What does the model pay attention to, and how do those things interact? |
| Trigger | Which recognizable situation should make the reader use it? |
| Analysis steps | What should the reader inspect, compare, or derive? |
| Worked example | How does the model change observation, judgment, or action? |
| Visibility | Which relationships or risks does the model reveal well? |
| Blind spots and complements | What does it hide or distort, and which other view should supplement it? |

Complete when readers can recognize the trigger, apply the model, and state what it misses.

## Case study

Use this type to preserve one real situation and test whether broader knowledge explains it. Keep decision-time facts separate from hindsight.

| Part | Question |
|---|---|
| Background and time | In what environment and phase did the event occur? |
| Information available then | What was known or knowable before the decision? |
| Goal and constraints | What had to change, and what could not change? |
| Options and expectations | Which options were considered, and what result was expected from each? |
| Judgment and action | What was selected, why, and what was done? |
| Observable result | What happened, and how did it differ from the expectation? |
| Causal interpretation and alternatives | Which mechanisms may explain the result, and what other explanations remain? |
| Transferable lesson | What may another context reuse? |
| Conditions and limits | Which case-specific facts restrict transfer? |

Complete when readers can reconstruct the original decision conditions and judge whether the lesson transfers.

## Reference

Use this type for fast, precise lookup. Move extended reasoning into a linked knowledge document.

| Part | Question |
|---|---|
| Scope | What does this reference cover and exclude? |
| Version, region, and time | Where and when is the answer valid? |
| Lookup entry | How can readers find the right item quickly? |
| Entries | Which consistent fields describe definitions, values, rules, commands, or records? |
| Examples, exceptions, and confusions | How is an entry used, when is it exceptional, and what resembles it? |
| Source and last verification | Where did the fact come from, and when was it last checked? |

Complete when readers can find an answer quickly and verify its applicable version, conditions, source, and date.
