---
tags: [tax, review, audit, retirement, cfp]
aliases: ["Strategy Review", "Deep Dive 2026"]
updated: 2026-10-14
---

# Full Strategy Review — October 2026

**Summary**: A CPA/CFP-level audit of the whole plan, including an audit of tonight's own work. **One material error found and corrected** (the "2027 converts at 8.8%" result was an artifact of single-year thinking — the true cost is ~35%). The **Florida move at ~2030** is worth far more than previously credited. And a lifetime projection shows the uncomfortable headline: **the original plan does not work** — converting only in 2042–2050 leaves **$6.4M still pre-tax at age 75**. The fix is not better conversion timing; it is **acquisition cadence**. Sustaining ~$900K/year of cost-seg property purchases and pairing them with conversions cuts projected lifetime tax by **~$1.5M**. Three structural gaps are also flagged, the largest being that **there is no taxable account to pay conversion taxes from.**
**Scope**: everything discussed 2026-08-13 and 2026-10-14, re-derived
**Tools**: `scripts/lifetime_projection.py`, `scripts/conversion_calculator.py`
**Related**: [[roth-conversion-annual-protocol]] · [[2026-acquisitions-analysis]] · [[tax-mitigation-master-plan]] · [[roth-conversion-window]]

---

## Part 1 — Audit of tonight's analysis

### ❌ CORRECTED: the "2027 converts at ~8.8%" result was wrong

Earlier tonight I reported that the NOL carryforward from the 2026 acquisitions would let ~$200K convert in 2027 at **8.8%**. **That figure is an artifact of single-year modelling and should be discarded.**

The reasoning error: post-2017 NOLs are capped at **80% of taxable income**, so each converted dollar raises taxable income, raises the 80% ceiling, and unlocks ~$0.80 more NOL. In a one-year snapshot only ~20¢ appears taxed. But the NOL consumed **would otherwise have sheltered the following year's W-2 income at 35–37% plus Colorado.** Tested across 2027+2028 together:

| Convert in 2027 | Single-year rate (wrong) | **True 2-year rate** |
|---|---|---|
| $100,000 | 5.3% | **36.8%** |
| $200,000 | 8.8% | **35.2%** |
| $300,000 | 15.4% | **32.9%** |

**Corrected guidance: do not convert into an NOL-carryforward year.** Let the carryforward burn against high-rate W-2 income instead.

### ✅ The general principle this exposes

A conversion is only genuinely cheap when it uses bracket space that would **otherwise expire unused**. That gives a clean test:

| Shelter | Does converting consume it? | Conversion genuinely cheap? |
|---|---|---|
| **§461(l) cost-seg allowance** — fixed at $512K regardless of income | **No** — the cap is income-independent | ✅ **Yes, the rate is real** |
| **NOL carryforward** — limited to 80% of *taxable income* | **Yes** — converting accelerates its use | ❌ **No, the low rate is an illusion** |
| **Empty retirement-year brackets** | Nothing to consume | ✅ **Yes** |

### ✅ What survives the audit

- **$155K at 24% in a post-relocation cost-seg working year** — holds. The §461(l) cap doesn't move with income, so nothing is displaced.
- **The §461(l) → NOL carryforward treatment** — confirmed against §461(l)(2) (treated as an NOL for §172 purposes) and the IRS Form 461 instructions. One secondary source claims a contrary "specified loss" treatment post-2024; it could not be verified against primary law. **Still worth one question to Zach Fox.**
- **$512,000 MFJ for 2026** — confirmed by multiple sources, down from $626,000.
- **Blended-rate targeting over marginal-rate stopping** — holds. IRMAA tiers are one-year spikes.
- **Colorado at ~4.4%** — confirmed empirically from the July pay advice ($20,580 withheld on $471,388 = 4.37%).
- **The backdoor Roth chain and $0.04 traditional IRA balance** — verified from statements.

### ⚠️ A finding about the 2026 acquisitions

Lumping all three properties into one year **cost deduction value**. The $512K of usable loss takes taxable income from $767,800 down to $255,800, so its last tranche only shelters income at **24%**:

| Band sheltered | Amount | Rate |
|---|---|---|
| 35% bracket | $255,350 | 35% |
| 32% bracket | $108,900 | 32% |
| 24% bracket | $147,750 | **24%** |
| **Blended** | **$512,000** | **~31% federal** |

Spread across two years, each year's loss would have stayed in the 35% band. **Roughly $20K left on the table, plus the timing cost of the carryforward.** Already-done for 2026 — but it confirms the standing rule in [[str-cost-segregation-playbook]]: **size the acquisition calendar to ~$512K of loss per year, no more.**

---

## Part 2 — The Florida move at ~2030 is the second-biggest lever in the plan

Moving in **3.5 years (≈2030)** rather than "sometime before 2041" changes the arithmetic materially.

| | Colorado | Florida |
|---|---|---|
| Conversion in a cost-seg year | 28.4% | **24.0%** |
| Years of post-move working life (2030–2041) | — | **12** |
| Conversion capacity at 24% over those years | — | **~$1.86M** |

**Why this works even while still employed**: a Roth conversion is intangible income, sourced to the **state of residence**. Once domiciled in Florida, Colorado cannot tax conversions — **even if his wages remain Colorado-source.** The conversion benefit does not depend on the wage question below.

> [!question] Open question worth ~$35K/year — do the *wages* also escape Colorado?
> **49 U.S.C. §40116(f)** taxes an air carrier employee who performs regularly assigned duties **on aircraft in two or more states** only in their state of residence (and any state where >50% of pay is earned). For a line pilot moving to Florida, Colorado wage tax disappears — worth ~$35,200/year on $800K.
>
> **His role makes this genuinely uncertain.** The pay advice shows "Flight Evaluator, 8256-B737 FLEET, Denver" in pay group "PIJ-Pilot Instr & Job Share." Research confirmed the statute but **did not resolve whether simulator/ground-instruction time counts as "duties on aircraft."** The presence of *Per Diem Pay* and *Flight Advance* on the stub suggests he does fly — which would support the exemption — but this needs a direct answer.
> → **Ask ALPA and Zach Fox before the move.** Over 12 years it is a **~$420,000** question.

**Also**: rental income from any property **physically located in Colorado remains Colorado-taxable forever**, regardless of residency. → Where are the three 2026 properties? Future acquisitions should favor no-tax states ([[str-cost-segregation-playbook#State selection]]).

---

## Part 3 — Lifetime projection: the original plan does not work

Modelled in `scripts/lifetime_projection.py`, all figures in **2026 real dollars** at a 4.5% real return.

| Strategy | Lifetime tax | Total converted | **Pre-tax at 75 (2051)** | First RMD |
|---|---|---|---|---|
| **A.** Convert only 2042–2050 *(the plan as written)* | $3,847,509 | $2.25M | **$6,390,462** | $259,122 |
| **B.** A + convert in post-FL cost-seg working years | $3,698,065 | $3.18M | $4,483,538 | $181,799 |
| **C.** B + a cost-seg deal **every** year + $400K retirement conversions | **$2,334,278** | $5.46M | **$961,231** | **$38,976** |

### What this says

1. **Strategy A fails.** Nine years of conversions cannot outrun ~$130K/year of employer contributions compounding at 4.5% real. The balance *grows* through the conversion window and arrives at 75 essentially untouched — **$6.4M, throwing $259K RMDs that grow to $362K by 84.**
2. **Strategy B helps but doesn't solve it** — $149K of lifetime saving, still $4.5M pre-tax at 75.
3. **Strategy C is the plan that works**: lifetime tax **$1.51M lower than A**, RMDs reduced to a rounding error, and **$10.4M in Roth at 75** — inherited tax-free under the 10-year rule.

### The real lever is acquisition cadence, not conversion timing

The difference between B and C is mostly *how often a cost-seg deal lands*. To sustain the full $512K §461(l) allowance each year:

| Reclass rate | Purchase price needed per year | Equity at 20–25% down |
|---|---|---|
| **70%** (RV/MHP parks) | **~$915,000** | ~$185–230K |
| 50% | ~$1.28M | ~$260–320K |
| **30%** (typical residential STR) | **~$2.13M** | ~$430–530K |

→ At 70% reclass, **~$900K of acquisitions per year** sustains the maximum deduction — very achievable on this income. At 30% it requires $2.1M/year, which likely is not. **This is the strongest financial argument for concentrating on RV/MHP parks**, independent of the returns on the real estate itself.

> [!warning] Model limitations — read before relying on these numbers
> Excludes IRMAA (roughly $130K over the retirement window, affecting all three scenarios similarly), NIIT, AMT, the SALT phase-down, and state tax on out-of-state rental income. Assumes a constant 4.5% real return with no sequence risk, flat real wages, and that REPS holds every year. **Directionally robust, not precise.** The ranking of A < B < C is the finding; the dollar amounts are estimates.

---

## Part 4 — Structural gaps not yet addressed

### 🔴 Gap 1: There is no taxable account to pay conversion taxes from

The plan repeatedly says *pay conversion tax from outside funds, never by withholding*. But **every liquid dollar found so far is inside a retirement account** — $1.66M 401(k), $85K after-tax sleeve, $17.7K Roth, and $0.04 in a traditional IRA. There is no taxable brokerage.

Strategy C requires roughly **$100–130K/year of outside cash for conversion taxes** across 2042–2050, plus living expenses in retirement. Without it, conversions must be funded by withholding — which **shrinks what lands in the Roth and defeats the exercise.**

Candidate sources, in order: **real estate cash flow** (the most natural, and already being built), a deliberate **taxable brokerage** funded from the PRAP Cash that currently arrives as taxable wages anyway, and the **RHA** covering retirement healthcare so those dollars aren't drawn from elsewhere.

→ **This belongs in the plan as a funding target with a number, not an assumption.** It is the most likely single point of failure.

### 🟠 Gap 2: Stacy's Social Security claiming strategy is probably wrong as written

The plan says *Stacy claims at 70 (2/2041)*. With **no earned income**, her benefit is likely **spousal**, and spousal benefits behave differently:

- **Spousal benefits earn no delayed retirement credits.** They max out at *her* FRA (67, Feb 2038). Delaying to 70 gains **nothing**.
- **She cannot claim a spousal benefit until Ryan files** — which under the current plan is **2046**, when she is 75.

→ **Open question: does Stacy have her own Social Security earnings record (40 quarters)?** If yes, she should likely claim her own benefit at her FRA and be topped up to the spousal amount when Ryan files. If no, there is no benefit until 2046 and the plan's income assumptions for 2041–2046 are wrong. **This changes conversion capacity in exactly the cheap years.**

### 🟡 Gap 3: Survivor exposure is named but never quantified

Under Strategy A, the survivor at 85 faces ~$360K of RMDs plus Social Security, filing **single** — half the bracket widths and half the IRMAA thresholds. That is the 35–37% bracket and top-tier IRMAA on income that was 24% as a couple. **Strategy C largely eliminates this**, which is arguably its biggest non-dollar benefit.

### Smaller items worth a pass

- **Estate**: ~$5–8M net worth against a $15M/$30M exemption — estate tax is not the constraint; **basis step-up and beneficiary designations are**. Confirm every account names individuals, not the estate.
- **Asset protection**: an active real estate operation with 3+ properties warrants an umbrella policy and entity review alongside the SPE structure already in place.
- **Children**: hiring them in the real estate business (deductible wages, their standard deduction shelters it, funds a Roth IRA with a 50-year runway) remains unexploited.
- **NIIT safe harbor**: with REPS and 500+ hours on the grouped activity, rental income escapes the 3.8% NIIT — worth confirming the hours support it.
- **2041 severance/PTO payout** at retirement is W-2 income landing in an already-partial year; confirm the amount before sizing 2041.

---

## Part 5 — Revised priority order

| # | Action | Why now | Value |
|---|---|---|---|
| 1 | **Rebuild Stacy's REP log** (July 11 → today) from primary sources | 11 weeks left; ~250 hours short | **~$200–215K of 2026 tax** |
| 2 | **Verify the three cost-seg studies** — reclass %, recourse financing, placed-in-service | Gates everything in item 1 | same $200–215K |
| 3 | **Commit to ~$900K/year of acquisitions** (park-weighted) | The single biggest lifetime lever | **~$1.5M lifetime** |
| 4 | **Ask ALPA/CPA the §40116(f) wage-sourcing question** | Decide before the 2030 move | ~$420K over 12 years |
| 5 | **Build the conversion-tax reserve plan** | The plan fails without it | structural |
| 6 | **Check Stacy's SS earnings record** | Changes claiming + conversion capacity | material |
| 7 | **Enable Ryan's $8,000 Roth catch-up** | Few pay periods left in 2026 | ~$8K/yr |
| 8 | **Stacy's spousal backdoor Roth** ($8,600) | Deadline 4/15/2027 | ~$8.6K/yr |
| 9 | **Hold the 2026 conversion decision** until items 1–2 resolve | 2027 is *not* the cheap year I claimed | avoids an error |

> [!warning] Planning analysis, not tax advice
> Every figure is modelled from published rules and estimated inputs by an AI assistant, and tonight's audit found one material error in its own prior work — which is the best argument for independent review. **Zach Fox at Incite Tax signs off before anything here is executed.** The REPS position and the 70% reclass rate are the two most audit-exposed elements.

**Related**: [[roth-conversion-annual-protocol]] · [[2026-acquisitions-analysis]] · [[tax-mitigation-master-plan]] · [[roth-conversion-window]] · [[household-timeline]] · [[stacy-rep-tracking-audit-2026]]
