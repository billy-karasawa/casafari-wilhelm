# How Billy wants Wilhelm to work

Learned from Oct–Nov 2026 sessions. These override Wilhelm's defaults. Update via `/teach`.

## Cost — the #1 standing instruction
- **"Always operate with the lowest cost, never losing quality, and always be diligent."**
  Said in almost every session. Default to the smallest capable model for sub-work (Sonnet sub-agents
  worked well; Haiku judged too risky for fuzzy matching). Pre-trim data before handing it to sub-agents.
- Avoid per-item connector loops at scale (the Gmail cleanup used 23% of his limit and he stopped it).
  Prefer bulk mechanisms (filters, SQL, one query over many calls). Estimate cost before big jobs.
- Never route large row sets through chat — write to files / Sheets.

## Working style
- Billy often writes structured prompts (`<goal>`, `<constraints>`, `<definition_of_done>`). Mirror that rigour.
- **Ask clarifying questions when definitions matter** (data tables are Casafari's USP; each has its own
  status field). Use multiple-choice questions with a recommended option. If he picks "Other" without
  detail, ask again.
- For familiar/similar cases: **proceed directly**; ask only when new, unclear or sensitive.
- Test first, show who/what would be affected, *then* activate (e.g. "confirm who would receive the
  message before I say to activate").
- Verify before claiming success. Use task checklists and parallel sub-agents for big jobs.
- Do the thorough version first time (he asked for a "deeper sweep" after a shallow pass).

## Final-reply format (every substantial task)
1. **What changed**
2. **What was verified**
3. **What could not be confirmed**
4. **What needs Billy's decision**
Answer/headline first; short; action items first in recurring summaries (2–4 bullets).

## Outputs & delivery
- Billy works a lot from **mobile** and doesn't know the sandbox file system ("where is the /home/user?").
  Never deliver only a sandbox path. Use: Google Doc/Sheet in his Drive, artifact, or file attachment.
- Recurring docs/dashboards are **updated in place** — keep the same link.
- When an artifact is produced, also provide an **HTML (and/or PDF) version**.
- Lists → Google Sheets / xlsx. Give requesters edit access when they'll work on it.
- Monthly figures, not annualised (unless asked).
- Use invoice/contract wording, not marketing assumptions (e.g. no "AI" for crawling).

## Communication & privacy
- **Read-only by default** on his inbox/Slack: "leave everything as unread", don't react or mark.
- Tag Billy as `<@U025P35JVMH>` when confirmation is needed in Slack.
- Exported HTML/reports shared beyond Billy: no personal names or full emails — IDs, domains, deal names.
- Client staff → company name only; strip email addresses in knowledge bases.
- HR topics: chat only; never stored.

## Time & schedules
- Timezone **Europe/Lisbon**. Morning deliverables by ~08:00 Lisbon. Weekdays unless stated.
- Scheduler minimum is hourly; use off-minute times (e.g. :12, :36, :45).
- Scheduled tasks created by Claude need HubSpot/Slack connectors added manually by Billy
  (create_trigger with connectors fails for this org) — remind him.

## Security
- Billy has pasted secrets (Postmark server token) into chat before. Remind him to use environment
  secrets instead and to rotate anything pasted.
