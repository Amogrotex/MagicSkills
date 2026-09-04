# Skill: debug

> Systematic root-cause debugging — evidence first, minimal fix, verified.

**Version:** 1.0.0  
**Chain well with:** think, test, review

---

## When to use

- Errors, exceptions, wrong output, crashes
- Regressions (“worked yesterday”)
- Flaky behavior, race-ish symptoms
- Performance anomalies with a suspected cause space

**Do not use when:** there is no failing behavior yet (use **plan** or **test** to define expected behavior first).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Symptom | yes | What goes wrong (message, wrong value, when) |
| Environment | no | OS, runtime versions, env (prod/stage/local) |
| Repro | no | Steps, inputs, frequency |
| Code / logs | no | Snippets, stack traces, links |
| Recent changes | no | Commits, deploys, config diffs |

---

## Process

### Step 1 — Capture the symptom precisely

- What is **expected** vs **actual**?
- When does it happen (always / sometimes / after X)?
- Blast radius (one user, one endpoint, whole system)?
- Quote exact error text / status codes / wrong values.

**Output of step:** Expected / Actual / Frequency / Scope / Evidence quote.

### Step 2 — Reproduce (or state blockers)

- Minimal reproduction steps.
- If you cannot reproduce: list what is missing to repro.
- Note whether this is prod-only and why that matters.

**Output of step:** Repro steps **or** blocker list.

### Step 3 — Gather evidence (no fixing yet)

- Stack traces, logs around the time window, failing assertions.
- Relevant code paths (entry → suspects).
- Recent changes that touch those paths.
- What you can **rule out** already.

**Output of step:** Evidence list + ruled-out list.

### Step 4 — Hypothesize (ranked)

- Write 3–5 concrete hypotheses (falsifiable).
- Rank by likelihood × ease of checking.
- For each: **how to confirm** and **how to kill**.

**Output of step:** numbered hypotheses with confirm/kill tests.

### Step 5 — Test hypotheses (bisect)

- Run the cheapest kill/confirm checks first.
- Record result per hypothesis: confirmed / killed / inconclusive.
- Stop when one root cause is confirmed with evidence.
- If all killed: generate new hypotheses from new evidence (say so).

**Output of step:** hypothesis scoreboard + confirmed root cause (or “still open”).

### Step 6 — Minimal fix

- Propose the **smallest** change that addresses the root cause (not every smell).
- Call out side effects and feature flags / rollout if relevant.
- Do **not** implement drive-by refactors here (use **refactor** later).

**Output of step:** fix description + why minimal + risks.

### Step 7 — Verify

- How to prove the fix works (test, manual check, metric).
- Regression checks (nearby behaviors).
- What to monitor after deploy.

**Output of step:** verification plan.

---

## Output (final)

```markdown
## Debug result

### Symptom
Expected: ...
Actual: ...

### Root cause
...

### Evidence
- ...

### Fix (minimal)
...

### Verification
- ...

### Hypotheses killed
- ...

### Follow-ups (optional, non-blocking)
- ...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Root cause is specific (file/function/condition), not “something in backend”
- [ ] At least one alternative hypothesis was seriously tested or killed
- [ ] Fix maps 1:1 to root cause
- [ ] Verification is defined before claiming “fixed”

---

## Anti-patterns

- Shotgun rewriting before a repro
- “Fixed” without saying how you know
- Blaming “race condition” / “caching” with no evidence
- Ignoring the first stack frame that is actually your code

---

## Example (miniature)

**Symptom:** 500 on `POST /checkout` when cart has a coupon.  
**Root cause:** `coupon.discount` null; code assumes number.  
**Fix:** default to `0` + validate coupon payload at boundary.  
**Verify:** unit test null discount + one integration request with bad coupon.
