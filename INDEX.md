# MagicSkills Index

Pick a skill — or **ANIZ** for the full pipeline.  
Set effort: **Fast** · **Balanced** (default) · **Max** — see `EFFORT.md`.

| Skill | Path | Use when |
|-------|------|----------|
| **ANIZ** (all-in-one) | `skills/aniz/SKILL.md` | Default · complex goals · “do everything” |
| **Research** | `skills/research/SKILL.md` | Facts, options, sourced recommendations |
| **Coding** | `skills/coding/SKILL.md` | Write / change code properly |
| **Cyber Security** | `skills/cyber-security/SKILL.md` | Defensive threats, hardening |
| **Scanning** | `skills/scanning/SKILL.md` | Checklist passes over code/config/deps |
| **Issues Founder** | `skills/issues-founder/SKILL.md` | Find, triage, write issue tickets |
| **Thinking** | `skills/thinking/SKILL.md` | Decisions, clarity, tradeoffs |
| **Debugger** | `skills/debugger/SKILL.md` | Bugs, errors, root cause |
| **Deep Search** | `skills/deep-search/SKILL.md` | Exhaustive multi-angle search |

## Effort cheat sheet

| Effort | Meaning |
|--------|---------|
| **Fast** | Minimum steps, quick direction, compressed output |
| **Balanced** | Full core process (default) |
| **Max** | Full process + extensions, highest rigor |

```
Effort: Max
Skill: Debugger
```
```
ANIZ · Effort: Fast
Mission: ...
```
```
Thinking (Fast) → Coding (Max)
```

## Auto-pick skill

1. ANIZ / all-in-one / multi-part / unnamed → **ANIZ**
2. stack trace / bug / broken → **Debugger**
3. implement / build / code → **Coding**
4. vulnerability / harden / secure → **Cyber Security**
5. scan / checklist / inventory → **Scanning**
6. find issues / triage / tickets → **Issues Founder**
7. dig / exhaustive / obscure → **Deep Search**
8. compare / best way / sources → **Research**
9. vague / decide / tradeoff → **Thinking**

## Auto-pick effort (if unspecified)

| Signal | Effort |
|--------|--------|
| “quick”, “tl;dr”, “rough”, time-boxed | Fast |
| “thorough”, “exhaustive”, “production”, “careful”, high stakes | Max |
| else | Balanced |

## Chains

```
ANIZ
Thinking → Research → Coding
Deep Search → Research → Thinking
Debugger → Coding → Scanning
Scanning → Cyber Security → Issues Founder
Coding → Issues Founder → Scanning
```

## Version

Pack `3.0.0` — effort-aware skills.
