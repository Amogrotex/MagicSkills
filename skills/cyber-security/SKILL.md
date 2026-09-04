# Skill: Cyber Security

> Defensive security analysis — threats, weaknesses, impact, and hardening guidance.

**Version:** 3.0.0  
**Chain well with:** Scanning, Issues Founder, Coding, Thinking, ANIZ  
**Effort levels:** Fast · Balanced · Max

---

## Mandate (hard rules — all efforts)

**Defensive only.**

- **Do:** weaknesses, impact, fixes, secure defaults, detection ideas, safe verification.
- **Do not:** exploits, weaponized PoCs, bypass kits, attack playbooks.
- If asked to attack: refuse that part; offer hardening + safe checks.
- Prefer fixes on systems the owner controls.

---

## When to use

- “Is this secure?”, threat model, auth/session design
- Hardening apps/APIs/configs (high level)
- Vulnerability *classes* in code (OWASP-style)

**Do not use when:** offensive tooling requested, or pure functional bug (→ Debugger).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | App, API, design, snippet |
| Trust boundaries | no | Users, roles, networks |
| Stack | no | Language, framework, host |
| Sensitivity | no | PII, payments, secrets |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Top risks + fixes | Solid threat + findings | Deep defensive review |
| **Threats** | 2–3 | Full sketch | Actors × assets matrix |
| **Findings depth** | P0/P1 only | P0–P2 | P0–P2 + systematic classes |
| **Steps** | 1, 3, 5 | 1–6 | 1–6 + Max extensions |
| **Verification** | Fix direction | Safe test ideas | Test + detect + review plan |

### Fast
- Boundaries skim → top weaknesses → priority fixes

### Balanced
- Full core defensive process

### Max
- Full process + STRIDE-ish pass, abuse cases, control gaps, residual risk register

---

## Process

### Step 1 — Asset & boundary map
- Protect what · trust boundaries · AuthN/AuthZ as understood  
*(Fast: short bullet map)*

**Output:** assets + boundaries

### Step 2 — Threat sketch
*(Balanced+)*
- Actors · goal classes · bad outcomes  
*(Not exploit steps)*

**Output:** threat list

### Step 3 — Weakness hunt (classes)
As applicable: broken auth/session, access control, injection classes, SSRF/path/deser, secrets, CSRF/CORS, crypto misuse, supply chain, misconfig/IAM, uploads.

Each finding: location, class, impact, likelihood L/M/H.

**Output:** findings draft

### Step 4 — Impact & priority
*(Balanced+; Fast: rank top 3)*
| ID | Class | Impact | Likelihood | P0–P2 | Fix direction |

**Output:** prioritized table

### Step 5 — Hardening plan
- Concrete remediations
- Safe verification (tests/config checks — **not** exploit scripts)
- Detection/logging where useful

**Output:** ordered remediations

### Step 6 — Residual risk
*(Balanced+)*
- Accepted remains · deeper review needs · monitoring

**Output:** residual risk

---

## Max extensions

### M1 — STRIDE-style pass
Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation — notes per boundary (descriptive).

### M2 — Abuse cases
Misuse stories as **defender** narratives (“abusive user attempts X”) + control that should stop it.

### M3 — Control catalog
Prevent / detect / respond for each P0–P1.

### M4 — Secure design alternatives
Safer pattern vs current; migration difficulty.

### M5 — Review checklist export
Paste-ready checklist for future changes in this area.

---

## Output (final)

```markdown
## Cyber Security result
**Effort:** Fast | Balanced | Max

### Scope
...

### Threat sketch
- ...

### Findings
| ID | Priority | Class | Where | Impact | Remediation |
|----|----------|-------|-------|--------|-------------|

### Hardening plan
1.
2.
3.

### Safe verification
- ...

### Residual risk
- ...

### Max only
#### STRIDE notes
...
#### Control catalog
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Effort announced
- [ ] Actionable defensive fixes
- [ ] Priorities match impact
- [ ] Zero exploit/PoC material

---

## Anti-patterns

- Scare list, no fixes
- Attack recipes “for education” when asked to break things
- Max theater without findings
