# Skill: Issues Founder

> Find real issues, triage them hard, write clear actionable issue reports.

**Version:** 3.0.0  
**Chain well with:** Scanning, Cyber Security, Debugger, Coding, ANIZ  
**Effort levels:** Fast · Balanced · Max

---

## When to use

- Find bugs/problems; turn scans into tickets; pre-ship defect hunt

**Do not use when:** one known bug needs root cause (→ Debugger) or only code wanted (→ Coding).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Code, design, scan output |
| Quality bar | no | Severity policy |
| Focus | no | Security, UX, perf, correctness |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Top issues now | Solid ticket pack | Exhaustive triage pack |
| **Lenses** | 2–3 | 5–6 | All 8 |
| **Tickets written** | P0–P1 only | P0–P2 | P0–P3 + icebox list |
| **Steps** | 1, 2, 4, 5 | 1–6 | 1–6 + Max extensions |
| **Evidence** | Location + why | Full ticket fields | + repro confidence notes |

### Fast
- Define focus → hunt hot lenses → triage → write P0/P1 tickets only

### Balanced
- Full process, proper tickets P0–P2

### Max
- All lenses, dedupe graph, fix-order dependencies, acceptance criteria per ticket

---

## Process

### Step 1 — Define “issue”
- Defect · risk · gap · debt (debt only if it blocks)
- Focus areas

**Output:** definitions + focus

### Step 2 — Hunt by lenses
1. Correctness / edges  
2. Errors & resilience  
3. Security & privacy (defensive only)  
4. Performance & resources  
5. UX / API usability  
6. Concurrency / idempotency  
7. Operability (logs/metrics/config)  
8. Tests missing for risky paths  

**Output:** raw notes (lens count by effort)

### Step 3 — Dedupe & evidence
*(Balanced+)*
- Merge dupes · where/what/impact/how-you-know · drop taste-only

**Output:** candidates + evidence

### Step 4 — Severity triage
| Sev | Meaning |
|-----|---------|
| P0 | Core break / critical security / data loss |
| P1 | Serious; near-term / ship risk |
| P2 | Real; schedule |
| P3 | Minor |
| Icebox | Valid, not worth now |

**Output:** triaged list

### Step 5 — Write issue tickets
Template:

```markdown
### [Sev] Title

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

*(Max: add Acceptance criteria)*

**Output:** ticket pack (depth by effort)

### Step 6 — Map fix order
*(Balanced+)*
- Sequence · quick wins · hand-offs (Debugger/Coding/Cyber Security)

**Output:** fix order

---

## Max extensions

### M1 — Dedupe graph
Which raw notes merged into which ticket.

### M2 — Acceptance criteria
Per P0–P2: testable done-when bullets.

### M3 — Effort labels
S/M/L per ticket for planning.

### M4 — Dependency map
Ticket blocked-by relationships.

### M5 — Release gate
Which issues must close before ship.

---

## Output (final)

```markdown
## Issues Founder result
**Effort:** Fast | Balanced | Max

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

### Max only
#### Release gate
...
#### Dependencies
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Effort announced
- [ ] Tickets have location + impact + evidence
- [ ] Severities not inflated
- [ ] Security tickets = remediation only, no exploits

---

## Anti-patterns

- 50 style nits as P0
- Vague “improve performance”
- Mixing five bugs in one ticket
