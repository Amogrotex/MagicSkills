# Skill: ANIZ (All-In-One)

> All-in-one router — chains every skill including Cyber (F001–F100), Attack Methods, Reverse Engineering, Stress Tests.

**Version:** 4.0.0  
**Default** when no skill named / “ANIZ” / “all in one”.  
**Effort:** Fast · Balanced · Max  

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Mission | yes | Goal |
| Artifacts | no | Code, logs, binaries, URLs |
| Effort | no | Fast / Balanced / Max (default Balanced) |
| Focus | no | `secure` · `cyber-full` · `re` · `stress` · `fix` · `build` · `learn` |

**Legacy mode:** `fast|full|secure` → Fast / Balanced / (Max + secure chain).

---

## Effort matrix (ANIZ)

| | **Fast** | **Balanced** | **Max** |
|--|----------|--------------|---------|
| Child effort | Fast | Balanced | Max |
| Chain length | 1–3 | 3–6 | 5–9 |
| Cyber features | 5–10 | 15–30 | 40+ |

---

## Process

### Step 0 — Mission brief
- One-line mission · tags: `learn|build|fix|audit|decide|re|stress|adversary`  
- Resolve Effort + Focus  
- Announce `ANIZ · Effort · Tags · Focus`

### Step 1 — Route

| Stage | Skill | When |
|-------|--------|------|
| T | Thinking | Ambiguity / multi-tag |
| DS | Deep Search | Obscure |
| R | Research | Facts/options |
| D | Debugger | Broken symptoms |
| C | Coding | Implement |
| S | Scanning | Code/config pass |
| CS | Cyber Security | Harden / F-features |
| AM | Attack Methods | Adversary paths / purple |
| RE | Reverse Engineering | Binary/protocol/bundle |
| ST | Stress Tests | Load/chaos/abuse stress |
| IF | Issues Founder | Tickets |

**Templates:**

| Tags / Focus | Fast | Balanced | Max |
|--------------|------|----------|-----|
| decide | T | T | T→R |
| learn | R | R→T | DS→R→T |
| build | T→C | T→R→C→IF | T→R→C→S→IF |
| fix | D→C | D→C→IF | D→C→S→IF |
| audit / secure | CS→IF | S→CS→IF | S→CS→AM→IF→C |
| cyber-full | CS→AM | S→CS→AM→IF | S→CS→AM→ST→IF→C |
| re | RE | RE→CS | RE→CS→AM→IF |
| stress | ST | ST→C | ST→CS→C→IF |
| adversary | AM | CS→AM→IF | S→CS→AM→ST→IF |
| build+secure | T→C→IF | T→C→S→CS→IF | T→R→C→S→CS→AM→ST→IF |
| unclear | T→C/R | T→R→C→IF | T→DS/R→D/C→S→IF |

Announce chain before run.

### Step 2 — Execute stages
For each stage: `### ANIZ stage: Skill · Effort` → run child skill → Stage result → pass artifacts.  
Cyber Security should load `features/F001-F100.md` when CS runs.  
Skip N/A with reason. Defensive/authorized rules still apply in AM/RE/ST/CS.

### Step 3 — Integrate
Single backlog P0–P2 · done vs remaining · conflicts resolved.

### Step 4 — Final pack
Emit Output + quality check.

---

## Max extensions

### M1 Stage scorecard  
### M2 Dependency backlog  
### M3 Mission risks  
### M4 Re-run plan (skill + effort + feature IDs)  
### M5 Executive one-pager  
### M6 Feature coverage summary (if CS ran)

---

## Output (final)

```markdown
## ANIZ result
**Effort:** Fast | Balanced | Max
**Focus:** ...

### Mission
...

### Chain run
1. ...

### Executive summary
...

### Deliverables
- ...

### Cyber features (if any)
done/skip/n/a counts

### Backlog
| ID | Pri | Item | From | Next |
|----|-----|------|------|------|

### Next actions
1.
2.
3.
4.
5.
```

---

## Quality bar

- [ ] Chain matches focus/effort  
- [ ] No fake stages  
- [ ] No weaponized exploit output  
- [ ] Integrated backlog  
