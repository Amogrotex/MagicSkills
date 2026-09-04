# MagicSkills Index

Pick a skill — or use **ANIZ** to run the full pipeline.

| Skill | Path | Use when |
|-------|------|----------|
| **ANIZ** (all-in-one) | `skills/aniz/SKILL.md` | Default. Complex goals. “Do everything.” Unsure which skill. |
| **Research** | `skills/research/SKILL.md` | Facts, options, best practices, comparisons with sources |
| **Coding** | `skills/coding/SKILL.md` | Write, change, or generate code properly |
| **Cyber Security** | `skills/cyber-security/SKILL.md` | Threats, hardening, secure design (defensive) |
| **Scanning** | `skills/scanning/SKILL.md` | Checklist pass over code, config, deps, surfaces |
| **Issues Founder** | `skills/issues-founder/SKILL.md` | Discover, triage, and write clear issue reports |
| **Thinking** | `skills/thinking/SKILL.md` | Hard decisions, clarity, tradeoffs before action |
| **Debugger** | `skills/debugger/SKILL.md` | Bugs, errors, wrong behavior, root cause |
| **Deep Search** | `skills/deep-search/SKILL.md` | Exhaustive search when normal research isn’t enough |

## Auto-pick

1. “ANIZ” / “all in one” / multi-part mission / no skill named → **ANIZ**
2. stack trace / bug / broken / error → **Debugger**
3. write code / implement / build feature / fix code → **Coding**
4. vulnerability / harden / OWASP / auth / secure → **Cyber Security**
5. scan / audit pass / checklist / inventory surfaces → **Scanning**
6. find bugs/issues / triage / ticket them → **Issues Founder**
7. “search everything” / obscure topic / leave no stone → **Deep Search**
8. compare / what is / best way / sources → **Research**
9. vague / decide / tradeoff / strategy → **Thinking**

## Suggested chains

```
ANIZ
Thinking → Research → Coding
Deep Search → Research → Thinking
Debugger → Coding → Scanning
Scanning → Cyber Security → Issues Founder
Coding → Issues Founder → Scanning
```

## Version

Pack `2.0.0` — skills listed above are the source of truth.
