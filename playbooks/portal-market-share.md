# Playbook: Portal market share / exclusivity (Spain)

- **Autonomy level:** see `_registry.md`
- **Cadence:** ad hoc (sales meetings with portals, e.g. Fotocasa)
- **Output destination:** markdown report + CSV; offer artifact/Drive (don't leave in the sandbox)
- **Last run:** 2026-11-03 — Barcelona province — `history/2026-11-03-barcelona-portal-share.md`

## Purpose
How exclusive each portal's stock is vs the others, how much agency stock is on no portal, and new
listings per month by portal and property type.

## Clarify first (Billy explicitly wants this — tables are Casafari's USP)
Use AskUserQuestion with options for: geography level (province / city / comarca), sale vs rent,
which sources count as "agency", property-type scope (rooms?), snapshot vs period.

## Data (BigQuery `casafari-cloud.tidb_prod`, europe-west4)
- `source_estates` (listings: `status` sale, `rent_status` rent, `estate_id`, `source_id`, `location_id`,
  `type_id`, `created_at`, `deleted_at`), `sources` (`domain`, `label`, `classified`, `stage`),
  `flat_locations`, `types.group`, `locations`.
- Portal = **source domain, not name**: Idealista `www.idealista.com`, Fotocasa `www.fotocasa.es`,
  Habitaclia `www.habitaclia.com`, Pisos `www.pisos.com`.
- Core SQL: `knowledge/data-sources.md` → "Portal exclusivity".

## Definitions (agreed 2026-11-03)
- Geography via the **listing's** `location_id` → `flat_locations.level3_location_id` (province) or
  `level5_location_id` (city). Barcelona province 10163, city 10544, Barcelonès comarca 10510.
- "On a portal" = active snapshot today; sale and rent counted separately.
- Property = Casafari `estate_id` (dedup). Production sources only: stage IN ('match','live','livenomatch').
- Agency = `classified=0` sources + classified=1 agency networks (E&V, RE/MAX Spain, Tecnocasa,
  Savills, Engel-type networks — list in the SQL).

## Quality checks
- [ ] Dry-run first (≈16 GB scan for a province).
- [ ] Unmatched (`estate_id` null) < 2% for portals.
- [ ] Quarantine/deprecated sources excluded.

## Known pitfalls
- No `idealista.es` source; idealista.pt is Portugal.
- Quarantined/deprecated sources (Milanuncios, Yaencontre, Hay Pisos…) still hold huge "active" counts.
- `estates.province_id` ≠ `locations` ids. `seen_at` is always 0; `updated_at` is not staleness.
- Fotocasa Dec 2024 spike = backfill. Rooms dominate Idealista "other".

## Open decisions (from last run, unanswered)
Include quarantined sources? Agency network list right? Drop rooms? Run city separately?
