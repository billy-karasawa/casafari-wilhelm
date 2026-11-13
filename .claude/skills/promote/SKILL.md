---
name: promote
description: Change Wilhelm's autonomy level (L0–L3) on a topic in playbooks/_registry.md after Billy explicitly agrees. Use for "promote", "demote", "you can do X on your own now", "let Wilhelm run X".
---

# /promote <topic> <L0|L1|L2|L3>

1. Find the topic row in `playbooks/_registry.md` and its playbook file.
2. Check readiness and tell Billy honestly before changing anything:
   - L0→L1: playbook has Steps, Definitions and Quality checks filled in.
   - L1→L2: ≥3 clean runs at L1; output destination and allowed recipients are explicit.
   - L2→L3: ≥5 clean runs at L2; escalation rules are explicit; a schedule is defined.
   Missing prerequisites → list them and ask whether to proceed anyway.
3. Only with Billy's explicit "yes" in this conversation: update the level, the date, and reset
   "Clean runs at level" to 0. Update the playbook header. Log in `training/log.md`
   (`promoted <topic> to Lx` or `demoted …` with the reason).
4. For L3: offer to create the scheduled task (create_trigger, fresh session per fire, prompt =
   "You are Wilhelm. Run playbooks/<topic>.md at L3 and report.") — only if Billy agrees.
5. Commit `promote: <topic> → Lx`.
