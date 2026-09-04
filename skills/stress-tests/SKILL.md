# Skill: Stress Tests

> Resilience & abuse stress testing — load, spike, soak, exhaustion, chaos, auth hammering plans and result analysis.

**Version:** 1.0.0  
**Chain well with:** Attack Methods, Cyber Security, Coding, Debugger, Scanning, Issues Founder, ANIZ  
**Effort levels:** Fast · Balanced · Max  
**Features:** F093–F100 (+ F001, F066, F067)

---

## Mandate

- Run or plan tests on **systems you own / are authorized** to test.  
- Goal: find breaking points, SLO gaps, amplification risks, weak limits — **safely**.  
- No DDoS instructions against third parties; no “take this site offline” playbooks.  
- Prefer staged environments; production only with explicit ROE and kill switches.

---

## When to use

- “Will it hold?”, capacity, rate limits, timeouts  
- Auth endpoints under hammering  
- Chaos / dependency failure behavior  
- Pre-launch resilience gate  

**Do not use when:** single functional bug (→ Debugger) or only security class review without load (→ Cyber Security / Attack Methods).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Target | yes | Service, endpoint list, env |
| SLOs / limits | no | latency, error rate, RPS, saturation |
| Auth model | no | tokens, login, public vs private |
| Tooling | no | k6, JMeter, Locust, ghz, chaos tools |
| ROE | yes if prod | windows, max RPS, abort rules |
| Effort | no | Fast / Balanced / Max |

---

## Effort matrix

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| **Goal** | Smoke stress + top risk | Solid suite plan/results | Full resilience program |
| **Profiles** | 1–2 | 4–6 | 8+ incl chaos |
| **Steps** | 1, 3, 5, 6 | 1–7 | 1–7 + Max extensions |
| **Chaos** | Optional note | 1–2 faults | Fault matrix |

---

## Process

### Step 1 — Scope, ROE, success
- Env · endpoints · max load · abort criteria  
- What “pass” means (SLO)  

**Output:** scope · ROE · SLOs

### Step 2 — Risk hypotheses
- Where it melts (DB, auth, memory, locks, third party)  
- Amplification / expensive routes  
- Shared limits (one tenant hurts all?)  

**Output:** hypothesis list

### Step 3 — Choose test profiles
From library (select by effort):

| Profile | Intent |
|---------|--------|
| P-SMOKE | Low RPS sanity |
| P-LOAD | Expected peak |
| P-SPIKE | Sudden 5–10× |
| P-SOAK | Long duration memory/leak |
| P-STRESS | Beyond peak until break |
| P-AUTH | Login/OTP/reset hammer + lockout check |
| P-BURST-WRITE | Heavy writes / checkout |
| P-PAGINATION | Huge offsets / deep pages |
| P-UPLOAD | Large/many uploads |
| P-FANOUT | Noisy neighbor / multi-tenant |
| P-TIMEOUT | Slow dependency |
| P-CHAOS-KILL | Kill replica / dependency |
| P-CHAOS-NET | Latency/loss inject |
| P-RETRY-STORM | Client retries amplify |
| P-CACHE-COLD | Cold start thundering herd |

**Output:** selected profiles + params (RPS, duration, VUs)

### Step 4 — Instrumentation
- Metrics: latency p50/p95/p99, error %, saturation, queue, CPU/mem, DB  
- Business metrics: failed logins, checkout success  
- Logs/traces needed  

**Output:** metrics checklist

### Step 5 — Execute or specify
- If tools available: run and capture  
- Else: exact scripts/commands **skeleton** + expected observations  
- Stop on abort criteria  

**Output:** run log / spec

### Step 6 — Analyze breakpoints
- Breaking point numbers  
- Failure mode (timeout, 500, data corruption?, retry storm)  
- Security-relevant: lockout bypass? auth CPU DoS?  

**Output:** breakpoint table

### Step 7 — Harden & handoff
- Limits, queues, bulkheads, timeouts, circuit breakers, scaling  
- Tickets via Issues Founder  
- Code changes via Coding  
- Method link via Attack Methods (availability impact class)  

**Output:** hardening + handoffs

---

## Max extensions

### M1 — Full matrix: endpoint × profile × result  
### M2 — Capacity model (back-of-envelope RPS → instances)  
### M3 — Game-day script (roles, timeline, comms)  
### M4 — Multi-region / failover stress  
### M5 — Data integrity checks under stress (not only HTTP 200)  
### M6 — Cost explosion risks (serverless bill shock)  
### M7 — Regression stress suite for CI (lighter profiles)

---

## Output (final)

```markdown
## Stress Tests result
**Effort:** Fast | Balanced | Max

### Scope & ROE
...

### SLOs
...

### Profiles run / planned
| Profile | Params | Result | Breakpoint |
|---------|--------|--------|------------|

### Failure modes
- ...

### Security-relevant notes
- ...

### Hardening
1.
2.
3.

### Feature IDs
F093–F100

### Max only
#### Capacity model
...
#### Game-day
...

### Next actions
1.
2.
3.
```

---

## Quality bar

- [ ] ROE / abort criteria clear  
- [ ] Profiles named with params  
- [ ] Breakpoints or explicit blockers  
- [ ] No third-party attack instructions  

---

## Anti-patterns

- “Just flood them” with no metrics  
- Prod stress without kill switch  
- Ignoring data integrity  
- Treating stress as only CPU, not auth/logic  
