# Context-driven illustration evaluation

Use `request.md` and `source.md` as a behavioral fixture. Keep this rubric out of the generating agent's context. Save generated documents, working notes, renders and findings outside production documentation.

## Run and review

1. Record the tested skill/method revision or snapshot and the request/source hashes. Give a fresh run only the request, source, snapshot and output directory. For comparisons, keep the request and execution settings identical across baseline and candidate runs.
2. Read the resulting document and inspect the actual figures. Use the working notes to locate the intended question, scope and type, but score the visible result. Record concrete labels, shapes, paths and source passages for each judgment.
3. Check the three reader tasks independently:
   - **Responsibilities and connections:** Show the three objects and supported access relationships. Architecture is the natural fit. Preserve the absence of direct console-to-store access; avoid suggesting a temporal pipeline or inventing deployment zones.
   - **Request selection and completion:** Expose the A-only, B-only and combined routes with their completion conditions. Flowchart is the natural fit. Show meaningful decision/branch notation, preserve independent A/B execution and distinguish one saved result from combined-request completion. A single successful trace cannot satisfy this view.
   - **B-only interaction:** Show ordered calls and returns among the same three participants. Sequence is the natural fit. Make lifelines, message order and save acknowledgment visible; complete the request only after that acknowledgment. Keep undefined retry paths absent.
4. Accept another type only when its defining grammar visibly answers the same task without losing a source condition. Reject cosmetic variety, three relabeled generic box diagrams, or a correct plan paired with an incorrect render. Permit shared node shapes where the selected grammar supports them; do not require a cylinder for the store in a sequence diagram.
5. Check compact labels, destination readability, resolved local asset links and retained editable sources. Keep production-check results separate from semantic judgments. Repair only behavior demonstrated by the result and rerun affected cases after a repair.

Complete when all three figures have observed artifacts or explicit limits, every reader task has an evidence-backed judgment, and the report distinguishes semantic correctness from rendering quality. A planning-only run, manual walkthrough or one successful sample does not establish reliable end-to-end generation.
