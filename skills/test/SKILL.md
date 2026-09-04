# Skill: test

> Design and reason about tests — cases, gaps, repros, and verification of fixes.

**Version:** 1.0.0  
**Chain well with:** debug, plan, refactor, review

---

## When to use

- “Write tests for X”
- After a bugfix (regression net)
- Before a risky change (characterization tests)
- Coverage feels fake; need real risk-based cases

**Do not use when:** there is no behavior or interface to test yet (define behavior with **think** / **plan** first).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Subject | yes | Function, API, UI flow, or system under test |
| Behavior | yes | Spec, expected rules, or current observed behavior |
| Stack | no | Language, framework, test runner |
| Known bugs | no | Issues to lock down |
| Constraints | no | No network, speed, flaky envs |

---

## Process

### Step 1 — Define behavior under test

- List **public behaviors** (inputs → outputs / effects).
- Separate pure logic vs side effects (DB, network, time, randomness).
- Note invariants that must always hold.

**Output of step:** behavior list + invariants.

### Step 2 — Risk & surface map

- What is most likely to break?
- Boundaries: empty, max, null, unicode, auth, concurrency, timezones.
- Dependencies to mock/fake/stub vs real.

**Output of step:** risk-ranked surfaces + test doubles strategy.

### Step 3 — Case catalog

Produce cases in a table:

| ID | Type | Setup | Action | Expected | Priority |
|----|------|-------|--------|----------|----------|
| T01 | happy | … | … | … | P0 |
| T02 | edge | … | … | … | P0 |
| T03 | error | … | … | … | P1 |
| T04 | regression | … | … | … | P0 |

Types: happy, edge, error, security, property/invariant, regression, performance (only if needed).

**Output of step:** the case table (aim 5–15 solid cases, not 100 weak ones).

### Step 4 — Choose level & structure

- Pick pyramid mix: unit / integration / e2e (justify briefly).
- Name test style: Arrange-Act-Assert or Given-When-Then.
- Data builders/fixtures needed.

**Output of step:** level plan + naming + fixtures.

### Step 5 — Implement or specify

- If code context allows: write the tests (or precise pseudocode matching the stack).
- If not: provide drop-in test skeletons the human can paste.
- One assertion theme per test; avoid giant multi-assert blobs.

**Output of step:** test code or skeletons.

### Step 6 — Gap analysis

- What is still untested and why (cost vs risk)?
- Flake risks and how to de-flake (time, order, network).
- CI notes (what must run on every PR).

**Output of step:** gaps + flake notes + CI recommendation.

---

## Output (final)

```markdown
## Test result

### Behaviors covered
- ...

### Case catalog
(table)

### Tests
(code or skeletons)

### Gaps & risks
- ...

### How to run
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Cases map to real risks, not only happy path
- [ ] At least one edge and one failure path
- [ ] Expectations are precise (values, errors, side effects)
- [ ] No dependency on wall-clock or test order unless isolated

---

## Anti-patterns

- Testing implementation details only (brittle private internals)
- Snapshot spam with no intent
- “Coverage 90%” with zero boundary cases
- Sleeping in tests to “wait for things”

---

## Example (miniature)

**Subject:** `applyCoupon(cart, coupon)`  
**P0 cases:** valid %, valid fixed, expired coupon, null discount field, cart empty, double-apply idempotency.
