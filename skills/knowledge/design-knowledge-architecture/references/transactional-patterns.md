# Transactional and distributed workflow patterns

Use these prompts when money, inventory, orders, entitlements, or another controlled state crosses asynchronous boundaries.

- Assign every authoritative fact and command to one Application owner.
- Keep Governance at the enforcement boundary: central policy may publish decisions or control state, but the owning subsystem executes through its normal command path.
- Specify behavior for missing, stale, conflicting, duplicate, delayed, partial, and unknown outcomes.
- Persist unknown outcomes and define reconciliation, replay, repair, evidence, and terminal-state convergence.
- Derive engineering strategy from hard recurring problems such as duplicate effects, multi-owner commit, state-machine races, replay drift, freshness gates, backpressure, failover fencing, compatibility, and unsafe repair.
- Keep ordinary component responsibility and straightforward validation in the subsystem or component note.

Treat these as reusable reasoning prompts, not as proof that a particular broker, database, topology, or transaction protocol fits a project.
