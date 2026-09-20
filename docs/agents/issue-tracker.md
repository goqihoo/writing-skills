# Issue tracker: Local Markdown

Issues and specifications for this repository live as Markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The specification is `.scratch/<feature-slug>/spec.md`
- Implementation issues are stored as individual files under `.scratch/<feature-slug>/issues/<NN>-<slug>.md`
- Ticket numbering starts at `01`
- Never combine all implementation tickets into one file
- Triage state is recorded as a `Status:` line near the top of each issue
- Comments and conversation history are appended under a `## Comments` heading

## Publishing to the issue tracker

When a skill says “publish to the issue tracker,” create the corresponding file under `.scratch/<feature-slug>/`, creating the directory when needed.

## Fetching a ticket

Read the referenced ticket file. The user will normally provide its path or issue number.

## Wayfinding operations

`/wayfinder` uses one map file and one child file per ticket.

- Map: `.scratch/<effort>/map.md`
- Child ticket: `.scratch/<effort>/issues/NN-<slug>.md`
- `Type:` records `research`, `prototype`, `grilling`, or `task`
- `Status:` records `claimed` or `resolved`
- `Blocked by: NN, NN` records blocking relationships
- A ticket is unblocked when every listed blocker is resolved
- Claim a ticket by setting `Status: claimed` before beginning work
- Resolve it by appending the result under `## Answer`, setting `Status: resolved`, and adding a summary and link to the map
