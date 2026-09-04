# MagicSkills Index

Catalog of skills. The loader picks from this list when the human does not name a skill.

| Skill | Path | Use when | Boosts |
|-------|------|----------|--------|
| **think** | `skills/think/SKILL.md` | Ambiguous goals, hard tradeoffs, need structured reasoning first | Clarity, assumptions, decision quality |
| **debug** | `skills/debug/SKILL.md` | Errors, wrong behavior, flaky systems, “it broke” | Root cause, evidence, minimal fix |
| **test** | `skills/test/SKILL.md` | Need coverage, reproduce bugs, verify a fix, design cases | Confidence, edge cases, regression safety |
| **plan** | `skills/plan/SKILL.md` | Multi-step work, features, migrations, unknown scope | Ordering, risks, milestones |
| **review** | `skills/review/SKILL.md` | PR/code/design critique, “is this safe/good?” | Defects, maintainability, security |
| **refactor** | `skills/refactor/SKILL.md` | Messy code that still works; improve structure | Clarity, no behavior change |
| **research** | `skills/research/SKILL.md` | Unknown APIs, options comparison, “what’s best practice?” | Sources, tradeoffs, recommendations |

## Auto-pick rules

Match the **strongest** signal in the human message:

1. stack trace / error / “not working” / bug → **debug** (prefix **think** if cause space is huge)
2. “write tests” / “how do we verify” / coverage → **test**
3. “how should we approach” / roadmap / epic → **plan** (prefix **think**)
4. “review this” / “any issues?” → **review**
5. “clean up” / “simplify” / “refactor” → **refactor**
6. “compare” / “what is X” / “best way to” (external knowledge) → **research**
7. vague / strategic / conflicting goals → **think** first

If two skills tie, prefer the chain in `LOADER.md` §4.

## Chains (copy-paste)

```
Chain: think → debug → test
Chain: think → plan → test → review
Chain: research → think → plan
Chain: refactor → test
Chain: debug → test → review
```

## Version

- Pack version: `1.0.0`
- Skill files are the source of truth; this index is the map only.
