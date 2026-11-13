# Playbook: Data operations monthly cost structure

- **Autonomy level:** see `_registry.md`
- **Cadence:** ad hoc; re-runnable monthly with fresh invoices + activity exports
- **Output destination:** xlsx + short summary — deliver as attachment **and** upload to Billy's Drive
  (never just a sandbox path)
- **Last run:** 2026-10-26 — €43,899/month — `history/2026-10-26-data-ops-cost-structure.md`

## Purpose
Monthly cost of data collection & processing split by pipeline, country and residential/commercial,
to support the agentic rebuild of data ops (one agent per pipeline).

## Pipelines
- **A — DQA**: source research & job creation (new-source jobs, fix jobs)
- **B — DC**: adding/fixing sources (parsers). B1 new build, B2 maintenance
- **C — Crawling**: proxy IPs (datacenter/residential), unblocker services, servers
- **D — Ingestion & processing** up to data science (the "MVP project"): GCP servers + people

## Inputs
- Payroll xlsx (DQA & DC): name, title, team, manager, country, gross salary (annual, EUR assumed)
- `[dqa] new source jobs`, `[dqa] source fix jobs creations`, `[dc] jobs by status` CSVs (last 365 days)
- `crawling settings` xlsx (~8,900 sources; listings last 3 complete months; **drop final totals row**)
- Drive folder `15beyh7kd1h0Qdg5LP6tcNcOKRyYT4-sl`: Oxylabs SoW + invoices, BrightData order form +
  invoices, `gcp costs.xlsx` (tab Namespaces; use column C "Data & Processing (Pre-DS)")

## Steps
1. Build an explicit name-mapping table payroll ↔ activity reports (diminutives/transliterations);
   confirm uncertain matches with Billy. Report names missing from payroll = leavers → no cost.
2. People cost per month = annual gross / 12, allocated by job counts per person, split country × type by
   each person's commercial/residential *ratio*.
3. DC closed rule: for Status = closed, count only "Jobs with Config Changes" + "Jobs with Fixed comment
   (no Config changes)" — the rest are system auto-closed.
4. Crawling: monthly run-rate from invoices (Oxylabs: exclude one-off commitment top-ups; use post-Aug
   prices), allocate to country × type by listings × crawler roles.
5. D: GCP column C as servers; named developers as D people.
6. Produce workbook: Summary, Country_Type, A_DQA, B_DC, C_Crawling, C_Source_Detail, D_Processing,
   Assumptions_Caveats ("Confirmed by user" / "Remaining caveats"). Recalculate & tie out.

## Definitions & rules (confirmed by Billy)
- **Monthly**, not annualised. FX placeholder 1.17 USD/EUR unless told otherwise.
- **No "AI" wording for crawling.** Use invoice terms: "Proxy IPs (Datacenter / Residential)",
  "Unblocker services (BrightData Web Unlocker, Oxylabs Web Unblocker)".
- "All Listings Created – Commercial/Residential" is a per-person total repeated on every row — use as
  ratio only, never sum.
- Contract floors: BrightData $9,500/mo commit (12 mo from 1 Feb 2026, non-cancellable);
  Oxylabs €8,000/mo minimum (12 mo, auto-renew). Savings on unblockers need renegotiation first.

## Quality checks
- [ ] Workbook totals tie out across tabs; no formula errors after recalc.
- [ ] Month-over-month change per pipeline within ±20% or explained.
- [ ] Every unmatched name listed in caveats.

## Known pitfalls
- CSV numbers have quoted thousands separators (`thousands=','`).
- `gcp costs.xlsx` covers Jan–Sep with no monthly split; ~46% of col C is shared-cluster overhead.
- D people is a floor (DS/platform staff not in payroll). Netnut, Zenrows, GoProxies: no cost data.
- Cheap execution: Billy wants the smallest model that keeps quality (Sonnet sub-agent worked; Haiku
  too risky for name matching).

## Training notes
- 2026-10-26 · monthly not annual · remove "AI services" wording · DC closed rule · leavers carry no cost.
