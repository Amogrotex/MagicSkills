# Skill: Cyber Security

> Defensive + adversary-informed security analysis — threats, method classes, weaknesses, hardening, detection. Pairs with Attack Methods, Reverse Engineering, Stress Tests.

**Version:** 4.0.0  
**Chain well with:** Attack Methods, Reverse Engineering, Stress Tests, Scanning, Issues Founder, Coding, Thinking, ANIZ  
**Effort levels:** Fast · Balanced · Max  
**Feature catalog:** `features/F001-F100.md` (100 features)

---

## Mandate

- Default: **harden owner systems** with optional **attacker-method framing** (classes, paths, ATT&CK) — not weaponized exploits.
- **Do:** weaknesses, impact, fixes, secure defaults, detection, authorized test plans, RE/stress handoffs.
- **Do not:** exploit code, malware, bypass kits, or attack third-party systems without authorization.
- Attack *thinking* is allowed as taxonomy + purple-team planning via **Attack Methods** skill / F076–F085.
- Prefer fixes and detections the owner can apply.

---

## When to use

- “Is this secure?”, threat model, harden, auth design  
- Adversary-informed review (how it could be abused — classes)  
- Drive the **100-feature** checklist  
- Gate before Stress Tests / RE / Attack Methods deep dives  

**Do not use when:** pure load test only (→ Stress Tests), pure binary RE (→ Reverse Engineering), or exploit writing requested (refuse payloads).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | App, API, design, snippet, arch |
| Trust boundaries | no | Users, roles, networks |
| Stack | no | Language, framework, host |
| Sensitivity | no | PII, payments, secrets |
| Profile | no | web-app, api, cloud, auth-heavy, mobile-backend, llm-app, binary/RE, full-max |
| Features | no | Explicit Fxxx list; else profile defaults |
| Effort | no | Fast / Balanced / Max |
| Adversary depth | no | off / light / full (full → also run Attack Methods) |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Top risks + fixes | Solid threat + findings | Deep review + feature sweep |
| **Features** | 5–10 | 15–30 | 40+ / profile full |
| **Threats** | 2–3 | Full sketch | Actors × assets + paths |
| **Steps** | 1, 3, 5, 7 | 1–8 | 1–8 + Max extensions |
| **Adversary** | light optional | light | full handoff Attack Methods |

---

## Process

### Step 1 — Scope, profile, features
- Target · ROE if any · profile  
- Load feature IDs from `features/F001-F100.md` (profile pack or explicit)  
- Announce Effort + profile + feature count  

**Output:** scope · profile · feature ID list

### Step 2 — Asset, data, boundary map
- Assets · data class (F004) · boundaries · AuthN/Z model (F006–F007)  

**Output:** maps

### Step 3 — Threat sketch (+ optional methods)
- Actors · goals · bad outcomes  
- If adversary depth light/full: note top method classes (or hand off Attack Methods)  

**Output:** threats · method hints

### Step 4 — Feature-driven weakness hunt
- Run selected F-features (especially C–F groups)  
- Classes: access control, injection, SSRF, secrets, auth, misconfig, supply chain, cloud, etc.  
- Each finding: location, class, impact, likelihood, feature ID  

**Output:** findings draft + feature run log

### Step 5 — Impact & priority
| ID | Feature | Class | Impact | Likelihood | P0–P2 | Fix |

**Severity:** P0 auth bypass / mass PII / payment fraud path / RCE class · P1 priv gap / secret in repo / weak reset · P2 headers / verbose errors · Info defense-in-depth  

**Output:** prioritized table

### Step 6 — Hardening + secure defaults
- Concrete remediations  
- Stack defaults when known (`patterns/` if present)  
- Prevent / detect / respond for P0–P1  

**Output:** hardening plan

### Step 7 — Safe verification
- AuthZ matrix tests · negative auth · config asserts · secret scan of diff  
- Link Stress Tests for abuse/load (F093–F100)  
- Link RE if binary/protocol unknown (F086–F092)  

**Output:** verification plan

### Step 8 — Residual risk + handoffs
- Accepted risk · blind spots (F010)  
- Next skills: Attack Methods, RE, Stress Tests, Issues Founder, Coding, Scanning  

**Output:** residual · handoffs

---

## Max extensions

### M1 — STRIDE per boundary (F012)  
### M2 — Abuse-case → control matrix (F015)  
### M3 — ATT&CK map of findings (F068) via Attack Methods  
### M4 — Secrets lifecycle (F046–F047)  
### M5 — Supply chain & CI (F051–F054)  
### M6 — Cloud/K8s pack (F056–F061)  
### M7 — Detection use-cases (F066–F067)  
### M8 — IR stubs (F070)  
### M9 — Fix PR security gate checklist  
### M10 — Full F001–F100 scorecard export  

---

## Output (final)

```markdown
## Cyber Security result
**Effort:** Fast | Balanced | Max
**Profile:** ...
**Features:** n selected · n done · n n/a

### Scope
...

### Threat sketch
- ...

### Feature run log
| ID | Status | Notes |
|----|--------|-------|

### Findings
| ID | Pri | Feature | Class | Where | Impact | Remediation |
|----|-----|---------|-------|-------|--------|-------------|

### Hardening plan
1.
2.
3.

### Safe verification
- ...

### Residual risk & blind spots
- ...

### Handoffs
- Attack Methods: ...
- Reverse Engineering: ...
- Stress Tests: ...
- Issues Founder / Coding: ...

### Max only
#### Scorecard / ATT&CK / STRIDE
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Effort + profile announced  
- [ ] Feature IDs used (not vague “checked security”)  
- [ ] Actionable fixes  
- [ ] No exploit/malware payloads  

---

## Anti-patterns

- Scare list, no fixes  
- Claiming 100/100 features done in Fast  
- Attack recipes for third parties  
- Ignoring handoffs to Stress/RE/Methods when needed  
