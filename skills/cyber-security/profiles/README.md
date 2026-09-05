# Cyber profiles

Profiles are **curated feature sets** for a target type. They answer "which of the 100 features do I run?" so you don't have to guess. Copy the ID set, run per the Cyber Security skill's effort matrix.

## When to use which

| Profile | Target looks like | Core question | F-set |
|---------|-------------------|---------------|-------|
| **web-app** | Server-rendered or SPA web app | Can a user touch another user's data or escalate? | F001–F010, F021–F035, F036–F041, F046, F066–F069, F076, F084, F093–F095, F100 |
| **api** | REST/GraphQL/gRPC backend | Object-level authz, resource abuse, API-specific classes | F001–F010, F022–F023, F032, F035, F036–F042, F046–F047, F066–F069, F076–F085, F093–F100 |
| **cloud** | Cloud infra / platform | IAM, exposure, isolation, IR readiness | F001–F010, F046–F055, F056–F065, F066–F075, F076–F083 |
| **auth-heavy** | IdP, login system, SSO integration | Can identities be forged, taken over, or enumerated? | F006–F007, F029, F036–F045, F066–F067, F095 |
| **mobile-backend** | Backend for a mobile app | Token handling, tenant isolation, API abuse | F022–F023, F036–F041, F046, F064, F084, F093 |
| **llm-app** | LLM-powered feature/agent | Prompt injection, data exfil via model, supply trust | F015, F018, F046, F055, F066, F076 + prompt-injection notes in SKILL.md |
| **binary/RE** | Binary, protocol, bundle, firmware | What does this artifact really do? | F001, F010, F046–F050, F068, F086–F092 |
| **full-max** | Anything, at Max effort | Everything applicable | all F001–F100 |

## Effort guidance per profile

- **Fast:** run the profile's *first listed group* only (usually foundations + one core section) — ~8 features.
- **Balanced:** foundations + core sections — ~20 features.
- **Max:** full set, plus chained skills (Attack Methods for H-features, RE for I-features, Stress for J-features).

## Common add-ons

- Payments/PII in scope → add F004, F009, F025, F065, F074.
- Third-party integrations → add F055, F044.
- Regulated environment → add F009, F072, F074.

## Defining a custom profile

```markdown
### Profile: <name>
Target: <description>
Question: <core question>
F-set: <IDs or ranges>
Skip: <IDs explicitly N/A + why>
Notes: <anything the runner must know>
```

Custom profiles live next to this README as `profiles/<name>.md` and should be referenced in the mission prompt (`Profile: <name>`).
