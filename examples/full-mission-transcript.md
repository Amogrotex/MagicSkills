# Example: full ANIZ mission transcript (gold standard)

A complete, realistic run to anchor output quality. Mission: security review of a small Express login endpoint.

**Human:** Follow LOADER.md · ANIZ · Effort: Balanced · Focus: secure · Mission: Harden this login code and file real issues.

```js
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const u = await db.query(`SELECT * FROM users WHERE email = '${email}'`);
  if (!u.rows[0] || !(await bcrypt.compare(password, u.rows[0].hash))) {
    return res.status(401).json({ error: 'user not found' });
  }
  const token = jwt.sign({ id: u.rows[0].id, role: u.rows[0].role }, SECRET, { expiresIn: '30d' });
  res.json({ token });
});
```

---

```
ANIZ · Effort: Balanced · Tags: audit/fix · Focus: secure
Chain: Scanning → Cyber Security → Issues Founder
```

### ANIZ stage: Scanning · Balanced

| # | Area | Status | Note |
|---|------|--------|------|
| 1 | Query construction | FINDING | string-interpolated SQL — injection (F024 / A03) |
| 2 | Error asymmetry | FINDING | "user not found" vs "wrong password" — enumeration oracle (F045 / A07) |
| 3 | Token TTL | FINDING | 30d static JWT, no rotation (F029/F039 / A07) |
| 4 | JWT claims | OK-ish | role taken from DB, not client — but see Cyber stage |
| 5 | Rate limiting | FINDING | none on route (F026/F095 / A04/API4) |
| 6 | Password storage | OK | bcrypt compare |

### ANIZ stage: Cyber Security · Balanced (profile: web-app, 21 features)

Run log (subset):

| ID | Status | Notes | Evidence | Out |
|----|--------|-------|----------|-----|
| F001 | done | ROE: owner's own code, authorized | snippet provided | — |
| F003 | done | boundary: client → route → DB | code path | — |
| F023 | n/a | single-user login, no object routes in scope | | |
| F024 | done | SQL injection via `email` interpolation | query string | P0 |
| F026 | done | no throttle on auth → stuffing class | no middleware | P1 |
| F029 | done | 30d JWT, no revoke path | sign options | P1 |
| F036 | done | bcrypt OK; no breach-list check | compare call | P2 |
| F039 | done | alg not allowlisted; role claim long-lived | sign options | P1 |
| F045 | done | response asymmetry enumerates users | error branch | P1 |
| F066 | done | no login-failure logging for detection | — | P1 |

Findings table (each carries its mapping):

| Finding | F-ID | Mapping | Severity | Fix | Ticket |
|---------|------|---------|----------|-----|--------|
| SQL injection in login query | F024 | A03 · ASVS V5 | P0 | parameterize: `WHERE email = $1` | #1 |
| User enumeration via error text | F045 | A07 · ASVS V2 | P1 | single generic 401 + uniform timing | #2 |
| 30d non-revocable JWT, role in claims | F029/F039 | A07 · ASVS V3 | P1 | 15-min access + rotating refresh; alg allowlist | #3 |
| No rate limit on /login | F026/F095 | A04 · API4 | P1 | limiter + exponential backoff by IP+email | #4 |
| No auth-event logging | F066 | A09 · CIS 8 | P1 | log {ok/fail, ip, email-hash} structured | #5 |

### ANIZ stage: Issues Founder · Balanced

| ID | Pri | Title | Acceptance |
|----|-----|-------|------------|
| #1 | P0 | Parameterize login query | no string interpolation in any query; test with `' OR 1=1 --` class input returns 401 |
| #2 | P1 | Uniform login failure response | identical body+timing for unknown user / wrong password |
| #3 | P1 | Short-lived JWT + refresh rotation | access ≤15 min; refresh rotation detects reuse; `algs: ['HS256']` |
| #4 | P1 | Rate limit /login | ≥5/min/IP+email → 429 with Retry-After |
| #5 | P1 | Auth event log | fail/success events queryable; no raw password in logs |

### ANIZ stage: Integrate

**Backlog:** 1×P0, 4×P1 · chain complete, no conflicts · #1 blocks deploy of this route.

### Final pack (abbreviated)

**Next actions:** 1) fix #1 now (one-line) · 2) #4 + #2 same PR · 3) #3 needs token design decision → Thinking skill · 4) #5 pairs with detection work (F067) · 5) re-scan after merge (PR gate).

**Quality bar:** chain matched focus · no fake stages · no exploit output (injection shown as fix, not payload) · integrated backlog ✓

---

*What makes this "gold standard": every finding has evidence (code location), a mapping (OWASP/ASVS/CIS), and a ticket with acceptance criteria. Copy this shape, not just the headings.*
