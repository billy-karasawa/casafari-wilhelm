---
name: brief
description: Wilhelm's start-of-day brief for Billy — open and overdue follow-ups, today's meetings that relate to tracked topics, scheduled playbook runs, and the 3 suggested next actions. Use for "brief me", "what's on today", "where are we".
---

# /brief

1. Load `followups/open-items.md`, `playbooks/_registry.md`, last 10 lines of `training/log.md`.
2. Check today's Google Calendar (Europe/Lisbon) for meetings touching tracked topics/stakeholders.
3. Produce, in this order, max ~20 lines:
   - **Overdue** (owner · item · days late)
   - **Due this week**
   - **Today's meetings** with prep notes from relevant playbooks/history
   - **Scheduled runs** (L2/L3 playbooks due today)
   - **Suggested next 3 actions** for Billy, and what Wilhelm will do on its own (L2+ only)
4. Ask whether to run `/followup` now.
