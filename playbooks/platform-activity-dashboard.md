# Playbook: Platform activity dashboard (self-serve API/MCP platform)

- **Autonomy level:** see `_registry.md` (already scheduled)
- **Cadence / scheduled tasks:**
  - `trig_01TbzUCqEjraVaiXYCdkt55X` "Refresh Platform activity" — daily 07:36 Lisbon, fresh session,
    no connectors (no HubSpot) — re-runs 6 datasets (kpis, funnel, daily, products, agents, orgs).
  - `trig_01B1sTeLoUcru82S1bS1GHsd` "Platform activity morning update" — weekdays 08:05 Lisbon, fires into
    the "Platform Activity" session: verify refresh + md5, fetch HubSpot, build, render check, send HTML,
    reply with summary (action items first, 2–4 bullets).
- **Output:** dashboard https://claude.ai/artifact/AAjCBWNqUYL9c8h14xyMaV + HTML snapshot (always both —
  "update all outputs").
- **Trend:** 23 Oct → 12 Nov: sign-ups 54 → 418; paying orgs 2 → 10; revenue €90 → €1,772; calls 1,078 → 10,319.
  49 prospect deals, 14 matched.

## Data (BigQuery `casafari-cloud.casafari_platform`)
- accounts, accounts_daily_snapshot (`is_internal`), usage_daily (`calls`, `billed_calls`, `units_billed`,
  `channel` mcp/rest, `product`), meter_snapshots (`trial_consumed`), invoices (`status='paid'`,
  `subtotal_cents`), api_keys, oauth_grants, oauth_clients.
- Customers = not internal in accounts AND never internal in daily snapshot.

## Funnel
Signed up → connected key/agent (api_keys ∪ oauth_grants) → made a call → billed call →
used ≥25% free tokens (`meter_snapshots.trial_consumed / trial_units`) → paid.

## KPIs
Sign-ups, active orgs (calls>0), paying orgs, revenue = SUM(subtotal_cents)/100, calls,
tokens = SUM(units_billed), free-token usage = SUM(trial_consumed)/SUM(trial_units).

## HubSpot prospect matching (sales redirected prospects to self-serve)
Deal props `platform_prospect`, `platform_prospect_email`, `platform_prospect_company_name`;
contact props `platform_account_id`, `hs_email_domain`.
Match order: **contact Account_ID → email domain(s) in prospect email → company name.**
Org name = sign-up email domain; "Personal" = consumer email (≈ half) — show HubSpot domain in grey.

## Rules
- HTML excludes names and full emails — account IDs, deal names, domains only.
- Verify the datasets against BigQuery with an MD5 fingerprint (routine runs retype rows).
- Tool returns max 50 rows → page with `ORDER BY TO_JSON_STRING(t) LIMIT 50 OFFSET n` (stable order).

## Data-quality flags for sales (open)
Test deal still flagged prospect; a casafari.com account not marked internal; E&V Rheinland matches 3
accounts, Mundo Franquicia 2 — need Account_ID on contacts; Gmail deals match only via Account_ID.
