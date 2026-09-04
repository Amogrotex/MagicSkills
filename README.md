# MagicSkills

**Link → AI reads skills → works step by step.**

A repo you give to any AI (ChatGPT, Claude, Cursor, Gemini, Arena, …).  
It loads skill prompts and follows them one by one.

## Skills (one by one)

| Skill | Folder | Makes the AI better at |
|-------|--------|-------------------------|
| **Research** | `skills/research` | Facts, comparisons, sourced recommendations |
| **Coding** | `skills/coding` | Spec → design → solid code → verify |
| **Cyber Security** | `skills/cyber-security` | Defensive threats, weaknesses, hardening |
| **Scanning** | `skills/scanning` | Checklist passes over code/config/deps |
| **Issues Founder** | `skills/issues-founder` | Find, triage, and write real issue tickets |
| **Thinking** | `skills/thinking` | Deep structured reasoning & decisions |
| **Debugger** | `skills/debugger` | Root-cause debugging |
| **Deep Search** | `skills/deep-search` | Exhaustive multi-angle search |
| **ANIZ** | `skills/aniz` | **ALL IN ONE** — auto-routes the full pipeline |

Security-related skills are **defensive only** (find & fix guidance — no exploit/attack playbooks).

---

## Quick start

### All-in-one (recommended)

```
Read and follow:
https://raw.githubusercontent.com/YOU/magicskills/main/LOADER.md

Then run ANIZ:
https://raw.githubusercontent.com/YOU/magicskills/main/skills/aniz/SKILL.md

Mission: <your goal>
```

### One skill only

```
Execute step by step:
https://raw.githubusercontent.com/YOU/magicskills/main/skills/coding/SKILL.md

Goal: <...>
Stack: <...>
```

### Auto-pick from index

```
Use MagicSkills index to choose skill(s), then run them:
https://raw.githubusercontent.com/YOU/magicskills/main/INDEX.md
Loader: https://raw.githubusercontent.com/YOU/magicskills/main/LOADER.md

Request: <...>
```

Replace `YOU/magicskills` with your GitHub user/repo.

### Local / cloned

```
Open magicskills/LOADER.md and magicskills/skills/aniz/SKILL.md
Mission: ...
Work step by step; mark each step complete.
```

---

## Layout

```
magicskills/
  LOADER.md           # how any AI must load & run skills
  INDEX.md            # catalog + auto-pick rules
  catalog.json        # machine-readable list
  skills/
    aniz/SKILL.md
    research/SKILL.md
    coding/SKILL.md
    cyber-security/SKILL.md
    scanning/SKILL.md
    issues-founder/SKILL.md
    thinking/SKILL.md
    debugger/SKILL.md
    deep-search/SKILL.md
  templates/SKILL.template.md
  examples/
```

---

## ANIZ in plain words

You state a **mission**. ANIZ:

1. Tags it (`learn` / `build` / `fix` / `audit` / `decide`)
2. Builds a **chain** of the skills above
3. Runs each skill step by step
4. Returns one pack: summary, deliverables, prioritized backlog, next actions

Modes: `fast` · `full` (default) · `secure`

---

## Add a skill

```bash
cp templates/SKILL.template.md skills/my-skill/SKILL.md
# edit, then add a row to INDEX.md and catalog.json
```

---

## Publish

```bash
cd magicskills
git remote add origin git@github.com:YOU/magicskills.git   # if needed
git push -u origin main
```

---

## Security notes

- Never commit API keys or tokens.
- If a token was pasted in chat, revoke it on the provider immediately.
- Cyber Security / Scanning / Issues Founder = defensive remediation only.

---

## License

MIT
