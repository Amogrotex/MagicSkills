# Skill: Debugger

> Systematic root-cause debugging — reproduce, hypothesize, prove, minimal fix, verify.

**Version:** 2.0.0  
**Chain well with:** Coding, Thinking, Scanning, Deep Search, ANIZ

---

## When to use

- Errors, exceptions, wrong output, crashes
- Regressions, flakes, “works on my machine”
- Performance symptoms with a bounded cause space

**Do not use when:** there is no failing behavior yet (define expected behavior first with Thinking/Coding).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Symptom | yes | What goes wrong |
| Evidence | no | Logs, stack traces, screenshots, snippets |
| Repro | no | Steps, frequency, environment |
| Recent changes | no | Commits, deploys, config |

---

## Process

### Step 1 — Pin the symptom

- Expected vs actual
- Frequency and scope
- Exact quotes (errors, status codes, bad values)

**Output of step:** Expected / Actual / Frequency / Scope / Quotes.

### Step 2 — Reproduce or block

- Minimal repro steps  
  **or** what is missing to reproduce

**Output of step:** repro **or** blocker list.

### Step 3 — Evidence only (no fix yet)

- Stack/logs/code path
- Recent changes touching the path
- Already ruled out

**Output of step:** evidence + ruled-out.

### Step 4 — Hypotheses (ranked)

- 3–5 falsifiable hypotheses
- For each: how to **confirm** / how to **kill**
- Rank by likelihood × cheapness to test

**Output of step:** numbered hypotheses.

### Step 5 — Bisect

- Run cheapest checks first
- Scoreboard: confirmed / killed / inconclusive
- Stop on proven root cause; if none, new hypotheses from new evidence

**Output of step:** scoreboard + root cause (or still open).

### Step 6 — Minimal fix

- Smallest change that addresses the cause
- Side effects / rollout notes
- No drive-by refactors

**Output of step:** fix plan (+ code if appropriate).

### Step 7 — Verify

- Proof the fix works
- Nearby regression checks
- What to monitor

**Output of step:** verification plan.

---

## Output (final)

```markdown
## Debugger result

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

### Killed hypotheses
- ...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Specific root cause (not “backend issue”)
- [ ] Alternatives tested or killed
- [ ] Fix maps to cause
- [ ] Verification defined before “fixed”

---

## Anti-patterns

- Shotgun rewrite before repro
- “Fixed” with no proof
- Blaming race/cache with zero evidence
