# <Product or Feature> PRD

## Document status

| Field | Value |
|---|---|
| Owner | <Name or role> |
| Acceptance state | Draft / Accepted |
| Currency state | Current / Needs review / Superseded |
| Last updated | <Date> |
| Decision deadline | <Date or not applicable> |

## Problem

Describe the affected user, their current situation, and the observed problem. Separate evidence from hypotheses.

### Evidence

- <Observation, data, research, or customer signal>

## Intended outcome

State what should change for the user and the business.

| Measure | Current state | Target | Evaluation window |
|---|---|---|---|
| <Metric or observable result> | <Baseline> | <Target> | <Period> |

## Users and scenarios

### <Primary user or role>

- **Situation:** <Trigger and context>
- **Current behavior:** <What happens now>
- **Expected behavior:** <What should happen>

## Scope

### Included

- <Behavior or capability>

### Non-goals

- <Explicitly excluded behavior or outcome>

## User journey

Describe one representative path from trigger to observable result before listing isolated requirements.

1. <User or system action>
2. <Product response>
3. <Observable result>

## Requirements

| ID | Required behavior | Rationale or source | Acceptance condition |
|---|---|---|---|
| R1 | <Observable behavior> | <Problem, outcome, rule, or constraint> | <Verifiable result> |

## Business rules and data meaning

| Rule or term | Meaning | Example | Exception |
|---|---|---|---|
| <Rule or term> | <Concrete definition> | <Representative case> | <Boundary case> |

## Edge and failure states

| Situation | Expected product behavior | User-visible result |
|---|---|---|
| <Empty, invalid, denied, timed out, retried, cancelled, or partial state> | <Behavior> | <Result> |

## Dependencies and constraints

- <External team, policy, platform, data, deadline, or technical constraint that changes product scope>

## Rollout and measurement

- **Release approach:** <Phases, eligibility, or feature flag>
- **Monitoring:** <Metrics and qualitative signals>
- **Stop or rollback condition:** <Observable threshold>

## Risks

| Risk | Impact | Mitigation or decision |
|---|---|---|
| <Risk> | <User or business consequence> | <Response> |

## Open decisions

| Question | Owner | Needed by | Effect if unresolved |
|---|---|---|---|
| <Question> | <Role> | <Date> | <Blocked scope or decision> |

## Acceptance summary

- [ ] The problem and outcome are supported by evidence or marked hypotheses.
- [ ] Scope, scenarios, requirements, rules, and acceptance conditions agree.
- [ ] Edge states, dependencies, rollout, measurement, and open decisions are visible.
