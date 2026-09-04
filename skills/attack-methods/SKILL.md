# Skill: Attack Methods

> Offensive **method taxonomy** & authorized test planning — kill chain, ATT&CK-style mapping, purple-team loops — without shipping exploits.

**Version:** 1.0.0  
**Chain well with:** Cyber Security, Reverse Engineering, Stress Tests, Scanning, Issues Founder, Thinking, ANIZ  
**Effort levels:** Fast · Balanced · Max  
**Features:** F076–F085 (+ F001, F016–F017, F068–F070)

---

## Mandate (hard)

This skill covers **how attackers think and which method classes exist**, for defense, authorized assessment planning, and education.

| Allowed | Not allowed |
|---------|-------------|
| Method names & categories | Copy-paste exploit code |
| Kill-chain / ATT&CK mapping | Weaponized PoCs / malware |
| Authorized test *plans* & checklists | Instructions to break into third-party systems |
| Impact stories & control gaps | Credential stuffing wordlists, brute tool configs aimed at others |
| Purple-team retest definitions | Bypass kits, ransomware builders |

If the human asks for a working exploit, raid kit, or attack on systems they do not own: **refuse that part**; provide method class, impact, detection, and hardening instead.  
**Authorized** penetration-style planning is OK when ROE/scope is explicit and ownership is clear — still no weaponized payloads in-repo outputs.

---

## When to use

- “How would this be attacked?” / attack surface methods  
- Map findings to ATT&CK / kill chain  
- Plan purple team or authorized assessment  
- Prioritize defenses by likely method classes  

**Do not use when:** they only want a code fix (→ Coding) or pure defensive config review without adversary framing (→ Cyber Security still fine).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | System/app/architecture |
| ROE / authorization | yes | Scope, ownership, limits |
| Architecture context | no | Diagrams, stack, trust zones |
| Known findings | no | From scan/cyber/RE |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Top method classes + controls | Full chain map | Emulation-grade plan (no payloads) |
| **Methods** | 5–8 | 12–20 | Broad catalog + paths |
| **Steps** | 1, 3, 5, 6 | 1–7 | 1–7 + Max extensions |
| **ATT&CK** | Optional tags | Map main techniques | Full layer-style table |

---

## Process

### Step 1 — ROE & objective
- Authorization · in/out of scope · forbidden techniques  
- Assessment objective (steal X, deny Y, — *as scenario*, not order to commit crime)  

**Output:** ROE block

### Step 2 — Target model
- Assets · actors · zones · crown jewels  
- Entry points inventory  

**Output:** target model

### Step 3 — Method catalog select
Pick relevant classes from the library below (tick applicable).

**Output:** selected method IDs + why

### Step 4 — Kill-chain narrative
Map methods across:

1. Recon  
2. Initial access  
3. Execution  
4. Persistence  
5. Privilege escalation  
6. Defense evasion (classes)  
7. Credential access  
8. Discovery  
9. Lateral movement  
10. Collection / exfil  
11. Impact  

**Output:** narrative table (stage · method class · likely precondition · worst impact · control that should break it)

### Step 5 — Path prioritization
- Most plausible paths (likelihood × impact)  
- Chokepoint controls  

**Output:** ranked paths P1…Pn

### Step 6 — Detect & harden
For each top path: prevent · detect · respond  

**Output:** control matrix

### Step 7 — Authorized test plan
*(Balanced+)*  
- Test cases as **safe verification** / purple checks  
- Success criteria · evidence to capture · rollback  
- Explicit: no production harm; data handling  

**Output:** test plan (methods, not exploits)

---

## Method class library (tick as applicable)

### Recon / surface
- M-REC-01 Open source intel (public)  
- M-REC-02 Attack surface enum (owned assets)  
- M-REC-03 Tech fingerprinting  
- M-REC-04 API/schema discovery  

### Initial access (classes)
- M-IA-01 Phishing / social (process tests)  
- M-IA-02 Valid accounts / stuffing *class*  
- M-IA-03 Exposed services exploitation *class*  
- M-IA-04 Supply-chain compromise *class*  
- M-IA-05 Misconfig public resource  

### Web / API method classes
- M-WEB-01 Auth bypass class  
- M-WEB-02 Access control / IDOR / BOLA  
- M-WEB-03 Injection classes  
- M-WEB-04 SSRF class  
- M-WEB-05 Deserialization class  
- M-WEB-06 File upload class  
- M-WEB-07 Business logic abuse  
- M-WEB-08 Race / TOCTOU money flows  
- M-WEB-09 Mass assignment  
- M-WEB-10 GraphQL/BFF abuse class  

### Credential & session
- M-CR-01 Session hijack *class*  
- M-CR-02 Token theft / replay *class*  
- M-CR-03 Password recovery abuse *class*  
- M-CR-04 MFA fatigue / bypass *classes* (control-focused)  

### Cloud / platform
- M-CL-01 Overwide IAM  
- M-CL-02 Metadata/SSRF-to-cloud  
- M-CL-03 Public storage  
- M-CL-04 CI token abuse *class*  
- M-CL-05 K8s RBAC / escape *classes* → controls  

### Identity / directory (enterprise)
- M-ID-01 Tier model breaks  
- M-ID-02 Kerberos *class* issues → hardening  
- M-ID-03 Lateral via identity  

### Impact
- M-IM-01 Data theft  
- M-IM-02 Integrity (fraud, tampering)  
- M-IM-03 Availability / ransomware *readiness*  
- M-IM-04 Abuse at scale (bot, spam, scrape)  

---

## Max extensions

### M1 — ATT&CK technique table (ID · name · detection · control)  
### M2 — Assumed-breach path set (3 starts)  
### M3 — Purple-team calendar (rounds, owners, KPIs)  
### M4 — Detection engineering stubs (log field needs)  
### M5 — Deception opportunities (canaries)  
### M6 — Stress Tests handoff (which methods need load/chaos)  
### M7 — Issues Founder export (one ticket per top path gap)

---

## Output (final)

```markdown
## Attack Methods result
**Effort:** Fast | Balanced | Max

### ROE
...

### Target model
...

### Methods selected
- M-WEB-02 ...

### Kill chain
| Stage | Method class | Precondition | Impact | Control break |
|-------|--------------|--------------|--------|---------------|

### Priority paths
1.
2.
3.

### Detect & harden matrix
| Path | Prevent | Detect | Respond |
|------|---------|--------|---------|

### Authorized test plan
...

### Feature IDs
F076–...

### Max only
#### ATT&CK map
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] ROE explicit  
- [ ] Methods are classes/plans, not exploit code  
- [ ] Every top path has a control break  
- [ ] Effort announced  

---

## Anti-patterns

- “Here’s the exploit script”  
- Attacking out-of-scope third parties  
- Scare chain with zero controls  
- Ignoring business-logic methods  
