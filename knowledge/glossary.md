# Casafari glossary

## Products & surfaces
- **Web app** — the main Casafari application (data in BigQuery `mongodb_app_prod`). Modules: Alerts,
  Metasearch (sourcing), Property Valuation/CMA, Lead Magnet widgets, Location Sourcing (CBE), AI Presentations.
- **Platform** — the self-serve API/MCP platform **developers.casafari.com** (data in `casafari_platform`).
  Live plans since 6 Nov 2026: Free (1,000 tokens), Agent €49, Agency €249 (10k tokens),
  Business €990 (50k tokens; €792/mo yearly). Claro Start €249, Claro AI €500 separate.
  Platform account data owner: Mila. Proposed volume ladder: 500k tokens/yr €12k · 2M €40k · 5M €80k.
- **API** (property data API) — separate paid subscription from the web app. Properties API (dedup, 24–36h lag),
  Alerts API (real time, not dedup, 12 months history, polling), Market Analytics (asking prices, 13–17% above
  notary), Comparables, Valuation. MCP beta = Market Analytics + Comparables. V1 property search off since Sep 2026.
- **CRM API** — different product (Casafari CRM); don't mix with property API.
- **CBE** — Casafari Business Expansion (`allowLocationSourcing`).
- **Feedcruncher**, **CRM** — bundles identified by company labels FEEDCRUNCHER / CASAFARICRM.
- **Lead Magnet** — lead-gen widget for agency sites; HubSpot line items "Lead Magnet – Broker/Agent".
- **Black Friday 2026** — token bonus codes (not price discounts): BLACKFRIDAY30 (+30% to 23 Nov),
  BLACKFRIDAY25 (+25% to 30 Nov). UTM campaigns `black-friday-2026`, `black-friday-2026-e1`.

## Commercial terms
- **Deal / contract subscription types:** New Business, Up-sell, Cross-sell, Retained, Recovered, Renewal,
  Downsell, NonRecurring, Churn; Partnership – Referral.
- **Contract stage** (Mongo `companies.contracts[].stage`): new (draft), paid, hold, deprecated, cancelled,
  finished. **Won = paid or hold.**
- **Company/user stage** (`employeesStage`, `employees[].stage`): `contract` = active customer;
  `contract_expired` = churned; `contract_hold` = paused with open invoice; `test`/`test_expired`/empty = leads.
- **Self-serve vs sales-led:** < €300 web-app MRR = self-serve.
- **Commission rules (10 Nov 2026):** sales commission only on New Business; AM bonus only on outbound upsell.
- **IAD rule:** don't close IAD agents' single accounts in ES/DE — IAD master deal carries penalties.
- **Data refresh claim (customer-facing):** daily for priority areas, weekly otherwise, major portals only.
- **API commercial norms:** 12-month contracts, 30 days' notice; 10–20% annual-payment discount, 10% bundle
  discount; per-call €0.80–€4.80; DE prices Alerts by population, ES per call, PT/IT bundles.
  Data may be used with AI but not to train models; display/resale/training needs written approval.

## Partners / deals
- **ApiCat / Api.Cat / Tecno API** — Associació d'Agents Immobiliaris de Catalunya reselling All-in-One licences
  (see `playbooks/apicat-licence-monitor.md`). Label **APICAT** = direct customers lost to ApiCat.
- **IAD** — agent network (Polo Properties / Maxime Hueber). **C21** — Century 21 (offices under
  "C21 Portugal/Spain [Integration]"). **Inmovilla** — CRM integration partner (children kept in audiences).
- **PISOS_COMPANY_TRIAL** — Pisos.com partner trial = free web app accounts, not churn.

## Data operations
- **DQA** — Data Quality Assurance: new-source & fix jobs, manual listing fixes, property merge/split.
- **DC** — Data Collection: parsers ("jobs"). Statuses done/closed/cant_implement/open/in_progress.
- **Pipelines A–D:** A DQA · B DC · C crawling (proxies, unblockers, servers) · D ingestion/processing (MVP).
- **Proxy vendors:** BrightData (USD, $9.5k/mo commit), Oxylabs (EUR, €8k/mo minimum), Netnut, Zenrows, GoProxies.
- **Source stages:** live, match, livenomatch (production) · new, prematch · quarantine, deprecated (exclude).
- **classified** (sources): 1 = portal/network, 0 = agency site.

## Email marketing
- Postmark campaign tag `<Campaign><wave>_<Segment>_<Lang>`; segments Churned, ClosedLostDeals, Activeweb.
- **Real CTR** = likely-human clickers / delivered (bot-filtered).

## Internal agents
- **Billience** — Billy's audience-list assistant (#audience-requests). **Mira** — Mila's bot.
  **Themis** — Legal's agent. **Mary by Claude** — Maryna's assistant.
