# Skill: Deep Search

> Exhaustive multi-angle search — when shallow research is not enough.

**Version:** 2.0.0  
**Chain well with:** Research, Thinking, Issues Founder, ANIZ

---

## When to use

- Obscure errors, rare APIs, “nobody talks about this”
- Need coverage across docs, code, issues, changelogs, forums
- Prior research felt thin or contradictory
- Human says “deep search”, “leave no stone”, “dig”

**Do not use when:** a single official doc answers it (→ Research) or you only need a quick decision (→ Thinking).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Error string, topic, API, behavior |
| Clues | no | Versions, env, what already failed |
| Scope | no | Languages, products, date range |

---

## Process

### Step 1 — Pin the query objects

- Exact strings to hunt (errors, symbols, CVEs, package names)
- Synonyms and related terms
- Version pins (language, lib, OS)

**Output of step:** query object list.

### Step 2 — Angle map

Cover **multiple angles** (skip only if truly N/A):

1. Official docs / API reference  
2. Changelogs / release notes / migration guides  
3. Issue trackers (open + closed)  
4. Source code / signatures / types  
5. Security advisories (if relevant)  
6. Community (SO, Discords, blogs) — low trust, high signal for workarounds  
7. Adjacent systems (proxies, OS limits, cloud quirks)

**Output of step:** angle checklist with planned queries.

### Step 3 — Execute angles

- For each angle: what you found, confidence (H/M/L), source
- Capture negative results (“not in docs”) — they matter
- Extract version-specific gotchas

**Output of step:** per-angle findings log.

### Step 4 — Cross-link & resolve conflicts

- Where sources agree
- Where they conflict → which is authoritative and why
- Timeline: did behavior change in version X?

**Output of step:** consensus vs conflict table.

### Step 5 — Synthesis

- Best current explanation
- Actionable fix or next experiment
- Dead ends (so we don’t repeat them)

**Output of step:** synthesis block.

### Step 6 — Search debt

- What still unsearched
- Queries worth running later
- Hand-off: Research (polish) / Debugger (apply) / Coding (implement)

**Output of step:** debt list + hand-off.

---

## Output (final)

```markdown
## Deep Search result

### Target
...

### Best explanation
...

### Confidence
High | Medium | Low — why

### Evidence map
| Angle | Finding | Source | Conf |
|-------|---------|--------|------|

### Conflicts resolved
- ...

### Dead ends
- ...

### Do next
1.
2.
3.

### Next actions
1.
2.
```

---

## Quality bar

- [ ] ≥3 angles actually covered
- [ ] Negative results recorded
- [ ] Versions called out
- [ ] No fake issue numbers or URLs

---

## Anti-patterns

- One Google-ish paraphrase called “deep”
- Only blogs, no primaries
- Ignoring closed issues / release notes
