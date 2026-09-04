# Skill: Issues Founder

> Find real issues, triage them hard, write clear actionable issue reports.

**Version:** 2.0.0  
**Chain well with:** Scanning, Cyber Security, Debugger, Coding, Review-style passes, ANIZ

---

## When to use

- “Find bugs / problems / issues in this”
- Turn scan or review notes into tickets
- Pre-ship defect hunt (functional, UX, reliability, security-as-issues)
- Human says “issues founder”, “find issues”, “triage”

**Do not use when:** a single known bug needs root cause (→ Debugger) or they only want code written (→ Coding).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Code, design, product area, scan output |
| Quality bar | no | What “good” means; severity policy |
| Focus | no | Security, UX, perf, correctness, docs |

---

## Process

### Step 1 — Define “issue”

Agree what counts:

- Defect (wrong behavior)
- Risk (likely future defect / security weakness)
- Gap (missing requirement, test, observability)
- Debt (only if it blocks change or reliability — avoid nit spam)

**Output of step:** issue definition + focus.

### Step 2 — Hunt by lenses

Run lenses (skip N/A):

1. Correctness / edge cases  
2. Error handling & resilience  
3. Security & privacy (defensive findings only)  
4. Performance & resource use  
5. UX / API usability  
6. Concurrency / idempotency  
7. Operability (logs, metrics, config)  
8. Tests missing for risky paths  

**Output of step:** raw notes per lens.

### Step 3 — Dedupe & evidence

- Merge duplicates
- Each surviving issue needs: **where**, **what**, **why it matters**, **how you know**
- Drop pure taste without impact

**Output of step:** candidate list with evidence.

### Step 4 — Severity triage

| Sev | Meaning |
|-----|---------|
| P0 | Breaks core / security critical / data loss — fix now |
| P1 | Serious; ship-blocker or near-term |
| P2 | Real issue; schedule |
| P3 | Minor / polish |
| Icebox | Valid but not worth a ticket now |

**Output of step:** triaged list.

### Step 5 — Write issue tickets

For each P0–P2 (and important P3), write:

```markdown
### [Sev] Title (short, specific)

**Type:** defect | risk | gap | debt
**Location:** ...
**Summary:** ...
**Steps / Evidence:** ...
**Expected:** ...
**Actual / Risk:** ...
**Impact:** ...
**Suggested fix:** ...
**Repro confidence:** High | Medium | Low
```

**Output of step:** ticket pack.

### Step 6 — Map fix order

- Recommended sequence (dependencies between fixes)
- Quick wins vs deep work
- Which tickets need Debugger / Coding / Cyber Security next

**Output of step:** fix order + hand-offs.

---

## Output (final)

```markdown
## Issues Founder result

### Focus
...

### Summary counts
P0: n | P1: n | P2: n | P3: n | Icebox: n

### Issues
(ticket pack)

### Fix order
1.
2.
3.

### Out of scope / icebox
- ...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Every ticket has location + impact + evidence
- [ ] Severities not inflated
- [ ] Actionable suggested fixes
- [ ] No exploit instructions inside security tickets — remediation only

---

## Anti-patterns

- 50 style nits as P0
- Vague “improve performance”
- Issues without location
- Mixing five bugs in one ticket
