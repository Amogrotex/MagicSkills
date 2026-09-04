# MagicSkills Index

Effort: **Fast** · **Balanced** (default) · **Max** — `EFFORT.md`.

| Skill | Path | Use when |
|-------|------|----------|
| **ANIZ** | `skills/aniz/SKILL.md` | All-in-one / default |
| **Research** | `skills/research/SKILL.md` | Facts, comparisons |
| **Coding** | `skills/coding/SKILL.md` | Implement code |
| **Cyber Security** | `skills/cyber-security/SKILL.md` | Harden + F001–F100 features |
| **Attack Methods** | `skills/attack-methods/SKILL.md` | Adversary methods, kill chain, purple plans |
| **Reverse Engineering** | `skills/reverse-engineering/SKILL.md` | Binaries, protocols, bundles |
| **Stress Tests** | `skills/stress-tests/SKILL.md` | Load, chaos, abuse stress |
| **Scanning** | `skills/scanning/SKILL.md` | Checklist scans |
| **Issues Founder** | `skills/issues-founder/SKILL.md` | Tickets / triage |
| **Thinking** | `skills/thinking/SKILL.md` | Decisions |
| **Debugger** | `skills/debugger/SKILL.md` | Bugs / root cause |
| **Deep Search** | `skills/deep-search/SKILL.md` | Exhaustive search |

## Feature pack

| Pack | Path |
|------|------|
| **100 cyber features** | `skills/cyber-security/features/F001-F100.md` |
| Profiles | `skills/cyber-security/profiles/` |
| PR gate | `skills/cyber-security/checklists/pr-security-gate.md` |
| Secure defaults | `skills/cyber-security/patterns/secure-defaults.md` |

## Auto-pick skill

1. ANIZ / all-in-one / unnamed → **ANIZ**  
2. reverse / binary / protocol / decompile → **Reverse Engineering**  
3. attack methods / kill chain / ATT&CK / purple / how would this be attacked → **Attack Methods**  
4. stress / load / soak / chaos / capacity → **Stress Tests**  
5. bug / error / crash → **Debugger**  
6. implement / code → **Coding**  
7. vulnerability / harden / OWASP / secure → **Cyber Security**  
8. scan / checklist → **Scanning**  
9. find issues / triage → **Issues Founder**  
10. dig / exhaustive → **Deep Search**  
11. compare / sources → **Research**  
12. decide / tradeoff → **Thinking**  

## Auto-pick effort

| Signal | Effort |
|--------|--------|
| quick, rough, tl;dr | Fast |
| thorough, production, exhaustive, full features | Max |
| else | Balanced |

## Chains

```
ANIZ
Cyber Security → Attack Methods → Issues Founder
Reverse Engineering → Cyber Security → Attack Methods
Stress Tests → Coding → Issues Founder
Scanning → Cyber Security → Stress Tests → Issues Founder
Thinking → Research → Coding
Debugger → Coding → Scanning
```

## Version

Pack `4.0.0` — RE + Attack Methods + Stress Tests + 100 features.
