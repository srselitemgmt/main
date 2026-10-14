#!/usr/bin/env python3
"""
Lifetime projection — Schubert household.  All figures in 2026 REAL dollars
(brackets and limits index with inflation, so real-dollar comparisons hold).

Question it answers: can the conversion plan actually drain the pre-tax
balance before RMDs, and what is the survivor exposed to if it doesn't?

ASSUMPTIONS ARE EDITABLE AT THE TOP. Every one is an estimate, not a fact.
"""
from dataclasses import dataclass

# ----------------------------------------------------------------- assumptions
REAL_RETURN      = 0.045     # 7% nominal less ~2.5% inflation
WAGES            = 800_000   # real, flat; 7/12 in 2041 (retires 8/3)
EMPLOYER_PRETAX  = 65_000    # 401(k) employer share landing pre-tax
MBCBP            = 65_000    # from 2028, replaces taxable PRAP Cash
ROTH_ADDS        = 39_000    # backdoor x2 + Roth catch-up + after-tax sweep
PRETAX_START     = 1_661_000
ROTH_START       = 17_674 + 85_038   # Roth IRA + after-tax sleeve swept in
FL_MOVE_YEAR     = 2030      # <-- 3.5 years out
RETIRE_YEAR      = 2041
RMD_YEAR         = 2051      # Ryan turns 75
RYAN_SS          = 61_000    # real, claimed at 70 (2046)
STACY_SS         = 22_000    # spousal-based; see open question in the review
OTHER_ORD        = 25_000    # interest / non-qualified dividends

B=[(24_800,.10),(100_800,.12),(211_400,.22),(403_550,.24),
   (512_450,.32),(768_700,.35),(10**12,.37)]
SD=32_200; CO_RATE=0.044
# Uniform Lifetime Table divisors from age 75
ULT={75:24.6,76:23.7,77:22.9,78:22.0,79:21.1,80:20.2,81:19.4,82:18.5,83:17.7,
     84:16.8,85:16.0,86:15.2,87:14.4,88:13.7,89:12.9,90:12.2,91:11.5,92:10.8,
     93:10.1,94:9.5,95:8.9}

def tax(ti):
    t=0;p=0
    for c,r in B:
        if ti>p: t+=(min(ti,c)-p)*r; p=c
        else: break
    return t

def run(label, convert_working_years, conv_retire, conv_working=155_000,
        costseg_every=2, verbose=False):
    pre, roth = PRETAX_START, ROTH_START
    lifetime_tax = 0.0; converted = 0.0; rows=[]
    for year in range(2026, 2066):
        age = year - 1976
        state = CO_RATE if year < FL_MOVE_YEAR else 0.0
        working = year <= RETIRE_YEAR
        w = WAGES if year < RETIRE_YEAR else (WAGES*7/12 if year==RETIRE_YEAR else 0)
        # --- income
        ss = (RYAN_SS if year >= 2046 else 0) + (STACY_SS if year >= 2046 else 0)
        ordinary = w + OTHER_ORD + 0.85*ss
        # --- cost-seg loss in working years (a deal every N years)
        loss = 512_000 if (working and (year-2026) % costseg_every == 0) else 0
        ordinary = max(0, ordinary - loss)
        # --- RMD
        rmd = pre / ULT.get(age, 8.9) if year >= RMD_YEAR else 0
        ordinary += rmd; pre -= rmd; roth += 0   # RMD spent, not reinvested
        # --- conversion
        conv = 0
        if working and convert_working_years and loss and year >= FL_MOVE_YEAR:
            conv = min(conv_working, pre)
        elif not working and year < RMD_YEAR:
            conv = min(conv_retire, pre)
        pre -= conv; roth += conv; converted += conv
        # --- tax
        ti = max(0, ordinary + conv - SD)
        lifetime_tax += tax(ti) + state*ti
        # --- contributions & growth
        if working:
            pre += EMPLOYER_PRETAX + (MBCBP if year >= 2028 else 0)
            roth += ROTH_ADDS
        pre *= 1+REAL_RETURN; roth *= 1+REAL_RETURN
        if year in (2030,2041,2045,2050,2051,2055,2060):
            rows.append((year,age,pre,roth,conv,rmd))
    return label, lifetime_tax, converted, pre, roth, rows

print("ALL FIGURES IN 2026 REAL DOLLARS.  Estimates, not projections of fact.\n")
scenarios=[
    run("A. No conversions until retirement (original plan)", False, 250_000),
    run("B. + convert in post-FL cost-seg working years", True, 250_000),
    run("C. B, but cost-seg deal EVERY year + bigger retirement conversions",
        True, 400_000, costseg_every=1),
]
print(f"{'strategy':<52}{'lifetime tax':>14}{'converted':>13}{'2051 pre-tax':>14}")
print("-"*93)
for lab,lt,cv,pre,roth,rows in scenarios:
    r2051=[r for r in rows if r[0]==2051][0]
    print(f"{lab:<52}{lt:>14,.0f}{cv:>13,.0f}{r2051[2]:>14,.0f}")
print()
for lab,lt,cv,pre,roth,rows in scenarios:
    print(f"\n{lab}")
    print(f"  {'year':>6}{'age':>5}{'pre-tax':>13}{'Roth':>13}{'converted':>11}{'RMD':>11}")
    for y,a,p,r,c,m in rows:
        print(f"  {y:>6}{a:>5}{p:>13,.0f}{r:>13,.0f}{c:>11,.0f}{m:>11,.0f}")
