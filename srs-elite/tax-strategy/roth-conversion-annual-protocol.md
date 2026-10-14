---
tags: [tax, roth, conversions, protocol, annual]
aliases: ["Conversion Protocol", "Annual Roth Decision", "How much to convert"]
updated: 2026-10-14
---

# Annual Roth Conversion Protocol — How Much to Convert, Every Year

**Summary**: The [[roth-conversion-window]] note says *when* the cheap years are. This note is the **decision engine**: a repeatable October process that computes how much to convert in any given year, given that year's actual income. The core rule is **blended-rate targeting — convert until the all-in cost of the whole conversion reaches 24%, then stop** — and the headline finding is that the strategy should **no longer wait for 2042**. A post-relocation working year carrying a full cost-segregation loss converts **~$155K at a flat 24%**, and the 2042–45 years paired with a cost-seg acquisition convert **~$550K at 23.9%**. Run `scripts/conversion_calculator.py` each October with that year's numbers.
**Tool**: `scripts/conversion_calculator.py` — refresh its tax tables every November
**Related**: [[roth-conversion-window]] · [[tax-mitigation-master-plan]] · [[str-cost-segregation-playbook]] · [[key-figures-2026]]

## The problem this solves

Roughly **99% of Ryan's retirement money is pre-tax** ([[schwab-portfolio-review-2026-07]]), projecting to **$6–7M by 2041**. Left alone that becomes RMDs at 32–37% plus a widow's-penalty tail. The nine-year 2042–2050 window cannot absorb it on its own — so the job is to find **every** year between now and death whose marginal cost is below the rate those dollars would otherwise face, and convert into it deliberately.

## Rule 1 — Target the blended rate, not the marginal rate

Convert until the **all-in cost of the entire year's conversion** reaches **24%**. Then stop.

This matters because IRMAA tiers are **one-year spikes, not permanent step-ups**. A naive "stop at the first cliff" rule leaves cheap bracket space stranded on the far side of it. In the 2042–45 scenario below, marginal-rate stopping converts **$125K**; blended-rate targeting converts **$250K at 23.0% all-in** — the same cost per dollar, twice the volume.

**Why 24%**: it is the rate those dollars face in the best realistic alternative year. Above it, you are no longer arbitraging — you're prepaying at a rate you could have beaten by waiting.

## Rule 2 — What each type of year is actually worth

Modelled on 2026 figures and ~$800K gross. Re-run annually; these are the shapes, not promises.

| Scenario | Convert | All-in rate | Verdict |
|---|---|---|---|
| **A.** Working year, Colorado, no cost-seg | **$0** | 37–39% | Never |
| **B.** Working year, Colorado, full §461(l) cost-seg loss | ~$155K | **28.4%** | Only if the later window is full |
| **C.** Working year, Colorado, *half*-sized cost-seg loss | **$0** | **39.4%** | **Trap — lands in the SALT torpedo** |
| **D.** 2042–45, retired + relocated, only Stacy's SS | **$250K** | **23.0%** | **Core of the plan** |
| **E.** 2042–45 **+ a cost-seg acquisition that year** | **$550K** | **23.9%** | **Best in the plan** |
| **F.** Post-relocation **working** year + full cost-seg loss | **$155K** | **24.0% flat** | **New — start years earlier** |
| **G.** Post-relocation working year, no cost-seg | **$0** | 37% | Never |

### Three findings that change the plan

**1. Relocation is worth more than previously credited.** Compare B (28.4%) with F (24.0%): the only difference is Colorado's 4.4%. Relocating doesn't merely protect retirement distributions under [[tax-mitigation-master-plan|4 U.S.C. §114]] — it **unlocks ~$155K/year of 24% conversions in every remaining working year that carries a cost-seg loss**. Relocating in 2032 instead of 2040 is worth roughly **$1.2M of additional converted balance** at the good rate.

**2. Half-measures are worse than nothing.** Scenario C is the trap: a cost-seg loss big enough to lower MAGI but not enough to clear the **SALT phase-down band ($505K–$606K)** leaves every conversion dollar at **39.4%**. Either the loss is large enough to drop MAGI below ~$290K, or there is no conversion that year. **Never convert into the torpedo.**

**3. Pre-Medicare years have no IRMAA constraint at all.** Ryan isn't on Medicare until 8/2041 and Stacy is [[household-timeline|declining until then]], so IRMAA's two-year lookback means **conversions before 2039 carry zero IRMAA cost**. Every conversion from 2042 onward drives a premium surcharge; the working-year conversions in F do not. That is a real, unpriced advantage of converting earlier.

## Rule 3 — Opportunistic triggers (any year, standing orders)

- **Market drawdown ≥15%** → accelerate that year's conversion and **convert in kind**. Same tax, more shares, and the recovery happens inside the Roth. Pre-committed now so it gets executed rather than debated.
- **Convert the most-depressed holdings, not a slice of everything.** With TSLA at 17.6% of the portfolio and a volatile speculative sleeve ([[schwab-portfolio-review-2026-07]]), moving the *beaten-down* positions in kind puts the highest-variance recovery inside the tax-free wrapper. Rebalancing inside the plan is tax-free, so this costs nothing to arrange.
- **Any year a cost-seg acquisition lands** → immediately re-run the calculator. The loss creates conversion room that expires 12/31.
- **Any year income drops unexpectedly** (furlough, medical leave, short year) → re-run.

## Rule 4 — Timing within the year

| | |
|---|---|
| **Decide** | October, with the CPA, using the calculator and a YTD income projection |
| **Execute** | **December**, once the year's income is essentially known — a conversion is **irreversible** (recharacterization was repealed in 2018), so late-year execution carries the least estimate risk |
| **Exception** | A ≥15% drawdown at any point — convert then, at the pre-agreed size |
| **Never** | Withhold the tax from the conversion itself. Pay from taxable funds; withholding shrinks what lands in the Roth |
| **Hard stop** | **December 31.** No grace period, unlike IRA contributions |

## The October worksheet — run this every year

```
cd srs-elite/tax-strategy/scripts
python3 conversion_calculator.py --wages <YTD-projected W-2> \
    --business-loss <projected non-passive RE loss> \
    --other-ordinary <interest, non-qual dividends> \
    --social-security <gross SS, if claimed> \
    --salt-paid <state+property tax> \
    --state-rate <0.044 Colorado | 0.0 after relocating> \
    [--medicare]        # once either spouse is enrolled
```

1. **Project the year's income** — W-2 through December, rental net, interest/dividends, any SS.
2. **Project the year's non-passive real estate loss** — cost-seg studies landing this year, capped at §461(l) ($512,000 MFJ in 2026).
3. **Run the calculator.** It returns the conversion that holds the blended rate at/under 24%, and flags SALT-torpedo and IRMAA-cliff zones.
4. **Sanity-check against the alternative**: is this rate better than what these dollars face in a future year? If the answer is no, convert nothing.
5. **Confirm the tax can be paid from taxable funds**, and that estimated-payment/safe-harbor coverage is arranged (110% of prior-year tax for high earners).
6. **Record the decision and the inputs** in this note's log below — the year-over-year trail is what makes next year's judgment better.
7. **Execute in December, in kind.**

## Decision log

| Year | Projected income | RE loss | Converted | All-in rate | Notes |
|---|---|---|---|---|---|
| 2026 | ~$800K | **~$1.0–1.26M** (3 properties, ~$1.8M, est. 70% reclass) | **pending** | 28.4% if taken | §461(l) caps 2026 use at $512K → AGI ~$288K; **$496–748K becomes an NOL carryforward**. Capacity $155K at 28.4%. **Decision held** pending the four verifications in [[2026-acquisitions-analysis]] — chiefly whether REPS holds. |
| 2027 | ~$800K | NOL carryforward | **plan ~$200K** | **~8.8%** ⚠️ | **Potentially the cheapest year in the plan** — the 80% NOL limit means each converted dollar unlocks ~$0.80 more NOL. Depends on carryforward size and on §461(l) carrying forward as an NOL. See [[2026-acquisitions-analysis]]. |

## Maintenance

- **Every November**: update the tax tables in `conversion_calculator.py` and [[key-figures-2026]] with the new IRS inflation figures and CMS IRMAA tiers. The script holds them in one `YearData` block for exactly this reason.
- **Every October**: run the worksheet above. A recurring reminder is set.
- **When circumstances change** (relocation date set, MBCBP turns on, a property closes, Medicare enrollment): re-run immediately rather than waiting for October.

> [!warning] Modelled, not filed
> Every figure here comes from the calculator using published 2026 rules and estimated inputs. It does not account for AMT, state-specific quirks of the destination state, NIIT interaction with large rental income, or the actual composition of Ryan's plan balances. **Zach Fox signs off on the number before any conversion is executed.**

**Related**: [[roth-conversion-window]] · [[tax-mitigation-master-plan]] · [[str-cost-segregation-playbook]] · [[schwab-portfolio-review-2026-07]] · [[key-figures-2026]]

---

## Scheduled task

**"Annual Roth Conversion Analysis — October"** (`trig_013TdNBEsq9A5jvSFsRFWGzH`) fires **October 6 each year, 7:48am MT**, in a fresh session: it reads this protocol, refreshes the tax tables, asks Ryan for the year's inputs, runs the calculator, reports the recommendation, and appends to the decision log above. Push + email notifications on.

Two caveats:
- **It stores no connectors** (a limitation of creating it from a coding session). If the run needs Gmail/Drive/Calendar, enable them once on the task in claude.ai → Settings, or recreate it there.
- **Its first firing is October 2027** — the **2026 decision is due now** and is being handled manually.
