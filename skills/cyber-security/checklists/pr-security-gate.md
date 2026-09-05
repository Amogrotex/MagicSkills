# PR security gate

Diff-based security review that runs **before merge** on every PR touching code, config, IaC, or dependencies. Lightweight by design — full review belongs to the Cyber Security skill.

**Verdicts:** `PASS` · `PASS WITH DEBT` (minor issues → tracked tickets) · `FAIL` (blocking issue present).

---

## Inputs

| Input | Source |
|-------|--------|
| Diff | the PR itself |
| Feature IDs touched | map diff to F-IDs below |
| Profile | project profile (see `../profiles/README.md`) |

## Diff → feature trigger map

| Change type | Gate checks | F-IDs |
|-------------|-------------|-------|
| Auth/session/JWT/OAuth code | F029, F036–F045 | auth section |
| Route/controller/handler added | F023 (ownership check on new route?), F024 (sinks), F035 (binding allowlist) |
| SQL/query/template strings | F024 parameterization |
| Dependency manifest / lockfile | F028 (SCA), F051–F052 (pin + provenance) |
| Secrets/config/env | F046 (no secrets in diff), F027 (misconfig) |
| Dockerfile / K8s / IaC | F061, F063 |
| CI workflow | F053 (permissions, fork PR secrets, pinned actions) |
| Crypto usage | F025, F048–F050 |
| New endpoint / API surface | F032 (SSRF), F034 (upload), F099 (unbounded query?) |
| Logs added/removed | F066 (baseline events kept) |

## Gate steps (in order)

1. **Scope the diff** — files changed, blast radius, which F-IDs triggered.
2. **Secrets sweep** — token/key/cert patterns in added lines. Any hit = FAIL.
3. **Dependency delta** — added/updated packages: known advisories (FAIL if critical with no override note), lockfile still present.
4. **Access-control check** — every new route/object read has an authorization decision. Missing = FAIL.
5. **Input path check** — new input → parameterized/encoded within 1 hop of entry. Missing = FAIL.
6. **Config drift** — headers, CORS, cookie attrs, TLS, debug flags unchanged or improved.
7. **Coverage note** — F-IDs checked this PR vs deferred (debt tickets).

## Verdict rules

- Any **FAIL-condition** step (2, 4, 5, critical advisory in 3) → `FAIL`.
- Only minor issues (naming, missing comment, hardening opportunity) → `PASS WITH DEBT` + tickets.
- Nothing triggered or all clean → `PASS`.

## Output template

```markdown
## PR security gate: PASS | PASS WITH DEBT | FAIL

**Scope:** <files/areas> · **Profile:** <profile>

| Step | Result | Notes |
|------|--------|-------|
| Secrets sweep | clean | |
| Dependency delta | 1 minor | lodash patch |
| Access control | clean | ownership check on /orders/:id |
| Input path | clean | parameterized query |
| Config drift | none | |

**F-IDs touched:** F023, F028
**Debt tickets:** #34 (CSRF token on /settings)
```
