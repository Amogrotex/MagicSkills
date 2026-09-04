# Skill: Scanning

> Systematic checklist scans — inventory surfaces, run structured passes, report cleanly.

**Version:** 3.0.0  
**Chain well with:** Cyber Security, Issues Founder, Coding, Debugger, ANIZ  
**Effort levels:** Fast · Balanced · Max

---

## Mandate (all efforts)

- Defensive / quality scanning on assets the human may assess.
- Inventories, checklist results, fix hints.
- **No** exploit payloads or instructions to scan/attack third-party systems without authorization. If unclear, assume **owner’s assets only** and state that.

---

## When to use

- “Scan this repo/file/config”
- Pre-release checklist, secrets/deps/surfaces

**Do not use when:** one bug’s root cause (→ Debugger) or full threat model narrative (→ Cyber Security).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Repo, files, config, design |
| Scan types | no | Pass IDs; default by effort |
| Baseline | no | Accepted risks |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Hottest hits | Solid multi-pass | Full surface + coverage |
| **Inventory** | Light | Full outline | Full + trust notes |
| **Default passes** | S1, S3, S4, S5 | S1–S8 | S1–S10 |
| **Steps** | 1, 3, 4 | 1–5 | 1–5 + Max extensions |
| **Clean passes** | Optional | Explicit | Explicit + limits |

### Fast
- Quick inventory → high-signal passes → normalized top findings

### Balanced
- Full selected passes + coverage notes

### Max
- All applicable passes, severity rubric, blind-spot map, re-scan plan

---

## Process

### Step 1 — Inventory
- Languages/manifests · entry points · auth vs public · config/env · data stores · external calls · CI hints  
*(Fast: half-page max)*

**Output:** inventory outline

### Step 2 — Select scan passes
*(Balanced+; Fast: fixed default set)*

| Pass | Name | Looks for |
|------|------|-----------|
| S1 | Secrets | Keys, tokens, `.env` committed |
| S2 | Dependencies | Risky/unpinned/abandoned (high level) |
| S3 | Auth surfaces | Login, tokens, sessions |
| S4 | Access control | IDs in URLs, admin, roles |
| S5 | Input edges | SQL/shell/HTML/path/parsers |
| S6 | Config hardening | Debug, CORS, defaults |
| S7 | Error/leakage | Stacks to client, PII in logs |
| S8 | Code quality risks | TODO security, ignored errors |
| S9 | Supply/CI | Install scripts, wide perms, unpinned actions |
| S10 | Privacy | PII fields, third-party sends |

**Output:** selected passes

### Step 3 — Run passes
- Method · hits · clean · limits

**Output:** per-pass results

### Step 4 — Normalize findings
| ID | Pass | Severity (Crit/High/Med/Low/Info) | Location | Issue | Fix |

**Output:** table

### Step 5 — Coverage report
*(Balanced+)*
- What was inspected · blind spots · hand-off skills

**Output:** coverage + hand-off

---

## Max extensions

### M1 — Surface matrix
Entry × auth level × data sensitivity.

### M2 — Severity rubric used
Why each severity; consistent rules.

### M3 — False-positive log
Reviewed-and-dismissed hits + why.

### M4 — Re-scan plan
What to re-check after fixes; CI gates to add.

### M5 — Pass scorecard
| Pass | Status | Hits | Notes |

---

## Output (final)

```markdown
## Scanning result
**Effort:** Fast | Balanced | Max

### Inventory summary
...

### Passes run
- ...

### Findings
| ID | Sev | Pass | Location | Issue | Fix |
|----|-----|------|----------|-------|-----|

### Clean passes
- ...

### Blind spots
- ...

### Max only
#### Surface matrix
...
#### Re-scan plan
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Effort announced
- [ ] Pass count meets effort
- [ ] Locations actionable
- [ ] No offensive payloads

---

## Anti-patterns

- Random nits called a scan
- Claiming CVE proof without evidence
- Skipping inventory on Max
