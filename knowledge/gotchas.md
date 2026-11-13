# Gotchas & data pitfalls (check before trusting a number)

## BigQuery / data model
- Contracts live in **Mongo `companies.contracts` JSON**, not `tidb_prod.companies_contract` (doesn't exist).
- `tidb user_subscriptions.status` active value is **'paid'**.
- `companies.status` = "active" for every company — never filter on it. Ignore `users.status`, `users.subscribe`.
- `NOT flag` drops NULLs — wrap in `IFNULL`. Use `SAFE_CAST(x AS DATE)`, not `SAFE.DATE`.
- `LAG … IGNORE NULLS` is unsupported; correlated subqueries rejected → use `LAST_VALUE … IGNORE NULLS` window.
- `allowWidgets` ≠ paying for Lead Magnet. `allowLocationSourcing` = CBE (not `sourcingAndUnderwriting`).
- Value-1 contracts are not customers by default (child paid by parent / order-billed / trial / internal).
- Sign-up placeholder companies carry label CASAFARI but are **not** internal (inbound non-converted).
- ~7,000 C21 users at active offices have no paid sub — per-user companies need the paid-sub check.
- Split contract ownership: weight by `owners.*.part`.
- Gross churn isn't visible in contracts (lost renewals create none).
- Listings: exclude quarantine/deprecated sources (huge stale "active" counts). Portal by **domain**.
  `estates.province_id` ≠ locations ids. `seen_at`=0; `updated_at` ≠ staleness. Idealista ES = `www.idealista.com`.
- API logs: neither table complete — merge both. Fingerprint not unique. `application@casafari.com` ≈ 20% internal traffic.
- Platform: use `meter_snapshots.trial_consumed` (not usage_daily) for trial usage; stable ORDER BY when paging;
  md5-check datasets that routines retype.
- Legal postcode exists for only ~38% of contacts; company city often = franchise HQ.

## HubSpot
- `query_crm_data`: ≤2 GROUP BY dims, extras dropped silently; counts may sum IDs.
- Missing deal country; churn-pipeline deals marked closed-won; €0 lost deals from bulk cleanup.
- Owner-based email search misses emails logged under another owner; keyword search misses unlabelled questions.

## Slack / Gmail / Drive
- Slack API can't see unread state → mentions + DMs + channel reads + **thread reads**; `oldest` filter misses replies.
- Agents post in channels (Mira, Themis, Billy's own agents) — check before flagging something as open.
- Gmail connector: one thread per call, two calls per move → expensive at scale; can't create filters.
- Connectors can't fetch large Slack/Gmail attachments.
- Slack `oldest` is epoch seconds: 11 Nov 2026 00:00 UTC = 1794355200 (not 1762819200, which is 2025). Compute with `date -d` before briefing sub-agents.
- Mention search with `<@U025P35JVMH>` returned only Postmark noise (13 Nov); search the plain keyword/name too.
- Mailcleanup converts non-ASCII to "?".

## Postmark
- 45-day message retention; most clicks are security scanners; opens inflated by Apple MPP; server is Live.
- Lifetime bounce 12.08% (> ~10% review threshold) because of May 20 & Jul 30 sends.

## Environment
- Sandbox files vanish when the session ends — persist to Drive/artifact/this repo.
- External CDNs may be blocked in the sandbox → inline JS libs in HTML.
- Very large single HTML (>2 MB) may not open on Billy's device — pack data column-wise.
- Scheduled tasks: connectors must be added manually by Billy; don't manually fire on a scheduled morning (double posts).
