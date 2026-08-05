# Owner Lookup & Skip Trace — Top 250 Workflow

**Summary**: Workflow for enriching the [[mhp-rv-50k-list|top-250 shortlist]] with owner names, mailing addresses, and tenure, then skip tracing to owner cell/contact. Automated for FL + Maricopa AZ (150 of 250 parks) via `scripts/enrich_owners.py`; manual portal links prefilled for the rest.
**Sources**: FL DOR statewide cadastral (ArcGIS REST), Maricopa County assessor API, county portals
**Last updated**: 2026-08-05

## The pipeline

1. **Owner lookup** (public records, free) → owner name, mailing address, parcel ID, last sale year/price → `data/top_250_enrichment_workbook.csv`
2. **Entity unwrap** (free) → LLC/trust owners resolved to a person via Sunbiz (FL) / state SOS registered-agent search → `data/entity_owners.csv`
3. **Skip trace** (paid, ~$0.10-0.20/record) → owner cell + email from name + mailing address → upload `data/skip_trace_upload.csv` to BatchSkipTracing (or PropStream/ReiSift)
4. Import the enriched workbook into the CRM; sort by TENURE_YRS desc — 15+ year owners are the priority sub-to/seller-carry conversations.

## Step 1: run the lookup script

> Claude's cloud session can't reach assessor sites (network policy blocks non-GitHub hosts), so run this anywhere with normal internet — laptop, or a Claude Code session in an environment with an open network policy:

```bash
cd srs-elite/real-estate/mhp-rv-national-list
python3 scripts/enrich_owners.py --input data/top_1000_shortlist.csv --top 250 --outdir data
```

No API keys needed. What it does:

- **FL parks (125)**: queries the Florida DOR statewide cadastral layer (all 67 counties, updated annually from every county appraiser's roll) by site address. Returns owner name, owner mailing address, DOR use code, just value, last sale year + price. Tenure = 2026 − last sale year.
- **Maricopa AZ (25)**: county assessor parcel search API.
- **Everything else (100)**: leaves STATUS = "needs manual lookup" with the county portal URL in LOOKUP_URL — a VA can clear these at ~2-3 min each (TN is one statewide portal; SC/NC/NV/TX portals are prefilled).
- Address matching is fuzzy (house number + street name), so expect ~80-90% auto-match on FL; misses fall back to manual.

## Step 2: entity owners

Parks owned by an LLC/trust land in `entity_owners.csv`. For FL entities, search [Sunbiz](https://search.sunbiz.org/Inquiry/CorporationSearch/ByName) → registered agent / managing member is usually the real owner; use their name + address in the skip trace instead. Mom-and-pop parks held in a family LLC are still terms candidates — the LLC is often just their lawyer's advice, not sophistication.

## Step 3: skip trace

`skip_trace_upload.csv` has the standard columns (FirstName, LastName, MailingAddress..., PropertyAddress...). Upload to BatchSkipTracing / BatchLeads; expect 70-80% hit rate on cells. The park TELEPHONE column from the raw list is the *office/park* line — still useful (the owner often answers at small parks), but the skip-traced cell is the real channel for the seller conversation.

## Prioritization once enriched

Work the workbook in this order:

1. `OWNER_TYPE = individual` + `TENURE_YRS >= 15` + `ABSENTEE = yes` — the classic tired-landlord trifecta
2. Individual + long tenure, local
3. Entity owners after unwrapping (skip obvious operators — 10+ parks under one entity means a portfolio owner, different pitch)
4. `LAST_SALE_PRICE` tiny or zero with old sale year usually means inherited or decades-held — excellent seller-carry candidates (installment sale defers their capital gain)

## Related pages

- [[mhp-rv-investment-strategy]] — the strategy this feeds
- [[mhp-rv-50k-list]] — the source dataset
