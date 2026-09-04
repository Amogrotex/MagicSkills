# Example: ANIZ with effort levels

## A) Fast

**Human:** ANIZ · Effort: Fast · Mission: Do we need Redis for session store on a single VPS app?

```
ANIZ · Effort: Fast · Tags: decide
Chain: Thinking (Fast)
```

**Thinking Fast:** 2 options (sticky sessions / memory vs Redis) → Decision: memory OK until multi-instance → Next: revisit when scaling horizontally.

**Backlog:** 3 short next actions. No full research stage.

---

## B) Balanced

**Human:** ANIZ · Effort: Balanced · Mission: Add rate limiting to public Express login; file issues on this snippet.

**Chain:** Thinking → Coding → Scanning → Cyber Security → Issues Founder (all Balanced)

Stage artifacts: decision, middleware sketch, scan table, security findings, P0–P2 tickets.

---

## C) Max

**Human:** ANIZ · Effort: Max · Focus: secure · Mission: Same login snippet — production hardening pack.

**Chain:** Thinking → Research → Coding → Scanning → Cyber Security → Issues Founder (all Max)

Extras: STRIDE notes, surface matrix, acceptance criteria on tickets, stage scorecard, re-run plan, regression net for auth.

---

## Per-stage override

```
ANIZ · Effort: Balanced
Overrides: Cyber Security=Max, Research=Fast
Mission: ...
```

Children inherit Balanced except CS=Max and Research=Fast.
