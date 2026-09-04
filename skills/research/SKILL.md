# Skill: research

> Gather and compare knowledge with sources — then recommend with tradeoffs.

**Version:** 1.0.0  
**Chain well with:** think, plan, review

---

## When to use

- “What’s the best way to…?”
- Unknown library/API/protocol
- Compare options (vendors, patterns, algorithms)
- Need current best practices or docs

**Do not use when:** the answer is fully contained in code the human already pasted (just read it) or the task is pure debugging of their system (**debug**).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Question | yes | What decision or understanding is needed |
| Context | no | Stack, constraints, scale |
| Must-consider | no | Options already on the table |
| Freshness | no | “Must be 2024+”, etc. |

---

## Process

### Step 1 — Frame the question

- Decision to be made **or** understanding needed.
- Success criteria for a good answer.
- Constraints that kill options early.

**Output of step:** framed question + criteria + constraints.

### Step 2 — Search plan

- Sub-questions to answer.
- Sources to prefer (official docs, RFCs, primaries > blogs).
- What you will ignore (SEO spam, undated posts when freshness matters).

**Output of step:** sub-questions + source plan.

### Step 3 — Gather findings

- For each sub-question: short facts with source attribution.
- Note dates / versions when relevant.
- Flag uncertainty and conflicts between sources.

**Output of step:** findings bullets with sources (title + URL or doc name).

### Step 4 — Compare options

| Option | Fits criteria? | Pros | Cons | When to pick |
|--------|----------------|------|------|--------------|

**Output of step:** comparison table.

### Step 5 — Recommend

- One primary recommendation + conditions.
- Runner-up.
- What to validate next in *their* environment (spike).

**Output of step:** recommendation block.

### Step 6 — Open gaps

- What is still unknown.
- What would change the recommendation.

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

- [ ] Recommendation tied to stated criteria
- [ ] At least one credible source per major claim when external knowledge is used
- [ ] Conflicts between sources acknowledged
- [ ] No fake citations or invented URLs

---

## Anti-patterns

- Dumping links without a decision
- Outdated advice presented as current
- “It depends” with no decision framework
- Ignoring the human’s constraints

---

## Example (miniature)

**Question:** Queue for 10k jobs/min on Node — Redis Streams vs RabbitMQ vs SQS?  
**Recommendation shape:** SQS if already on AWS and ops simplicity > fancy routing; else Rabbit for complex routing; Streams if Redis already core and team is strong on it.
