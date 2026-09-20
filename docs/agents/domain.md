# Domain Docs

This is a single-context repository. Engineering skills use its domain documentation to preserve established terminology and architectural decisions.

## Read before exploring

Read these sources when they exist and are relevant:

- `CONTEXT.md` at the repository root
- ADRs under `docs/adr/`

If they do not exist, proceed silently. Do not create placeholders or report their absence as a problem. `/domain-modeling`, `/grill-with-docs`, and related engineering flows create them when terminology or decisions are actually resolved.

## Layout

```text
/
├── CONTEXT.md
├── docs/
│   └── adr/
└── skills/
```

## Use established vocabulary

When an issue, specification, proposal, test, or implementation names a domain concept, use the term defined in `CONTEXT.md`.

Do not replace established terms with casual synonyms. If a required concept is missing, first determine whether the proposed term is unnecessary or represents a genuine modeling gap.

## Respect architectural decisions

Read ADRs related to the area being changed. If proposed work conflicts with an accepted ADR, identify the conflict explicitly instead of silently overriding it.

For example:

> Contradicts ADR-0007 — reconsidering it because the original operating constraint no longer applies.
