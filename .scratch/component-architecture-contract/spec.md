# Component architecture template and writing contract

Status: complete

Implement the four confirmed chapters and revised guarantee-driven mechanism selection. Preserve the other three templates/contracts, skill identities, registry authorities and unrelated work. Do not change company documents or installed plugin caches.

## Accepted correction

Replace the fixed 并发控制 subsection with actual named mechanism topics chosen from the problem, interface promises, architecture characteristics and constraints. Preserve concurrency obligations when applicable; do not remove concurrency coverage where it determines correctness. State/resources and algorithm/protocol content are also proportional to the real mechanism. Verification follows the selected mechanisms rather than imposing a technical checklist.

Require an internal mechanism figure and a figure for every independently explained key algorithm flow, protocol interaction or other key flow. Require important state/resource lifecycle views conditionally. Keep context and verification figures optional unless an independently expanded key flow requires one.

## Previous obligation mapping

| Previous content | New location |
| --- | --- |
| Problem and concrete use | 1.1 |
| Consumers, scope, private/shared use and parent authority | 1.2 |
| Guarantees, qualities, principles and material constraints | 1.3 |
| Observed starting point, changes and assumptions | Explicit 1.4 plus metadata |
| Operations and input/output meaning | 2.1 |
| Usage conditions, completion/errors and dependency guarantees | 2.2–2.3 |
| Error/compatibility, substitution and consumer impact | 2.3–2.4 |
| Internal structure, choices, alternatives/costs and extension boundaries | 3.1 and selected actual topics |
| State/resource lifecycle, persistence, reconstruction and sensitive data | 3.2 where applicable |
| Algorithm/protocol steps and worked behavior | 3.3 where applicable |
| Ordering, atomicity, concurrency/cancellation and interleavings | Selected named topic or owning algorithm/state explanation when material |
| Failure, retry/replay, recovery evidence, limits and operating signals | 故障与恢复 and affected mechanism |
| Contract/guarantee verification | 4.1 |
| Mechanism, boundaries, quality scenarios and tradeoff validation | 4.2, selected from actual mechanisms |
| Replacement guarantees, transition/migration/rollback and coordination | Contract in 2.4, realization in 3, verification in 4.3 |
| Actual versus planned/illustrative evidence | Explicit 4.4 |
| Applicability limits, gaps, owners and redesign triggers | 4.5 |

## Completion

Review a full non-concurrency-centered synthetic Component artifact and rendered figures. Check stateless, concurrency-critical, shared-consumer and replacement adaptations. Validate links, packaging, existing tests, available validators, shell syntax and whitespace. Distinguish self-review from independent testing and proposed mechanisms from verified implementation.
