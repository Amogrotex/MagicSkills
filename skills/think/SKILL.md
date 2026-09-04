# Skill: think

> Structured reasoning before action — surface goals, assumptions, options, and a clear decision.

**Version:** 1.0.0  
**Chain well with:** plan, debug, research, review

---

## When to use

- The request is vague, broad, or high-stakes
- Multiple interpretations or tradeoffs exist
- You need alignment before coding, debugging, or planning
- Conflicting constraints (“fast” vs “correct” vs “cheap”)

**Do not use when:** the task is a single obvious mechanical step with clear acceptance criteria (go straight to the domain skill).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Request | yes | What the human wants |
| Context | no | Background, stack, prior decisions |
| Constraints | no | Hard limits (time, tools, “must not”) |

---

## Process

### Step 1 — Restate the real goal

- Rewrite the request as a **success condition** in one sentence.
- Separate **goal** (outcome) from **means** (how they suggested doing it).
- List stakeholders or systems affected (if any).

**Output of step:**
```
Goal: ...
Means suggested: ...
Success looks like: ...
```

### Step 2 — Inventory knowns & unknowns

- **Knowns:** facts from the human or context
- **Unknowns:** what would change the approach
- **Assumptions:** what you will treat as true if not corrected (label each)

**Output of step:** three short bullet lists (Knowns / Unknowns / Assumptions).

### Step 3 — Options & tradeoffs

- Generate 2–4 distinct approaches (not minor variants).
- For each: upside, downside, risk, effort (S/M/L).
- Note irreversible decisions.

**Output of step:** a markdown table:

| Option | Upside | Downside | Risk | Effort |
|--------|--------|----------|------|--------|

### Step 4 — Decide & justify

- Pick one option (or a hybrid) with a **why**.
- State what would make you change your mind.
- List what to do **first** (max 5 next moves).

**Output of step:** Decision + justification + reversal triggers + first moves.

### Step 5 — Stress test (light)

- Devil’s advocate: strongest objection to the decision.
- Failure mode: how this goes wrong.
- Mitigations (brief).

**Output of step:** Objection / Failure / Mitigation (3 bullets).

---

## Output (final)

```markdown
## Think result

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
```

---

## Quality bar

- [ ] Goal is outcome-based, not solution-based
- [ ] At least two real options were considered
- [ ] Assumptions are explicit
- [ ] First moves are actionable today

---

## Anti-patterns

- Jumping to implementation mid-think
- One option dressed up as analysis
- Hidden assumptions
- Endless rumination with no decision

---

## Example (miniature)

**Input:** “Should we rewrite the payment service?”  
**Decision shape:** Keep service; extract fraud checks module; revisit rewrite if latency p99 > X for 2 sprints.
