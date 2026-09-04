# Skill: Coding

> Ship solid code — clarify behavior, design small, implement clean, verify.

**Version:** 2.0.0  
**Chain well with:** Thinking, Research, Debugger, Issues Founder, Scanning, ANIZ

---

## When to use

- Write new code, features, scripts, components
- Modify existing code with clear intent
- Generate production-minded implementations (not throwaway junk)

**Do not use when:** root cause of a bug is still unknown (→ Debugger first) or the goal itself is unclear (→ Thinking first).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Goal | yes | What the code must do |
| Stack | yes | Language, framework, runtime |
| Context | no | Existing files, APIs, style |
| Constraints | no | Perf, no-new-deps, public API freeze |

---

## Process

### Step 1 — Spec the behavior

- Inputs / outputs / side effects
- Error cases
- Non-goals (what we are *not* building)

**Output of step:** short behavior spec.

### Step 2 — Shape the design

- Where code lives (files/modules)
- Data structures & interfaces (types/signatures)
- Dependencies (reuse vs add)
- Edge cases list

**Output of step:** design sketch (signatures + file plan).

### Step 3 — Implement in thin slices

- Build the smallest working slice first
- Prefer clarity over cleverness
- Match existing project style when context exists
- No drive-by unrelated refactors

**Output of step:** code (or ordered patches).

### Step 4 — Self-review the diff

Check for:

- Correctness vs spec
- Error handling
- Resource cleanup / boundaries
- Security footguns (injection, secrets, authz) at a glance
- Naming and readability

**Output of step:** self-review notes (issues found + fixed).

### Step 5 — Verify

- How to run / test
- Happy path + ≥1 edge + ≥1 failure case
- If tests can’t run here: provide exact commands and expected results

**Output of step:** verification plan (+ tests if applicable).

### Step 6 — Handoff

- What was done
- What remains
- Risks / TODOs

**Output of step:** handoff bullets.

---

## Output (final)

```markdown
## Coding result

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

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Matches spec
- [ ] Edge/error paths considered
- [ ] Runnable or clearly testable
- [ ] No invented project files presented as already existing

---

## Anti-patterns

- Giant dump with no structure
- “Something like this” pseudo-code when real code was asked
- Silent scope creep / rewrites
- Ignoring the repo’s existing patterns
