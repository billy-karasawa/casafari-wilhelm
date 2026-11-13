# Playbook: HubSpot email/calendar connection check → #hubspot_updates

- **Autonomy level:** see `_registry.md` (already running on a schedule)
- **Cadence:** Mon & Wed 07:45 Europe/Lisbon — scheduled task `trig_014jGd47DXSPKrWD5SaMxt9Z`
  ("HubSpot connection check – #hubspot_updates", fresh session per run)
- **Output destination:** Slack #hubspot_updates (C0AHXHC4NRE) — internal, pre-agreed

## Purpose
Nudge Sales Enterprise reps whose HubSpot email or calendar connection is broken.

## Steps
1. HubSpot `users`: `search_crm_objects`, filter `hs_assigned_seats CONTAINS_TOKEN "sales-enterprise"`,
   `hs_deactivated` ≠ true, limit 200. Props: `hs_connected_email_status`, `hs_calendar_sync_enabled`,
   `hs_calendar_connection_status`, `hs_meetings_enabled`, `hs_email`, `hs_searchable_calculated_name`.
2. Exclude: **Mila Suharev, Nils Henning, Billy ("PLG Casafari"), Yehor**. (Mila *Escalera* is included.)
3. Flag if Email Status ≠ ENABLED, or Calendar Sync ≠ true, or Calendar Status ≠ true, or
   Scheduling Pages ≠ on. Blank = failing.
4. Map to Slack IDs (search by name/surname — email search returns nothing):
   Iñigo U03BE169EBH · Mila Escalera U05EU7H0F39 · Manuel Maldonado U019YP8FYQG ·
   Natalia Soto U01425DN2Q3 · Nuño U020QLN5MEZ (Slack uses his other surname) · Gabriel Meza (in task prompt).
5. If nobody flagged → **post nothing**.

## Message format
```
🔌 HubSpot connection check – <Day DD Mon>
• <@rep> — <failing items>
Fix: HubSpot → Settings → General → Email / Calendar
```

## Escalate when
- Same rep flagged ≥3 runs in a row (currently watch Natalia Soto, Gabriel Meza) → tell Billy.
- Flagged count > 10 (likely a HubSpot-wide issue, not reps).

## Known pitfalls
- `create_trigger` with `connectors` failed for this org → Billy added HubSpot & Slack manually in the
  scheduled-task settings. Any new scheduled task will need the same.
- Don't fire manually on a scheduled morning — reps get tagged twice.

## Training notes
- 2026-11-02 · test run + confirm recipients before activating.
- 2026-11-11 · cadence changed from weekdays to Mon/Wed.
