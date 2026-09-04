# Skill: Thinking

> Deep structured reasoning — clarify goals, challenge assumptions, decide with tradeoffs.

**Version:** 3.0.0  
**Chain well with:** Research, Coding, ANIZ, Debugger  
**Effort levels:** Fast · Balanced · Max

---

## When to use

- Vague, high-stakes, or conflicting goals
- Need clarity before coding or researching
- Multiple valid approaches; must choose

**Do not use when:** one clear mechanical step with obvious acceptance criteria.

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Request | yes | What they want |
| Context | no | Background, stack, constraints |
| Hard limits | no | Time, money, “must not” |
| Effort | no | Fast / Balanced / Max (default Balanced) |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Direction in minutes | Sound decision | Decision that survives stress |
| **Options** | 2 | 2–4 | 4–6 + “do nothing” |
| **Steps** | 1, 3, 4 | 1–6 | 1–6 + Max extensions |
| **Prose** | Bullets only | Short sections | Full + devil’s advocate memo |
| **Next actions** | 1–3 | 3–5 | 5 + validation experiment |

### Fast
- Skip long unknown inventories; list only critical assumptions (max 3)
- One primary option + one alternative
- No extended stress essay

### Balanced
- Full core process below

### Max
- Full process, then **Max extensions**
- Pre-mortem, second-order effects, decision journal
- Explicit “what would change my mind” metrics

---

## Process

### Step 1 — Restate the real goal
- One sentence **outcome** (not the method).
- Goal vs suggested means.
- Observable “done”.

**Output:** `Goal / Means suggested / Done looks like`

### Step 2 — Known / unknown / assume
*(Balanced+; Fast: only top 3 assumptions)*
- Knowns · Unknowns · Assumptions (labeled)

**Output:** three lists

### Step 3 — Force options
- Genuinely different approaches (count by effort).
- Table: Option | Upside | Downside | Risk | Effort (S/M/L) | Reversible?

**Output:** options table

### Step 4 — Decide
- Pick + **why**
- Reversal triggers
- First moves

**Output:** decision block

### Step 5 — Stress test
*(Balanced+)*
- Strongest objection · failure mode · mitigations

**Output:** 3 bullets (Max: expand to short pre-mortem)

### Step 6 — Quality check
*(Balanced+)*
- Real goal answered? Hidden assumptions? Smallest validation experiment?

**Output:** pass/fail + experiment

---

## Max extensions

### M1 — Pre-mortem
Assume the decision failed in 6 months. List 5 reasons. Mitigate top 3.

### M2 — Second-order effects
Who/what else changes? Incentives, ops load, lock-in.

### M3 — Decision journal
Record: context, options, choice, expected outcome, review date.

### M4 — Counter-recommendation
Best case for the **rejected** runner-up. Why still reject?

---

## Output (final)

```markdown
## Thinking result
**Effort:** Fast | Balanced | Max

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

### Max only
#### Pre-mortem
...
#### Decision journal
...

### Next actions
1.
2.
```

---

## Quality bar

- [ ] Effort announced and followed
- [ ] Outcome-based goal
- [ ] Options count meets effort
- [ ] Assumptions explicit
- [ ] Actionable first moves

---

## Anti-patterns

- Jumping to code mid-think
- One option fake-analyzed
- Running Max depth when asked Fast (or the reverse)
