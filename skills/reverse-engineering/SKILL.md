# Skill: Reverse Engineering

> Systematic reverse engineering — understand binaries, protocols, bundles, and undocumented behavior; turn insights into defenses and issues.

**Version:** 1.0.0  
**Chain well with:** Attack Methods, Cyber Security, Stress Tests, Deep Search, Debugger, Coding, Issues Founder, ANIZ  
**Effort levels:** Fast · Balanced · Max  
**Features:** F086–F092 (+ F001, F010, F046–F050, F068 as needed)

---

## Mandate

- **Authorized targets only** (software you own, have permission to analyze, or public research with legal right).
- Goal: **understand behavior**, document surface, find weaknesses, propose hardening — not ship malware or crack protection for piracy.
- Outputs: analysis plans, findings, diagrams, safe verification — **no** weaponized exploits or ready-to-abuse crack tools.
- If asked to pirate, bypass paid licensing maliciously, or attack third parties: refuse; offer legitimate interoperability / owner-side analysis.

---

## When to use

- Undocumented binary, library, firmware, minified bundle
- Unknown protocol / file format
- “What does this build do?” / malware *triage* at high level (IOC + behavior, not DIY malware)
- Crypto/protocol confusion in a client you own

**Do not use when:** pure source-level bug with full code (→ Debugger / Coding) or only generic web OWASP (→ Cyber Security).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | File type, path, URL, hash, platform |
| Goal | yes | Interop, security review, debug, protocol doc |
| Permission | yes | Confirm authorization |
| Tools available | no | disassembler, debugger, emulator, browser devtools |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Rough map + top risks | Solid RE report | Deep multi-pass RE |
| **Passes** | Static skim | Static + light dynamic plan | Static + dynamic + protocol + crypto notes |
| **Steps** | 1, 2, 4, 6 | 1–7 | 1–7 + Max extensions |
| **Artifacts** | Surface list | Full notes + findings | + timelines, graphs, handoffs |

---

## Process

### Step 1 — Authorize & fingerprint
- Confirm permission / ROE  
- File type, hashes, arch (x86/ARM/wasm/JS), packer signals  
- High-level goal success criteria  

**Output:** ROE · fingerprint · goal

### Step 2 — Surface map
- Imports/exports · strings of interest · sections · entrypoints  
- For JS/mobile: permissions, endpoints, native bridges  
- External calls (DNS, IPs, URLs) if visible  

**Output:** surface map

### Step 3 — Static analysis
*(Balanced+)*  
- Control-flow hotspots · interesting functions · config blobs  
- Crypto constants / protocol magic · dangerous APIs (exec, eval, deserialize)  
- Obfuscation level (none/light/heavy)  

**Output:** static notes + hotspots table

### Step 4 — Behavior hypotheses
- What the target likely does (features + risky behaviors)  
- Trust assumptions (who it talks to, what it trusts)  
- 3–8 falsifiable hypotheses  

**Output:** hypothesis list

### Step 5 — Dynamic / runtime plan
*(Balanced+; execute only if authorized & environment safe)*  
- How to run safely (VM, net sinkhole, sample data)  
- Breakpoints / hooks / logs of interest  
- What evidence would confirm each hypothesis  

**Output:** dynamic plan (+ results if run)

### Step 6 — Protocol / data format notes
- Messages, fields, auth material handling  
- Serialization choices · integrity checks  
- Undocumented commands  

**Output:** protocol/format sketch

### Step 7 — Findings → harden / handoff
- Security-relevant findings (classes + impact)  
- Interop docs for owners  
- Hand off: Cyber Security, Attack Methods taxonomy, Issues Founder, Coding  

**Output:** findings + handoffs

---

## Max extensions

### M1 — Call graph / module map (text)  
### M2 — String & IOC table (domains, paths, mutex names)  
### M3 — Crypto use map (algorithms suspected, key provenance *if evident*)  
### M4 — Obfuscation defeat *strategy* (rename, decomp prioritization) — not commercial crack  
### M5 — Compare versions (diff behaviors across builds)  
### M6 — RE lab notes template for repeat sessions  
### M7 — Safe test harness ideas (owner unit/integration checks)

---

## Output (final)

```markdown
## Reverse Engineering result
**Effort:** Fast | Balanced | Max

### Target fingerprint
...

### Surface map
...

### Behavior summary
...

### Hypotheses & evidence
| H | Status | Evidence |
|---|--------|----------|

### Protocol / format
...

### Security findings
| ID | Class | Where | Impact | Hardening |
|----|-------|-------|--------|-----------|

### Feature IDs run
F086–...

### Handoffs
- ...

### Max only
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] Authorization stated  
- [ ] Effort announced  
- [ ] No weaponized exploit/malware output  
- [ ] Findings actionable for owners  

---

## Anti-patterns

- Piracy / license-fire bypass as the goal  
- “RE” that is only guessing with no surface evidence  
- Dumping raw shellcode as a deliverable  
