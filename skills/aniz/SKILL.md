# Skill: ANIZ (All-In-One)

> **A**ll-i**n**-**I**n-one engi**z** — auto-route every skill as one pipeline, with **Fast / Balanced / Max** effort.

**Version:** 3.0.0  
**Uses:** every skill in this pack  
**Default** when the human does not name a skill or says “ANIZ” / “all in one” / “full pass”.  
**Effort levels:** Fast · Balanced · Max

---

## When to use

- Missions spanning idea → research → build → harden → issues
- “Make it good end-to-end” / unsure which skill
- Only a goal + this repo link

**Do not use when:** a single named skill was requested (honor it; still apply effort).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Mission | yes | Goal in plain language |
| Artifacts | no | Code, logs, URLs, constraints |
| Effort | no | Fast / Balanced / Max (default **Balanced**) |
| Focus | no | `secure` bias (extra CS/Scanning), `fix` bias, etc. |

**Legacy:** `mode: fast|full|secure` still works → map: `fast`→Fast, `full`→Balanced, `secure`→Max + security-heavy chain.

---

## Effort matrix (ANIZ-level)

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Shortest useful chain | Solid end-to-end | Thorough mission pack |
| **Child effort** | All children **Fast** | All **Balanced** | All **Max** (or override per stage) |
| **Chain length** | 1–3 stages | 3–5 stages | 4–7 stages as needed |
| **Stage prose** | Mini results only | Full stage results | Full + integration depth |
| **Backlog** | Top 3 actions | P0–P2 table | Full backlog + deps + gates |

Per-stage override example: `ANIZ Effort: Balanced; Coding: Max; Research: Fast`.

---

## Process

### Step 0 — Mission brief
- One-sentence mission
- Tags (multi): `learn` | `build` | `fix` | `audit` | `decide`
- Resolve **Effort** (and optional focus)
- Announce: `ANIZ · Effort: X · Tags: …`

**Output:** Mission / Tags / Effort / Focus

### Step 1 — Route (build the chain)

| Stage | Skill | Include when |
|-------|--------|--------------|
| T | Thinking | Ambiguity, tradeoffs, multi-tag |
| DS | Deep Search | Obscure / thin info / nasty errors |
| R | Research | Facts, options, docs |
| D | Debugger | Broken with symptoms |
| C | Coding | Implementation needed |
| S | Scanning | Code/config to pass over |
| CS | Cyber Security | Auth, data, “secure it”, focus=secure |
| IF | Issues Founder | Ticket list / triage |

**Templates by tags × effort:**

| Tags | Fast chain | Balanced chain | Max chain |
|------|------------|----------------|-----------|
| decide | T | T | T (+ R if needed) |
| learn | R | R → T | DS → R → T |
| build | T → C | T → R → C → IF | T → R → C → S → IF |
| fix | D → C | D → C → IF | D → C → S → IF |
| audit | S → IF | S → CS → IF | S → CS → IF → C (fix P0s) |
| build+audit | T → C → IF | T → R → C → S → IF | T → R → C → S → CS → IF |
| unclear | T → C or T → R | T → R → C → IF | T → DS/R → D/C → S → IF |

Announce chain **before** running.  
**Output:** ordered chain + why each stage

### Step 2 — Execute stages
For each stage:

1. `### ANIZ stage: <Skill> · Effort: <…>`
2. Run that skill’s process at the resolved child effort
3. Emit **Stage result** (Summary + Artifacts + Hand-off)
4. Pass artifacts forward

Rules:
- No fake stages; skip with reason if N/A mid-flight
- Debugger verification required at Balanced/Max when D ran
- Cyber Security & Scanning stay **defensive only**
- Missing input: ask once; continue other stages if possible

**Output:** concatenated stage results

### Step 3 — Integrate
- Resolve cross-stage conflicts
- Single prioritized backlog
- Done vs remaining

**Output:** integration + backlog

### Step 4 — Final mission pack
Emit ANIZ Output. Check:
- [ ] Chain matched mission + effort
- [ ] Each stage left a real artifact
- [ ] Next actions concrete

---

## Max extensions (ANIZ)

### M1 — Stage scorecard
| Stage | Effort | Status | Key artifact | Open loops |

### M2 — Dependency backlog
Backlog items with blocked-by links.

### M3 — Mission risks
Top risks across stages + early warnings.

### M4 — Re-run plan
What to re-invoke (which skill + effort) after human does next actions.

### M5 — Executive one-pager
10 lines suitable for a teammate who skips stage logs.

---

## Output (final)

```markdown
## ANIZ result
**Effort:** Fast | Balanced | Max

### Mission
...

### Chain run
1. Thinking (Fast) — ...
2. ...

### Executive summary
(Fast: 3 lines · Balanced: 5–10 · Max: 10 + risks)

### Decisions
- ...

### Deliverables
- Code / patches: ...
- Research: ...
- Debug: ...
- Scan / security: ...
- Issues: ...

### Backlog
| ID | Pri | Item | From | Next skill |
|----|-----|------|------|------------|

### Risks & unknowns
- ...

### Max only
#### Stage scorecard
...
#### Re-run plan
...

### Next actions
1.
2.
3.
4.
5.
```

---

## Quality bar

- [ ] Effort announced (ANIZ + children)
- [ ] Explicit chain before execution
- [ ] No fake stage output
- [ ] Defensive security only
- [ ] Integrated backlog

---

## Anti-patterns

- Always running every skill (ignore effort)
- Essay with no stage structure
- Dropping verification on fix chains
- Child Max when ANIZ Fast was requested (unless per-stage override)

---

## Example

**Mission:** “Add password reset to Express API; don’t be dumb on security.”  
**Effort:** Balanced · **Tags:** build + audit  
**Chain:** Thinking → Research → Coding → Scanning → Cyber Security → Issues Founder  
*(All children Balanced unless overridden)*
