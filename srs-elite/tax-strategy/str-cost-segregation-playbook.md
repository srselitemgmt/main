---
tags: [tax, real-estate, str, cost-segregation, passive-losses, depreciation]
aliases: ["STR Playbook", "Cost Segregation Playbook", "STR Loophole"]
updated: 2026-08-13
---

# STR + Cost Segregation Playbook — Offsetting W-2 Income With Real Estate

**Summary**: Cost segregation plus permanent 100% bonus depreciation turns a single acquisition into a $250–350K first-year deduction against ordinary income at a 35–45% effective rate. Getting that deduction past §469 requires one of two doors, and **we have both**: [[reps-real-estate-professional-status|Stacy's Real Estate Professional Status]] opens *every* rental — long-term rentals and MHP lot rent included — and the short-term rental exception covers anything with ≤7-day average stays independently. With REPS live, §469 stops being the binding constraint and **§461(l)'s $512,000 excess business loss cap becomes the real ceiling**. The strategy rests on **contemporaneous time logs** and **recourse-structured seller debt**.
**Sources**: IRC §469, §465, §461(l), §280A, §168 · Temp. Reg. §1.469-1T(e)(3)(ii)(A), §1.469-5T(a) · OBBBA (P.L. 119-21)
**Related**: [[tax-mitigation-master-plan]] · [[mhp-rv-investment-strategy]] · [[key-figures-2026]]

> [!warning] The most audit-exposed part of the plan
> Material participation and at-risk positions are decided on facts and documentation, not on strategy. **The IRS wins most material-participation cases on recordkeeping alone.** Everything here needs CPA sign-off before the first cost-seg year. Nothing in this note is a substitute for a proper cost segregation study by a qualified firm.

## The §469 problem, and our two doors through it

Under §469(c)(2), **rental activity is passive per se** — regardless of how much work you do. Passive losses can only offset passive income; the excess is suspended indefinitely. There are three ways out:

| Exit | Requirement | Available to us? |
|---|---|---|
| **§469(i) special allowance** | Up to $25,000 of rental losses, phased out $100K–$150K MAGI | ❌ **No** — we are far above $150K |
| **Real Estate Professional Status** | One spouse alone: 750+ hours in real property trades **and** more than half of *all* their personal service time | ✅ **Yes — Stacy qualifies.** Opens **every** rental |
| **STR exception** | Average period of customer use ≤ 7 days + material participation | ✅ Yes — independent of REPS, covers non-rental activities |

**REPS is the bigger door and should be the primary position.** Stacy works full-time in real estate — seller leads, acquisitions, tenant management — which satisfies both §469(c)(7)(B) tests on her own hours. That makes **all** rental losses non-passive on the joint return, including the long-term rentals and MHP lot rent that the STR exception can never reach. Full mechanics, the mandatory second step, and the documentation requirements are in **[[reps-real-estate-professional-status]]**.

**The STR exception still matters** for two reasons: STRs are *not* rental activities, so they sit outside the §1.469-9(g) rental aggregation and are tested on their own; and it is the fallback if REPS ever fails in a given year. REPS is re-tested annually — a year where Stacy works less is a year the long-term rental losses go back to being suspended, while ≤7-day STRs keep working regardless. **Holding both positions is genuine redundancy, not duplication.**

> [!important] What changes now that REPS is live
> §469 is no longer what limits us. **§461(l)'s $512,000 excess business loss cap is** — see [[#4. Excess business loss — §461(l)]]. The acquisition calendar should be sized to that number, not to what §469 will let through.

## The STR exception, precisely

Temp. Reg. **§1.469-1T(e)(3)(ii)(A)** excludes from the definition of "rental activity" any activity where **the average period of customer use is 7 days or less**. Not being a rental activity, it escapes the per-se passive rule of §469(c)(2) entirely — and is then tested as an ordinary trade or business, where **material participation makes it non-passive**.

A related exception at **§1.469-1T(e)(3)(ii)(B)** covers average stays of **30 days or less where significant personal services are provided**. The 7-day test is cleaner and easier to defend; **target it.**

**Average period of customer use = total rental days ÷ number of bookings.** Computed per property, per year.

→ **Operational consequence**: cap booking length. A single 30-day winter booking can drag the annual average above 7 days and silently reclassify the entire property as passive for that year. **Set a maximum stay length in the platform settings** and reconcile the average quarterly, not at year-end.

### Material participation — the tests that matter

Temp. Reg. §1.469-5T(a) lists seven tests. Three are realistic here:

| Test | Standard | Notes |
|---|---|---|
| **#3** | **100+ hours, and not less than any other individual** | **The workhorse.** Note the reg says *not less than* — tying is sufficient. |
| **#1** | 500+ hours in the activity | Safest, no comparison to anyone else needed |
| **#2** | Substantially all of the participation in the activity | Works for a genuinely self-managed single property |

Two provisions that help:
- **§469(h)(5): a spouse's participation counts as the taxpayer's.** Hours are aggregated across spouses whether or not they file jointly. This makes the 100-hour test very achievable.
- **Reg. §1.469-4 grouping election**: multiple STRs can be grouped as a single activity, aggregating hours across properties. File the election; it is generally binding once made. **Do not group STRs with long-term rentals** — mixing non-rental and rental activities is only permitted in narrow circumstances and risks the whole position.

### The property manager trap

Test #3 compares your hours to **any other individual** — including a paid property manager, a cleaner, and a co-host. If a full-service manager logs 150 hours and you log 120, **you fail**, and every dollar of loss becomes suspended.

→ **On the STR group, self-managing remains a requirement, not a preference** — the ≤7-day properties sit outside the rental aggregation and have to clear material participation on their own. If you hire help there, structure it as **task-specific vendors** (a cleaner per turnover, a handyman per call) rather than a manager with a broad ongoing role, and **track their hours too** so you can prove you exceeded each of them.

> [!tip] REPS relaxes this for the long-term rentals
> On the aggregated rental activity, Stacy and Ryan's hours combine under §469(h)(5) against the **500-hour test**, where no comparison to any other individual is required. That means **third-party property management is survivable on the long-term rentals and parks** in a way it is not on the STRs — useful as the portfolio scales past what two people can personally run.

### Time logs — the thing that actually decides audits

Hours that count: guest communication, booking management, pricing, cleaning and turnovers, maintenance and repairs, supply runs, listing photography and copy, reviewing and responding to reviews, property setup and furnishing, dealing with vendors.

Hours that **do not** count: "investor activities" — reviewing financial statements, studying market reports, monitoring performance in a non-managerial capacity (Reg. §1.469-5T(f)(2)(ii)). Travel time is contested; log it separately so it can be removed without collapsing the total.

**Log requirements:**
- **Contemporaneous** — created as the work happens. A log reconstructed after an audit letter is worth close to nothing, and courts have said so repeatedly.
- Date, hours, description specific enough to be verifiable, and who performed the work
- Corroborate wherever possible: platform message timestamps, calendar entries, receipts, mileage, vendor invoices
- **Log the vendors' and cleaners' hours too** — you need the comparison for test #3

Use a dedicated app or a single spreadsheet, updated weekly. This is the cheapest insurance in the plan.

## Cost segregation

A cost segregation study reallocates the purchase price from the 39-year building shell into shorter-lived components that qualify for **100% bonus depreciation** — which OBBBA made **permanent** for property acquired after **January 19, 2025**.

| Component | Life | Bonus eligible? | Examples |
|---|---|---|---|
| Land | — | No | Never depreciable |
| **Personal property** | **5 yr** | ✅ | Furniture, appliances, carpet, window treatments, decorative lighting, cabinetry |
| **Land improvements** | **15 yr** | ✅ | Driveway, walkways, landscaping, fencing, pool, exterior lighting, site utilities |
| **Qualified Improvement Property** | **15 yr** | ✅ | Interior non-structural improvements to **nonresidential** buildings |
| Building shell | 39 yr | ❌ | Structure, roof, HVAC, plumbing, electrical core |

Bonus depreciation applies to property with a recovery period of **20 years or less** — so the 5- and 15-year buckets qualify in full, and the shell does not.

### 39-year, not 27.5-year — and that's an advantage

A property is "residential rental property" (27.5-year) only if it is **not** used on a transient basis. An STR with average stays under 30 days is generally **nonresidential real property — 39-year**. Practitioners vary on this; confirm the position with the CPA.

The upside: **QIP is only available for nonresidential property.** Being classified 39-year means interior renovations can be treated as 15-year QIP with 100% bonus, which residential rental property cannot do. For a renovation-heavy STR strategy this more than offsets the slower shell depreciation.

### Worked example — illustrative

A $1.2M STR, placed in service in June, furnished:

| | |
|---|---|
| Purchase price | $1,200,000 |
| Less land (20%) | ($240,000) |
| Depreciable building basis | $960,000 |
| Plus furnishings purchased separately | $80,000 |
| **Total depreciable basis** | **$1,040,000** |

Cost seg study allocation:

| Bucket | Amount | Year 1 deduction |
|---|---|---|
| 5-year personal property (18%) | $190,000 | **$190,000** (100% bonus) |
| 15-year land improvements (13%) | $130,000 | **$130,000** (100% bonus) |
| 39-year shell (69%) | $720,000 | $10,000 (mid-month convention, June) |
| **Total year-1 depreciation** | | **$330,000** |

Net rental income before depreciation: ~$45,000 → **net non-passive loss of ~$285,000**, deductible against W-2 income.

**Value of that deduction** depends on where it lands relative to the SALT phase-down. Pulling MAGI from ~$600K down to ~$315K passes straight through the **SALT torpedo band ($505K–$606K), where the true marginal rate is 45.5%**, then through 35% and 32%:

→ **roughly $105,000–$120,000 of federal tax saved in year one**, plus state tax saved while still resident in a tax state.

**Sequence acquisitions so the deduction lands on the highest-MAGI years first**, and aim the first slice at the torpedo band. See [[tax-mitigation-master-plan#1f. Aim deductions at the SALT torpedo]].

## The four limitations that can neutralize all of this

Losses have to clear **four separate gates, in order**. Any one of them can zero out the benefit.

### 1. Basis
Losses cannot exceed your basis in the activity.

### 2. At-risk — §465

This is the one that kills seller-financed deals, and it is the caveat already flagged in [[mhp-rv-investment-strategy]].

You are at risk for cash contributed, **recourse** debt you're personally liable for, and **qualified nonrecourse financing**. But qualified nonrecourse financing must come from a **"qualified person"** — and under §49(a)(1)(D)(iv), incorporated by §465(b)(6)(D), **the seller of the property is expressly excluded.**

→ **Nonrecourse seller carry-back financing does not create at-risk basis.** On a deal with 15% down and 85% seller carry, year-1 deductible losses are capped near the cash invested — the six-figure cost-seg loss simply does not land.

**The fix**: make the seller note **recourse — personally guaranteed.** Recourse debt is at-risk debt regardless of who the lender is. This is a negotiating point to raise at LOI stage, not at closing, and it is cheap to ask for: most mom-and-pop sellers care about the payment stream and the price, not the recourse label.

**Subject-to deals are murkier** — the loan stays in the seller's name, so whether the buyer is treated as having the debt at all is fact-dependent. Flag every sub-to deal for CPA review **before** counting on year-1 losses.

### 3. Passive activity loss — §469
Cleared two ways: **[[reps-real-estate-professional-status|Stacy's REPS]] + the §1.469-9(g) aggregation election** for all rentals, and the **STR exception + material participation** for ≤7-day properties. Re-tested every year.

### 4. Excess business loss — §461(l)

**This is now our binding constraint.** With §469 cleared by REPS, nothing stops the losses until here.

Net business losses above **$512,000 (MFJ, 2026)** cannot offset non-business income in the current year; the excess becomes an **NOL carryforward** (usable against 80% of future taxable income).

Note this threshold **dropped** from $626,000 in 2025 — OBBBA made the limitation permanent and reverted the thresholds to their original TCJA levels.

→ **Size the acquisition calendar to $512,000 of net loss per year** — roughly **$1.7–2.0M of purchase price annually** at typical reclass rates, depending on furnishing and land allocation. Stacking three large acquisitions into one year doesn't produce a bigger deduction; it pushes the excess into a carryforward and wastes the 45.5% SALT-torpedo rate available this year. **Spreading acquisitions across years is now a tax decision, not just a capital one.**

## Other rules that bind

### §280A personal use
If personal use of the dwelling exceeds **14 days or 10% of rental days**, deductions are limited to rental income — **no loss allowed.** For a cost-seg property, target **zero personal use**.

Days spent **substantially full-time on repairs and maintenance do not count as personal use** — but document them properly. Renting to family below market rate **is** personal use.

### Self-employment tax
Rental income is excluded from SE tax under §1402(a)(1) unless services are substantial enough to make it hotel-like. Cleaning between guests and providing linens is generally fine; **daily maid service, meals, and tours are not.**

**Important clarification**: material participation for §469 does **not** create SE tax exposure. They are different code sections with different tests, and they are routinely confused. You can materially participate for loss purposes without converting rental income into self-employment income.

### QBI — §199A
A rental trade or business can qualify for the 20% QBI deduction (safe harbor: Rev. Proc. 2019-38, 250+ hours). In loss years this works against you — negative QBI carries forward and reduces future QBI deductions. Minor, but the CPA should track it.

### Recapture on sale
Cost segregation is a **deferral**, not forgiveness — unless you never sell:

| On sale | Rate |
|---|---|
| §1245 recapture on 5- and 15-year property | **Ordinary income**, up to 37% |
| §1250 unrecaptured gain on the shell | **25%** |
| Remaining gain | 15–20% + 3.8% NIIT |

Recapture at ordinary rates can exceed the 35% at which the deduction was originally taken if rates rise or the sale lands in a high-income year.

**Two clean exits:**
- **§1031 exchange** — defers everything into the replacement property. STRs qualify as business/investment property.
- **Die owning it** — the basis step-up **eliminates all accumulated depreciation recapture permanently.** This is what turns the deferral into a genuine permanent benefit, and it's why [[tax-mitigation-master-plan#Phase 6 — RMD Era (2051+)]] says preserve step-up rather than sell.

**Rule: 1031 until death.** Plan acquisitions as permanent holds.

## Suspended passive losses from pre-REPS years

Any losses suspended before REPS was in place — or in a year REPS fails — are not lost. Three ways they pay off:

1. **Offset passive income** from other properties as the portfolio matures
2. **Release on full disposition** — §469(g): a fully taxable disposition of the entire interest releases *all* suspended losses from that activity against **any** income, including non-passive
3. **The $25,000 allowance returns** if MAGI ever drops below $150,000 — unlikely at our income

> [!warning] The aggregation election interacts with point 2
> Once the §1.469-9(g) election groups all rentals into one activity, selling a single property is no longer a disposition of "the activity," so it does **not** release that property's suspended losses. If there is a meaningful bank of pre-REPS suspended losses, **sequence the election and any planned disposition with the CPA** — see [[reps-real-estate-professional-status#The trade-off in the aggregation election]].

## Connecting to the MHP/RV strategy

The existing [[mhp-rv-investment-strategy]] targets mom-and-pop MHP and RV parks on seller terms. **Stacy's REPS changes the conclusion here — MHP parks are now viable during the working years, not just after retirement.**

**1. MHP lot rent is a long-term rental — and REPS is the only thing that reaches it.** Cost segregation on a park is *excellent*: roads, pads, site utilities, and utility infrastructure are largely **15-year land improvements** eligible for 100% bonus depreciation, which makes parks one of the most cost-seg-favorable asset classes in existence. The STR exception can never reach lot rent. **REPS can** — which means park losses now offset Ryan's W-2 income currently.

**2. RV parks qualify under both doors.** An RV park renting sites nightly and weekly has an **average period of customer use well under 7 days**, putting it inside the §1.469-1T(e)(3)(ii)(A) exception independently of REPS. That redundancy is worth something: an RV park keeps working in a year Stacy's REPS fails.

Revised acquisition priority:

| Asset | Cost seg quality | Loss usable against W-2? |
|---|---|---|
| **MHP, lot rent only** | **Excellent (15-yr heavy)** | ✅ **Yes — via REPS** (was ❌ before) |
| **RV park, transient sites** | **Excellent (15-yr heavy)** | ✅ **Yes — via REPS *or* STR exception** |
| Residential STR | Very good | ✅ Yes — via either door |
| Long-term residential rental | Moderate | ✅ Yes — via REPS |

→ **The "wait until retirement for MHPs" constraint is gone.** Buy the best deal on its own merits; the tax treatment no longer discriminates between asset types. Two residual preferences: **RV parks carry door redundancy** (REPS-independent), and **transient RV sites are more likely to trigger SE tax** if substantial services are provided — model that, don't ignore it.

The practical rule for terms deals is now: **cost-seg study + recourse-guaranteed seller note + Stacy's REPS documented + annual loss under $512K = a six-figure W-2 offset. Nonrecourse seller carry = no year-one benefit at all**, regardless of REPS.

## State selection

Real property income and gain are **always taxable by the state where the property sits** — 4 U.S.C. §114's protection for retirement income does not extend to real estate. A property in a high-tax state creates a permanent filing obligation and a permanent tax leak, even after we relocate.

→ **Buy only in no-income-tax or low-tax states.** The existing Tier A targeting (**TX, FL, TN, NV** — no income tax; **NC, SC, GA, AZ, AL, ID, UT** — low) already does this correctly. Keep it that way, and treat "would I want to file a return in this state for 30 years?" as a screening criterion alongside the underwriting.

## Pre-acquisition checklist

**Every acquisition:**
- [ ] Property in a no-tax or low-tax state
- [ ] Which door is this property using — **REPS** (rental, in the aggregation) or the **STR exception** (≤7-day, standalone)? Decide before closing, not at filing
- [ ] Time log started **on day one**, tracking Stacy's hours, Ryan's hours, and every vendor's hours
- [ ] Cost segregation study engaged with a qualified firm **before** filing, ideally before closing
- [ ] Seller financing, if any, is **recourse / personally guaranteed** (§465)
- [ ] Projected loss keeps total business losses under the **§461(l) $512K cap** for the year
- [ ] **Placed in service by 12/31** — this is what controls the deduction year, not the closing date
- [ ] Exit assumed to be **1031 or death**, never a plain taxable sale
- [ ] CPA has reviewed the material participation and at-risk positions **in writing**

**Additionally, if it's going through the STR door:**
- [ ] Booking policy caps stay length → annual average **≤ 7 days**, verified quarterly
- [ ] **We self-manage** — no manager who could out-hour us; vendors are task-specific
- [ ] Personal use planned at **zero** (§280A)
- [ ] Services kept below "hotel-like" to avoid SE tax

**Additionally, if it's going through the REPS door:**
- [ ] Included in the **§1.469-9(g) aggregation election**, consistent with prior years
- [ ] Stacy's year-to-date hours on pace for 750 and the >50% ratio — see [[reps-real-estate-professional-status#Annual REPS checklist]]

**Related**: [[reps-real-estate-professional-status]] · [[tax-mitigation-master-plan]] · [[roth-conversion-window]] · [[household-timeline]] · [[key-figures-2026]] · [[mhp-rv-investment-strategy]]
