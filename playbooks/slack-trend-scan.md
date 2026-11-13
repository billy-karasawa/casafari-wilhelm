# Playbook: Slack trend & direction scan

- **Autonomy level:** L1 (Draft) since 2026-11-13, covering the trend scan plus the 5 derived reports below. See `_registry.md`.
- **Cadence:** ad hoc. **Last run:** 2026-11-13 v2 (week closed, ~125 threads), window 2–13 Nov. Doc: https://docs.google.com/document/d/1RTMRtS-gRIXO89BundRvRszv5ZXNP3qeDPU5zxGC9i0/edit (HTML copy in `reports/`)
- **Output destination:** Google Doc in Billy's Drive plus an HTML version (no personal names in anything shared beyond Billy)

## L1 scope (approved by Billy 2026-11-13)
Wilhelm produces each report itself. Each one goes **only to Billy**, as a private Google Doc updated in place plus HTML.
Nothing goes to Slack, email or HubSpot; any nudge stays a draft for Billy (Slack approval gate).
Each report has a **Definitions** block and **Quality checks** in "Derived reports" below.

## Purpose
Read Slack activity over a time window and answer three questions:
1. Which issues or requests keep coming back, and could their handling be automated?
2. Which initiatives and topics are new, and what trends do they show?
3. Which direction is the company taking?

## Key people (weight their posts higher)
Mila, Nils and Mitya (founders) · Yehor (RevOps) · Maryna (PMM) · Roman (PM leader) · Cátia (Legal) ·
Tiago (Finance) · Kate B (Data & API).

## Steps
1. Compute the Slack `oldest` ts with `date -d` (see gotchas).
2. Run parallel Sonnet sub-agents, each covering a slice of channels:
   - founders / leadership
   - commercial (sales, churn, pricing)
   - product / platform / API / MCP
   - legal / finance / ops
   - data / monitoring
3. Each agent returns structured rows: date · channel · author role · topic tag · type
   (request / issue / initiative / decision / announcement) · one-line summary · permalink.
4. Also run a `from:<person>` search for each key person over the window.
5. Synthesis:
   - Recurring = the same topic tag 3 or more times, or from 2 or more people.
   - Trends = topic tags first seen in the window, or rising versus the prior window.
   - Direction = what the founders, Yehor and Roman announce, decide and prioritise.
6. For each automation candidate give: frequency, current owner, proposed handling (bot / rule / form / scheduled agent), and effort.

## Quality checks
- Cite permalinks for every claim. Separate observed facts from inference.
- Filter bot-agent noise (Mira, Themis, Mary, Billience, monitoring bots), but count bot alerts that nobody acknowledged as a signal.

## Lessons from run 1 (2026-11-13)
- 5 Sonnet slices with ~110–170k tokens each was enough. Create the Doc by uploading the HTML file with `Drive.create_file` (file reference); Drive then reports `fileSize: 1`, which is normal, so verify by reading the content.
- Slack search results often lack per-message permalinks. Ask the agents for `ts` values to rebuild them.
- Many founder posts are written by agents (Mila: Mira/Opusik/OG-Agent; Nils [BOT]; Tiago's agent signature). Label them as founder-sanctioned.
- Reconcile counts across slices. The catch-up sweep said "~11 forms citing ApiCat", but the full read found 54 churn forms in 12 days, only 4 of them ApiCat-related.

## Lessons from run 2 (v2, 2026-11-13 evening)
- A thread-depth pass changed conclusions: Sotheby's was decided, the domain-verification ask was void, a cancellation flag was stale, #es_monitoring had reactions, and every #data_issues ticket was answered. **Never report "no reply" from search snippets alone; open the thread.**
- Read #tools-support. It holds the largest manual ops load (~48 tickets in 12 days).
- Slack shows UTC−3, so add 3h for Lisbon. Channel IDs: GJWLX7M2R = #portugal, C0B3J6YBEP4 = leadership group DM, C0C92GC8H2Q = #platform-api-mcp, C0C96PNLUE8 = custom requests, C07PFCLQE6S = #revsquad_and_legal.
- Update the Doc in place with `tools/html2docreq.py` (HTML → Docs batchUpdate), run by a sub-agent so the large JSON stays out of the main context. Copy the script into the repo if it's reused.

## Derived reports (L1, drafts to Billy only)

### R1 · Weekly churn-reason report
- **Cadence:** Mondays, for the previous Mon–Sun. Sources: #churn-spain, #churn-portugal, #churn-italy, #churn-france, #churn-germany.
  Cross-check with HubSpot churn-pipeline deals.
- **Definitions:**
  - Churn form = one cancellation-form post (bot or human) per company. Duplicates for the same company in the week count once.
  - Reason buckets: closing business / short-term / low use · no results / data gaps · price · alternative (name it) ·
    API.cat / Colegio de APIs · other.
  - MRR = the MRR stated on the form. If none is stated, use the HubSpot company MRR and mark it "(HS)".
- **Output:** count and MRR by country × reason, a week-on-week change, top 5 by MRR, and the API.cat share.
- **Quality checks:** form totals reconcile ±10% with HubSpot churn deals. Swings over 20% vs the prior week → stop and flag.
  No commentary on individual reps.

### R2 · Weekly legal-asks digest
- **Cadence:** Mondays. Sources: #revsquad_and_legal (C07PFCLQE6S), Themis posts, Legal tags of Billy or Yehor in any channel.
- **Definitions:**
  - Open ask = a Legal question addressed to commercial (Billy, Yehor, sales) with no answer from that person in the thread.
  - Age = days since the first ask.
- **Output:** a table of topic · counterparty · who it waits on · age · last chase · link. Ordered by age.
- **Quality checks:** open every thread before marking it open. Drop any thread resolved since the last run, and list it under "closed this week".

### R3 · Daily unanswered-inbound-requests digest
- **Cadence:** weekdays by ~08:00 Lisbon. Sources: #platform-api-mcp-custom-requests (C0C96PNLUE8), commercial@ / platform@ follow-ups
  visible in Slack, and Gmail threads where Billy is To/CC.
- **Definitions:**
  - Inbound request = an external prospect or customer asking for custom data, licensing, pricing or a quote.
  - Unanswered = no reply from Casafari staff in the thread or email after 1 business day.
- **Output:** list of company · ask (one line) · owner (if any) · age · whether it's a legal question · link.
  Standard answers that already exist are marked.
- **Quality checks:** check the thread and any CC'd email before calling something unanswered. Agent drafts don't count as replies.

### R4 · #tools-support ticket-type report
- **Cadence:** weekly (Mondays). Source: #tools-support (C016GRLBSN5).
- **Definitions:** ticket = one parent post. Types: device-limit · trial / €1-contract activation · trial reset ·
  Smartlink email change · deletion / GDPR · billing admin · other.
- **Output:** count by type × market, median time to first reply, top 3 repeat requesters (by team, not by person), and
  automation candidates with estimated hours saved.
- **Quality checks:** exclude "staff test" posts. Compare against the 2–13 Nov baseline (~48 tickets in 12 days).

### R5 · Black Friday attribution (BigQuery)
- **Cadence:** on request, and after each wave (email 2 on 19 Nov, then 24 and 30 Nov). Read-only queries.
- **Source:** `casafari-cloud.casafari_platform` (account_attribution with utm_*, accounts, usage_daily), refreshed ~02:30 UTC.
  Exclude internal accounts (`accounts_daily_snapshot.is_internal`).
- **Definitions:**
  - BF sign-up = a new account created from 12 Nov with a BF utm_campaign, or a redemption of BLACKFRIDAY30 / BLACKFRIDAY25.
  - Channels: email (Postmark waves), app banner, mobile banner, console, other.
  - Conversion = a BF account with any billed units (usage_daily.billed_calls > 0) or a paid plan.
- **Output:** sign-ups by channel and day, conversions, tokens or bonus granted, and a reconciliation against Mila's
  agent's posts (456 / 389) and HubSpot (16).
- **Quality checks:** estimate the cost (bytes scanned) before running. If the totals differ from Slack-reported numbers by more than 20%,
  explain the gap before reporting.
