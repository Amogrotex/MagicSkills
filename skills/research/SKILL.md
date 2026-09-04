# Skill: Research

> Structured fact-finding — clear question, credible sources, comparison, recommendation.

**Version:** 2.0.0  
**Chain well with:** Deep Search, Thinking, Coding, ANIZ

---

## When to use

- “What is X?”, “best way to…”, “compare A vs B”
- Need docs, patterns, APIs, ecosystem facts
- Decision needs evidence, not vibes

**Do not use when:** pure debugging of the human’s own code (→ Debugger) or they asked for exhaustive multi-angle hunt (→ Deep Search).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Question | yes | What must be answered |
| Context | no | Stack, scale, constraints |
| Options on table | no | A/B already considered |
| Freshness | no | e.g. prefer current docs |

---

## Process

### Step 1 — Frame

- Decision or understanding needed
- Success criteria for a good answer
- Constraints that kill options early

**Output of step:** framed question + criteria + constraints.

### Step 2 — Research plan

- Sub-questions (3–7)
- Source preference: official docs, specs, primary data > random blogs
- What to ignore (undated SEO spam when freshness matters)

**Output of step:** sub-questions + source plan.

### Step 3 — Gather

- Facts per sub-question with attribution
- Note version/date when relevant
- Flag conflicts between sources

**Output of step:** findings with sources (no fake URLs).

### Step 4 — Compare

| Option | Fit to criteria | Pros | Cons | Best when |

**Output of step:** comparison table.

### Step 5 — Recommend

- Primary pick + conditions
- Runner-up
- What to validate in *their* environment (spike)

**Output of step:** recommendation block.

### Step 6 — Gaps

- Still unknown
- What would flip the recommendation

**Output of step:** gaps + revisit triggers.

---

## Output (final)

```markdown
## Research result

### Question
...

### Recommendation
...

### Why
...

### Alternatives
| Option | Verdict |
|--------|---------|

### Key findings
- ... (source)

### Sources
1. ...
2. ...

### Validate next
- ...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Tied to criteria
- [ ] Real sources for external claims
- [ ] Conflicts acknowledged
- [ ] No invented citations

---

## Anti-patterns

- Link dump, no decision
- Outdated advice as current
- “It depends” with no framework
