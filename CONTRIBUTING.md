# Contributing to MagicSkills

Skills are markdown executed by AI models — clarity beats cleverness.

## Ground rules

1. **Safety first.** No exploit code, malware, or content that assumes unauthorized targets. Attack material stays taxonomy/plans/controls (see every skill's mandate).
2. **Keep the contract.** Every `SKILL.md` keeps the shared shape: Inputs → Effort matrix → Process → Max extensions → Output → Quality bar. Use `templates/SKILL.template.md`.
3. **IDs are stable.** Never renumber F001–F100; add new features at the end or in a new pack file.
4. **Mappings required.** New cyber features need a Check-for / Verify-by / Maps-to triple so output stays auditable.
5. **Bump versions.** Update `catalog.json` version **and** the INDEX.md "Pack" line together (CI enforces this).

## Before you open a PR

```bash
python scripts/lint_pack.py
```

All checks green, or the CI will block you. The linter validates: catalog paths, skill folders, F001–F100 completeness, relative links, and version sync.

## Adding a skill

1. Copy `templates/SKILL.template.md` → `skills/<kebab-name>/SKILL.md`.
2. Fill the contract sections; write effort matrices for Fast/Balanced/Max.
3. Register in `catalog.json` (path + triggers) and `INDEX.md` (use-when row).
4. Add an example run under `examples/` — a real transcript, not a sketch.

## Adding a profile / pattern

- Profiles: `skills/cyber-security/profiles/<name>.md` following the custom-profile template in `profiles/README.md`.
- Secure defaults: `skills/cyber-security/patterns/secure-defaults.md` — one stack per section, defaults only (the "right default beats a long list").

## Commits & PRs

- Small, single-purpose PRs. Title: `area: what changed` (e.g. `cyber: add F021 grid guidance`).
- Run the PR security gate mindset on your own diff: no secrets, no permission widening.
