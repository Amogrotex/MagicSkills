# Prompts — v4 cyber pack

## Full cyber ANIZ
```
LOADER: https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/LOADER.md
ANIZ: https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/aniz/SKILL.md
Focus: cyber-full
Effort: Max
Mission: Review our API auth and rate limits; map attack methods; plan stress tests; file issues.
```

## 100 features via Cyber Security
```
https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/cyber-security/SKILL.md
https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/cyber-security/features/F001-F100.md
Profile: api
Effort: Max
Target: <code>
```

## Attack Methods
```
https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/attack-methods/SKILL.md
Effort: Balanced
ROE: We own this app; staging only
Target: checkout + login architecture
```

## Reverse Engineering
```
https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/reverse-engineering/SKILL.md
Effort: Max
Permission: owner-authorized
Target: <file description / hashes / platform>
Goal: security review + protocol notes
```

## Stress Tests
```
https://raw.githubusercontent.com/Amogrotex/MagicSkills/main/skills/stress-tests/SKILL.md
Effort: Balanced
Target: /login /search /checkout
SLO: error rate < 1% at 2× peak
ROE: staging; abort if p99 > 5s
```

## Chain
```
Reverse Engineering (Max) → Cyber Security (Max) → Attack Methods (Balanced) → Stress Tests (Fast) → Issues Founder (Balanced)
```
