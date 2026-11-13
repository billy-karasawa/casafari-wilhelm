# Wilhelm — Billy's Senior Business Analyst

Wilhelm is a Claude persona backed by this repo. Open any Claude Code session (web, mobile, desktop) on
`casafari-wilhelm` and it becomes Wilhelm: it loads `CLAUDE.md`, your preferences, the open-items tracker and
its autonomy level for each topic.

## Daily use
| You say | Wilhelm does |
|---|---|
| `/brief` | Overdue & due follow-ups, today's meetings, scheduled runs, 3 next actions |
| `/followup` | Checks Slack/Gmail/HubSpot for replies on open items, drafts nudges |
| any analysis ask | Finds the playbook, follows it at its autonomy level |
| `/teach <lesson>` | Files a correction or rule in the right place |
| `/debrief` | Saves the session's lessons, items and playbook updates; commits & pushes |
| `/promote <topic> <level>` | Changes autonomy after you confirm |

## How training works
1. New topics start at **L0 (Shadow)** — Wilhelm proposes, you steer.
2. Each correction you make is logged (`training/log.md`) and baked into the playbook.
3. After enough clean runs Wilhelm suggests a promotion: **L1 Draft → L2 Act & report → L3 Autonomous**
   (scheduled task). HR topics are capped at L1. Nothing external is sent without the playbook allowing it.

## Layout
```
CLAUDE.md                 identity, rules, autonomy ladder
knowledge/                user-preferences, glossary, data-sources (+SQL), gotchas, stakeholders
playbooks/                one file per recurring topic + _registry.md (autonomy levels) + _template.md
followups/open-items.md   tracker of everything pending
training/log.md           corrections & lessons, append-only
history/                  one digest per past session
.claude/skills/           brief, followup, teach, debrief, promote
.claude/agents/wilhelm.md subagent definition for delegation
```

Seeded on 2026-11-13 from 12 earlier sessions (Oct–Nov 2026).
