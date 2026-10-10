# Diagram content preparation

Prepare the content model before selecting a visual type or drawing geometry. This is a source-analysis step, not a diagram-layout constraint.

## Read the figure's context

For a document illustration, read its owning section, the surrounding explanation needed to interpret it, and the governing source model or decisions. Establish the audience, the section's reader question, the depicted scope and abstraction level, and any current/target or proposal/accepted distinction. Use the section's intended explanation when drafting a new document. For a standalone visual, establish the same context from the request and supplied sources.

Identify the relationship or behavior the reader must be able to reconstruct from this figure. Carry forward conditions that change that interpretation, such as optional paths, independent operations, completion semantics, ownership, or trust boundaries. Resolve missing context from available sources before drawing; expose material uncertainty instead of filling it from a specimen.

## Prepare the content model

Extract only the objects, relationships, states, quantities, and boundaries needed to answer the reader question. For each object, the name is the only required content. Add one optional short detail only when the name alone does not identify the responsibility, boundary, input-to-output change, or necessary technical qualifier. Treat subtitle, tool, chip, port, boundary, and similar metadata as conditional fields: include them only when the source supports them and they change interpretation.

Identify each object's role in this view and each relationship's meaning before choosing symbols. Distinguish an actor, service, store, operation, state, entity, and deployment host where that distinction matters. Keep these roles in the working model; they need not become extra visible labels. The same named object may play different roles in different views.

Rewrite source prose into compact labels before it reaches the diagram. Do not solve excessive content by truncating or wrapping it after layout. Keep sentences, stage lists, output inventories, and explanatory prose in the consuming document. When the supported meaning cannot remain concise at destination width, split overview from detail and prepare each as a separate visual result.

The content is ready when the figure has a source-grounded reader question and scope, every retained item and relationship serves that question, every optional field changes interpretation, and no object depends on explanatory prose inside its frame.
