# Skill: Thinking

> Deep structured reasoning — clarify goals, challenge assumptions, decide with tradeoffs.

**Version:** 2.0.0  
**Chain well with:** Research, Coding, ANIZ, Debugger

---

## When to use

- Vague, high-stakes, or conflicting goals
- Need clarity before coding or researching
- Multiple valid approaches; must choose
- Human says “think”, “reason”, “help me decide”

**Do not use when:** the task is a single clear mechanical step with obvious acceptance criteria.

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Request | yes | What they want |
| Context | no | Background, stack, constraints |
| Hard limits | no | Time, money, “must not” |

---

## Process

### Step 1 — Restate the real goal

- One sentence **outcome** (not the method they assumed).
- Separate goal vs suggested means.
- Define “done” in observable terms.

**Output of step:**
```
Goal: ...
Means suggested: ...
Done looks like: ...
```

### Step 2 — Known / unknown / assume

- Knowns (facts given)
- Unknowns (would change the plan)
- Assumptions (labeled; invite correction)

**Output of step:** three bullet lists.

### Step 3 — Force options

- 2–4 genuinely different approaches.
- Table: Option | Upside | Downside | Risk | Effort (S/M/L) | Reversible?

**Output of step:** options table.

### Step 4 — Decide

- Pick one (or hybrid) + **why**.
- Reversal triggers (“change mind if…”).
- First moves (max 5).

**Output of step:** decision block.

### Step 5 — Stress test

- Strongest objection
- How this fails
- Mitigations

**Output of step:** 3 bullets.

### Step 6 — Thinking quality check

- Did we answer the real goal?
- Any hidden assumption still buried?
- What’s the smallest experiment to validate?

**Output of step:** pass/fail notes + experiment.

---

## Output (final)

```markdown
## Thinking result

### Goal
...

### Decision
...

### Why
...

### Assumptions
- ...

### Open questions
- ...

### First moves
1.
2.
3.

### Revisit if
- ...

### Next actions
1.
2.
```

---

## Quality bar

- [ ] Outcome-based goal
- [ ] ≥2 real options
- [ ] Explicit assumptions
- [ ] Actionable first moves

---

## Anti-patterns

- Jumping to code mid-think
- One option fake-analyzed
- Endless rumination, no decision
