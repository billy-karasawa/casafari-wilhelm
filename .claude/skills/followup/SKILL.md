---
name: followup
description: Sweep for replies and progress on every open item in followups/open-items.md (Slack, Gmail, HubSpot, Calendar), update statuses, and draft nudges for overdue items. Use when Billy asks "what's pending", "chase", "follow up", or at the start of a working day.
---

# /followup — chase open items

1. Read `followups/open-items.md` and `playbooks/_registry.md`.
2. For each item with status `open` or `waiting`:
   - Search the channel named in its **Where** column (Slack thread/channel, Gmail thread,
     HubSpot deal/ticket) for activity since **Last checked**.
   - If answered → summarise the answer in one line, set status `done` (or `next-step` with the
     new action), and file any new knowledge via the `/teach` rules.
   - If no answer and past **Due** → draft a short, polite nudge in Billy's tone
     (see `knowledge/user-preferences.md`). **Never send it yourself** — Slack messages always need Billy's
     approval (Slack approval gate in `CLAUDE.md`); leave every nudge as a draft for Billy.
3. Update **Last checked** on every item touched.
4. Report to Billy:
   - ✅ Resolved since last check
   - ⏳ Still waiting (with days overdue)
   - ✉️ Nudges drafted / sent (links)
   - 🆕 New items spotted (things Billy was asked or promised in Slack/email that aren't tracked yet — propose adding them)
5. Commit `followup: sweep YYYY-MM-DD`.
