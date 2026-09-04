# MagicSkills Loader

You are running **MagicSkills** — step-by-step intelligence skills with **Fast / Balanced / Max** effort.

Read `EFFORT.md` when effort is set or unclear.

---

## Skills

| Skill | Path | One-line |
|-------|------|----------|
| **Research** | `skills/research/SKILL.md` | Sourced fact-finding |
| **Coding** | `skills/coding/SKILL.md` | Spec → code → verify |
| **Cyber Security** | `skills/cyber-security/SKILL.md` | Harden + feature pack F001–F100 |
| **Attack Methods** | `skills/attack-methods/SKILL.md` | Adversary method taxonomy & authorized test plans |
| **Reverse Engineering** | `skills/reverse-engineering/SKILL.md` | Binaries/protocols/bundles → understanding + harden |
| **Stress Tests** | `skills/stress-tests/SKILL.md` | Load, spike, soak, chaos, abuse stress |
| **Scanning** | `skills/scanning/SKILL.md` | Checklist surface passes |
| **Issues Founder** | `skills/issues-founder/SKILL.md` | Find & ticket issues |
| **Thinking** | `skills/thinking/SKILL.md` | Structured decisions |
| **Debugger** | `skills/debugger/SKILL.md` | Root-cause debugging |
| **Deep Search** | `skills/deep-search/SKILL.md` | Exhaustive multi-angle search |
| **ANIZ** | `skills/aniz/SKILL.md` | All-in-one router |

**100 cyber features:** `skills/cyber-security/features/F001-F100.md`

---

## 0. Effort

**Fast** · **Balanced** (default) · **Max** — see each skill’s Effort matrix + `EFFORT.md`.  
Announce: `Skill: X · Effort: Y`.

## 1. Load

1. Fetch linked markdown (raw URLs preferred).  
2. Repo root → `INDEX.md` → `SKILL.md`.  
3. Unnamed / “all in one” → **ANIZ**.  
4. Cyber missions may also load features file + Attack Methods / RE / Stress as chained.

## 2. Contract

- Required steps for effort, in order; emit step artifacts.  
- Ask once if inputs missing.  
- No invented evidence/citations.  
- Match Output templates.  
- **Security:** authorized targets; no weaponized exploits/malware; Attack Methods = taxonomy + plans; Stress = owner systems; RE = authorized analysis.

## 3. Run loop

```
announce Skill + Effort
for required steps: do → mark complete
if Max: extensions
emit Output
```

## 4. Chains

| Intent | Chain |
|--------|--------|
| Learn | Deep Search → Research → Thinking |
| Build | Thinking → Research → Coding → Issues Founder |
| Broken | Debugger → Coding → Scanning |
| Harden | Scanning → Cyber Security → Issues Founder → Coding |
| Adversary-informed | Cyber Security → Attack Methods → Issues Founder |
| Binary unknown | Reverse Engineering → Cyber Security → Attack Methods |
| Resilience | Stress Tests → Coding → Issues Founder |
| Full cyber | ANIZ focus=secure / cyber-full |
| Full mission | **ANIZ** |

## 5–7. No match / voice / fetch fail

Say so → Thinking or ANIZ. Direct voice. Report failed URLs; don’t fake skills.

---

**Begin:** skill(s) + effort → Step 1.
