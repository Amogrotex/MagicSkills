# How to prompt MagicSkills

## Minimal

```
Follow https://raw.githubusercontent.com/YOU/magicskills/main/skills/think/SKILL.md

Task: We need to cut API p99 latency 30% without a rewrite.
```

## With loader (best)

```
Read https://raw.githubusercontent.com/YOU/magicskills/main/LOADER.md
then use the index to pick skills:
https://raw.githubusercontent.com/YOU/magicskills/main/INDEX.md

Request: Checkout 500s when coupons apply. Here's the stack trace: ...
```

## Chain explicitly

```
Run MagicSkills chain: think → debug → test
Loader: https://raw.githubusercontent.com/YOU/magicskills/main/LOADER.md

Context:
...
```

## Cursor / coding agents

```
Before changing code, load and follow:
/skills/debug/SKILL.md  (or paste raw GitHub URL)

Work step by step; don't skip verification.
```

## Local path style

If the repo is cloned into the workspace:

```
Open magicskills/LOADER.md and magicskills/INDEX.md.
Pick skills for: <request>
Execute step by step; show step outputs.
```

## Tips

1. Always give **symptom + context** for debug/test.  
2. Name the skill when you know it; otherwise point at `INDEX.md`.  
3. Ask for the **final Output section** if the model drifts into a free-form essay.  
4. For coding agents, pin: “Do not skip steps. Mark each step complete.”
