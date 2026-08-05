#!/usr/bin/env python3
"""Score the national MHP/RV 50K list for acquisition targeting.

Scoring model (0-100 composite):
  MARKET (0-40)      state-level: population/job growth, landlord friendliness,
                     absence of MHP-specific rent caps or opportunity-to-purchase drag
  COUNTY_BONUS (0-15) curated high-growth counties (Sunbelt boom metros)
  SUBTO (0-30)       mom-and-pop / subject-to & seller-finance likelihood:
                     size band sweet spot + name signals (franchise/resort = corporate)
  CASHFLOW (0-15)    lot-rent cashflow proxy: affordability states + viable lot count

Usage: python3 score_parks.py <input_csv> <output_dir>
Outputs: scored_full.csv, top_1000_shortlist.csv, state_summary.csv, county_summary.csv
"""
import csv
import re
import sys
from collections import defaultdict

# --- State market tiers -----------------------------------------------------
# A: strong in-migration + landlord-friendly + no MHP rent regulation
TIER_A = {"TX", "FL", "NC", "SC", "TN", "GA", "AZ", "AL", "ID", "UT", "NV"}
# B: stable cashflow markets, moderate growth, generally landlord-neutral
TIER_B = {"IN", "OH", "MO", "OK", "KY", "AR", "KS", "NE", "IA", "WI", "MI",
          "PA", "VA", "WV", "MS", "LA", "NM", "WY", "MT", "SD", "ND", "NH", "ME"}
# C: MHP-specific rent caps, opportunity-to-purchase mandates, or heavy
# tenant-protection regimes that slow lot-rent growth and complicate exits
TIER_C = {"CA", "NY", "NJ", "MA", "CT", "RI", "VT", "OR", "WA", "CO", "MN",
          "IL", "DE", "MD", "HI", "AK", "DC"}

MARKET_SCORE = {}
for s in TIER_A:
    MARKET_SCORE[s] = 40
for s in TIER_B:
    MARKET_SCORE[s] = 26
for s in TIER_C:
    MARKET_SCORE[s] = 8

# --- High-growth counties (state, county-name-upper) ------------------------
GROWTH_COUNTIES = {
    ("AZ", "MARICOPA"), ("AZ", "PINAL"), ("AZ", "YAVAPAI"),
    ("NV", "CLARK"), ("NV", "WASHOE"),
    ("ID", "ADA"), ("ID", "CANYON"), ("ID", "KOOTENAI"),
    ("UT", "UTAH"), ("UT", "WASHINGTON"), ("UT", "SALT LAKE"),
    ("TX", "MONTGOMERY"), ("TX", "FORT BEND"), ("TX", "WILLIAMSON"),
    ("TX", "HAYS"), ("TX", "COMAL"), ("TX", "DENTON"), ("TX", "COLLIN"),
    ("TX", "KAUFMAN"), ("TX", "ELLIS"), ("TX", "PARKER"), ("TX", "JOHNSON"),
    ("TX", "GUADALUPE"), ("TX", "ROCKWALL"), ("TX", "HUNT"), ("TX", "BASTROP"),
    ("FL", "POLK"), ("FL", "PASCO"), ("FL", "LAKE"), ("FL", "OSCEOLA"),
    ("FL", "ST. JOHNS"), ("FL", "ST JOHNS"), ("FL", "MANATEE"),
    ("FL", "SARASOTA"), ("FL", "LEE"), ("FL", "MARION"), ("FL", "HERNANDO"),
    ("FL", "CLAY"), ("FL", "SUMTER"), ("FL", "CHARLOTTE"), ("FL", "VOLUSIA"),
    ("NC", "WAKE"), ("NC", "MECKLENBURG"), ("NC", "JOHNSTON"),
    ("NC", "BRUNSWICK"), ("NC", "UNION"), ("NC", "CABARRUS"),
    ("NC", "IREDELL"), ("NC", "HARNETT"), ("NC", "FRANKLIN"),
    ("NC", "PENDER"), ("NC", "CHATHAM"),
    ("SC", "HORRY"), ("SC", "YORK"), ("SC", "LANCASTER"), ("SC", "BERKELEY"),
    ("SC", "DORCHESTER"), ("SC", "SPARTANBURG"), ("SC", "GREENVILLE"),
    ("SC", "LEXINGTON"), ("SC", "CHARLESTON"),
    ("TN", "WILLIAMSON"), ("TN", "RUTHERFORD"), ("TN", "MONTGOMERY"),
    ("TN", "WILSON"), ("TN", "SUMNER"), ("TN", "MAURY"), ("TN", "KNOX"),
    ("TN", "SEVIER"), ("TN", "HAMILTON"),
    ("GA", "FORSYTH"), ("GA", "CHEROKEE"), ("GA", "JACKSON"),
    ("GA", "WALTON"), ("GA", "BARROW"), ("GA", "PAULDING"),
    ("GA", "GWINNETT"), ("GA", "HENRY"), ("GA", "BRYAN"), ("GA", "EFFINGHAM"),
    ("AL", "MADISON"), ("AL", "LIMESTONE"), ("AL", "BALDWIN"),
    ("AL", "SHELBY"), ("AL", "LEE"),
    ("VA", "CHESTERFIELD"), ("VA", "HANOVER"), ("VA", "SPOTSYLVANIA"),
    ("VA", "STAFFORD"), ("VA", "NEW KENT"),
    ("MO", "CHRISTIAN"), ("MO", "ST. CHARLES"), ("MO", "ST CHARLES"),
    ("AR", "BENTON"), ("AR", "WASHINGTON"), ("AR", "SALINE"),
    ("OK", "CANADIAN"), ("OK", "WAGONER"), ("OK", "CLEVELAND"),
    ("IN", "HAMILTON"), ("IN", "HENDRICKS"), ("IN", "BOONE"),
    ("IN", "JOHNSON"), ("IN", "HANCOCK"),
    ("KY", "SCOTT"), ("KY", "SHELBY"), ("KY", "OLDHAM"), ("KY", "WARREN"),
    ("MI", "OTTAWA"), ("MI", "KENT"), ("MI", "LIVINGSTON"),
    ("OH", "DELAWARE"), ("OH", "WARREN"), ("OH", "UNION"),
    ("WI", "DANE"), ("WI", "ST. CROIX"), ("WI", "ST CROIX"),
}

# --- Name signals -----------------------------------------------------------
CORPORATE_PAT = re.compile(
    r"\b(KOA|KAMPGROUND|RESORT|COMMUNITIES|MHC|PROPERTIES|MANAGEMENT|"
    r"EQUITY LIFESTYLE|SUN COMMUNITIES|RHP|HOMETOWN|YES COMMUNIT|UMH|"
    r"HAVENPARK|LAKESHORE|INSPIRE|MERITUS|CAL-AM|JELLYSTONE|THOUSAND TRAILS|"
    r"OUTDOOR RESORTS|ENCORE)\b")
MOM_POP_PAT = re.compile(
    r"(\w+'S\b|\b(COURT|TRAILER|VILLAGE|ACRES|GROVE|SHADY|COUNTRY|"
    r"HILLSIDE|LAKESIDE|CREEKSIDE|RIVERSIDE|OAK|PINE|MAPLE|WILLOW|"
    r"SUNSET|SUNNY|WHISPERING|BROOK)\b)")


def score_row(r):
    state = r["STATE"].strip().upper()
    county = r["COUNTY"].strip().upper()
    name = r["NAME"].strip().upper()
    size = r["SIZE"].strip().upper()
    units_raw = r["UNITS"].strip()
    units = None
    try:
        u = float(units_raw)
        if u > 0:
            units = u
    except ValueError:
        pass

    market = MARKET_SCORE.get(state, 20)
    county_bonus = 15 if (state, county) in GROWTH_COUNTIES else 0

    # Subject-to / mom-and-pop likelihood (0-30)
    if units is not None:
        if 10 <= units <= 60:
            subto = 24          # sweet spot: real income, still mom-and-pop
        elif 61 <= units <= 100:
            subto = 20
        elif units < 10:
            subto = 8           # too small to matter
        else:
            subto = 10          # >100 lots: likely professionally owned
    else:
        subto = {"SMALL (<50)": 20, "MEDIUM (51-100)": 22,
                 "LARGE (>100)": 10}.get(size, 14)
    if CORPORATE_PAT.search(name):
        subto = max(0, subto - 15)
        flag_corp = True
    else:
        flag_corp = False
    if MOM_POP_PAT.search(name):
        subto = min(30, subto + 6)

    # Cashflow proxy (0-15): viable lot count in affordable, growing markets
    if units is not None:
        cf_size = 9 if units >= 25 else (6 if units >= 10 else 2)
    else:
        cf_size = {"SMALL (<50)": 5, "MEDIUM (51-100)": 9,
                   "LARGE (>100)": 9}.get(size, 5)
    cf_state = 6 if state in TIER_A else (4 if state in TIER_B else 1)
    cashflow = cf_size + cf_state

    total = market + county_bonus + subto + cashflow
    if total >= 75:
        tier = "A"
    elif total >= 55:
        tier = "B"
    else:
        tier = "C"

    flags = []
    if flag_corp:
        flags.append("corporate/franchise name")
    if "RECREATIONAL" in r["TYPE"]:
        flags.append("RV park")
    if "MIGRANT" in r["TYPE"]:
        flags.append("migrant housing component")
    if units is None:
        flags.append("unit count unknown")
    return market, county_bonus, subto, cashflow, total, tier, "; ".join(flags)


def main(inp, outdir):
    rows = list(csv.DictReader(open(inp, encoding="utf-8", errors="replace")))
    seen = set()
    deduped = []
    for r in rows:
        k = (r["NAME"], r["ADDRESS"], r["CITY"], r["STATE"])
        if k in seen:
            continue
        seen.add(k)
        deduped.append(r)

    out_fields = ["NAME", "ADDRESS", "CITY", "STATE", "ZIP", "TELEPHONE",
                  "TYPE", "COUNTY", "UNITS", "SIZE", "MARKET_SCORE",
                  "COUNTY_BONUS", "SUBTO_SCORE", "CASHFLOW_SCORE",
                  "TOTAL_SCORE", "TIER", "FLAGS"]
    scored = []
    for r in deduped:
        m, cb, st, cf, tot, tier, flags = score_row(r)
        zip5 = r["ZIP"].split(".")[0].zfill(5) if r["ZIP"].strip() else ""
        units = r["UNITS"].replace("-999.0", "").replace(".0", "")
        scored.append({
            "NAME": r["NAME"], "ADDRESS": r["ADDRESS"], "CITY": r["CITY"],
            "STATE": r["STATE"], "ZIP": zip5, "TELEPHONE": r["TELEPHONE"],
            "TYPE": r["TYPE"], "COUNTY": r["COUNTY"], "UNITS": units,
            "SIZE": r["SIZE"], "MARKET_SCORE": m, "COUNTY_BONUS": cb,
            "SUBTO_SCORE": st, "CASHFLOW_SCORE": cf, "TOTAL_SCORE": tot,
            "TIER": tier, "FLAGS": flags})
    scored.sort(key=lambda x: -x["TOTAL_SCORE"])

    def dump(path, data):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=out_fields)
            w.writeheader()
            w.writerows(data)

    dump(f"{outdir}/scored_full.csv", scored)
    dump(f"{outdir}/top_1000_shortlist.csv", scored[:1000])

    st_sum = defaultdict(lambda: {"parks": 0, "tier_a": 0, "avg": 0.0})
    for r in scored:
        s = st_sum[r["STATE"]]
        s["parks"] += 1
        s["tier_a"] += r["TIER"] == "A"
        s["avg"] += r["TOTAL_SCORE"]
    with open(f"{outdir}/state_summary.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["STATE", "PARKS", "TIER_A_PARKS", "AVG_SCORE"])
        for st, s in sorted(st_sum.items(), key=lambda kv: -kv[1]["tier_a"]):
            w.writerow([st, s["parks"], s["tier_a"],
                        round(s["avg"] / s["parks"], 1)])

    co_sum = defaultdict(lambda: {"parks": 0, "tier_a": 0})
    for r in scored:
        c = co_sum[(r["STATE"], r["COUNTY"])]
        c["parks"] += 1
        c["tier_a"] += r["TIER"] == "A"
    with open(f"{outdir}/county_summary.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["STATE", "COUNTY", "PARKS", "TIER_A_PARKS"])
        for (st, co), c in sorted(co_sum.items(),
                                  key=lambda kv: -kv[1]["tier_a"])[:100]:
            w.writerow([st, co, c["parks"], c["tier_a"]])

    tiers = defaultdict(int)
    for r in scored:
        tiers[r["TIER"]] += 1
    print(f"scored {len(scored)} unique parks (removed "
          f"{len(rows) - len(deduped)} dupes)")
    print("tiers:", dict(tiers))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
