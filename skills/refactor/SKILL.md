# Skill: refactor

> Improve structure without changing behavior — small steps, safety net on.

**Version:** 1.0.0  
**Chain well with:** test, review, debug

---

## When to use

- Code works but is hard to change
- Duplication, blurry modules, giant functions
- Prepare an area for a feature (make the change easy)
- Naming / API clarity improvements

**Do not use when:** behavior is wrong (use **debug** first) or you intentionally want a rewrite (use **think** + **plan**).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Files / module / function to improve |
| Smell | yes | What’s painful about it |
| Tests | no | Existing coverage; if weak, say so |
| Constraints | no | “Don’t change public API”, perf budget |

---

## Process

### Step 1 — Characterize current behavior

- What must remain identical (inputs/outputs/side effects)?
- Public API surface that cannot break.
- If tests are weak: list **characterization tests** to add first (hand off details to **test** if needed).

**Output of step:** behavior lock + API lock + test readiness.

### Step 2 — Identify smells (not solutions yet)

- Concrete smells with locations (long method, feature envy, shotgun surgery, etc.).
- Which smells block the human’s real goal the most?

**Output of step:** prioritized smell list.

### Step 3 — Choose refactor moves

- Pick a short sequence of **named** moves (extract function, extract module, rename, introduce parameter object, move method, …).
- Each move must be small enough to verify alone.
- Avoid mixing behavior changes.

**Output of step:** ordered move list.

### Step 4 — Safety plan

- Run which tests after each move?
- How to diff behavior (golden cases, snapshot of pure outputs)?
- Rollback unit (commit per move recommended).

**Output of step:** safety plan.

### Step 5 — Apply (or specify) moves

- For each move: before → after sketch, why safer/clearer.
- If implementing: one move at a time with verification notes.
- Keep diffs reviewable.

**Output of step:** per-move notes or code.

### Step 6 — Confirm no behavior change

- Checklist of behaviors re-verified.
- Explicitly list anything that **did** change (and why — should be empty or docs-only).

**Output of step:** confirmation checklist.

---

## Output (final)

```markdown
## Refactor result

### Behavior locked
- ...

### Moves
1. ...
2. ...

### Diff summary
...

### Verification
- ...

### Residual smells (accepted)
- ...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] No intentional feature changes mixed in
- [ ] Moves are sequenced and verifiable
- [ ] Public contracts called out
- [ ] Tests or characterization plan exists

---

## Anti-patterns

- “Refactor” that also fixes bugs and adds features
- Big-bang rewrite in one step
- Renaming everything for taste with no pain addressed
- Breaking callers “temporarily”

---

## Example (miniature)

**Smell:** 200-line `handleCheckout` mixes pricing, tax, payment, email.  
**Moves:** extract `priceCart` → extract `computeTax` → extract `chargePayment` → leave orchestrator thin.
