# Skill: review

> Structured review of code or design — defects, risks, and actionable feedback.

**Version:** 1.0.0  
**Chain well with:** test, debug, plan, refactor

---

## When to use

- Pull requests, patches, design docs
- “Any issues with this?”
- Pre-merge or pre-release gate
- Security / reliability concern on a change

**Do not use when:** the human wants a greenfield design from zero (use **think** + **plan**).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Artifact | yes | Diff, files, design text, or description |
| Intent | yes | What the change is supposed to achieve |
| Standards | no | Style, security bar, performance budget |

---

## Process

### Step 1 — Understand intent

- Restate what the change claims to do.
- Identify entry points and critical paths touched.

**Output of step:** intent + critical paths.

### Step 2 — Correctness

- Logic bugs, off-by-ones, state mistakes, error handling holes.
- Concurrency / idempotency / time / nulls where relevant.
- Mismatches vs stated intent.

**Output of step:** correctness findings (severity-tagged).

### Step 3 — Safety & abuse

- AuthZ/AuthN gaps, injection, secret leakage, SSRF, unsafe deserialization, etc. (as applicable).
- Data loss / partial failure / retry hazards.

**Output of step:** safety findings.

### Step 4 — Maintainability

- Naming, structure, duplication, API clarity.
- Testability; missing tests for risky paths.
- Observability (logs/metrics) gaps.

**Output of step:** maintainability findings.

### Step 5 — Performance & ops (if relevant)

- N+1, unbounded work, blocking calls, hot-path allocations.
- Migration / deploy / rollback notes.

**Output of step:** perf/ops findings or “N/A”.

### Step 6 — Prioritize & recommend

Severity scale:

| Sev | Meaning |
|-----|---------|
| P0 | Must fix before merge/ship |
| P1 | Should fix soon; real risk |
| P2 | Improve when touching area |
| Note | Question / suggestion only |

**Output of step:** prioritized list with concrete fixes (not vague “clean this up”).

---

## Output (final)

```markdown
## Review result

### Intent (restated)
...

### Verdict
Approve | Approve with nits | Request changes

### Findings
| ID | Sev | Area | Issue | Suggested fix |
|----|-----|------|-------|---------------|

### What’s good
- ...

### Test gaps
- ...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Every P0/P1 has a concrete suggested fix
- [ ] Intent was understood before nitpicking style
- [ ] At least one positive observation (what’s good)
- [ ] No invented line numbers or fake diff hunks

---

## Anti-patterns

- Style-only review while missing a logic bug
- “LGTM” with no reading
- Rewriting the author’s approach without a defect
- Security theater without a real path to exploit

---

## Example (miniature)

**Finding:** P0 — `userId` taken from client body instead of session on `/transfer`.  
**Fix:** derive identity server-side; add test for spoofed body id.
