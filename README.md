# MagicSkills

**Intelligence booster for any AI.**  
Give the AI a link to this repo (or a single skill file). It reads the skill prompts and runs them **step by step** — debug, test, think, plan, review, refactor, research, and more.

```
You:  Use https://github.com/YOU/magicskills — skill: debug
AI:   Loads skills/debug/SKILL.md → follows steps 1…N until done
```

---

## Quick start (any AI)

1. Host this repo on GitHub (public) or any raw URL host.
2. Paste one of these prompts into Claude, ChatGPT, Cursor, Gemini, etc.

### Option A — Full pack (recommended)

```
Read and follow the MagicSkills loader:
https://raw.githubusercontent.com/YOU/magicskills/main/LOADER.md

My task: <describe what you need>
```

### Option B — Single skill

```
Read this skill and execute it step by step:
https://raw.githubusercontent.com/YOU/magicskills/main/skills/debug/SKILL.md

Context: <paste error / code / goal>
```

### Option C — Auto-pick

```
Open the MagicSkills index, pick the best skill(s) for my request, then run them in order:
https://raw.githubusercontent.com/YOU/magicskills/main/INDEX.md

Request: <your request>
```

Replace `YOU/magicskills` with your GitHub user/org and repo name.

---

## What’s inside

| Path | Purpose |
|------|---------|
| `LOADER.md` | Meta-prompt: how the AI must load & run skills |
| `INDEX.md` | Catalog of skills + when to use each |
| `skills/<name>/SKILL.md` | One skill = clear steps the AI must follow |
| `templates/SKILL.template.md` | Blueprint to add your own skills |
| `examples/` | Sample runs so humans & AIs see the expected shape |

### Core skills (intelligence boosters)

| Skill | Boosts |
|-------|--------|
| **think** | Structured reasoning before acting |
| **debug** | Systematic root-cause debugging |
| **test** | Test design, gaps, and verification |
| **plan** | Break work into ordered steps |
| **review** | Code / design review checklist |
| **refactor** | Safe improvement without behavior change |
| **research** | Gather, compare, and cite findings |

---

## Skill format (short)

Every skill is a markdown file with:

1. **When to use** — triggers
2. **Inputs** — what the human should provide
3. **Process** — numbered steps (mandatory order)
4. **Output** — exact shape of the final answer
5. **Quality bar** — what “done” means
6. **Anti-patterns** — what not to do

See `templates/SKILL.template.md`.

---

## Add your own skill

```bash
cp templates/SKILL.template.md skills/my-skill/SKILL.md
# edit the file, then add a row to INDEX.md
```

Keep steps **atomic, ordered, and checkable**. Prefer verbs: *List*, *Hypothesize*, *Verify*, *Report*.

---

## Design principles

1. **Steps over vibes** — the AI must not skip steps.
2. **Evidence over guesses** — debug/test/research demand proof.
3. **Composable** — chain skills (`think` → `plan` → `debug` → `test`).
4. **Model-agnostic** — plain markdown; no proprietary tool APIs required.
5. **Link-loadable** — one URL is enough; no install.

---

## Security

- Never put API keys, tokens, or secrets in this repo or in skill files.
- If you ever paste a token in chat, **revoke it immediately** on the provider.
- Skills may ask the AI to read code you provide; treat untrusted code as untrusted.

---

## License

MIT — use freely, improve freely.
