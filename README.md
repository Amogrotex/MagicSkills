# MagicSkills

**Link → AI reads skills → works step by step — at Fast, Balanced, or Max effort.**

Give this repo to any AI (ChatGPT, Claude, Cursor, Gemini, Arena, …).  
It loads skill prompts and follows them in order.

**Repo:** https://github.com/Amogrotex/MagicSkills

---

## Effort levels (every skill)

| Effort | Use for | Depth |
|--------|---------|-------|
| **Fast** | Speed, drafts, first slice | Minimum viable steps |
| **Balanced** | Default quality | Full core process |
| **Max** | High stakes, thorough | Full process + extensions |

Details: [`EFFORT.md`](./EFFORT.md) · each skill has an **Effort matrix**.

```
Effort: Fast | Balanced | Max
```

---

## Skills

| Skill | Folder | Boosts |
|-------|--------|--------|
| **ANIZ** | `skills/aniz` | **ALL IN ONE** pipeline + effort routing |
| **Research** | `skills/research` | Sourced recommendations |
| **Coding** | `skills/coding` | Spec → design → code → verify |
| **Cyber Security** | `skills/cyber-security` | Defensive hardening |
| **Scanning** | `skills/scanning` | Checklist surface passes |
| **Issues Founder** | `skills/issues-founder` | Find & ticket real issues |
| **Thinking** | `skills/thinking` | Structured decisions |
| **Debugger** | `skills/debugger` | Root-cause debugging |
| **Deep Search** | `skills/deep-search` | Multi-angle exhaustive search |

Security-related skills are **defensive only** (no exploit/attack playbooks).

---

## Quick start

### ANIZ + effort

```
Follow https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/LOADER.md
Read https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/EFFORT.md
Run https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/aniz/SKILL.md

Mission: <your goal>
Effort: Balanced
```

### One skill

```
Execute step by step:
https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/coding/SKILL.md

Effort: Max
Goal: <...>
Stack: <...>
```

### Mixed efforts in a chain

```
Loader: https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/LOADER.md
Chain: Thinking (Fast) → Research (Max) → Coding (Balanced)
Request: <...>
```

---

## Layout

```
magicskills/
  LOADER.md
  EFFORT.md
  INDEX.md
  catalog.json
  skills/
    aniz/
    research/
    coding/
    cyber-security/
    scanning/
    issues-founder/
    thinking/
    debugger/
    deep-search/
  templates/
  examples/
```

---

## ANIZ (plain words)

1. You state a **mission** + optional **Effort**
2. ANIZ tags it: learn / build / fix / audit / decide
3. Builds a **chain** of skills (length depends on effort)
4. Runs each child skill at that effort (or per-stage override)
5. Returns one pack: summary, deliverables, backlog, next actions

---

## Add a skill

```bash
cp templates/SKILL.template.md skills/my-skill/SKILL.md
# include Effort matrix (Fast / Balanced / Max)
# register in INDEX.md + catalog.json
```

---

## License

MIT
