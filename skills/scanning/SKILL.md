# Skill: Scanning

> Systematic checklist scans — inventory surfaces, run structured passes, report cleanly.

**Version:** 2.0.0  
**Chain well with:** Cyber Security, Issues Founder, Coding, Debugger, ANIZ

---

## Mandate

- **Defensive / quality scanning only** on code, configs, deps, and designs the human is allowed to assess.
- Produce inventories, checklist results, and fix hints.
- Do **not** produce exploit payloads, attack automation, or instructions to scan/attack third-party systems without authorization context. If scope is unclear, assume **only assets the human owns** and state that assumption.

---

## When to use

- “Scan this repo/file/config”
- Pre-release checklist, dependency pass, secret hygiene pass
- Inventory endpoints, permissions, env vars, attack surface (descriptive)

**Do not use when:** they need root-cause on one bug (→ Debugger) or full threat modeling narrative (→ Cyber Security).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Repo path, files, config, design |
| Scan types | no | Which passes (see Step 2); default = sensible set |
| Baseline | no | Known accepted risks |

---

## Process

### Step 1 — Inventory

Map what exists:

- Languages / package manifests
- Entry points (HTTP routes, CLIs, workers, cron)
- Auth’d vs public surfaces
- Config & env surface
- Data stores & external calls
- CI/CD hints if present

**Output of step:** inventory outline.

### Step 2 — Select scan passes

Choose applicable passes (skip N/A with reason):

| Pass ID | Name | Looks for |
|---------|------|-----------|
| S1 | Secrets | API keys, tokens, private keys, `.env` committed |
| S2 | Dependencies | Known risky patterns, pinned/unpinned, abandoned libs (high level) |
| S3 | Auth surfaces | Login, tokens, session flags, password flows |
| S4 | Access control | IDs in URLs, admin routes, role checks |
| S5 | Input edges | Parsers, SQL/raw query, shell, HTML, file paths |
| S6 | Config hardening | Debug left on, permissive CORS, directory listing, default creds |
| S7 | Error/leakage | Stack traces to clients, verbose errors, PII in logs |
| S8 | Code quality risks | Huge functions, `TODO security`, panic/unwrap abuse, ignored errors |
| S9 | Supply/CI | Install scripts, wide permissions, unpinned actions (if present) |
| S10 | Privacy | PII fields, retention, third-party sends |

**Output of step:** selected passes list.

### Step 3 — Run passes

For each selected pass:

- Method (what you inspected)
- Hits (file/area + brief note)
- Clean (explicitly say clean if nothing found)
- Limits (what you could not see)

**Output of step:** per-pass results.

### Step 4 — Normalize findings

| ID | Pass | Severity | Location | Issue | Recommended fix |

Severity: Critical / High / Medium / Low / Info

**Output of step:** normalized table.

### Step 5 — Coverage report

- % of inventory actually inspected
- Blind spots (binaries, missing lockfiles, unreachable private code)
- Suggested follow-up skills (Cyber Security, Issues Founder, Coding)

**Output of step:** coverage + hand-off.

---

## Output (final)

```markdown
## Scanning result

### Inventory summary
...

### Passes run
- S1 ... 
- ...

### Findings
| ID | Sev | Pass | Location | Issue | Fix |
|----|-----|------|----------|-------|-----|

### Clean passes
- ...

### Blind spots
- ...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Inventory before opinions
- [ ] Explicit clean passes (not only bad news)
- [ ] Locations specific enough to act
- [ ] No offensive payloads

---

## Anti-patterns

- Random nits called a “scan”
- Only style issues under a security banner
- Claiming CVE confirmation without evidence
