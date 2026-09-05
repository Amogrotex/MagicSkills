#!/usr/bin/env python3
"""MagicSkills pack linter — validates internal consistency (stdlib only).

Checks:
  1. catalog.json is valid JSON; every referenced path exists.
  2. Every skill directory under skills/ has a SKILL.md and is in catalog.json.
  3. F001..F100 each appear exactly once in the feature pack.
  4. Relative markdown links resolve to real files.
  5. catalog.json version matches the version stated in INDEX.md.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


# 1. catalog.json
catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
for key in ("loader", "effort", "index"):
    p = ROOT / catalog[key]
    if not p.exists():
        err(f"catalog.json '{key}' path missing: {catalog[key]}")

skill_paths = set()
for skill in catalog["skills"]:
    p = ROOT / skill["path"]
    skill_paths.add(skill["id"])
    if not p.exists():
        err(f"catalog skill path missing: {skill['path']} ({skill['id']})")

# 2. skills dirs <-> catalog
for d in sorted((ROOT / "skills").iterdir()):
    if not d.is_dir():
        continue
    if not (d / "SKILL.md").exists():
        err(f"skills/{d.name}/ has no SKILL.md")
    if d.name not in skill_paths:
        err(f"skills/{d.name}/ exists but is not in catalog.json")

# 3. feature IDs
feat_file = ROOT / "skills/cyber-security/features/F001-F100.md"
text = feat_file.read_text(encoding="utf-8")
# strip fenced code blocks so example rows in templates don't count as feature rows
text = re.sub(r"```.*?```", "", text, flags=re.S)
rows = re.findall(r"^\|\s*F(\d{3})\s*\|", text, flags=re.M)
seen = {}
for i in rows:
    seen[i] = seen.get(i, 0) + 1
for n in range(1, 101):
    fid = f"{n:03d}"
    count = seen.get(fid, 0)
    if count == 0:
        err(f"feature F{fid} missing from feature pack")
    elif count > 1:
        err(f"feature F{fid} appears {count} times as a table row")

# 4. relative md links
link_re = re.compile(r"\]\(([^)#\s]+)(?:#[^)\s]*)?\)")
for md in ROOT.rglob("*.md"):
    for m in link_re.finditer(md.read_text(encoding="utf-8")):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:", "/")):
            continue
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            err(f"{md.relative_to(ROOT)}: broken link '{target}'")

# 5. version sync
m = re.search(r"Pack\s*`?([0-9]+\.[0-9]+\.[0-9]+)`?", (ROOT / "INDEX.md").read_text(encoding="utf-8"))
if not m:
    err("INDEX.md: no 'Pack x.y.z' version line found")
elif m.group(1) != catalog["version"]:
    err(f"version mismatch: catalog.json={catalog['version']} INDEX.md={m.group(1)}")

if errors:
    print(f"✖ {len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"✔ pack lint clean (catalog {catalog['version']}, {len(skill_paths)} skills, F001–F100 complete)")
