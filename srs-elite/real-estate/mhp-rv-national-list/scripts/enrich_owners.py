#!/usr/bin/env python3
"""Owner lookup + skip-trace prep for the scored MHP/RV shortlist.

Automated sources (public, no API key):
  FL  — Florida DOR statewide cadastral (all 67 counties): owner name,
        mailing address, last sale year/price, just value, via ArcGIS REST.
  AZ  — Maricopa County assessor parcel search API.

Everything else gets a prefilled county-portal LOOKUP_URL for manual/VA work.

Usage:
  python3 enrich_owners.py --input top_1000_shortlist.csv --top 250 --outdir .
  python3 enrich_owners.py ... --offline   # skip network, just build workbook

Outputs:
  top_<N>_enrichment_workbook.csv  one row per park, owner fields filled where
                                   an API match was found, STATUS + LOOKUP_URL
  skip_trace_upload.csv            individual owners w/ mailing address, ready
                                   for BatchSkipTracing/PropStream upload
  entity_owners.csv                LLC/trust/corp owners -> registered-agent
                                   lookup (Sunbiz URL prefilled for FL)
"""
import argparse
import csv
import json
import re
import time
import urllib.parse
import urllib.request

FL_CADASTRAL = ("https://services9.arcgis.com/Gh9awoU677aKree0/arcgis/rest/"
                "services/Florida_Statewide_Cadastral/FeatureServer/0/query")
MARICOPA_SEARCH = "https://mcassessor.maricopa.gov/parcel/search"

ENTITY_PAT = re.compile(
    r"\b(LLC|L L C|INC|CORP|LP|LLP|LTD|TRUST|TR|TRUSTEE|PARTNERSHIP|"
    r"PROPERTIES|HOLDINGS|INVESTMENTS|ENTERPRISES|CO-OP|COOP|ASSN|"
    r"ASSOCIATION|CHURCH|CITY OF|COUNTY)\b")

COUNTY_PORTALS = {
    ("AZ", "MARICOPA"): "https://mcassessor.maricopa.gov/",
    ("AZ", "YAVAPAI"): "https://yavapaiaz.gov/departments/assessor",
    ("AZ", "PINAL"): "https://www.pinalcountyaz.gov/Assessor",
    ("SC", "HORRY"): "https://www.horrycountysc.gov/apps/landrecords/",
    ("SC", "LEXINGTON"): "https://lex-co.sc.gov/departments/assessor",
    ("SC", "GREENVILLE"): "https://www.greenvillecounty.org/appsas400/votaxqry/",
    ("SC", "YORK"): "https://www.yorkcountygov.com/309/Assessor",
    ("SC", "CHARLESTON"): "https://sc-charleston.publicaccessnow.com/",
    ("SC", "BERKELEY"): "https://berkeleycountysc.gov/dept/assessor/",
    ("TN", None): "https://assessment.cot.tn.gov/RE_Assessment/",
    ("NC", "WAKE"): "https://services.wake.gov/realestate/",
    ("NC", "MECKLENBURG"): "https://property.spatialest.com/nc/mecklenburg/",
    ("NC", "BRUNSWICK"): "https://tax.brunswickcountync.gov/itsnet/",
    ("NC", "PENDER"): "https://www.pendercountync.gov/tax/",
    ("NC", "HARNETT"): "https://www.harnett.org/tax/",
    ("NC", "JOHNSTON"): "https://taxpay.johnstonnc.com/taxes/search",
    ("NC", "CABARRUS"): "https://www.cabarruscounty.us/departments/tax-administration",
    ("NV", "CLARK"): "https://maps.clarkcountynv.gov/assessor/AssessorParcelDetail/",
    ("NV", "WASHOE"): "https://www.washoecounty.gov/assessor/online_data/",
    ("TX", "COMAL"): "https://esearch.comalad.org/",
    ("TX", "PARKER"): "https://esearch.parkercad.org/",
    ("TX", "FORT BEND"): "https://esearch.fbcad.org/",
    ("TX", "ELLIS"): "https://esearch.elliscad.com/",
    ("TX", "JOHNSON"): "https://esearch.johnsoncad.com/",
    ("TX", "GUADALUPE"): "https://esearch.guadalupead.org/",
    ("TX", "MONTGOMERY"): "https://esearch.mcad-tx.org/",
    ("AL", "BALDWIN"): "https://baldwincountyal.gov/departments/revenue-commission",
    ("AL", "LEE"): "https://leecountyrevenuecommissioner.com/",
    ("GA", "GWINNETT"): "https://gwinnettassessor.manatron.com/IWantTo/PropertyGISSearch.aspx",
    ("GA", "HENRY"): "https://qpublic.schneidercorp.com/Application.aspx?AppID=735",
    ("ID", "ADA"): "https://adacounty.id.gov/assessor/property-search/",
    ("ID", "CANYON"): "https://www.canyoncounty.id.gov/elected-officials/assessor/",
    ("ID", "KOOTENAI"): "https://www.kcgov.us/149/Assessor",
    ("UT", "UTAH"): "https://www.utahcounty.gov/LandRecords/",
    ("UT", "SALT LAKE"): "https://slco.org/assessor/new/query/interactive.cfm",
}


def lookup_url(state, county, name, city):
    url = COUNTY_PORTALS.get((state, county)) or COUNTY_PORTALS.get((state, None))
    if url:
        return url
    q = urllib.parse.quote_plus(f"{county} county {state} property search {name} {city}")
    return f"https://www.google.com/search?q={q}"


def get_json(url, params, retries=3):
    qs = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{qs}", headers={
        "User-Agent": "Mozilla/5.0 (owner-research script)",
        "Accept": "application/json"})
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(2 * (i + 1))


def norm_street(addr):
    """'1210 CALVARY ROAD' -> ('1210', 'CALVARY') for LIKE matching."""
    parts = addr.strip().upper().split()
    if len(parts) >= 2 and parts[0][0].isdigit():
        street = parts[1]
        if street in {"N", "S", "E", "W", "NE", "NW", "SE", "SW", "NORTH",
                      "SOUTH", "EAST", "WEST"} and len(parts) >= 3:
            street = parts[2]
        return parts[0], street
    return None, None


def fl_lookup(row):
    num, street = norm_street(row["ADDRESS"])
    if not num:
        return None
    where = (f"PHY_ADDR1 LIKE '{num} %{street}%' "
             f"AND PHY_CITY = '{row['CITY'].upper()}'")
    fields = ("PARCEL_ID,OWN_NAME,OWN_ADDR1,OWN_ADDR2,OWN_CITY,OWN_STATE,"
              "OWN_ZIPCD,DOR_UC,JV,SALE_YR1,SALE_PRC1,PHY_ADDR1,PHY_CITY")
    data = get_json(FL_CADASTRAL, {
        "where": where, "outFields": fields, "returnGeometry": "false",
        "resultRecordCount": 5, "f": "json"})
    feats = data.get("features") or []
    if not feats and row["ZIP"]:
        where = f"PHY_ADDR1 LIKE '{num} %{street}%' AND PHY_ZIPCD LIKE '{row['ZIP']}%'"
        data = get_json(FL_CADASTRAL, {
            "where": where, "outFields": fields, "returnGeometry": "false",
            "resultRecordCount": 5, "f": "json"})
        feats = data.get("features") or []
    if not feats:
        return None
    # prefer the mobile-home-park use code (FDOR DOR_UC 028) if present
    feats.sort(key=lambda f: 0 if str(f["attributes"].get("DOR_UC", "")).strip()
               in ("028", "28") else 1)
    return feats[0]["attributes"]


def maricopa_lookup(row):
    data = get_json(MARICOPA_SEARCH, {
        "q": f"{row['ADDRESS']} {row['CITY']}"})
    results = (data or {}).get("results") or (data if isinstance(data, list) else [])
    if not results:
        return None
    r0 = results[0]
    return {
        "PARCEL_ID": r0.get("APN") or r0.get("apn"),
        "OWN_NAME": r0.get("Owner") or r0.get("ownerName"),
        "OWN_ADDR1": r0.get("OwnerAddress") or "",
        "OWN_CITY": "", "OWN_STATE": "", "OWN_ZIPCD": "",
        "SALE_YR1": r0.get("SaleDate", ""), "SALE_PRC1": r0.get("SalePrice", ""),
        "JV": r0.get("FCV", ""), "DOR_UC": r0.get("PropertyType", "")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--top", type=int, default=250)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--offline", action="store_true",
                    help="skip network lookups; just build the workbook")
    ap.add_argument("--year", type=int, default=2026,
                    help="current year for tenure calc")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.input, encoding="utf-8")))[:args.top]
    out_rows, skip_rows, entity_rows = [], [], []
    hits = 0

    for i, row in enumerate(rows):
        state, county = row["STATE"], row["COUNTY"]
        rec = {**{k: row[k] for k in ("NAME", "ADDRESS", "CITY", "STATE", "ZIP",
                                      "TELEPHONE", "COUNTY", "UNITS", "SIZE",
                                      "TOTAL_SCORE")},
               "OWNER_NAME": "", "OWNER_MAIL_ADDR": "", "OWNER_MAIL_CITY": "",
               "OWNER_MAIL_STATE": "", "OWNER_MAIL_ZIP": "", "PARCEL_ID": "",
               "LAST_SALE_YR": "", "LAST_SALE_PRICE": "", "JUST_VALUE": "",
               "TENURE_YRS": "", "OWNER_TYPE": "", "ABSENTEE": "",
               "STATUS": "needs manual lookup",
               "LOOKUP_URL": lookup_url(state, county, row["NAME"], row["CITY"])}

        attrs = None
        if not args.offline:
            try:
                if state == "FL":
                    attrs = fl_lookup(row)
                elif state == "AZ" and county == "MARICOPA":
                    attrs = maricopa_lookup(row)
            except Exception as e:
                rec["STATUS"] = f"lookup error: {type(e).__name__}"
            time.sleep(0.5)

        if attrs and attrs.get("OWN_NAME"):
            hits += 1
            own = str(attrs["OWN_NAME"]).strip()
            mail = " ".join(str(attrs.get(k) or "").strip()
                            for k in ("OWN_ADDR1", "OWN_ADDR2")).strip()
            rec.update({
                "OWNER_NAME": own, "OWNER_MAIL_ADDR": mail,
                "OWNER_MAIL_CITY": str(attrs.get("OWN_CITY") or "").strip(),
                "OWNER_MAIL_STATE": str(attrs.get("OWN_STATE") or "").strip(),
                "OWNER_MAIL_ZIP": str(attrs.get("OWN_ZIPCD") or "").strip(),
                "PARCEL_ID": str(attrs.get("PARCEL_ID") or ""),
                "LAST_SALE_YR": str(attrs.get("SALE_YR1") or ""),
                "LAST_SALE_PRICE": str(attrs.get("SALE_PRC1") or ""),
                "JUST_VALUE": str(attrs.get("JV") or ""),
                "STATUS": "auto-filled"})
            try:
                yr = int(float(rec["LAST_SALE_YR"]))
                if 1900 < yr <= args.year:
                    rec["TENURE_YRS"] = args.year - yr
            except (ValueError, TypeError):
                pass
            is_entity = bool(ENTITY_PAT.search(own.upper()))
            rec["OWNER_TYPE"] = "entity" if is_entity else "individual"
            park_city = row["CITY"].strip().upper()
            rec["ABSENTEE"] = ("yes" if rec["OWNER_MAIL_CITY"] and
                               rec["OWNER_MAIL_CITY"].upper() != park_city
                               else "no")
            if is_entity:
                sunbiz = ("https://search.sunbiz.org/Inquiry/CorporationSearch/"
                          "ByName" if state == "FL" else "")
                entity_rows.append({"PARK_NAME": row["NAME"], "OWNER_NAME": own,
                                    "STATE": state,
                                    "REGISTERED_AGENT_LOOKUP": sunbiz or
                                    rec["LOOKUP_URL"]})
            else:
                parts = own.replace("&", " ").split()
                skip_rows.append({
                    "FirstName": parts[1] if len(parts) > 1 else "",
                    "LastName": parts[0] if parts else "",
                    "MailingAddress": mail,
                    "MailingCity": rec["OWNER_MAIL_CITY"],
                    "MailingState": rec["OWNER_MAIL_STATE"],
                    "MailingZip": rec["OWNER_MAIL_ZIP"],
                    "PropertyAddress": row["ADDRESS"],
                    "PropertyCity": row["CITY"],
                    "PropertyState": state, "PropertyZip": row["ZIP"],
                    "ParkName": row["NAME"],
                    "ParkPhone": row["TELEPHONE"]})
        out_rows.append(rec)
        if (i + 1) % 25 == 0:
            print(f"{i+1}/{len(rows)} processed, {hits} auto-filled")

    def dump(path, data, fields):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(data)

    n = len(rows)
    dump(f"{args.outdir}/top_{n}_enrichment_workbook.csv", out_rows,
         list(out_rows[0].keys()))
    if skip_rows:
        dump(f"{args.outdir}/skip_trace_upload.csv", skip_rows,
             list(skip_rows[0].keys()))
    if entity_rows:
        dump(f"{args.outdir}/entity_owners.csv", entity_rows,
             list(entity_rows[0].keys()))
    print(f"done: {n} parks, {hits} auto-filled, "
          f"{len(skip_rows)} individual owners -> skip_trace_upload.csv, "
          f"{len(entity_rows)} entity owners -> entity_owners.csv")


if __name__ == "__main__":
    main()
