# Skill: Debugger

> Systematic root-cause debugging — reproduce, hypothesize, prove, minimal fix, verify.

**Version:** 3.0.0  
**Chain well with:** Coding, Thinking, Scanning, Deep Search, ANIZ  
**Effort levels:** Fast · Balanced · Max

---

## When to use

- Errors, wrong output, crashes, regressions, flakes

**Do not use when:** no failing behavior yet (define expected behavior first).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Symptom | yes | What goes wrong |
| Evidence | no | Logs, stacks, snippets |
| Repro | no | Steps, frequency, env |
| Recent changes | no | Commits, deploys, config |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Likely cause + next check | Proven cause + minimal fix | Cause + fix + regression net |
| **Hypotheses** | 1–2 | 3–5 | 5–8, scored |
| **Steps** | 1, 4, 5, 6 | 1–7 | 1–7 + Max extensions |
| **Verify** | Smoke idea | Defined checks | Checks + monitors + regressions |
| **Evidence bar** | Best available | Quote + path | Timeline + bisect notes |

### Fast
- Pin symptom → top hypotheses → best next probe / likely fix
- May stop at “still open + next command” if evidence thin

### Balanced
- Full core process; don’t claim fixed without verification plan

### Max
- Full process + timeline, instrument plan, differential debug, postmortem stub

---

## Process

### Step 1 — Pin the symptom
- Expected vs actual · frequency · scope · exact quotes

**Output:** Expected / Actual / Frequency / Scope / Quotes

### Step 2 — Reproduce or block
*(Balanced+; Fast if easy)*
- Minimal repro **or** blockers

**Output:** repro or blockers

### Step 3 — Evidence only (no fix yet)
*(Balanced+)*
- Stack/logs/path · recent changes · ruled out

**Output:** evidence + ruled-out

### Step 4 — Hypotheses (ranked)
- Falsifiable hypotheses (count by effort)
- Confirm / kill tests each
- Rank likelihood × cheapness

**Output:** numbered hypotheses

### Step 5 — Bisect
- Cheapest checks first
- Scoreboard: confirmed / killed / inconclusive
- Stop on proven cause; else new hypotheses

**Output:** scoreboard + root cause or still open

### Step 6 — Minimal fix
- Smallest change for the cause
- Side effects / rollout
- No drive-by refactors

**Output:** fix plan (+ code if appropriate)

### Step 7 — Verify
*(Balanced+; Fast: one smoke check)*
- Proof · nearby regressions · monitor

**Output:** verification plan

---

## Max extensions

### M1 — Incident timeline
First seen · deploy markers · rate · user impact.

### M2 — Instrumentation plan
Logs/metrics/breakpoints to add if still open.

### M3 — Differential debug
Working vs broken env/input/commit; bisect strategy.

### M4 — Regression net
Tests/cases that would have caught this (hand off to Coding).

### M5 — Postmortem stub
Root cause category · detection gap · prevention.

---

## Output (final)

```markdown
## Debugger result
**Effort:** Fast | Balanced | Max

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

### Max only
#### Timeline
...
#### Regression net
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Effort announced
- [ ] Cause specificity matches evidence
- [ ] Hypothesis count meets effort
- [ ] No “fixed” without verification at Balanced+

---

## Anti-patterns

- Shotgun rewrite before repro
- Blaming race/cache with zero evidence
- Max novel when user asked Fast
