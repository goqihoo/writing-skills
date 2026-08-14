# Writing Skills

Composable agent skills for writing reusable knowledge, product requirements, technical designs, and decision records.

The set separates shared writing discipline from deliverable-specific structure. Start with `ask-writing` when the right skill is unclear.

## Invocation

Use `$ask-writing` in Agent Skills-compatible clients or `/ask-writing` in Claude Code. The router returns a ready-to-type invocation for the current client.

## Installation

Choose one installation route. The Claude Code plugin is a managed bundle; `skills.sh` installs editable skill files for Codex and other Agent Skills-compatible clients. Installing both creates duplicate copies of every skill.

### Claude Code

Add this repository as a plugin marketplace, then install the bundle:

```bash
claude plugin marketplace add goqihoo/writing-skills
claude plugin install writing-skills@goqihoo
```

From inside Claude Code, use the equivalent commands:

```text
/plugin marketplace add goqihoo/writing-skills
/plugin install writing-skills@goqihoo
```

### Codex and other agents

Use [skills.sh](https://skills.sh/) to select the skills and agents you want:

```bash
npx skills@latest add goqihoo/writing-skills
```

The installer writes skills into your project so you can edit them. Run `npx skills@latest update` when you want the latest versions.

## Maintainer setup

Run the development linker to expose every skill to Claude Code and Agent Skills-compatible harnesses:

```bash
scripts/link-skills.sh
```

The script creates symlinks in `~/.claude/skills` and `~/.agents/skills`. It stops if a destination already contains a non-symlink with the same skill name.

## Skills

### Foundations

**Model-invoked**

- [ask-writing](skills/foundations/ask-writing/SKILL.md) — Explain the available skills and recommend the next one to invoke.
- [writing-docs](skills/foundations/writing-docs/SKILL.md) — Apply the shared workflow and clarity rules used by every document skill.

### Knowledge

**Model-invoked**

- [write-knowledge-document](skills/knowledge/write-knowledge-document/SKILL.md) — Create, revise, or review reusable knowledge using the structure that matches its future use.

### Product

**Model-invoked**

- [write-product-requirements](skills/product/write-product-requirements/SKILL.md) — Create, revise, or review a PRD that aligns scope, behavior, and acceptance.

### Technical

**Model-invoked**

- [write-technical-design](skills/technical/write-technical-design/SKILL.md) — Create, revise, or review an implementation-ready technical design.
- [write-decision-record](skills/technical/write-decision-record/SKILL.md) — Record one material decision, its alternatives, costs, and review triggers.

## Adding a deliverable

Create a new skill when a document has a distinct reader decision, stable structure, and completion test. Keep variants inside an existing skill when they differ only in length or presentation.
