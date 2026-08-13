---
tags: [tax, real-estate, reps, passive-losses, stacy]
aliases: ["REPS", "Real Estate Professional Status"]
updated: 2026-08-13
---

# Real Estate Professional Status — Stacy

**Summary**: Stacy works full-time in real estate — seller lead generation, acquisitions, and tenant management — making **Real Estate Professional Status available to this household**, a categorically bigger lever than the STR exception: REPS turns **all** rental losses non-passive on the joint return, so they offset Ryan's W-2 income directly. This has been an active project since at least April: a tracking system, election template, and decision framework already exist (merged below). **Current 2026 status: 564.54 hours logged through 7/10, tracking pipeline broken since then, and the pace projects short of 750** — see [[stacy-rep-tracking-audit-2026]] for the full audit and fix list.
**Sources**: IRC §469(c)(7), §469(h)(5), §461(l) · Reg. §1.469-9, §1.469-5T(a) · prior-AI corpus: `decision-tree-nonpassive-path`, `grouping-election-statement`, `CONTEXT-DUMP` (Drive, Apr 2026)
**CPA**: Zach Fox, Incite Tax — reviews the election, the property list, and the annual REP memo
**Related**: [[stacy-rep-tracking-audit-2026]] · [[str-cost-segregation-playbook]] · [[tax-mitigation-master-plan]] · [[household-timeline]] · [[mhp-rv-investment-strategy]]

## Current status — 2026 tax year (as of 2026-08-13)

| Metric | Value | State |
|---|---|---|
| Hours logged (through 7/10) | **564.54** | log stale since 7/11 |
| Recoverable from calendar gap 7/11–8/13 | ~21 | pending reconciliation |
| Questionable entries to purge | **~65** (driver's ed, tax-strategy meetings, aviation stray, undescribed) | pending — see audit F4 |
| **Defensible base** | **~500–520** | |
| Needed by 12/31 | 750 | **~230–250 to go ≈ 12/week** |
| >50% test | not formally tracked | trivially true (no other occupation) — document it |

The gap is closable because her strongest hours — negotiations, tenant management, CRM/lead work — are mostly **not being captured** (they never hit a calendar, and the pipeline only reads calendars). Toggl timers on non-calendar work is the single behavior that fixes both pace and composition. Full findings: [[stacy-rep-tracking-audit-2026]].

> [!warning] REPS is the most litigated position in real estate tax
> The IRS challenges it routinely and wins most cases **on the time log alone** — not on whether the work was real, but on whether it was documented as it happened. Everything below depends on Stacy keeping a contemporaneous log from day one. Get written CPA sign-off before relying on this.

## Why this changes the plan

The previous version of this plan assumed REPS was unavailable and built everything around the short-term rental exception. That was the correct read for a household where the only worker is a full-time W-2 earner. It is the wrong read here.

| | Without REPS | **With Stacy's REPS** |
|---|---|---|
| Short-term rental losses (≤7-day stays) | Non-passive ✅ | Non-passive ✅ |
| **Long-term rental losses** | Suspended ❌ | **Non-passive ✅** |
| **MHP lot-rent park losses** | Suspended ❌ | **Non-passive ✅** |
| RV park losses | Non-passive ✅ | Non-passive ✅ |
| Must cap guest stays at 7 days? | **Yes** | **No** |
| Must self-manage to beat a PM's hours? | **Yes** | Materially easier |
| Binding constraint on deductions | §469 passive loss rules | **§461(l) excess business loss — $512,000** |

**The single biggest consequence**: the [[mhp-rv-investment-strategy|MHP/RV acquisition strategy]] no longer has to wait until retirement. Mobile home park lot rent is a classic long-term rental — the one thing the STR exception could never reach. Under REPS it becomes fully deductible against Ryan's W-2 income. **Roads, pads, and site utilities are 15-year land improvements eligible for 100% bonus depreciation**, which makes parks one of the most cost-seg-favorable asset classes that exists.

## How Stacy qualifies — the two tests

Both tests in §469(c)(7)(B), every year, and **Stacy must pass them on her own hours**:

| Test | Requirement |
|---|---|
| **1. The majority test** | More than **50%** of her personal services in *all* trades or businesses must be in real property trades or businesses in which she materially participates |
| **2. The hours test** | More than **750 hours** of service in those real property trades or businesses |

> [!important] Hours cannot be combined for these two tests
> On a joint return, REPS is satisfied "if and only if **either spouse separately** satisfies such requirements." Ryan's hours **do not count** toward Stacy's 750 or her 50%. This is the most common way people get this wrong.
>
> The flip side is that Stacy only has to clear it alone — and since real estate is her full-time occupation with no competing job, the 50% test is easy and 750 hours is roughly 15 hours a week.

**Qualifying real property trades or businesses** (§469(c)(7)(C)): development, redevelopment, construction, reconstruction, acquisition, conversion, **rental, operation, management, leasing, or brokerage**.

Stacy's actual work maps cleanly onto this:

| What she does | Category | Counts? |
|---|---|---|
| Seller lead generation and outreach | Acquisition / brokerage | ✅ |
| Negotiating and closing purchases | Acquisition | ✅ |
| Tenant management, leasing, rent collection | Rental / operation / management | ✅ |
| Contractor and turn management | Operation | ✅ |
| Underwriting and market analysis for **our own** acquisitions | Acquisition | ✅ (see the investor-hours trap below) |

## The second step everyone misses

Qualifying as a real estate professional **does not by itself make the losses deductible.** It only removes the automatic "rental = passive" rule of §469(c)(2). Each rental activity must *still* pass material participation — and by default that is tested **property by property**, which is nearly impossible across a portfolio.

**The fix is the aggregation election under Reg. §1.469-9(g)**: a statement filed with the return electing to treat all interests in rental real estate as **a single activity**. Then material participation is tested once, on the combined portfolio.

And here is where the rules flip in our favor:

> [!tip] Ryan's hours DO count at this stage
> §469(h)(5): "any participation by the taxpayer's spouse shall be treated as participation by the taxpayer." Spousal hours cannot be combined for the REPS *qualification* tests — but they **are** combined for **material participation**. So once Stacy qualifies, Ryan's evenings and weekends on the portfolio count toward the 500-hour material participation test on the aggregated activity.

**Two-step summary:**

1. **Stacy alone** clears 750 hours + >50% of her personal services → she is a real estate professional
2. **File the §1.469-9(g) election**, aggregating all rental real estate into one activity → **Stacy + Ryan's combined hours** establish material participation in it

→ Both steps are required. Step 1 without step 2 leaves the losses passive anyway.

### The trade-off in the aggregation election

Aggregation is not free, and it is **binding in future years** unless there is a material change in facts:

- **Cost**: §469(g) releases suspended losses only on disposing of an *entire activity*. Once aggregated, selling one property is not disposing of the activity, so it does not free that property's suspended losses. This partly undercuts the "pair a disposition with a conversion year" play in [[roth-conversion-window#Sheltering conversions with real estate losses]].
- **Why it matters less for us**: under REPS the losses aren't being suspended in the first place — they're deducted currently. The suspended-loss release only matters for pre-REPS years or years REPS fails.

→ **Decide this with the CPA before filing**, ideally in the same conversation that reviews Stacy's log methodology. If there is a meaningful bank of suspended losses from prior years, the sequencing of the election matters.

### STRs stay outside the election

Short-term rentals with ≤7-day average stays are **not rental activities at all**, so they sit outside the §1.469-9(g) rental aggregation entirely and need their own material participation. Do **not** try to group them with the long-term rentals — mixing rental and non-rental activities is permitted only in narrow circumstances and risks the whole position.

In practice this is easy: with two people working the portfolio, the 500-hour test or the "100 hours and not less than any other individual" test is achievable on the STR group separately. Details in [[str-cost-segregation-playbook#Material participation — the tests that matter]].

## What REPS does NOT fix

REPS clears **one** of four gates. The other three are unchanged, and with REPS unlocking far more deductible loss, they now bind harder than before.

| Gate | Status under REPS |
|---|---|
| **§469 passive loss** | ✅ **Cleared** — this is what REPS does |
| **§461(l) excess business loss** | ❌ **Now the binding constraint — $512,000 MFJ** |
| **§465 at-risk** | ❌ Unchanged — nonrecourse seller carry still creates no at-risk basis |
| **Basis** | ❌ Unchanged |

> [!warning] §461(l) is now the real ceiling
> Net business losses above **$512,000 (MFJ, 2026)** cannot offset non-business income; the excess carries forward as an NOL usable against 80% of future taxable income. Before, §469 stopped the losses long before this mattered. Now that REPS lets everything through, **$512,000 is the practical annual cap on deductible real estate losses** — and it *dropped* from $626,000 in 2025.
>
> → **Size the acquisition calendar to this number.** Roughly $1.7–2.0M of purchase price per year at typical cost-seg reclass rates. Stacking three large acquisitions into one year wastes deductions into a carryforward instead of using them at 45.5%.

The **at-risk problem is unchanged and still the deal-killer** on seller-financed acquisitions: nonrecourse seller carry-back is not qualified nonrecourse financing under §465(b)(6)(D), so the year-one loss does not land. The fix — negotiate seller notes as personally guaranteed/recourse — is in [[str-cost-segregation-playbook#2. At-risk — §465]] and it is an LOI-stage ask.

## Documentation — the thing that actually decides audits

REPS cases are won and lost on records. Courts have repeatedly rejected logs reconstructed after an audit notice, even where the underlying work plainly happened.

**Stacy's log must capture:**

- **Date, hours, specific description, and property or activity** — "worked on rentals, 6 hrs" is worthless; "showed 412 Oak to 3 prospective tenants, ran applications, 3.5 hrs" is defensible
- **Contemporaneous entry** — daily or weekly, never reconstructed. Use a calendar or dedicated app whose entries carry real timestamps
- **Total personal service hours across all activities**, not just real estate — the 50% test is a *ratio*, so the denominator has to be provable too. If she does any non-real-estate work, log it
- **Ryan's hours separately**, for the material participation step
- **Corroboration**: CRM activity, MLS logins, email and text timestamps, mileage, contractor invoices, lease documents, closing files

> [!tip] The investor-hours trap
> Hours in a purely **investor** capacity do not count (Reg. §1.469-5T(f)(2)(ii)) — reviewing financial statements, studying market reports, or monitoring performance without day-to-day management involvement. Since Stacy *is* the day-to-day manager, most of her time is fine, but **underwriting and market study should be logged in the context of active acquisition work** on specific deals, not as generic research. Travel time is contested — log it as its own line so it can be removed without collapsing the total.

**Also worth having**: a short written memo each year, prepared with the CPA, stating the basis for the REPS position and the hour totals. It costs almost nothing and converts an audit from a reconstruction exercise into a document review.

## Per-property mapping — current portfolio

From the April decision-tree work, updated to the vault's framework. Which door each property uses:

| Property | Type / avg stay | Nonpassive path | Status |
|---|---|---|---|
| **Passionflower Circle** (FL, Disney STR) | ≤7-day STR | STR exception — material participation per property; **excluded from the grouping election** | Dual-path: works with or without REPS |
| **Mt Pleasant RV Park** (431 Mt Pleasant Rd) | Transient RV, ≤7-day typical | STR exception if active JV role; REPS covers any rental component | Door redundancy — strongest tax asset |
| **Kalispell co-living** (21 1st Ave W, MT) | >7-day — true rental | **REPS + grouping election required** | Locked to Stacy's annual qualification |
| **Fort Collins co-living** (420 Starway) | >7-day — true rental | **REPS + grouping election required** | Locked to Stacy's annual qualification |
| **Country Club View Apartments** (OK, LP interest) | LTR syndication | **None — trapped passive.** REPS does not cover a passive LP position with no material participation | Losses carry forward; release on full disposition |

Two structural notes carried over from the prior work:
- **Risk concentration**: every co-living/LTR property's tax outcome depends on one annually-retested fact — Stacy's REPS. STRs and transient RV parks qualify property-by-property without her. Tilting new acquisitions toward ≤7-day assets reduces the single-point-of-failure risk.
- **Stacy is managing member on all held-property SPEs** (per the Dan Gunther JV structure, which also allocates 100% of tax benefits to Ryan & Stacy). Keep it that way — it is what makes her hours attributable to each property's operations, and the grouping election must list every SPE with EINs.

## Filing infrastructure (already built, Apr 2026)

| Artifact | Where | State |
|---|---|---|
| **§1.469-9(g) grouping election statement** — ready-to-file template with property/EIN schedule, watch-outs (STRs excluded; binding; per-Stacy not per-couple) | Drive: `grouping-election-statement.md` | Template complete; needs property list + Zach Fox review; files with the first REPS-claimed return |
| **Nonpassive decision tree** — per-property flowchart (STR loophole vs. REPS vs. trapped) | Drive: `decision-tree-nonpassive-path.md` | Sound; superseded in part by this vault |
| **Hours log + reconciliation system** | Drive xlsx + local sync | **Broken — see [[stacy-rep-tracking-audit-2026]]** |
| NIIT note | — | REPS rentals with 500+ hours also qualify for the **NIIT safe harbor** — rental income escapes the 3.8% tax. One more reason to clear 500 on the grouped activity, not just scrape 750 overall. |

One rule from the prior work worth preserving verbatim: **W-2 employee hours don't count toward REPS unless she owns >5% of the employer.** Her eXp agent work is independent-contractor commission work, so it counts — but if she ever takes a W-2 role at a brokerage, that changes.

## Interaction with Stacy's own income

If Stacy earns commission income as a licensed agent, that is **Schedule C self-employment income**, and it opens a retirement vehicle the household is not currently using:

- **Solo 401(k)**: her own $24,500 deferral + $8,000 catch-up (she is 55), plus employer profit sharing up to a **$72,000 §415(c) limit — $80,000 with catch-up**. This is a *separate* limit from Ryan's employer plan.
- Her deferral limit is personal to her, not shared with Ryan's.
- **Her catch-up may be pre-tax**, unlike Ryan's. The 2026 Roth catch-up mandate keys off prior-year **FICA wages from the plan sponsor**; a sole proprietor with Schedule C earnings and no W-2 wages generally falls outside it. Confirm with the CPA — it is worth real money.
- **QBI**: real estate agents and brokers are **not** a specified service trade or business, so her commission income is eligible for the 20% §199A deduction, subject to the wage/property limits at our income level.
- An S-corp election could reduce her SE tax but also reduces the earnings base for the solo 401(k) and interacts with QBI. **Model it; don't assume it.**

→ See [[tax-mitigation-master-plan#1a. Fill the qualified plans — in this order]].

## Annual REPS checklist

- [ ] **January**: confirm the log tool is running and Stacy's baseline is set for the year
- [ ] **Quarterly**: reconcile hours to date against the 750-hour pace (~188/quarter) and re-confirm the >50% ratio
- [ ] **October**: project year-end hours with the CPA; if the 750 is at risk, there is still time to fix it
- [ ] **At filing**: confirm the §1.469-9(g) aggregation election is in place and consistent with prior years
- [ ] **At filing**: annual REPS memo with hour totals, signed off by the CPA
- [ ] **Each acquisition**: confirm the year's projected loss stays under the §461(l) cap

> [!danger] REPS is tested every single year
> It is not a status you attain once. If Stacy has a year where she works less — an illness, a family situation, a career shift — that year's rental losses revert to passive and get suspended. Plan acquisitions with that fragility in mind, and never let a year's tax outcome depend on a REPS qualification that is only marginally met.

**Related**: [[str-cost-segregation-playbook]] · [[tax-mitigation-master-plan]] · [[household-timeline]] · [[roth-conversion-window]] · [[key-figures-2026]]
