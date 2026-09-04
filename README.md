# MagicSkills

**Link → AI reads skills → step-by-step at Fast / Balanced / Max.**

https://github.com/Amogrotex/MagicSkills

---

## Effort

| Effort | Depth |
|--------|--------|
| **Fast** | Minimum viable steps |
| **Balanced** | Full core process (default) |
| **Max** | Full + extensions |

See `EFFORT.md`.

---

## Skills

| Skill | Boosts |
|-------|--------|
| **ANIZ** | All-in-one router |
| **Research** | Sourced answers |
| **Coding** | Solid implementation |
| **Cyber Security** | Harden + **100 features (F001–F100)** |
| **Attack Methods** | Adversary method taxonomy, kill chain, purple plans |
| **Reverse Engineering** | Binaries, protocols, bundles |
| **Stress Tests** | Load, spike, soak, chaos, abuse stress |
| **Scanning** | Surface checklists |
| **Issues Founder** | Ticket real issues |
| **Thinking** | Decisions |
| **Debugger** | Root cause |
| **Deep Search** | Exhaustive search |

### Cyber feature pack

`skills/cyber-security/features/F001-F100.md` — foundations, threat model, OWASP/API, auth, secrets/supply chain, cloud, detection/IR, **attack method features**, **RE features**, **stress features**.

---

## Quick start

```
Follow https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/LOADER.md
Effort: Max
Run https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/aniz/SKILL.md
Focus: cyber-full
Mission: <goal>
```

```
Skill: Attack Methods · Effort: Balanced
ROE: owner app only
Target: <architecture>
```

```
Skill: Reverse Engineering · Effort: Max
Target: <binary or protocol>
Permission: owner-authorized
```

```
Skill: Stress Tests · Effort: Fast
Target: POST /login
SLO: p95 < 300ms at 50 RPS
```

```
Cyber Security · Profile: api · Effort: Max
Features: from F001-F100.md
```

---

## Rules of the road

- Authorized targets for RE, stress, and adversary planning  
- Attack Methods = **classes, paths, plans, controls** — not exploit/malware kits  
- Prefer hardening, detection, tickets, tests  

---

## Layout

```
LOADER.md · EFFORT.md · INDEX.md · catalog.json
skills/
  aniz/ coding/ research/ thinking/ debugger/ deep-search/
  scanning/ issues-founder/
  cyber-security/   # SKILL + features/F001-F100.md + profiles + checklists + patterns
  attack-methods/
  reverse-engineering/
  stress-tests/
```

---

## License

MIT
