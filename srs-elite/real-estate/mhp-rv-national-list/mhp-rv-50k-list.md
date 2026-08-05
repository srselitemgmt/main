# National MHP / RV Park 50K List

**Summary**: National list of 54,270 mobile home parks, RV parks, and MHP/RV/migrant housing sites (54,060 unique after dedupe) with address, county, phone, and size data. This is the raw prospecting universe behind the [[mhp-rv-investment-strategy|MHP/RV investment strategy]].
**Sources**: Uploaded `SPECIAL_LIST_NATIONAL_MHP_RV_50K.csv` (2026-08-05)
**Last updated**: 2026-08-05

## What's in the list

| Field | Coverage | Notes |
|---|---|---|
| NAME, ADDRESS, CITY, STATE, ZIP, COUNTY | 100% | 49 states (no HI/DC). ZIP is float-formatted in the raw file (e.g. `5201.0` = 05201); cleaned to 5-digit in scored outputs |
| TELEPHONE | 100% | Every row has a phone — this list is cold-call ready |
| TYPE | 100% | 51,174 mobile home parks · 3,039 RV parks · 57 MHP/RV/migrant housing |
| SIZE | 100% | SMALL (<50): 38,169 · MEDIUM (51-100): 9,014 · LARGE (>100): 7,087 |
| UNITS | 18% | Exact lot count known for 9,766 rows; `-999.0` = unknown. Median known count: 34 lots |

Top states by count: FL (5,913), CA (5,070), TX (3,564), NC (2,963), AL (2,464), SC (2,439), LA (1,776), NY (1,608), PA (1,592), AZ (1,493).

## Caveats

- **No ownership data.** The list has park names, not owner names/entities. Owner lookup (county assessor, skip trace) is the first enrichment step before outreach.
- **No financials.** No lot rents, occupancy, or debt info — the scoring model uses size and market proxies instead.
- **Unit counts mostly missing** (82%). The SIZE band is used as fallback in scoring.
- **210 duplicate rows** removed in the scored outputs.
- Vintage unknown — verify a park still operates before spending outreach dollars on it.

## Files

- `data/SPECIAL_LIST_NATIONAL_MHP_RV_50K.csv` — raw list as uploaded
- `data/scored_full.csv` — all 54,060 unique parks with scores (see strategy page for model)
- `data/top_1000_shortlist.csv` — highest-scoring 1,000 targets
- `data/state_summary.csv`, `data/county_summary.csv` — market roll-ups
- `scripts/score_parks.py` — reproducible scoring script

## Related pages

- [[mhp-rv-investment-strategy]] — how this list becomes deals
