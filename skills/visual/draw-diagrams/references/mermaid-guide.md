# Mermaid guide

Use Mermaid for portable context, component, flow, sequence, state, and simple deployment diagrams when automatic layout remains clear.

## Theme

Start standalone diagrams with a base theme using the style-guide tokens. The templates under `assets/` provide working flow and sequence starters. Keep stable node IDs separate from display labels.

## Semantics

- Use `flowchart LR` for request, event, and data movement; use `flowchart TB` for layers, decisions, and vertical recovery.
- Use `-->` for synchronous or definite flow and `-.->` for asynchronous, delayed, optional, or eventual flow.
- Use `sequenceDiagram` when ordering, concurrency, acknowledgment, retries, or timing is the question. Prefer `alt`, `opt`, `par`, `loop`, and `critical` over simulated control-flow labels.
- Use semantic classes only when the state exists. Recheck numbered `linkStyle` rules after adding or reordering edges.
- Keep labels short, quote punctuation when required, and split before shrinking text.

## Delivery and validation

Keep Mermaid inline when Markdown is the source of truth. Use `.mmd` when rendering or reuse is part of the workflow.

Preview in the destination. When Mermaid CLI is available:

```bash
mmdc -i path/to/diagram.mmd -o /tmp/diagram.svg
```

Inspect label wrapping, crossings, ambiguous directions, whitespace, sequence width, and semantic line styles.
