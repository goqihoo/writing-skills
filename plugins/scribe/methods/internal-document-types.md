# Internal Document Type method

Use this method inside a Writer that owns registered Internal Document Types and compatible Freeform Artifacts.

## Registry routing

1. Read the owning Writer's `references/internal-document-types.yaml` as the configuration authority; preserve that owner when the active Writer declares an explicit adaptation.
2. Select a registered type from the user's explicit result first. Use the target title, path, reader question, content, and healthy siblings only to confirm or infer an underspecified request.
3. Apply an explicit user-request adaptation branch declared by the active Writer before ordinary routing, preserving the owning registry and authority. Otherwise route an independently owned Public Skill result to that skill without invoking it.
4. Treat a compatible occasional artifact that matches the Writer's authority but no registered type as a Freeform Artifact. Do not reject it or create a permanent type automatically.
5. After resolving any declared adaptation, stop when the requested artifact still belongs to an unsupported authority scope or drafting would formalize an unsupported company or product boundary.

## Structure modes

- A type without `template` uses Freeform Structure. Derive its artifact plan from the reader question, authority, evidence, completion profile, and healthy local conventions. Resolve routine headings without interviewing the user.
- A type with `template` reads only the configured asset, whether local or shared under `methods/architecture-templates/assets/`, and applies its explicit policy:
  - `fixed` preserves exact headings, order, and fields.
  - `sequence` preserves reasoning or action order while allowing subject-specific headings.
  - `adaptive` preserves content responsibilities while allowing merging, reordering, layout changes, and visible omission.
- A Freeform Artifact uses the Writer's general authority and completion contract without pretending it is a registered type.

## Completion

The routing is complete when one Writer owns the result, the selected registered type or Freeform fallback is explicit inside the execution, the applicable authority and evidence boundaries are preserved, only an assigned template constrains structure, and the configured or general completion contract is checkable.
