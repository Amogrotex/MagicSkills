# Skill: Coding

> Ship solid code — clarify behavior, design small, implement clean, verify.

**Version:** 3.0.0  
**Chain well with:** Thinking, Research, Debugger, Issues Founder, Scanning, ANIZ  
**Effort levels:** Fast · Balanced · Max

---

## When to use

- Write or change code, features, scripts, components
- Production-minded implementations

**Do not use when:** root cause unknown (→ Debugger) or goal unclear (→ Thinking).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Goal | yes | What the code must do |
| Stack | yes | Language, framework, runtime |
| Context | no | Files, APIs, style |
| Constraints | no | Perf, deps, API freeze |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Working slice | Clean, verified feature | Production-hardened |
| **Design** | Signatures only | Files + types + edges | + failure modes, rollout |
| **Tests** | How-to-run notes | Happy + edge + fail | Table of cases + code |
| **Self-review** | Quick pass | Structured checklist | + security/perf lens |
| **Steps** | 1, 3, 5 | 1–6 | 1–6 + Max extensions |

### Fast
- Tiny spec → code → run instructions
- Skip long design essays and deep review

### Balanced
- Full core process

### Max
- Full process + characterization tests, API notes, rollback, complexity notes

---

## Process

### Step 1 — Spec the behavior
- Inputs / outputs / side effects
- Error cases
- Non-goals  
*(Fast: 5 lines max)*

**Output:** behavior spec

### Step 2 — Shape the design
*(Balanced+)*
- Files/modules · interfaces · deps · edges

**Output:** design sketch

### Step 3 — Implement in thin slices
- Smallest working slice first
- Clarity > cleverness
- Match project style when known
- No unrelated refactors

**Output:** code / patches

### Step 4 — Self-review
*(Balanced+; Fast: 3-bullet glance)*
- Correctness · errors · resources · security footguns · naming

**Output:** review notes (+ fixes applied)

### Step 5 — Verify
- Run/test instructions
- Cases by effort (see matrix)
- If can’t run: exact commands + expected results

**Output:** verification plan (+ tests)

### Step 6 — Handoff
*(Balanced+)*
- Done · remains · risks/TODOs

**Output:** handoff bullets

---

## Max extensions

### M1 — Case table
| ID | Type | Input | Expected | Covered by |

### M2 — API / contract notes
Public signatures, error codes, backwards compatibility.

### M3 — Failure & rollback
Partial failure, idempotency, how to revert.

### M4 — Complexity & perf notes
Expected cost, obvious bottlenecks, safe limits.

### M5 — Security glance
AuthZ, injection surfaces, secret handling in *this* change.

---

## Output (final)

```markdown
## Coding result
**Effort:** Fast | Balanced | Max

### Spec
...

### Design
...

### Code
...

### How to run / test
...

### Self-review
- ...

### Risks & TODOs
- ...

### Max only
#### Case table
...
#### Rollback
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Effort announced
- [ ] Matches spec
- [ ] Verification depth meets effort
- [ ] No fake “existing” project files

---

## Anti-patterns

- Giant unstructured dump
- Pseudo-code when real code was asked
- Silent rewrites
- Max gold-plating on Fast request
