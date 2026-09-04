# Skill: Deep Search

> Exhaustive multi-angle search — when shallow research is not enough.

**Version:** 3.0.0  
**Chain well with:** Research, Thinking, Issues Founder, ANIZ  
**Effort levels:** Fast · Balanced · Max

---

## When to use

- Obscure errors, rare APIs, contradictory info
- Need docs + issues + source + changelogs
- Human says “deep search”, “dig”, “leave no stone”

**Do not use when:** one official doc answers it (→ Research).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Error, topic, API, behavior |
| Clues | no | Versions, env, failed attempts |
| Scope | no | Languages, products, dates |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Best lead quickly | Solid multi-angle picture | Exhaustive map + dead ends |
| **Angles** | 2–3 | 4–6 | All 7 + adjacent |
| **Steps** | 1, 3, 5 | 1–6 | 1–6 + Max extensions |
| **Negatives** | Optional | Record key misses | Full dead-end log |
| **Confidence** | H/M/L gut | Justified | Justified + what would raise it |

### Fast
- Pin queries → hit highest-yield angles only → synthesize lead

### Balanced
- Full core multi-angle pass

### Max
- All angles, version timeline, conflict court, search debt ledger

---

## Process

### Step 1 — Pin the query objects
- Exact strings (errors, symbols, packages, CVEs)
- Synonyms · version pins

**Output:** query object list

### Step 2 — Angle map
*(Balanced+; Fast: pick top angles only)*

1. Official docs / API reference  
2. Changelogs / release notes / migrations  
3. Issue trackers (open + closed)  
4. Source code / types / signatures  
5. Security advisories (if relevant)  
6. Community (lower trust)  
7. Adjacent systems (OS, proxy, cloud limits)

**Output:** angle checklist + queries

### Step 3 — Execute angles
- Per angle: finding, confidence H/M/L, source
- Note negatives
- Version gotchas

**Output:** per-angle log

### Step 4 — Cross-link & conflicts
*(Balanced+)*
- Agree vs conflict · authority · version timeline

**Output:** consensus/conflict table

### Step 5 — Synthesis
- Best explanation · action/experiment · dead ends

**Output:** synthesis block

### Step 6 — Search debt
*(Balanced+)*
- Unsearched · later queries · hand-off skill

**Output:** debt + hand-off

---

## Max extensions

### M1 — Version timeline
Behavior by version; when it changed; migration notes.

### M2 — Conflict court
For each major conflict: claim A vs B, evidence, ruling, residual doubt.

### M3 — Adjacent blast
Drivers, containers, reverse proxies, rate limits, clocks, locales.

### M4 — Reproducible search log
Queries/strings another person can re-run.

### M5 — Hand-off pack
Ready input blocks for Debugger / Coding / Research.

---

## Output (final)

```markdown
## Deep Search result
**Effort:** Fast | Balanced | Max

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

### Max only
#### Version timeline
...
#### Search log
...

### Do next
1.
2.
3.
```

---

## Quality bar

- [ ] Effort announced
- [ ] Angle count meets effort
- [ ] No fake issue numbers/URLs
- [ ] Versions called out when relevant

---

## Anti-patterns

- One shallow paraphrase called “deep”
- Only blogs, no primaries
- Max dump with no synthesis
