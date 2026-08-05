# MHP / RV Park Investment Strategy — Subject-To & Seller-Finance Focus

**Summary**: Strategy for turning the [[mhp-rv-50k-list|54K national MHP/RV list]] into acquisitions, prioritizing mom-and-pop parks likely to sell subject-to or with seller financing, in landlord-friendly growth markets that cash flow on lot rent. A scoring model ranks all 54,060 parks; 9,896 land in Tier A.
**Sources**: `SPECIAL_LIST_NATIONAL_MHP_RV_50K.csv`, scored via `scripts/score_parks.py`
**Last updated**: 2026-08-05

## The thesis

Mobile home parks are the most mom-and-pop-owned asset class in commercial real estate. The majority of the ~44,000 US parks are still held by original or long-tenure individual owners — often free-and-clear or with old low-rate debt, tired of managing, with no succession plan. That's exactly the seller profile that says yes to subject-to, seller carry, or master-lease-with-option. Meanwhile the asset itself is supply-constrained (near-zero new park zoning), has the lowest turnover cost of any rental (tenant-owned homes = tenants pay to move, ~$5-10K, so they don't), and lot rents in growth markets have been compounding well above inflation.

The play: **buy small/medium mom-and-pop parks in Sunbelt growth counties on seller terms, professionalize operations, push lot rents to market, and hold for cashflow** — with cost segregation on land improvements (roads, pads, utility infrastructure are largely 15-year property eligible for 100% bonus depreciation) making year-1 tax outcomes exceptional.

## The funnel

| Stage | Count | What happens |
|---|---|---|
| Raw list | 54,270 | Dedupe → 54,060 unique parks |
| Scored | 54,060 | Composite 0-100 score (model below) |
| Tier A (score ≥75) | 9,896 | The prospecting universe |
| Top-1000 shortlist | 1,000 | First outreach wave: enrich → skip trace → contact |
| Target: LOIs | 20-40 | ~2-4% response-to-conversation rate on quality lists |
| Target: closings | 2-5/yr | Seller-terms deals only |

## Scoring model (what `score_parks.py` does)

**Composite = MARKET (0-40) + COUNTY_BONUS (0-15) + SUBTO (0-30) + CASHFLOW (0-15)**

- **MARKET** — state tier. Tier A (40 pts): TX, FL, NC, SC, TN, GA, AZ, AL, ID, UT, NV — in-migration, landlord-friendly, no MHP rent regulation. Tier B (26): stable Midwest/South cashflow states. Tier C (8): states with MHP-specific rent caps or tenant opportunity-to-purchase mandates (CA, NY, NJ, MA, CT, RI, VT, OR, WA, CO, MN, IL, DE, MD) — these add regulatory drag on rent growth and complicate exits.
- **COUNTY_BONUS** — curated list of ~100 boom counties (Maricopa/Pinal AZ, Polk/Pasco/Marion FL, Horry/Greenville SC, Wake/Johnston NC, Williamson/Rutherford TN, Montgomery/Fort Bend TX, etc.).
- **SUBTO** — mom-and-pop / seller-terms likelihood. Sweet spot is 10-60 lots (enough income to matter, small enough that institutions don't want it). Corporate/franchise name signals (KOA, "Resort", "Communities", known operators) get penalized; classic mom-and-pop naming ("...Court", "...Acres", possessive names) gets a bump.
- **CASHFLOW** — viable lot count × affordable-market proxy. 25+ lots at Sunbelt lot rents clears meaningful cashflow even at seller-carry debt service.

Results: FL (3,559 Tier A), SC (1,209), TX (1,140), NC (898), AZ (873), AL (608), GA (396), TN (386), NV (287), ID (216), UT (153).

**Top target counties** (Tier-A park density): Polk FL (452), Maricopa AZ (428), Hillsborough FL (299), Pasco FL (265), Horry SC (244), Greenville SC (196), Volusia FL (186), Lee FL (183), Baldwin AL (172), Lexington SC (166), Marion FL (164), Pinal AZ (146), Spartanburg SC (143), Lake FL (142), Clark NV (141).

## What makes a park likely to sell subject-to

The list can't see these directly — they're what enrichment and the first phone call establish:

1. **Owner tenure 15+ years** (county assessor: last arm's-length sale date). Long tenure = low basis, big equity, often free-and-clear or small old loans — ideal for seller carry; existing low-rate debt = ideal for sub-to.
2. **Individual or family-LLC ownership**, not a fund or operator entity.
3. **Owner age 60+** / out-of-state owner address (absentee + retirement horizon).
4. **Tired-landlord signals**: below-market lot rents, park-owned home headaches, deferred maintenance visible on satellite/street view, no website or online presence.
5. **No broker listing** — off-market only. Once listed, terms deals mostly die.

**Deal structures, in order of preference:**
- **Seller carry** (most common for free-and-clear mom-and-pops): 10-20% down, 5-6% interest, 20-30yr amortization, 5-10yr balloon. Pitch: installment-sale tax treatment beats a lump sum they'd owe capital gains + recapture on.
- **Subject-to** existing financing where a loan survives (verify no due-on-sale enforcement risk appetite; parks often have local-bank debt where the bank will consent).
- **Hybrid**: sub-to the existing note + seller carry the equity gap.
- **Master lease with option** when the seller isn't ready to deed — control now, close later.

> **Tax caveat**: subject-to / seller-financed acquisitions can hit **at-risk limitations** (§465) that gate loss deductions — the vault's first-year projection model already flags this ("At-risk gate: CHECK"). Run every terms deal through that check with Zach Fox before counting on year-1 losses.

## Quick underwriting screen (before any LOI)

- **Income**: lots × occupancy × market lot rent × 12. Verify rent roll against bank deposits.
- **Expense ratio**: 30-35% of gross for tenant-owned-home parks on city utilities; 40%+ if park pays water/sewer or has park-owned homes. Private well/septic/lagoon = capex bomb, price it or pass.
- **Value**: NOI ÷ cap. Underwrite at 7-8% cap in Tier A metros for stabilized; mom-and-pops with below-market rents often trade at effective 9-11% on pro-forma.
- **The upside math**: a 40-lot park at $350 lot rent, 80% occupied ≈ $134K gross / ~$90K NOI. Same park at market $525 rent, 95% occupied ≈ $240K gross / ~$165K NOI — value roughly doubles without adding a single lot.
- **Kill criteria**: flood zone, >30% park-owned homes (that's a rental business, not a land lease), failing private utilities without priced remediation, Tier C state.

## Outreach playbook

Every row has a phone number — this list is unusually cold-call ready.

1. **Enrich** (top 1,000 first): county assessor owner lookup → skip trace owner cell/address → flag corporate owners out.
2. **Sequence**: direct mail (handwritten-style, "I'd like to buy your park, flexible on terms and timing") → cold call 5-7 days later → SMS follow-up. 6-8 touches over 12 months; park sellers move slowly.
3. **Script core**: tenure question → pain question (management, collections, infrastructure) → terms trial balloon ("if the price was right, would you rather get paid over time and skip a big tax bill, or all cash?").
4. **Track in CRM** with the score fields imported — work Tier A counties in geographic clusters so diligence trips and eventual management overlap.
5. **RV parks** (3,039 rows, flagged in scored output): treat as a separate campaign — they're operating businesses (nightly/seasonal revenue, staff) not land-lease, but the same mom-and-pop seller dynamics apply and STR-style depreciation outcomes can be even better.

## Next actions

1. Pull the top-1000 shortlist and run assessor/skip-trace enrichment (VAs or a service like PropStream/ReiSift/USLandGrid).
2. Pick 2-3 launch counties from the top-county table — Polk/Pasco FL, Horry SC, and Maricopa/Pinal AZ are the strongest density+growth combos — and mail wave 1.
3. Stand up the underwriting screen as a one-pager per responding park; anything passing goes into the first-year tax projection model in the vault.
4. Re-score whenever enrichment adds owner-tenure data — tenure is a stronger sub-to predictor than anything currently in the model.

## Related pages

- [[mhp-rv-50k-list]] — the dataset behind this strategy
