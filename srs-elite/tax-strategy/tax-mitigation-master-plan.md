---
tags: [tax, retirement, strategy, master-plan, roth, real-estate]
aliases: ["Tax Mitigation Master Plan", "Tax Plan"]
updated: 2026-08-12
---

# Tax Mitigation Master Plan — W-2 Years Through Age 65+

**Summary**: A five-phase plan to minimize lifetime (not annual) tax across the W-2 accumulation years and retirement at 65. The engine is a single arbitrage: **defer income now at ~35–45% and recognize it later at ~24% federal-only**, funded by a relocation to a no-income-tax state before retirement. Real estate — short-term rentals with cost segregation — is the one structure that converts depreciation into deductions against W-2 income while holding a full-time job. Everything else is sequencing.
**Profile**: MFJ · age 50–54 · household W-2 income $400–750K · currently in an income-tax state, relocating to a no-tax state before 65 · hard retirement at 65
**Sources**: [[key-figures-2026]] · [[retirement-tax-rules-primer]] · [[str-cost-segregation-playbook]] · [[roth-conversion-window]]
**Status**: framework for review with CPA — see [[#Open items to resolve]]

> [!warning] This is a planning framework, not tax advice
> Every number here is modeled from published 2026 figures and general rules. Nothing should be executed without your CPA signing off on your actual return position — particularly the material-participation and at-risk positions in [[str-cost-segregation-playbook]], which are the most audit-exposed part of the plan. Run this by Zach Fox before the first cost-seg year.

## The core insight

There is one number that determines whether this plan works: **the spread between the rate at which we defer income and the rate at which we recognize it.**

| | Now (working) | Later (65–75, relocated) |
|---|---|---|
| Federal marginal | 35% | 24% target |
| State marginal | applies | **0%** |
| SALT torpedo band ($505K–$606K MAGI) | +10.5 pp effective | n/a |
| NIIT on investment income | 3.8% | avoidable on ordinary income |
| **Effective marginal on deferral** | **~40–46%** | **~24–27%** |

**That spread is 15–20 points, and it is available on every dollar we can legally move from the left column to the right.** Nothing else in this plan — not asset location, not tax-loss harvesting, not charitable timing — is worth a fraction as much.

Three things make the spread unusually large for us:

1. **The relocation.** Federal law (4 U.S.C. §114) bars our current state from taxing retirement plan distributions once we establish domicile elsewhere. This is not a loophole requiring interpretation; it is a federal preemption statute. Every dollar deferred now escapes state tax **permanently**.
2. **The hard stop at 65 with RMDs at 75.** Born 1960 or later means RMD age 75. Retiring at 65 gives a **ten-year window** with no earned income and no forced distributions — the largest such window the current rules allow.
3. **The Social Security delay.** Deferring benefits to 70 both increases them 24% above the age-67 amount and keeps years 65–70 nearly income-free, making the first five conversion years the cheapest.

The plan below is essentially: *maximize what goes into the left column, engineer the emptiest possible income years in the right column, and move as much as possible across.*

## The four buckets

Everything sorts into four tax treatments. Strategy is mostly deciding what goes where.

| Bucket | Tax on growth | Tax on withdrawal | Step-up at death? | What belongs here |
|---|---|---|---|---|
| **Pre-tax** (401k, trad IRA) | none | ordinary income | **No** | Bonds, REITs, high-turnover strategies. Fill first while at 35%. |
| **Roth** (Roth IRA/401k) | none | **none** | n/a — already tax-free | **Highest-expected-return assets.** Small-cap value, emerging markets, concentrated growth. |
| **Taxable brokerage** | dividends + realized gains | LTCG/basis | **Yes** | Broad-market index ETFs. Never sell what you'll die owning. |
| **Real estate** | sheltered by depreciation | recapture, or **deferred forever** via 1031 | **Yes** (wipes recapture) | STRs for W-2 offset; MHP/RV for long-hold cashflow. |

**The two rules that fall out of this table:**

- **Pre-tax gets no step-up → convert it.** Taxable and real estate get a step-up → hold them to death. This resolves the apparent tension between "convert aggressively" and "let investments grow untouched": convert the IRA, never touch the brokerage.
- **Roth is where growth belongs.** A dollar of growth in a Roth is worth ~1.3× the same dollar in pre-tax. Put the assets with the widest return distribution there — the tax-free treatment is most valuable exactly where the outcome is most uncertain.

## Phase map

Ages are primary; calendar years assume born 1974 — **adjust ±2 years for actual birth year.**

| Phase | Age | Years | Mission |
|---|---|---|---|
| **1 — Accumulate & Defer** | 52–59 | 2026–2033 | Max every deferral. Build the STR engine. Start the Roth clock. |
| **2 — Position** | 60–64 | 2034–2038 | Super catch-up. Relocate and document domicile. Fund the conversion-tax reserve. Clean up IRAs. |
| **3 — The Golden Window** | 65–70 | 2039–2044 | Retire. Medicare + SSA-44. Delay SS. **Largest conversions.** |
| **4 — Taper** | 70–75 | 2044–2049 | SS turns on. QCDs from 70½. Final conversions before RMDs. |
| **5 — RMD Era** | 75+ | 2049+ | RMDs, QCDs, Roth as the flexible bucket, step-up preservation. |

---

## Phase 1 — Accumulate & Defer (age 52–59)

**Mission: get the maximum number of dollars into the pre-tax and Roth buckets at a 40%+ effective deduction rate, and stand up the real estate engine.**

### 1a. Fill the qualified plans — in this order

| Priority | Vehicle | Amount (2026, per person) | Why here |
|---|---|---|---|
| 1 | 401(k) elective deferral, **pre-tax** | $24,500 | Deducted at 35% + state. Highest-value dollar available. |
| 2 | Employer match / profit sharing | plan-dependent | Free money; counts toward the $72,000 §415(c) limit. |
| 3 | **HSA, family, invested not spent** | $8,750 (+$1,000 each at 55) | The only triple-tax-free account. See 1b. |
| 4 | 401(k) catch-up — **must be Roth** | $8,000 | See note below. |
| 5 | **Backdoor Roth IRA**, each spouse | $8,600 | $17,200/yr of Roth space at any income. |
| 6 | **Mega backdoor Roth** — after-tax 401(k) + in-plan conversion | up to the §415(c) gap | The largest Roth channel available. Plan-dependent. |
| 7 | Taxable brokerage | remainder | Step-up eligible; funds Phase 3 conversion taxes. |

**On the Roth catch-up mandate**: from 2026, because prior-year wages exceed $150,000, catch-up contributions *must* be Roth. This reads like a tax increase and is actually a gift — it adds **$8,000 per person of Roth space that does not consume the pre-tax limit**. Roth at a 35% marginal rate is normally a bad trade; being forced into it at the margin, on top of a full pre-tax deferral, is not. **The one real risk: if the plan does not offer a Roth option, the catch-up is forfeited entirely.** Confirm the plan supports Roth catch-up — this is a same-week task, not a someday task.

**On the mega backdoor Roth**: this is the highest-leverage unknown in Phase 1. If the plan allows after-tax contributions *and* in-plan Roth conversion (or in-service withdrawal), the annual ceiling is $80,000 per person minus deferrals minus employer contributions — potentially $30–40K/yr of additional Roth funding. Over eight years that is a materially different retirement. **Get the plan document and confirm both features.**

### 1b. Treat the HSA as a retirement account, not a health account

Pay current medical costs out of pocket. Invest the HSA fully in equities. Keep every receipt indefinitely — there is no deadline on reimbursement, so a documented $200K of unreimbursed expenses becomes a tax-free withdrawal at any point in the future.

Two constraints: HSA contributions must **stop 6 months before Medicare enrollment**, and a handful of states tax HSA contributions at the state level (confirm for the current state, irrelevant after relocating).

### 1c. Clear the pro-rata problem now, not later

Backdoor Roth contributions are only clean if there is **no pre-tax balance in any traditional, SEP, or SIMPLE IRA** as of December 31 — the pro-rata rule under §408(d)(2) aggregates them all and makes each conversion partly taxable.

→ **Roll any existing traditional/SEP IRA balances into the current 401(k)** before doing backdoor contributions. Do this first, in that order. It is a one-time cleanup that unlocks $17,200/yr of Roth space for the rest of the working years.

### 1d. Start the five-year Roth clock — this week

If either spouse lacks a Roth IRA opened 5+ tax years ago, open and fund one now. Cost: essentially nothing. Value: removes a five-year constraint from every future decision. See [[retirement-tax-rules-primer#2. Roth withdrawals are tax-free if requirements are met|the two five-year clocks]].

### 1e. Stand up the real estate engine

This is the only lever in Phase 1 that creates deductions *beyond* the qualified-plan limits, and the only one that can offset W-2 income directly. It is complex enough to warrant its own note: **[[str-cost-segregation-playbook]]**.

The one-paragraph version: long-term rentals produce **passive** losses that we cannot use — the $25,000 special allowance is fully phased out above $150K MAGI, and Real Estate Professional Status is unavailable to a full-time W-2 earner. **Short-term rentals with an average stay of 7 days or less are not "rental activities" under the §469 regulations at all**, so with material participation their losses are **non-passive and offset W-2 income**. Combine that with cost segregation and 100% permanent bonus depreciation and a single acquisition can generate a six-figure first-year deduction against ordinary income at a 40%+ effective rate.

Two hard constraints to internalize now:
- **Self-manage.** The easiest material participation test is 100 hours *and more than any other individual*. Hiring a full-time property manager who works more hours than you **fails** it. Your stated intent to run STR management yourself is exactly what makes this work — it is a requirement, not a preference.
- **Keep contemporaneous time logs.** The IRS wins most material-participation cases on recordkeeping alone. A reconstructed log created after an audit notice is worth close to nothing.

### 1f. Aim deductions at the SALT torpedo

Between **$505,000 and ~$606,000 MAGI**, each extra dollar of income also destroys 30¢ of SALT deduction — a **45.5% true marginal rate** in the 35% bracket. A cost-seg loss that pulls MAGI from $600K down to $505K is worth ~45.5¢ per dollar, not 35¢.

→ **Sequence acquisitions so that cost-seg deductions land in the years with the highest MAGI**, and target the top of that band first. If the state has a **pass-through entity tax (PTET)** election available and we hold business income in an LLC or S-corp, that election bypasses the SALT cap entirely — check whether the current state offers one.

### 1g. Asset location — free return, no risk

| Account | Holds |
|---|---|
| Pre-tax 401(k)/IRA | Bonds, TIPS, REITs, high-turnover or high-yield strategies |
| **Roth** | **Highest-expected-return equities** — small-cap value, emerging markets, concentrated growth |
| Taxable | Broad-market index ETFs (low turnover, qualified dividends), municipal bonds while in a tax state |

Also in taxable: **direct indexing or systematic tax-loss harvesting**, to bank capital losses. Losses carry forward indefinitely with no expiration and become genuinely valuable in Phase 3 — they can absorb depreciation recapture on a property sale or offset gains realized to fund conversion taxes.

### 1h. Charitable timing — front-load into the high-income years

OBBBA introduced a **0.5%-of-AGI floor** on itemized charitable deductions and a **35¢-per-dollar cap** on itemized deduction value in the 37% bracket, both starting 2026. Combined with the fact that QCDs become available at 70½ and are strictly better, the conclusion is clean:

→ **Do all lump-sum charitable giving in the working years, via a donor-advised fund, funded with appreciated stock** (avoids the capital gain *and* generates the deduction). Bunch multiple years into a single high-MAGI year. **The final working year is the single best year to fund a DAF.** After 70½, all giving switches to QCDs.

### 1i. If there are children

- **Hire them in the real estate business** at a defensible wage for real work. Deductible to the business; their standard deduction shelters it; the earned income makes them eligible for a Roth IRA with a 50+ year runway.
- **529 → Roth IRA rollover** (SECURE 2.0): $35,000 lifetime, requires a 15-year-old account. Open 529s early even if underfunded, purely to start that clock.
- **"Trump accounts"** (OBBBA, from July 2026): $5,000/yr for children under 18, with a $1,000 federal seed for children born 2025–2028. Low priority, but free money if eligible.

---

## Phase 2 — Position (age 60–64)

**Mission: everything that must be true *before* retirement, done in the right order. This phase has the most irreversible steps and the least margin for error.**

### 2a. The relocation — the highest-value action in the plan

Do not treat this as a lifestyle decision with a tax side effect. It is worth more than every other item in this plan combined, and it must be **complete and defensible before the first conversion year.**

**What §114 protects** once domicile changes: 401(k) and IRA distributions, Roth conversions, and qualified plan income cannot be taxed by the former state, regardless of where earned.

**What it does not protect** — still taxable by the source state:
- Rental income and gain on real property physically located there → **another reason to buy investment real estate in no-tax states**, which the [[mhp-rv-investment-strategy]] Tier A targeting (TX, FL, TN, NV, AZ, SC, NC, GA, AL, ID, UT) already does
- **Non-qualified deferred comp, unless paid in substantially equal periodic payments over 10+ years** → if any NQDC exists, **elect a 10+ year payout schedule now**, while the election is still available. A lump sum or 5-year payout is taxable by the old state; a 10-year stream is not. This election window closes and does not reopen.
- Equity compensation attributable to services performed there
- Partnership or business income sourced there

**Domicile is a facts-and-circumstances test, and high-tax states audit it aggressively.** Build the record deliberately: sell or genuinely rent out the old residence, change driver's licenses and vehicle registrations, register to vote and actually vote, move primary physicians and dentists, move banking and safe deposit boxes, update estate documents to the new state's law, shift club and church memberships, and **keep a day-count log**. Where day counts are close, contemporaneous evidence wins and reconstruction loses.

### 2b. Super catch-up, ages 60–63

The catch-up limit rises to **$11,250** for ages 60, 61, 62, and 63 — then drops back to the standard catch-up at 64. Four years only. Take all of it. (Still Roth, per the mandate.)

### 2c. Fund the conversion-tax reserve

Phase 3 requires paying roughly **$85K/year all-in** (federal tax plus IRMAA surcharge) on conversions, from **outside** the IRA, for ten years — call it **$850K–$950K of taxable-account liquidity** in today's dollars, with a buffer. Materially more if we take the fast lane.

Two requirements on that money:
- **Low embedded capital gains**, so raising cash doesn't itself create a taxable event competing for bracket space. Direct the last few years of taxable savings into this reserve deliberately rather than letting it accumulate in highly appreciated positions.
- Held in cash/short bonds for the first 2–3 years of need; the remainder can stay invested.

**Do not fund conversion taxes by withholding from the conversion.** That shrinks what lands in the Roth, which is the entire objective.

### 2d. Consolidate for the QCD window

QCDs can only be made from **IRAs, not 401(k)s**. Before 70½, roll 401(k) balances to a traditional IRA. Sequence matters: do this **after** the backdoor-Roth years end, or the pro-rata problem from 1c returns.

### 2e. Rule of 55 — know it exists

Separating from service in or after the year you turn 55 allows penalty-free withdrawals from **that employer's** 401(k) — not from an IRA. Probably unused given retirement at 65, but it is the escape hatch if retirement comes early.

### 2f. Pre-retirement housekeeping

- Confirm Medicare enrollment timing; **stop HSA contributions 6 months prior**
- Harvest remaining capital losses while there is ordinary income to absorb $3,000/yr of them
- Fund the DAF in the final working year (see 1h)
- Update estate documents to the new state; confirm beneficiary designations name individuals, not the estate, on every retirement account
- Model the first-year Medicare/IRMAA hit and prepare **Form SSA-44**

---

## Phase 3 — The Golden Window (age 65–70)

**Mission: the emptiest income years we will ever have. Convert aggressively.**

Detailed mechanics, sizing math, and the IRMAA-vs-bracket tradeoff live in **[[roth-conversion-window]]**. The summary:

1. **Retire at 65 → straight to Medicare.** No ACA bridge needed, no subsidy cliff to manage.
2. **File Form SSA-44 immediately** — "work stoppage" is a qualifying life-changing event, letting SSA price premiums off a current-year estimate rather than the final W-2 years.
3. **Delay Social Security to 70.** Benefits grow ~8%/yr past FRA, reaching 124% of PIA — an inflation-adjusted, longevity-hedged, government-backed return that is unavailable anywhere else. It also keeps ages 65–70 nearly income-free, which is what makes the first five conversion years the cheapest.
4. **Live off the taxable account** — return of basis plus dividends, minimal recognized income.
5. **Convert traditional → Roth up to the IRMAA tier boundary just below the top of the 24% bracket.** In 2026 terms that is **$410,000 of MAGI**, not the $435,750 that fills the 24% bracket. See [[roth-conversion-window#Why we stop at the IRMAA boundary, not the bracket top]] — the last $25,750 of conversion carries a 37.5% marginal cost once the IRMAA cliff is included, which defeats the purpose.
6. **Convert in-kind, and convert into weakness.** Moving shares rather than cash during a drawdown transfers more shares for the same tax. A 20% market decline is a 20%-off sale on Roth conversions — pre-decide this so it gets executed rather than debated.
7. **Convert the highest-growth assets first** — whatever ends up in the Roth compounds tax-free forever.

**One pairing worth planning for**: selling a long-term rental or MHP in a fully taxable disposition **releases its suspended passive losses against any income, including non-passive income** (§469(g)). Pairing a disposition with a large conversion year lets those otherwise-stranded losses absorb conversion income. See [[str-cost-segregation-playbook#Suspended passive losses are not lost]].

---

## Phase 4 — Taper (age 70–75)

**Mission: Social Security turns on, conversion room shrinks, QCDs begin. Finish the job before RMDs.**

- **Age 70: claim Social Security** at 124% of PIA. Assume 85% taxable and stop optimizing it.
- **Age 70½: QCDs become available** — $111,000 per person in 2026 terms, $222,000 for the couple. **From here, all charitable giving is QCDs.** Excluded from AGI entirely, which means they also reduce IRMAA MAGI and NIIT exposure — strictly better than a deduction.
- **Recalculate conversion room annually.** Social Security consumes bracket space that conversions used to occupy. Room shrinks each year; keep converting to the same IRMAA boundary, just with less headroom.
- **Age 74–75: final conversions.** These are the last years before RMDs make distributions mandatory. Note the two-year IRMAA lag means these conversions set premiums at ages 76–77, after the program ends.

## Phase 5 — RMD Era (age 75+)

**Mission: the traditional balance should now be small enough that RMDs are a non-event. Preserve step-up.**

- **RMDs begin at 75.** If the conversion program worked, the remaining pre-tax balance is modest and the RMD fits inside low brackets.
- **Satisfy RMDs with QCDs** to the extent of charitable intent.
- **Withdrawal order**: RMDs first (mandatory), then taxable dividends/interest, then Roth last. Roth is the flexibility instrument — use it in years where an extra dollar of ordinary income would cross an IRMAA cliff.
- **Preserve step-up.** Do not sell appreciated taxable securities or real estate. Spend from Roth and cash instead. Every appreciated asset held to death passes with a clean basis — and for real estate, **the step-up erases all accumulated depreciation recapture**, which is what makes the cost-seg strategy in Phase 1 a permanent benefit rather than a deferral.
- **Estate**: at a $30M MFJ exemption, estate tax is likely not the constraint. The binding issue is income tax on heirs — which is exactly what the Roth conversions solved, since inherited Roths are drained over 10 years **tax-free**.

---

## Annual operating cadence

| When | Do |
|---|---|
| **January** | Fund backdoor Roths for both spouses. Set payroll deferrals to max out over the year. |
| **Ongoing** | Log real estate participation hours contemporaneously. Non-negotiable. |
| **June** | Mid-year MAGI projection. Check position vs. the SALT torpedo band and IRMAA boundaries. |
| **October** | Tax projection with CPA. Size the year's conversion or cost-seg target. Decide on acquisitions needing to close by 12/31. |
| **November** | **Refresh [[key-figures-2026]]** with next year's IRS and CMS figures. |
| **December** | Execute conversions (hard 12/31 deadline, no do-overs). Harvest losses. Fund DAF. Confirm any property placed in service by 12/31. |

---

## What can break this

| Risk | Severity | Mitigation |
|---|---|---|
| **Material participation disallowed on STRs** | High — retroactive reclassification to passive, losses suspended, interest and penalties | Contemporaneous logs. Self-manage. Never let a manager out-hour you. Document the ≤7-day average stay. |
| **Residency audit by the former state** | High — could tax the entire conversion program | Build the domicile record deliberately in Phase 2. Day-count log. Don't keep the old house available. |
| **At-risk limits (§465) on seller-financed deals** | High — kills year-1 losses entirely | Seller financing is **not** qualified nonrecourse financing. Make seller notes recourse/personally guaranteed. See [[str-cost-segregation-playbook#2. At-risk — §465]] — this is the caveat already flagged in [[mhp-rv-investment-strategy]]. |
| **§461(l) excess business loss cap** | Medium — $512,000 MFJ in 2026, and it *dropped* from $626,000 | Excess becomes an NOL carryforward, not a permanent loss. Spread large cost-seg years rather than stacking them. |
| **Mega backdoor Roth unavailable in the plan** | Medium — removes the largest Roth channel | Confirm plan features now. If absent, more goes to taxable and Phase 3 conversions carry more weight. |
| **Legislative change** | Medium | Bonus depreciation and the STR treatment are the exposed items. Both are current law with no sunset, but the plan should not depend on a single year's rules. |
| **Depreciation recapture on a forced sale** | Medium | 1031 exchange, or hold to death for step-up. Bank capital losses in Phase 1 as a buffer. |
| **Market decline early in Phase 3** | Low — actually favorable | Convert in-kind into weakness. Hold 2–3 years of spending in cash so conversions are never forced from depressed assets. |

---

## Open items to resolve

These change the numbers materially. Ordered by leverage.

1. **Does either spouse work part-time or not at all?** If one spouse can meet **Real Estate Professional Status** (750+ hours in real property trades *and* more than half of their total personal service time), then **all** rental losses — including long-term rentals and MHP/RV parks — become non-passive on the joint return and offset W-2 income. REPS is tested per spouse, but the benefit flows to the joint return. This is by far the largest single unresolved lever and would substantially change the real estate strategy in [[str-cost-segregation-playbook]].
2. **Does the 401(k) plan allow after-tax contributions plus in-plan Roth conversion?** Determines whether the mega backdoor Roth is available. Get the plan document.
3. **Does the plan offer Roth catch-up?** If not, $8,000/person/year of catch-up is forfeited outright from 2026.
4. **Any existing traditional/SEP/SIMPLE IRA balances?** Determines whether backdoor Roth is clean or needs the 1c cleanup first.
5. **Any non-qualified deferred compensation?** If yes, the payout election must be 10+ years to escape former-state tax under §114. Time-sensitive.
6. **Exact birth year** — confirms RMD age 75 and pins every calendar year in the phase map.
7. **Current state, and target state and move year.** Determines PTET availability, HSA state treatment, audit-aggressiveness, and when the conversion window can open.
8. **Current balances by bucket** (pre-tax / Roth / taxable / HSA / real estate equity) — needed to size the actual conversion ladder in [[roth-conversion-window]] rather than reason from ratios.
9. **Charitable intent, annual and lifetime.** Determines whether DAF bunching in Phase 1 and the QCD program in Phase 4 are worth building around.

**Related**: [[roth-conversion-window]] · [[str-cost-segregation-playbook]] · [[key-figures-2026]] · [[retirement-tax-rules-primer]] · [[mhp-rv-investment-strategy]]
