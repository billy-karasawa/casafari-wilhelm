# Postmark server connection & campaign KPIs (29 Oct / 11 Nov 2026)

**Goal:** connect to Postmark server CASAFARI_2026; later "check the stats, provide summary KPIs for each previous campaign".

**Done:** connected via Postmark REST API (proxy-authenticated). Built per-tag KPI table with a bot-click filter.

**Key numbers:** lifetime sent 64,629; lifetime bounce 12.08% (Postmark reviews accounts at ~10%).
Recent sends bounce 0–3%; May 20 (28.1%) and Jul 30 (11.4%) sends caused the high lifetime rate.
~90% of ai-presentation-builder-2026 clicks were bots/scanners; real click rates ~1–2%.

**Open:** per-language breakdown of ai-presentation-builder-2026 offered, not done; recommend
setting up bounce/delivery/click webhooks (none configured).

**Output:** KPI table in chat only.
