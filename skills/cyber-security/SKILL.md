# Skill: Cyber Security

> Defensive security analysis — threats, weaknesses, impact, and hardening guidance.

**Version:** 2.0.0  
**Chain well with:** Scanning, Issues Founder, Coding, Thinking, ANIZ

---

## Mandate (hard rules)

This skill is **defensive only**.

- **Do:** identify weaknesses, explain impact, recommend fixes, secure defaults, detection ideas.
- **Do not:** write exploits, weaponized PoCs, bypass kits, or step-by-step attack instructions aimed at breaking into systems.
- If asked to attack or exploit: refuse that part; offer hardening and safe verification instead.
- Prefer fixes the owner can apply on systems they control.

---

## When to use

- “Is this secure?”, threat model, auth/session design
- Hardening apps, APIs, configs, cloud IAM (high level)
- Reviewing code for vulnerability classes (OWASP-style)
- Responding to a suspected weakness with remediation

**Do not use when:** the human wants offensive tooling/exploits, or a pure functional bug with no security angle (→ Debugger).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | App, API, design, snippet, architecture |
| Trust boundaries | no | Users, roles, networks, tenancy |
| Stack | no | Language, framework, host |
| Sensitivity | no | PII, payments, secrets, regulated data |

---

## Process

### Step 1 — Asset & boundary map

- What needs protection (data, functions, keys)
- Trust boundaries (browser, API, admin, workers, third parties)
- AuthN / AuthZ model (as understood)

**Output of step:** assets + boundaries diagram (text).

### Step 2 — Threat sketch

- Who might abuse it (roles: anonymous, user, insider, dependency)
- What they might try *at a class level* (e.g. “IDOR on object IDs”) — not exploit steps
- What “bad outcome” looks like (data leak, account takeover, fraud, RCE class, etc.)

**Output of step:** threat list (actor → goal → bad outcome).

### Step 3 — Weakness hunt (classes)

Inspect for common classes **as applicable**:

- Broken auth / session / token handling  
- Broken access control (IDOR, privilege rise)  
- Injection (SQL/command/XSS/template) — describe pattern & fix  
- SSRF, path traversal, unsafe deser (if relevant)  
- Secrets in code/config/logs  
- CSRF, CORS misconfig  
- Crypto misuse, weak randomness  
- Supply chain / dependency risk (high level)  
- Misconfiguration & over-permissioned IAM  
- Unsafe file upload / parsing  

For each finding: location, class, impact, likelihood (L/M/H).

**Output of step:** findings table draft.

### Step 4 — Impact & priority

| ID | Class | Impact | Likelihood | Priority (P0–P2) | Fix direction |

**Output of step:** prioritized table.

### Step 5 — Hardening plan

- Concrete remediations (secure patterns, config, code changes)
- Safe verification ideas (unit tests, config checks, authz tests) — **not** exploit scripts
- Defense in depth (detect/log/alert) where useful

**Output of step:** remediation list ordered by priority.

### Step 6 — Residual risk

- What remains accepted
- What needs deeper human/pentest review
- Monitoring suggestions

**Output of step:** residual risk block.

---

## Output (final)

```markdown
## Cyber Security result

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

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Findings are specific and actionable
- [ ] Priorities reflect real impact
- [ ] Fixes are defensive and practical
- [ ] No exploit/PoC attack material

---

## Anti-patterns

- Scare list with no fixes
- Generic “use HTTPS” only when deeper issues exist
- Delivering attack recipes “for education” when asked to break things
