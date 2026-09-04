# Example: Debug session trail

This is what a **good** MagicSkills run looks like when the human says:

> Use MagicSkills debug.  
> Our API returns 500 on `POST /checkout` when the cart has coupon `SAVE10`.  
> Stack: Node + Express. Error: `TypeError: Cannot read properties of null (reading 'toFixed')` in `pricing.js:42`.

---

### Skill loaded
`skills/debug/SKILL.md` — symptom + stack trace present.

### Step 1 — Capture the symptom precisely
- **Expected:** 200 with discounted total  
- **Actual:** 500, `TypeError` on `null.toFixed`  
- **Frequency:** always when coupon present  
- **Scope:** checkout only  
- **Evidence:** `pricing.js:42` — `discount.toFixed(2)`

✓ Step 1 complete

### Step 2 — Reproduce
1. Add item to cart  
2. Apply `SAVE10`  
3. `POST /checkout`  
→ 500 reproduced locally with same stack.

✓ Step 2 complete

### Step 3 — Gather evidence
- `coupons` table row for `SAVE10` has `discount_value = NULL`  
- Code path: `getCoupon` → `applyDiscount` assumes number  
- Ruled out: payment provider (error is before charge)

✓ Step 3 complete

### Step 4 — Hypothesize
1. DB null discount (likely) — confirm: inspect row; kill: if non-null still crashes  
2. Wrong coupon shape from cache — confirm: log parsed coupon  
3. Race overwriting coupon — confirm: only if intermittent (it’s not)

✓ Step 4 complete

### Step 5 — Test hypotheses
- H1 confirmed: row null; code no guard  
- H2 killed: raw DB value already null  
- H3 killed: always fails

**Root cause:** `applyDiscount` does not treat null/invalid `discount_value`; bad data accepted at write time.

✓ Step 5 complete

### Step 6 — Minimal fix
1. Guard in `applyDiscount`: treat null/NaN as 0 **or** reject coupon  
2. Validate on coupon create/update  
Prefer: **reject invalid coupons at apply** + fix data row (correct business rule).

✓ Step 6 complete

### Step 7 — Verify
- Unit: `applyDiscount(100, null)` → error or defined behavior  
- Integration: `SAVE10` with null → 400 “invalid coupon”, not 500  
- Happy: valid 10% coupon still discounts

✓ Step 7 complete

## Debug result

### Symptom
Expected: discounted checkout  
Actual: 500 on null `discount_value`

### Root cause
`pricing.js` assumes `discount` is a number; DB allowed null.

### Evidence
- Stack at `pricing.js:42`  
- DB row null  
- Fails only with coupon

### Fix (minimal)
Validate coupon payload; return 400 on invalid; backfill/fix `SAVE10` row.

### Verification
Unit + one integration test for null discount.

### Next actions
1. Patch guard + validation  
2. Add regression test  
3. Audit other coupons for nulls
