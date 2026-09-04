# Example: ANIZ mission trail (miniature)

**Human:** Run ANIZ. Mission: Add rate limiting to our public Express API and file any issues you spot in the snippet.

```js
// app.js (snippet)
app.post('/login', async (req, res) => {
  const user = await db.findUser(req.body.user);
  if (user && user.password === req.body.password) {
    res.json({ token: user.id });
  } else res.status(401).end();
});
```

---

### ANIZ Step 0 — Mission brief
- Mission: Add rate limiting; surface issues in login snippet  
- Tags: `build` + `audit`  
- Mode: `full`

### ANIZ Step 1 — Route
Chain: **Thinking → Coding → Scanning → Cyber Security → Issues Founder**  
(Why: need approach, implementation, surface scan, security lens, tickets)

### Stage: Thinking
- Decision: token-bucket / middleware rate limit per IP on `/login` + fix auth issues separately  
- First moves: define limits, implement middleware, don’t store plaintext passwords as follow-up P0

### Stage: Coding
- Spec: 10 req/min/IP on `/login`, 429 + Retry-After  
- Design: `rateLimit` middleware, in-memory store for single node  
- Code: (middleware sketch)  
- Verify: burst 11th request → 429

### Stage: Scanning
- S1 Secrets: none in snippet  
- S3 Auth: plaintext password compare; token = user.id  
- S4 Access: N/A small snippet  
- Findings: High auth storage/compare; High predictable token

### Stage: Cyber Security
- Threats: credential stuffing, token guessing, password leak from DB compromise  
- Hardening: hash passwords (argon2/bcrypt), opaque session/JWT with secret, lockout/rate limit, generic 401  

### Stage: Issues Founder
- P0: Passwords compared in plaintext  
- P0: Token is raw user id  
- P1: No rate limit (addressed by coding stage — verify merged)  
- P2: No structured audit log on auth failure  

## ANIZ result (short)

**Deliverables:** rate-limit approach + middleware direction; security findings; issue tickets.  
**Backlog:** P0 password hashing; P0 opaque tokens; confirm rate limit wired on `/login`.  
**Next actions:** implement hash migration; issue session tokens; add tests for 429 and auth negatives.
