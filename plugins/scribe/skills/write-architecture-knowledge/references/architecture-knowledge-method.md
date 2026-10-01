# Architecture Knowledge method

Frame the reusable question before selecting structure:

- name the Architecture Object when the knowledge concerns a class of objects, or name the recurring architecture problem when no single object applies;
- bound applicability, exclusions, authority, evidence, and expected change;
- select only the Business, Data, Application, and Technology domains that change the reader decision;
- apply only the Security, Governance, and Runtime viewpoints that expose material cross-cutting concerns;
- use domain, application, governance, and runtime correctness as final checks rather than mandatory sections.

For every proposed pattern or option, state:

- applicability and constraints;
- responsibilities, information authority, state ownership, and decision authority;
- benefits, costs, and tradeoffs;
- failure, degradation, and recovery behavior;
- evidence and validation approach;
- transition and review triggers.

Derive subject-specific headings from the reader question. Keep company choices as examples or links. A company Technical Architecture, System Architecture, Project Documentation, or Machine Authority never becomes general Knowledge merely because it illustrates a pattern.

## Select the reading path

Select the dominant reader task before outlining. Keep one coherent article for mixed requests; use the dominant task to choose the sequence and incorporate secondary concerns where needed.

- **Explain a concept or relationship:** move from a concrete puzzle to the model or distinction, a worked example and counterexample, then a test the reader can apply elsewhere. Compare alternatives only when the distinction requires them.
- **Compare architectural options:** establish the common scenario and criteria, explain each mechanism, compare consequences under the same conditions, then give conditional selection and validation guidance.
- **Explain a reusable pattern:** move from problem and forces to structure and mechanism, a worked scenario and failure, then applicability, alternatives, and adoption conditions.

Treat these paths as outlining choices rather than new document types. Let a conceptual topic use change impact or dependency reasoning instead of manufacturing a request-processing flow. Preserve the template's relevant content responsibilities while adapting the order.

## Learning and transfer

Use the adaptive template to teach the mechanism before presenting selection guidance. Recover general principles from a concrete worked example by naming which assumptions can change and which invariants must hold. Use a counterexample or unsuitable context to bound the claim. Apply the shared Architecture Reasoning Method for model, scenario, and evidence checks; keep the template as the output-structure authority.

Complete the knowledge artifact only when its reader can transfer the model to another case and make the intended judgment; require adoption validation when adoption is part of that judgment.
