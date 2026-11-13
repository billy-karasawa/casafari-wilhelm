---
name: teach
description: Record a correction, preference or new piece of knowledge Billy just taught Wilhelm, filing it in the right memory file. Use whenever Billy says "remember", "from now on", "no, it should be…", corrects a number/definition, or explains how something works.
---

# /teach — capture a lesson

Input: the lesson in Billy's words (args), or infer it from the last correction in the conversation.

1. Classify the lesson (one or more):
   - Preference about output/communication → `knowledge/user-preferences.md`
   - Term / KPI / product definition → `knowledge/glossary.md`
   - Table, column, query, API detail → `knowledge/data-sources.md`
   - Data pitfall / exclusion → `knowledge/gotchas.md`
   - Person / role → `knowledge/stakeholders.md`
   - Topic-specific procedure → the matching `playbooks/<topic>.md` ("Training notes" + fix the steps)
2. Edit the target file so the rule is stated **positively and concretely** (what to do, with an
   example), replacing any contradicting older text rather than appending a contradiction.
3. Append one line to `training/log.md`:
   `- YYYY-MM-DD · <topic> · <lesson> → filed in <file>`
4. If this is the 2nd correction on the same playbook within 7 days, tell Billy and suggest a
   demotion via `/promote`.
5. Confirm back in one line: what you filed and where. Commit with message `teach: <short lesson>`.
