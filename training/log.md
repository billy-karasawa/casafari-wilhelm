# Training log

Append-only record of what Billy taught or corrected. Newest at the bottom.
Format: `- YYYY-MM-DD · <topic> · <lesson> → filed in <file>`

## Seeded from earlier sessions (Oct–Nov 2026)
- 2026-10-23 · api-requests · Data "in TiDB" is reachable via BigQuery `casafari-cloud.tidb_prod` — check BigQuery first → knowledge/data-sources.md
- 2026-10-26 · data-ops-cost · Work monthly, not annualised → knowledge/user-preferences.md
- 2026-10-26 · data-ops-cost · No "AI services" wording for crawling; use invoice terms → playbooks/data-ops-cost-structure.md
- 2026-10-26 · data-ops-cost · DC closed jobs: count only config-change + fixed-comment jobs → playbooks/data-ops-cost-structure.md
- 2026-10-26 · data-ops-cost · Don't deliver sandbox paths; Billy can't reach /home/user → knowledge/user-preferences.md
- 2026-10-26 · pricing · Balears licence price is €45 → playbooks/apicat-licence-monitor.md
- 2026-10-26 · pricing · AM comes from BigQuery settings.accountManager.name, not old files → playbooks/web-app-pricing.md
- 2026-10-26 · pricing · Promo codes with allowed_domains apply automatically → playbooks/web-app-pricing.md
- 2026-11-02 · inbox · Connector bulk cleanup too expensive (23% of limit) — use Gmail filters → playbooks/inbox-triage.md
- 2026-11-02 · hubspot-check · Exclude Mila Suharev, Nils, Billy, Yehor; Mila Escalera is included → playbooks/hubspot-connection-check.md
- 2026-11-02 · hubspot-check · Test, confirm recipients, then activate → knowledge/user-preferences.md
- 2026-11-03 · portal-share · Identify portals by source domain, not name; ask clarifying questions on definitions → playbooks/portal-market-share.md
- 2026-11-05 · audience-lists · Only actual customers: user-level stage=contract → playbooks/audience-lists.md
- 2026-11-05 · audience-lists · Valuation usage = valuationRequests.type IS NULL → knowledge/data-sources.md
- 2026-11-05 · audience-lists · BigQuery for inclusion; HubSpot/Postmark unsubscribes only for exclusion → playbooks/audience-lists.md
- 2026-11-10 · catch-up · Read-only, leave everything unread; verify status at thread level → playbooks/catch-up-brief.md
- 2026-11-11 · catch-up · Do the deep sweep on the first pass → playbooks/catch-up-brief.md
- 2026-11-11 · hubspot-check · Cadence Mon/Wed mornings → playbooks/hubspot-connection-check.md
- 2026-11-11 · general · "Lowest cost, never losing quality, always diligent"; proceed directly on similar cases → knowledge/user-preferences.md
- 2026-11-12 · apicat · Lever = grow ApiCat child user count, not retention discounts; reject weak fuzzy matches → playbooks/apicat-licence-monitor.md
- 2026-11-12 · platform · Contact Account_ID first in prospect matching; always produce HTML too; no names/emails in HTML → playbooks/platform-activity-dashboard.md

## Live log
- 2026-11-13 · registry · Billy approved all proposed levels: catch-up brief L2, follow-ups L2 (internal nudges only), Postmark KPIs L2, Api.Cat monitor L2, inbox triage L1 (list only) → playbooks/_registry.md
- 2026-11-13 · slack · Any Slack message (reply, DM, post, nudge) needs Billy's approval first, at all levels → CLAUDE.md, playbooks/_registry.md, followup skill
- 2026-11-13 · followup · Full sweep; doc 1-vU80… refreshed in place and renamed "2 to 13 Nov"; HR items kept out of the doc (chat only); tracker C0BF6BRQA8K may not be the Mila/Nuño split thread → followups/open-items.md, knowledge/gotchas.md
- 2026-11-13 · trend-scan · First Slack trend & direction scan (2–13 Nov); corrected ApiCat churn share (4/54) → playbooks/slack-trend-scan.md, knowledge/gotchas.md
- 2026-11-13 · trend-scan · v2 thread-depth pass corrected 5 v1 claims (Sotheby's decided, domain-verification void, stale cancellation flag, es_monitoring reactions, data_issues answered) → playbooks/slack-trend-scan.md, knowledge/gotchas.md
- 2026-11-13 · registry · promoted slack-trend-scan to L1 (scan + 5 derived reports R1–R5: churn reasons, legal-asks digest, unanswered inbound, #tools-support types, BF attribution); Billy's explicit OK; drafts to Billy only → playbooks/_registry.md, playbooks/slack-trend-scan.md
