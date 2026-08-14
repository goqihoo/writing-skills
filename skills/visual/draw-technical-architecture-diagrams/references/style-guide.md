# Technical visual style

Use a calm technical-editorial system: warm canvas, neutral surfaces, slate text and structure, one blue focus, sparse semantic accents, flat geometry, and generous whitespace.

## Tokens

| Role | Hex | Use |
|---|---:|---|
| Canvas | `#F8FAFC` | Default background |
| Surface | `#FFFFFF` | Nodes and panels |
| Text | `#0F172A` | Titles and names |
| Secondary text | `#64748B` | Annotations |
| Border | `#CBD5E1` | Normal boundaries |
| Connector | `#94A3B8` | Ordinary relationships |
| Focus | `#2563EB` / `#EFF6FF` | One real focal element or path |
| Success | `#16A34A` / `#F0FDF4` | Verified or healthy state only |
| Warning | `#D97706` / `#FFF7ED` | Delay, retry, or degradation only |
| Error | `#DC2626` / `#FEF2F2` | Failure, rejection, or attack only |
| External | `#7C3AED` / `#F3E8FF` | External actor or platform |

Do not color every peer differently by default. When color identifies real categories, retain labels and do not let category colors imply status.

## Typography and spacing

- Use `Inter`, `Noto Sans SC`, or `PingFang SC`; use `JetBrains Mono` for protocols or symbols.
- Use 20–24 px titles, 14–16 px node names, and at least 11–12 px annotations.
- Keep nodes to a name and one short responsibility line.
- Use an 8 px spacing grid, 8–12 px corner radius, 1–1.5 px normal borders, and 2 px only for a real focus.
- Keep peer nodes aligned and equally sized when their roles are equal.

## Shape and connector meaning

| Form | Meaning |
|---|---|
| Rounded rectangle | Logical service, module, or application |
| Rectangle | Runtime unit or process |
| Cylinder | Durable storage or log |
| Pill or actor | User, client, or external actor |
| Solid container | Ownership, trust, domain, or deployment boundary |
| Dashed container | Optional, future, or logical scope |
| Solid arrow | Synchronous, gating, or definite flow |
| Dashed arrow | Asynchronous, delayed, optional, or eventual flow |
| Red arrow | Failure, rejection, or exceptional flow |

Name every boundary. Use a double-headed arrow only for a genuinely bidirectional interaction.

## Layout

- Use left-to-right for request, business, and data flows; top-to-bottom for layers and decision trees; outside-to-inside for trust; normal direction with failures branching downward.
- Keep one primary axis. Restructure or split when crossings remain.
- Separate context, component, deployment, sequence, and failure views rather than mixing them.
- Default to `1200 × 800` for documents and `1600 × 900` for wide presentation output.

## Accessibility and delivery

- Pair semantic colors with labels, shapes, or line styles; avoid red/green-only meaning.
- Add an accessible title and description to SVG or HTML and meaningful alt text to raster output.
- Retain editable source beside exports and use relative links from Markdown.
- Inspect both source and render; syntax validity alone is insufficient.
