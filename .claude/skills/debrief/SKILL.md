---
name: debrief
description: End-of-session wrap-up for Wilhelm. Saves lessons, new knowledge, open items and playbook updates from this conversation into the repo, then commits and pushes. Use when Billy says "wrap up", "debrief", "save this", or before a long session ends.
---

# /debrief — persist what this session learned

1. Review the whole conversation and list:
   - Corrections / preferences → apply `/teach` rules for each.
   - New or changed open items → update `followups/open-items.md` (owner, due, where, status).
   - Work that will recur → create or update `playbooks/<topic>.md` from `_template.md`,
     and add/refresh its row in `playbooks/_registry.md` (new topics start at **L0**;
     increment the topic's "Runs" and "Clean runs" counters — a clean run = no correction from Billy).
   - Outputs produced (docs, artifacts, files, scheduled tasks) → add links to the playbook's "Last run".
2. Write `history/YYYY-MM-DD-<slug>.md` (≤40 lines): goal, what was done, key numbers, decisions, open items.
3. If a topic now has ≥3 clean runs at its current level, suggest a promotion to Billy (don't apply it).
4. `git add -A && git commit -m "debrief: <slug>"` and push to the current branch.
5. Reply with a 5-line summary of what was saved.
