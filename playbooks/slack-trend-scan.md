# Playbook: Slack trend & direction scan

- **Autonomy level:** L0 (new, 2026-11-13); see `_registry.md`
- **Cadence:** ad hoc. **Last run:** 2026-11-13 v2 (week closed, ~125 threads), window 2–13 Nov. Doc: https://docs.google.com/document/d/1RTMRtS-gRIXO89BundRvRszv5ZXNP3qeDPU5zxGC9i0/edit (HTML copy in `reports/`)
- **Output destination:** Google Doc in Billy's Drive plus an HTML version (no personal names in anything shared beyond Billy)

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
