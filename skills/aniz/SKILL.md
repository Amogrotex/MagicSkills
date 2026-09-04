# Skill: ANIZ (All-In-One)

> **A**ll-i**n**-**I**n-one engi**z** — auto-route Thinking, Deep Search, Research, Coding, Debugger, Scanning, Cyber Security, and Issues Founder as one pipeline.

**Version:** 2.0.0  
**Uses:** every skill in this pack  
**Default skill** when the human does not name one or says “ANIZ” / “all in one” / “full pass”.

---

## When to use

- Complex missions spanning idea → research → build → harden → issues
- “Make it good end-to-end”
- Unsure which single skill fits
- Human links the repo and only states a goal

**Do not use when:** they named a single skill and want only that (honor the single skill).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Mission | yes | Goal in plain language |
| Artifacts | no | Code, logs, URLs, constraints |
| Mode | no | `fast` (lean chain) or `full` (default) or `secure` (security-heavy) |

---

## Process

### Step 0 — Mission brief

- Restate mission in one sentence
- Detect type tags (multi-select): `learn` | `build` | `fix` | `audit` | `decide`
- Pick **mode**: full / fast / secure (ask only if ambiguous and high-cost)

**Output of step:**
```
Mission: ...
Tags: ...
Mode: full | fast | secure
```

### Step 1 — Route (build the chain)

Select stages from this menu (include only what the mission needs):

| Stage | Skill | Include when |
|-------|--------|--------------|
| T | Thinking | Ambiguity, tradeoffs, or multi-tag mission |
| DS | Deep Search | Obscure / thin info / nasty error strings |
| R | Research | Need facts, options, docs |
| D | Debugger | Something broken with symptoms |
| C | Coding | Implementation or code change needed |
| S | Scanning | Repo/config/code exists to pass over |
| CS | Cyber Security | Auth, data, trust boundaries, “secure it” |
| IF | Issues Founder | Want a ticket list / triage pack |

**Default templates:**

| Tags | Mode | Chain |
|------|------|-------|
| decide | fast | T |
| learn | fast | R → T |
| learn | full | DS → R → T |
| build | fast | T → C |
| build | full | T → R → C → S → IF |
| fix | fast | D → C |
| fix | full | D → C → S → IF |
| audit | fast | S → IF |
| audit | full | S → CS → IF |
| audit | secure | S → CS → IF → C (fixes) |
| build+audit | full | T → R → C → S → CS → IF |
| mixed / unclear | full | T → (R or DS) → (D if broken else C) → S → IF |

Announce the chain **before** running it.

**Output of step:** ordered chain with one-line why each stage is included.

### Step 2 — Execute stages in order

For each stage in the chain:

1. State `### ANIZ stage: <Skill>`
2. Run that skill’s **Process** steps (condensed only if mode=`fast`: keep all *critical* steps, shorten prose)
3. Emit a **Stage result** mini-block (Summary + Artifacts + Hand-off)
4. Pass artifacts forward (decisions, findings, code, repros)

Rules:

- Do not skip Debugger verification when stage D ran
- Cyber Security & Scanning stay **defensive only**
- If blocked on missing input: ask once, continue other stages if possible
- If a stage is clearly N/A mid-flight: mark skipped + reason (don’t fake work)

**Output of step:** concatenated stage results.

### Step 3 — Integrate

- Resolve conflicts between stages (e.g. Research vs code reality)
- Single prioritized backlog (P0–P2)
- What’s done vs remaining

**Output of step:** integration summary + backlog.

### Step 4 — Final mission pack

Produce the ANIZ final output (below). Quality-check:

- [ ] Chain matched mission
- [ ] Each included stage left a real artifact
- [ ] Next actions are ordered and concrete

---

## Output (final)

```markdown
## ANIZ result

### Mission
...

### Chain run
1. Thinking — ...
2. ...

### Executive summary
(5–10 lines max)

### Decisions
- ...

### Deliverables
- Code / patches: ...
- Research notes: ...
- Debug root cause: ...
- Scan / security findings: ...
- Issues backlog: ...

### Backlog (priority)
| ID | Pri | Item | From stage | Next skill |
|----|-----|------|------------|------------|

### Risks & unknowns
- ...

### Next actions
1.
2.
3.
4.
5.
```

---

## Fast mode shortcuts

- Thinking: Steps 1,3,4 only  
- Research: Steps 1,3,5  
- Coding: Steps 1,3,5  
- Debugger: Steps 1,4,5,6,7  
- Scanning: inventory + highest-signal passes only (S1,S3,S4,S5,S6)  
- Issues Founder: P0–P1 tickets only  

Full and secure modes run complete child skills.

---

## Quality bar

- [ ] Explicit chain before execution
- [ ] No fake stage output
- [ ] Defensive security only
- [ ] One integrated backlog at the end

---

## Anti-patterns

- Running every skill always (waste)
- ANIZ that is only a long essay with no stage structure
- Dropping verification on fix chains
- Offensive security content

---

## Example (miniature)

**Mission:** “Add password reset to our Express API and make sure it’s not dumb-secure.”  
**Tags:** build + audit · **Mode:** full  
**Chain:** Thinking → Research (token patterns) → Coding → Scanning → Cyber Security → Issues Founder  
**Deliverables:** design decision, code, scan table, security findings, P0–P2 tickets.
