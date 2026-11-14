# Playbook registry — Wilhelm's autonomy per topic

Source of truth for autonomy. **Current** is what Wilhelm may do today. **Proposed** is Wilhelm's suggestion,
pending Billy's confirmation via `/promote`.
All proposed levels approved by Billy on 2026-11-13.

> **Slack approval gate (2026-11-13, all levels):** every Slack message Wilhelm sends (replies, DMs, posts,
> nudges) needs Billy's approval first. L2/L3 still apply to analysis and non-Slack outputs.
> The pre-existing scheduled HubSpot check task runs from its own prompt, outside this repo.
 Levels: L0 Shadow · L1 Draft · L2 Act & report · L3 Autonomous.

| Topic | Playbook | Current | Proposed | Since | Runs | Clean runs at level | Notes |
|---|---|---|---|---|---|---|---|
| HubSpot connection check | `hubspot-connection-check.md` | **L3** | L3 | 2026-11-02 | 3+ | 3 | Already scheduled & activated by Billy (Mon/Wed 07:45) |
| Platform activity dashboard | `platform-activity-dashboard.md` | **L3** | L3 | 2026-11-12 | 5+ | 1 | Scheduled daily refresh + weekday summary; activated by Billy |
| Catch-up brief / `/brief` | `catch-up-brief.md` | **L2** | L2 | 2026-11-13 | 2 | 0 | Read-only, output to Billy's private doc — low risk |
| Follow-up tracking / `/followup` | `../followups/open-items.md` | **L2 (internal nudges)** | L2 (internal nudges) | 2026-11-13 | 0 | 0 | Nudges are drafts only; Billy approves each Slack/email nudge |
| Postmark campaign KPIs | `postmark-campaign-kpis.md` | **L2** | L2 | 2026-11-13 | 1 | 0 | Read-only reporting |
| Api.Cat licence monitor | `apicat-licence-monitor.md` | **L2** | L2 | 2026-11-13 | 3 | 0 | Refresh on request; strategic decisions stay with Billy |
| Web App pricing & price book | `web-app-pricing.md` | L1 | L1 | 2026-11-13 | many | 0 | Draft book unapproved; any quote → Billy |
| Portal market share | `portal-market-share.md` | L1 | L1 | 2026-11-13 | 1 | 1 | Definitions must be clarified each time |
| Data-ops cost structure | `data-ops-cost-structure.md` | L1 | L1 | 2026-11-13 | 1 | 0 | 4 iterations of corrections last time |
| API request analysis | `api-requests-analysis.md` | L1 | L1 | 2026-11-13 | 1 | 1 | |
| API Q&A knowledge base | `api-knowledge-base.md` | L1 | L1 | 2026-11-13 | 2 | 2 | |
| Marketing audience lists | `audience-lists.md` | L0 | L0 | 2026-11-13 | — | — | Owned by Billience; Wilhelm observes/audits only |
| Gmail inbox triage | `inbox-triage.md` | **L1 (list only)** | L1 (list only) | 2026-11-13 | 1 | 0 | Never bulk-move; cost lesson |
| Sales rep performance review | `sales-rep-performance-review.md` | L1 | **L1 (cap)** | 2026-11-13 | 1 | 1 | HR — never above L1 |
| Slack trend & direction scan + derived reports (churn reasons, legal-asks digest, unanswered inbound, #tools-support types, BF attribution) | `slack-trend-scan.md` | **L1** | L1 | 2026-11-13 | 3 | 1 | Promoted by Billy 13 Nov. Drafts to Billy only (private Doc + HTML); no Slack/email/CRM writes |

## Promotion criteria
- L0→L1: playbook has steps, definitions, quality checks.
- L1→L2: ≥3 clean runs at L1, explicit destination/recipients.
- L2→L3: ≥5 clean runs at L2, explicit escalation rules, schedule defined.
- Demote on 2 corrections within 7 days or any unapproved outbound action.
