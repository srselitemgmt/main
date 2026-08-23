---
tags: [tax, reps, audit, automation, stacy]
aliases: ["REP Tracking Audit", "REP Hours Audit 2026"]
updated: 2026-08-13
---

# Stacy's REP Hour Tracking — Automation & Log Audit (2026-08-13)

**Summary**: Deep-dive review of every automation and artifact behind Stacy's REP hour tracking. The system is well-designed — actual-time entries, a reconciliation log with evidence citations, standing correction directives — but it is **broken in ways that currently threaten the 2026 REP claim**: the pipeline has logged nothing since **July 10** (5 weeks), the weekly cron **failed on every recorded run** and alerts no one, the year-end pace projects to roughly **665 hours — under the 750 floor**, and the logged 564.54 hours contain **~65+ hours of non-qualifying or double-counted entries** plus a composition problem (webinar-heavy) that an auditor would attack first. Findings ranked below, with fixes.
**Scope**: `Stacy_Schubert_REP_Hours_Log_2026.xlsx`, `rep-hours-cron.log`, local `sync.py`/`SKILL.md` (via reconciliation-log references), Google Calendar sources, prior sheets, prior-AI documents. **Not inspected**: claude.ai Routines (tool approval unavailable this session) and the live local files in `~/Desktop/ai-os-blueprint` (local machine, not reachable from this environment) — both flagged below.
**Related**: [[reps-real-estate-professional-status]] · [[tax-mitigation-master-plan]]

## The system as built (inventory)

| Component | Location | State | Last activity |
|---|---|---|---|
| **Master hours log** — `Stacy_Schubert_REP_Hours_Log_2026.xlsx` | Google Drive | 274 entries, **564.54 hrs** YTD, with Category/Property summaries and a **Reconciliation Log** | Last entry **7/10**; last modified **7/11** |
| **Weekly cron** — `rep-hours-cron.log` | Local machine → Drive | **Every recorded run failed** ("ERROR: Calendar pull failed", Sundays 12:03) | Last log line **5/3** |
| **`sync.py` + `SKILL.md`** (rep-hours skill) | Local machine `~/Desktop/ai-os-blueprint` | Patched **7/8** per reconciliation log (aviation-exclusion filter; Toggl-actuals directive). **Drive mirrors are wrong/stale** — the Drive `sync.py` is actually a stray httpcore library file | Unknown since 7/11 |
| **Data sources** | Google Calendar ×5 (primary, Owners Club 2026, OC Level 1, SubTo Bonus, Colorado) + **Toggl** timers | Reachable, healthy | Live |
| **Prior sheets** | `REP Time Sheet 2025`, `January 2026 Meetings & REP Hours` | Superseded (uniform scheduled-time blocks; replaced by actuals methodology) | Jan 2026 |
| **Prior-AI documents** | Drive: `grouping-election-statement.md`, `decision-tree-nonpassive-path.md`, `CONTEXT-DUMP.md` | Sound; now merged into this vault — see [[reps-real-estate-professional-status]] | Apr 2026 |

**Standing directives recovered from the reconciliation log** (these are working policy and are preserved going forward):
1. **Toggl actuals trump calendar-scheduled times** (Ryan, 2026-07-08)
2. **Remove aviation false positives** — Ryan's United events are not Stacy's real property services (standing Q1 action)
3. Corrections go through the Reconciliation Log with evidence source, old/new values, and approver — never silent edits. *This is genuinely good audit hygiene; keep it.*

## Findings, ranked

### F1 — CRITICAL: the pipeline has been dead for 5 weeks
No entries since **7/10**. The weekly cron failed with "Calendar pull failed" on **all five recorded runs** (4/7 → 5/3) and then stopped logging entirely; the July entries that do exist came from manual/AI sessions, not the cron. Nothing alerts anyone when the pipeline fails — the gap was silent.

**Recoverable now**: the primary calendar shows **21 candidate events ≈ 20.7 hours** in the gap window (7/11–8/13): recurring `POD 12 - OC-L1 Office Hours` (×5), `Pod 12 Office Hours with Rayce` (×5), `Doran's office meeting` (×5), `CAPTAIN + POD MEETING` (×5), and one `DealSauce skip trace — top 250 MHP/RV park targets` (0.5). The OC/SubTo bonus calendars and Toggl need the same sweep before entries are final. ("Before School Checkin" 8/7 is personal — excluded.)

### F2 — CRITICAL: pace projects **below 750**
564.54 logged + ~21 recoverable ≈ **585 hours** through 8/13, with ~20 weeks left. Reaching 750 needs **~8.2 hrs/week**; the visible calendar cadence is running **~4 hrs/week** since June. Straight-line projection: **~665 hours — a fail.**

The gap is closable, because her *real* work is under-captured (see F3): acquisition negotiations, tenant management, CRM/lead follow-up mostly never hit a calendar, so the calendar-driven pipeline never sees them. The fix is behavioral + mechanical: **Toggl timers on all non-calendar work**, and the weekly digest showing pace-vs-target so a shortfall is visible in September, not December.

### F3 — CRITICAL: hour composition is audit-weak
75.2% of logged hours sit in a generic "Lead Generation" bucket, and the bulk of entries are **webinars, community Zooms, and training sessions** (Daily Dial, BONUS classes, summits, semester sessions). Under audit, education/seminar and investor-type hours are the first thing struck — Tax Court has repeatedly disallowed them as personal services in a real property trade or business — and if the webinar block goes, the 750 collapses.

Meanwhile the log **under-represents her strongest hours**: seller negotiations (Bjorn/420 Starway, Tyler/Winding Dr), underwriting with named counterparties, tenant management, property visits. Those are exactly the operational hours that survive audits.

→ **Reweight both the work and the logging.** Target: operational categories (acquisition, negotiation, management, financing) ≥ 60% of hours by year-end. Log the real work she already does; treat community Zooms as the garnish, not the meal.

### F4 — HIGH: ~65+ hours of non-qualifying or suspect entries in the log
| Entries | Hours | Problem |
|---|---|---|
| `Drivers Education` ×4 (5/29–6/1) | **29.45** | Almost certainly Tucker's driver's-ed shuttle — not real property services. Remove or re-justify. |
| Tax / Entity Strategy meetings (Karlton Dennis, Tax Alchemy, Candice Castner, Trina, summits…) | **28.67** | Investor-type activity under Reg. §1.469-5T(f)(2)(ii) — managing one's own tax position is not a real property trade or business. Presumptively strike. |
| `ST – 737 Stand-Down Meeting (Nix/Juhl)` (5/19) | 1.70 | Ryan's United Airlines event — the 7/8 aviation filter's pattern missed it. Patch the filter (`737`, `stand-down`, fleet codes). |
| `Colorado Water Law` (6/11) | 4.02 | Education; weak unless tied to a specific deal's due diligence. |
| `New Event` (5/14, 11 PM) | 1.07 | No description — worthless in audit. Describe or delete. |
| `Vitalant Ryan` (3/24) | 0.33 | Blood-donation errand. Remove. |
| `Ryan meeting` / `Ryan Shubert and Jeremy Werden` etc. | ~0.2 | No REP-relevant description. |

Purging these takes defensible hours to roughly **500–520**, which widens the F2 shortfall to ~250 hours — the two findings compound. Better to purge now and manage pace deliberately than have an auditor do the purging later.

### F5 — HIGH: overlapping time blocks
Multiple same-day entries overlap (e.g., 1/5 East Coast dial 4:59–8:03 **and** West Coast 7:00–9:46; 1/6 6:49–9:12 and 8:46–11:24; 4/22 has five stacked 0.5-hr EXP classes 6:55–9:26 while also meeting "Bjorn Seller #2" 6:30–7:24). Double-counted minutes are a classic credibility kill — courts treat impossible schedules as evidence the whole log is reconstructed. → Add an **overlap detector** to the sync (flag any entry intersecting another same-day entry) and reconcile via the Reconciliation Log.

### F6 — MEDIUM: the >50% test has no denominator
The log tracks the 750-hour numerator but not **total personal services**. For Stacy the ratio should be trivially satisfied (real estate is her only occupation) — but an audit-ready file states that affirmatively. → One line in the annual REP memo: her total personal-service hours and the absence of other employment, signed with the CPA.

### F7 — MEDIUM: the workbook's summaries disagree
Category summary totals **564.54**; property summary totals **551.35** (13.19 orphaned — summary ranges not extended as rows were added). Cosmetic, but an examiner notices arithmetic that doesn't tie. → Fix the ranges; add a self-check row (category total = property total = entry total).

### F8 — MEDIUM: no failure alerting, single-machine dependency
The cron failed for a month with zero notification, and the whole pipeline depends on one local machine being awake on Sundays. → Move the weekly job to a **cloud Routine** (spec below) whose *first duty* is freshness-checking the log and **alerting when something is wrong**, independent of whether the local sync runs.

### F9 — LOW: housekeeping
Log header still shows SSN placeholder (fine — keep it out of Drive); entity shown is SRS Elite Mgmt LLC only, while the [[reps-real-estate-professional-status#The second step everyone misses|grouping election]] must list **every** SPE (per the Dan Gunther JV structure, Stacy is managing member on all held-property SPEs — the log's Property column should map 1:1 to those SPEs and EINs when the election is filed).

## Audit gaps I could not close from this session
- **claude.ai Routines/scheduled tasks** — the trigger-listing tool required an interactive approval this autonomous session couldn't provide. If any old REP-related Routine exists there, it should be found and reconciled with the new one below.
- **The live `sync.py`/`SKILL.md`** on the local machine — I could only see their behavior through the reconciliation log. The Drive "backup" of `sync.py` is the wrong file entirely (an httpcore library module) — whatever backed it up grabbed a venv file. → Re-mirror the real skill files to Drive or, better, commit them to this repo under `srs-elite/tax-strategy/tooling/`.

## The go-forward tracking system

**Design principle: the cloud watches, the log stays canonical, silence is never assumed to be health.**

1. **Weekly cloud Routine (Sunday evening)** — runs in a fresh session, independent of the local machine:
   - Pull the week's events from all 5 calendars; filter through the qualifying rules (aviation exclusions **including flight-ops patterns like "737"**, personal-event exclusions, ≤7-day STR notes)
   - Cross-check log freshness (last entry date vs. today) and **compute pace vs. 750**
   - Draft the weekly digest to contact@srselitemgmt.com: candidate entries, flags (overlaps, non-RE strays, missing descriptions), pace status, and any "PIPELINE STALE" alert
   - Ryan approves; approved entries land in the xlsx with the Reconciliation Log untouched policy
2. **Monthly quality pass** — category mix (operational ≥ 60% target), overlap scan, description completeness
3. **Quarterly** — reconcile Toggl actuals vs. calendar per the standing directive; CPA-facing pace memo
4. **Annually** — REP memo (hours, >50% affirmation, methodology) with Zach Fox; grouping-election property list refresh

## Routine created (2026-08-13) — one step left

A weekly cloud Routine now exists: **`trig_01UxvoQ2GU7Y8rM5TbfopRCH` — "Stacy REP Hours — Weekly Tracker & Pipeline Watchdog"**, firing **Sundays ~6:11 PM MT** (first run 8/16), with push + email notifications on completion. Each run: pulls the week from all 5 calendars, applies the qualifying/exclusion rules (aviation patterns including `737`/`stand-down`, personal events, tax-strategy meetings), checks log freshness, computes pace vs. 750, and leaves a Gmail **draft** digest for Ryan's approval — it never edits the xlsx itself.

> [!warning] One-time step needed from Ryan
> Routines created from this coding session **cannot carry the Google connector grants**, so until fixed the weekly run will fire and loudly report "Calendar/Drive/Gmail tools unavailable" (by design — failures are never silent) but can't build the digest. **Fix (~1 minute): open claude.ai → Settings → Routines → "Stacy REP Hours — Weekly Tracker & Pipeline Watchdog" → edit and enable the Google Calendar, Google Drive, and Gmail connectors → save.** Alternatively, ask Claude in a claude.ai chat (where connectors are live) to recreate the Routine from this note's spec, then delete the old trigger ID above.

## Fix list (ordered)

- [ ] **Rebuild 7/11–8/13 from calendars + Toggl** (~21 hrs candidate from primary alone; sweep OC/SubTo calendars too) — via the Reconciliation Log, evidence-cited
- [ ] **Purge/reclassify F4 entries** (~65 hrs) through the Reconciliation Log — before anyone relies on the totals
- [ ] **Patch the aviation filter** for the 5/19 miss pattern (`737`, `stand-down`, pairing codes)
- [ ] **Enable connectors on the weekly Routine** (see box above) — the only step between here and a working watchdog
- [ ] **Start Toggl timers on non-calendar work** — negotiations, tenant management, CRM time; this is what closes the F2 gap with strong hours
- [ ] Fix workbook summary ranges + add tie-out check (F7)
- [ ] Add overlap detection to sync.py (F5)
- [ ] Commit the real sync.py/SKILL.md to this repo (F8/gap)
- [ ] Add the >50% denominator line to the annual memo (F6)
- [ ] September checkpoint with Zach Fox: pace, composition, and whether 2026 REP is claimable on the trajectory — **decide by Q3-end, not at filing time**

**Related**: [[reps-real-estate-professional-status]] · [[tax-mitigation-master-plan]] · [[household-timeline]]
