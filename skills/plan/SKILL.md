# Skill: plan

> Break work into ordered, risk-aware steps with clear done criteria.

**Version:** 1.0.0  
**Chain well with:** think, test, review, research

---

## When to use

- Features, migrations, multi-file changes
- “How do we ship X?”
- Unclear scope or dependencies
- Need a checklist others can follow

**Do not use when:** a single small edit is already specified (just do it).

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Outcome | yes | What “shipped” means |
| Context | no | Codebase shape, constraints, deadlines |
| Non-goals | no | Explicit out-of-scope |

---

## Process

### Step 1 — Outcome & boundaries

- One-sentence outcome.
- In scope / out of scope.
- Constraints (tech, time, people).

**Output of step:** Outcome / In / Out / Constraints.

### Step 2 — Discover dependencies

- Prerequisites (data model, auth, APIs, feature flags).
- Unknowns that block sequencing.
- External owners or systems.

**Output of step:** dependency list + blockers.

### Step 3 — Slice into milestones

- 2–5 milestones, each demoable or verifiable.
- Prefer vertical slices over “all backend then all frontend” when possible.

**Output of step:** milestone list with done criteria each.

### Step 4 — Task breakdown

For each milestone, tasks:

| ID | Task | Depends on | Effort | Risk | Done when |
|----|------|------------|--------|------|-----------|

**Output of step:** task table.

### Step 5 — Risks & safety

- Top risks and mitigations.
- Rollback / feature-flag strategy if relevant.
- Test checkpoints (link to **test** skill mentally).

**Output of step:** risks table + safety net.

### Step 6 — Execution order (today)

- The exact next 3–7 actions in order.
- What to defer deliberately.

**Output of step:** ordered now-list + defer-list.

---

## Output (final)

```markdown
## Plan result

### Outcome
...

### Scope
In:
Out:

### Milestones
1. ... — done when: ...
2. ...

### Tasks
(table)

### Risks
| Risk | Mitigation |
|------|------------|

### Do next
1.
2.
3.

### Defer
- ...
```

---

## Quality bar

- [ ] Every milestone has a done criterion
- [ ] Tasks are small enough to finish in one sitting when possible
- [ ] Dependencies are explicit
- [ ] First “Do next” item is startable immediately

---

## Anti-patterns

- 40-item flat todo with no order
- Planning implementation details before outcome is clear
- No rollback thinking on prod-touching work
- Scope that quietly includes rewrites

---

## Example (miniature)

**Outcome:** Users can reset password via email link.  
**Milestones:** token model → email send → consume link UI → rate limits → metrics.
