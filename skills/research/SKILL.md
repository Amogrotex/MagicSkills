# Skill: Research

> Structured fact-finding — clear question, credible sources, comparison, recommendation.

**Version:** 3.0.0  
**Chain well with:** Deep Search, Thinking, Coding, ANIZ  
**Effort levels:** Fast · Balanced · Max

---

## When to use

- “What is X?”, “best way…”, “compare A vs B”
- Docs, patterns, APIs, ecosystem facts

**Do not use when:** pure debugging (→ Debugger) or exhaustive multi-angle hunt (→ Deep Search).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Question | yes | What must be answered |
| Context | no | Stack, scale, constraints |
| Options on table | no | A/B already considered |
| Freshness | no | Prefer current docs |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Best-guess answer now | Defensible recommendation | Publication-grade brief |
| **Sources** | 1–2 strong | 3–6 | 7+ across types; note conflicts |
| **Options compared** | ≤2 | 2–4 | 4–6 |
| **Steps** | 1, 3, 5 | 1–6 | 1–6 + Max extensions |
| **Citations** | Name + link if known | Required for claims | + dates/versions |

### Fast
- Frame → top findings → recommend
- Skip big comparison tables if only one serious option

### Balanced
- Full core process

### Max
- Multiple source types; steelman each option; risk register; spike plan

---

## Process

### Step 1 — Frame
- Decision vs understanding
- Success criteria
- Constraints that kill options

**Output:** framed question + criteria + constraints

### Step 2 — Research plan
*(Balanced+)*
- Sub-questions (Fast: skip formal plan; Balanced: 3–5; Max: 5–8)
- Source preference: official > primary > commentary

**Output:** sub-questions + source plan

### Step 3 — Gather
- Facts with attribution
- Version/date when relevant
- Conflicts flagged

**Output:** findings + sources (no fake URLs)

### Step 4 — Compare
*(Balanced+; Fast if ≥2 options)*
| Option | Fit | Pros | Cons | Best when |

**Output:** comparison table

### Step 5 — Recommend
- Primary + conditions · runner-up · validate-in-env spike

**Output:** recommendation block

### Step 6 — Gaps
*(Balanced+)*
- Unknowns · flip triggers

**Output:** gaps + revisit

---

## Max extensions

### M1 — Source quality score
For each key source: type (official/spec/blog), recency, bias risk, weight.

### M2 — Steelman matrix
Best argument *for* each rejected option before dismissing.

### M3 — Risk register
What goes wrong if recommendation is wrong? Early warning signs?

### M4 — Spike plan
Smallest empirical test (time-boxed) to confirm fit in *their* stack.

### M5 — Bibliography
Clean source list with one-line takeaway each.

---

## Output (final)

```markdown
## Research result
**Effort:** Fast | Balanced | Max

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

### Validate next
- ...

### Max only
#### Source quality
...
#### Spike plan
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Effort announced
- [ ] Recommendation tied to criteria
- [ ] Source count meets effort
- [ ] No invented citations

---

## Anti-patterns

- Link dump, no decision
- Max-length essay on Fast
- Outdated advice as current
