# Changelog

## 4.1.0

**Deepening pass — same architecture, more substance per unit.**

- **Feature pack deepened:** every feature F001–F100 now carries *Check for / Verify by / Maps to* (OWASP Top 10 2021, OWASP API 2023, ASVS 4.0, MITRE ATT&CK, NIST CSF 2.0, CIS v8, SLSA, SAMM). Findings gain a mappings column so output is auditable.
- **Profiles made real:** `profiles/README.md` expanded from a stub into per-profile F-sets, effort guidance, add-ons, and a custom-profile template.
- **Secure defaults library:** `patterns/secure-defaults.md` grown into per-stack hardened baselines (Express, FastAPI/Django, Spring, Go, Postgres, Redis, Nginx, Docker, JWT, OAuth/OIDC, cloud IAM, CI/CD, TLS).
- **PR security gate:** `checklists/pr-security-gate.md` is now a full diff-based gate with trigger map, ordered steps, verdict rules, and output template.
- **Gold-standard transcript:** `examples/full-mission-transcript.md` — complete ANIZ secure-chain run to anchor output quality.
- **CI:** `scripts/lint_pack.py` + workflow validating catalog paths, skill folders, F001–F100 completeness, relative links, version sync.
- **Governance:** CONTRIBUTING.md (contract rules, stable-ID policy, versioning), this changelog.

## 4.0.0

Initial public layout: loader/index/catalog, 12 skills, ANIZ router, 100-feature pack, effort levels (Fast/Balanced/Max), chains.
