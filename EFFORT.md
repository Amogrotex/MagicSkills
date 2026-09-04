# MagicSkills Effort Levels

Every skill supports three **effort** settings. The human may set effort globally or per skill.

| Effort | Alias | Intent | Depth | Cost |
|--------|-------|--------|-------|------|
| **Fast** | `fast`, `quick`, `low` | Speed, direction, first slice | Minimum viable steps | Low |
| **Balanced** | `balanced`, `normal`, `default`, `medium` | Solid default quality | Full core process | Medium |
| **Max** | `max`, `deep`, `high`, `thorough` | Exhaustive, highest rigor | Full process + extensions | High |

---

## How the AI must apply effort

1. **Resolve effort** (first match wins):
   - Explicit: `Effort: Fast|Balanced|Max` or `effort=fast`
   - Per skill: `Coding: Max, Thinking: Fast`
   - ANIZ mission mode maps to effort (see ANIZ) unless overridden
   - Else **Balanced**
2. State at start: `Skill: X · Effort: Y`
3. Follow that skill’s **Effort matrix** for:
   - which steps are required / optional / extended
   - depth targets (counts, tables, tests)
   - output verbosity
4. Do **not** silently upgrade Fast → Max. Do **not** silently downgrade Max → Fast.
5. If blocked on time/tools in Max, say what was cut and why.

---

## Global behavior by effort

### Fast
- Shortest path to a usable answer
- Prefer tables and bullets over prose
- 1–2 options max when choosing
- Skip polish, long alternatives, and optional deep dives
- Still: no invented evidence; security skills stay defensive
- Final Output template **required** but compressed

### Balanced
- Run the skill’s full core **Process** in order
- Enough evidence and alternatives to trust the result
- Clear Next actions (3–5)
- Default for almost everything

### Max
- Full Process + **Max extensions** listed in each skill
- More hypotheses, angles, cases, adversarial review
- Explicit uncertainty, blind spots, and validation plan
- Cross-check conflicting info
- Longer artifact trail; still structured (not a wall of fluff)

---

## Prompt examples

```
Effort: Fast
Skill: Debugger
Symptom: ...
```

```
Run ANIZ · Effort: Max
Mission: ...
```

```
Coding with effort=balanced
Goal: ...
```

```
Chain: Thinking (Fast) → Research (Max) → Coding (Balanced)
```
