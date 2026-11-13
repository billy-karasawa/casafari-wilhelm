# Playbook: Sales rep performance review (peer comparison)

- **Autonomy level:** **L1 max — HR-sensitive, never promote above L1**
- **Cadence:** ad hoc (probation decisions, performance reviews)
- **Output destination:** chat only, unless Billy asks for a doc. Never post or share.
- **Memory rule:** store method and definitions only. **Never** store conclusions about individuals.

## Purpose
Compare one or more reps against same-country peers on wins, value, pipeline and retention.

## Data sources
- **Contracts:** `casafari-cloud.mongodb_app_prod.companies` → JSON array `contracts`
  (not `tidb_prod.companies_contract`, which doesn't exist).
- **Reps:** `casafari-cloud.tidb_prod.admin_users` (`id`, `name`, `real_name`, `group`, `is_active`,
  `created_at` = start-date proxy). `contracts.owners.{first,second,third}.id` → `admin_users.id`.
- **HubSpot:** owners via `search_owners`; deals via `query_crm_data` filtered by `hubspot_owner_id`,
  `closedate`, `hs_is_closed_won`, summing `amount_in_home_currency` (EUR); company count per owner = book size.

## Steps
1. Identify reps in admin_users and HubSpot owners.
2. Owner-credit per contract (credit = value × part/100) — see SQL in `knowledge/data-sources.md`.
3. Metrics per rep: contracts won (count & credit), won value by subscriptionType, monthly trend
   drafts vs won vs deprecated, HubSpot closed won/lost & win rate, open pipeline, book size,
   value kept % on RETAINED/RECOVERED (vs previous non-new contract of same company).
4. Peers = same country, ≥2 wins in window; highlight similar-tenure peers as fairest comparison.
5. Present table + caveats; recommendation framed as input for Billy, not a decision.

## Definitions
- Won = contract `stage IN ('paid','hold')`. "Draft owner" has no literal field → use `contracts.owners`.

## Known pitfalls
- Gross churn is NOT measurable from contracts (lost renewals create no contract); HubSpot Churn
  pipeline barely used → ask for renewals-due list.
- Split ownership inflates raw counts — always weight by `part`.
- Some HubSpot lost deals are €0 (bulk cleanup) — distorts win rate; exclude or flag.
- Probation end dates are not in the data.
