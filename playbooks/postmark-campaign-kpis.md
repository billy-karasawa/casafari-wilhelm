# Playbook: Postmark email campaign KPIs

- **Autonomy level:** see `_registry.md`
- **Cadence:** ad hoc, usually after a campaign send
- **Output destination:** chat table (offer an artifact page if it'll be shared)
- **Last run:** 2026-11-11 — see `history/2026-10-29-postmark-campaign-kpis.md`

## Purpose
Report delivery and engagement per campaign (tag) for the marketing broadcast stream, with
bot clicks filtered out.

## Inputs & data sources
- Postmark server **CASAFARI_2026** (ID 19235117), host `api.postmarkapp.com` (proxy-authenticated;
  header `X-Postmark-Server-Token` — the proxy fills it, use a dummy value).
- Streams: `broadcast` = all campaigns; `outbound` = transactional (almost unused).

## Steps
1. `GET /stats/outbound/sends?fromdate=..&todate=..` → find send days.
2. `GET /messages/outbound?count=500&offset=N&fromdate=..&todate=..` per send day → collect tags.
   count+offset is capped at 10,000: split the time window recursively until each chunk ≤ 9,500.
3. `GET /stats/outbound?tag=<tag>` (add `&messagestream=broadcast`) per tag.
4. `GET /messages/outbound/clicks?count=500&offset=N&tag=<tag>` → click events (capped at 10k; if more,
   estimate from the sampled share and say so).
5. Apply the bot filter, compute KPIs, rank campaigns.

## Definitions
- Tag pattern `<Campaign><wave>_<Segment>_<Lang>` — e.g. `BusinessBeats1_Churned_IT`.
  Segments: Churned, ClosedLostDeals, Activeweb. `-test` suffix = test sends (exclude).
- Delivered = Sent − Bounced · Bounce % = Bounced / Sent · Open % = UniqueOpens / Delivered
- Raw CTR = UniqueLinksClicked / Delivered (can exceed 100% — unique *links*, not people)
- CTOR = UniqueLinksClicked / UniqueOpens
- **Real CTR** = likely-human unique clickers / Delivered. A message counts as bot/scanner if it clicked
  ≥3 distinct links within 120 s of the first click, or hit unsubscribe plus ≥3 other links.

## Quality checks
- [ ] Exclude `-test` tags.
- [ ] Flag any send with bounce > 5%; flag account lifetime bounce vs Postmark's ~10% review threshold.
- [ ] State that opens are inflated by Apple Mail Privacy Protection.

## Known pitfalls
- Postmark keeps message-level data **45 days only**; older sends are date-only (no tag/subject/clicks).
- Most raw clicks are corporate security scanners (~90% on ai-presentation-builder-2026).
- Server delivery type is **Live** — never send test emails from this server without approval.

## Escalate when
- Lifetime bounce rising or a send > 10% bounce. Suggest list hygiene / webhooks.

## Training notes
- (none yet)
