# Content Boundaries

Use local repository definitions first. Use these defaults only when the repository has not established a term.

## Classification model

Classify content through four independent questions:

1. **Subject:** What object, activity, commitment, or body of knowledge does it describe?
2. **Change authority:** Which external authority or internal role can make the statements outdated?
3. **Lifetime:** Does it survive a company, product, implementation, customer, or initiative change?
4. **Reader action:** Does the reader need to understand, decide, build, operate, approve, or deliver something?

Prefer change authority and lifetime over keywords in the title.

| Content class | What it owns | What changes its truth | Example |
|---|---|---|---|
| Domain | Independent professional concepts, mechanisms, methods, and constraints reusable across businesses | External evidence, standards, research, and professional practice | How MFA reduces account-takeover risk |
| Business | Actors, value exchange, rules, decisions, and lifecycle of a business activity | Industry practice, business policy, market structure, and regulation | How cyber-insurance underwriting reaches a decision |
| Product | User outcomes, offered capabilities, observable behavior, scope, and product commitments | Product decisions and releases | What evidence a risk-intelligence product accepts |
| Technical | System boundaries, implementation, integration, operation, and engineering constraints | Architecture, code, infrastructure, and operational decisions | How an underwriting agent retrieves evidence |
| Project | Customer-specific scope, decisions, delivery state, and acceptance | The project's stakeholders, contract, schedule, and delivery choices | A carrier implementation's agreed data mapping |
| Company | Organization-specific strategy, roles, policies, and internal operating facts | Company leadership and authorized internal owners | CyberSecured's product investment priorities |

Business and domain are different axes. A business combines knowledge from several domains. For example, cyber insurance can use cybersecurity, insurance, actuarial, legal, and operational-resilience knowledge without making cyber insurance the parent domain of each discipline.

## Counterfactual tests

- If the company disappeared, would the statement remain true? If yes, it is probably not company knowledge.
- If the product were replaced, would the statement remain true? If yes, it may be business or domain knowledge.
- If the implementation changed, would the statement remain true? If no, it is probably technical.
- If the customer or initiative changed, would the statement remain true? If no, it is probably project knowledge.
- Who can approve a change to the statement? Use that authority to break ties.

## Mixed material

Keep one document when supporting facts serve one primary reader action and change together. Split or relocate material when different parts have different authorities, lifetimes, or independent readers.

Give the source material one canonical home. Link to it from other contexts instead of maintaining equivalent explanations in several directories.

When no existing directory can own a valid class without breaking its stated boundary, report a **taxonomy gap**. Propose the missing boundary and its relationship to existing directories before proposing moves.
