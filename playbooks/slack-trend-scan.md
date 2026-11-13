# Playbook: Slack trend & direction scan

- **Autonomy level:** L0 (new, 2026-11-13); see `_registry.md`
- **Cadence:** ad hoc (first ask: 2 to 13 Nov 2026, Billy's absence window)
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
