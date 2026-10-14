#!/usr/bin/env python3
"""
Roth conversion sizing calculator — Schubert household.

Answers one question each year: how much should we convert, and what does the
last dollar actually cost once brackets, the SALT phase-down, NIIT and the
IRMAA cliff are all priced in?

Usage:
    python3 conversion_calculator.py                 # run the built-in scenarios
    python3 conversion_calculator.py --wages 800000 --business-loss 512000

REFRESH EVERY NOVEMBER: update YEARS[] with the new IRS/CMS figures.
See ../key-figures-2026.md for sources.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass, field

# ---------------------------------------------------------------- tax tables
@dataclass(frozen=True)
class YearData:
    year: int
    brackets: list                 # (upper taxable-income bound, rate)
    std_deduction: int
    salt_cap: int
    salt_phasedown_start: int      # MAGI where the cap starts shrinking
    salt_phasedown_rate: float     # cap reduced by this × excess MAGI
    salt_floor: int
    niit_threshold: int            # MAGI, MFJ, not indexed
    ebl_cap: int                   # §461(l) excess business loss, MFJ
    irmaa_tiers: list              # (MAGI upper bound, annual cost for a couple)

Y2026 = YearData(
    year=2026,
    brackets=[(24_800, .10), (100_800, .12), (211_400, .22), (403_550, .24),
              (512_450, .32), (768_700, .35), (10**12, .37)],
    std_deduction=32_200,
    salt_cap=40_400, salt_phasedown_start=505_000,
    salt_phasedown_rate=0.30, salt_floor=10_000,
    niit_threshold=250_000,
    ebl_cap=512_000,
    irmaa_tiers=[(218_000, 4_870), (274_000, 7_166), (342_000, 10_640),
                 (410_000, 14_110), (750_000, 17_582), (10**12, 18_742)],
)
YEARS = {2026: Y2026}


def tax_on(taxable: float, yd: YearData) -> float:
    t, prev = 0.0, 0
    for cap, rate in yd.brackets:
        if taxable > prev:
            t += (min(taxable, cap) - prev) * rate
            prev = cap
        else:
            break
    return t


def salt_allowed(magi: float, salt_paid: float, yd: YearData) -> float:
    cap = yd.salt_cap
    if magi > yd.salt_phasedown_start:
        cap = max(yd.salt_floor, cap - yd.salt_phasedown_rate * (magi - yd.salt_phasedown_start))
    return min(salt_paid, cap)


def irmaa_cost(magi: float, yd: YearData, on_medicare: bool) -> float:
    if not on_medicare:
        return 0.0
    for bound, cost in yd.irmaa_tiers:
        if magi <= bound:
            return cost
    return yd.irmaa_tiers[-1][1]


# ---------------------------------------------------------------- the model
@dataclass
class Scenario:
    label: str
    wages: float = 0.0             # W-2 (after pre-tax deferrals)
    other_ordinary: float = 0.0    # interest, non-qualified dividends, pensions
    social_security: float = 0.0   # gross; 85% assumed taxable
    business_loss: float = 0.0     # non-passive RE loss (REPS/STR), pre-§461(l)
    itemized_non_salt: float = 0.0 # mortgage interest, charitable, etc.
    salt_paid: float = 40_000.0
    on_medicare: bool = False      # drives whether IRMAA applies 2 yrs later
    state_rate: float = 0.0        # 0.044 Colorado, 0.0 after relocation
    year: int = 2026

    def base_agi(self, yd) -> float:
        loss = min(self.business_loss, yd.ebl_cap)
        return max(0.0, self.wages + self.other_ordinary
                   + 0.85 * self.social_security - loss)

    def total_cost(self, conversion: float, yd: YearData) -> float:
        """Federal + state + IRMAA at a given conversion size."""
        magi = self.base_agi(yd) + conversion
        deductions = max(yd.std_deduction,
                         self.itemized_non_salt + salt_allowed(magi, self.salt_paid, yd))
        taxable = max(0.0, magi - deductions)
        return (tax_on(taxable, yd)
                + self.state_rate * taxable
                + irmaa_cost(magi, yd, self.on_medicare))


def analyze(sc: Scenario, step: int = 5_000, max_conv: int = 1_500_000):
    yd = YEARS[sc.year]
    base = sc.base_agi(yd)
    zero = sc.total_cost(0, yd)
    rows = []
    prev_cost = zero
    for conv in range(step, max_conv + step, step):
        cost = sc.total_cost(conv, yd)
        marginal = (cost - prev_cost) / step
        cumulative = (cost - zero) / conv
        rows.append((conv, base + conv, marginal, cumulative))
        prev_cost = cost
    return base, rows


def recommend(sc: Scenario, target_rate: float):
    """Largest conversion whose ALL-IN (blended) rate stays at/under target_rate.

    Deliberately blended, not marginal: IRMAA tiers are one-year *spikes*, not
    permanent step-ups, so a naive marginal rule stops dead at the first cliff
    and leaves cheap bracket space unused on the far side of it. The right
    question is "how much can we move while the average cost stays acceptable."
    """
    base, rows = analyze(sc)
    best = 0
    for conv, magi, marginal, cumulative in rows:
        if cumulative <= target_rate + 1e-9:
            best = conv
    return base, best


def report(sc: Scenario, target_rate: float = 0.24):
    yd = YEARS[sc.year]
    base, rec = recommend(sc, target_rate)
    print(f"\n{'='*74}\n{sc.label}  [{sc.year}]\n{'='*74}")
    loss_used = min(sc.business_loss, yd.ebl_cap)
    if sc.business_loss:
        carry = sc.business_loss - loss_used
        print(f"  Business loss {sc.business_loss:>12,.0f}  (§461(l) allows {loss_used:,.0f}"
              + (f"; {carry:,.0f} → NOL carryforward)" if carry else ")"))
    print(f"  AGI before conversion         {base:>12,.0f}")
    print(f"  Medicare / IRMAA applies:     {'YES' if sc.on_medicare else 'no'}"
          f"   State rate: {sc.state_rate:.1%}")
    if rec:
        cost = sc.total_cost(rec, yd) - sc.total_cost(0, yd)
        print(f"\n  >> CONVERT {rec:,.0f}  (marginal stays ≤ {target_rate:.0%})")
        print(f"     Resulting MAGI            {base+rec:>12,.0f}")
        print(f"     Total cost of conversion  {cost:>12,.0f}   "
              f"= {cost/rec:.1%} all-in")
    else:
        print(f"\n  >> CONVERT $0 — already above the {target_rate:.0%} marginal threshold")
    print(f"\n  {'Conversion':>12} {'MAGI':>12} {'marginal':>10} {'all-in':>9}")
    shown = 0
    for conv, magi, marginal, cumulative in analyze(sc, step=25_000)[1]:
        if marginal > 0.40 or shown > 13:
            break
        flag = ''
        if sc.on_medicare:
            for bound, _ in YEARS[sc.year].irmaa_tiers:
                if magi - 25_000 <= bound < magi:
                    flag = '  << IRMAA cliff'
        if YEARS[sc.year].salt_phasedown_start < magi <= YEARS[sc.year].salt_phasedown_start + 101_400:
            flag += '  << SALT torpedo'
        print(f"  {conv:>12,} {magi:>12,.0f} {marginal:>9.1%} {cumulative:>9.1%}{flag}")
        shown += 1


SCENARIOS = [
    Scenario("A. Working year, NO cost-seg — the base case",
             wages=800_000, state_rate=0.044),
    Scenario("B. Working year WITH a full §461(l) cost-seg loss",
             wages=800_000, business_loss=512_000, state_rate=0.044),
    Scenario("C. Working year, half-sized cost-seg loss",
             wages=800_000, business_loss=250_000, state_rate=0.044),
    Scenario("D. 2042-45 'cheap years' — retired, relocated, only Stacy's SS",
             other_ordinary=40_000, social_security=60_000,
             on_medicare=True, state_rate=0.0),
    Scenario("E. 2042-45 cheap year PLUS a cost-seg acquisition",
             other_ordinary=40_000, social_security=60_000, business_loss=300_000,
             on_medicare=True, state_rate=0.0),
    Scenario("F. *** THE SWEET SPOT *** post-relocation working year + full cost-seg loss",
             wages=800_000, business_loss=512_000, state_rate=0.0),
    Scenario("G. Post-relocation working year, no cost-seg (for contrast)",
             wages=800_000, state_rate=0.0),
]

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--wages", type=float)
    ap.add_argument("--other-ordinary", type=float, default=0)
    ap.add_argument("--social-security", type=float, default=0)
    ap.add_argument("--business-loss", type=float, default=0)
    ap.add_argument("--salt-paid", type=float, default=40_000)
    ap.add_argument("--state-rate", type=float, default=0.0)
    ap.add_argument("--medicare", action="store_true")
    ap.add_argument("--target-rate", type=float, default=0.24)
    a = ap.parse_args()
    if a.wages is not None:
        report(Scenario("Custom scenario", wages=a.wages,
                        other_ordinary=a.other_ordinary,
                        social_security=a.social_security,
                        business_loss=a.business_loss, salt_paid=a.salt_paid,
                        on_medicare=a.medicare, state_rate=a.state_rate),
               a.target_rate)
    else:
        for s in SCENARIOS:
            report(s)
