# Data sources & working queries

General: BigQuery project **`casafari-cloud`**, location europe-west4. Use the BigQuery MCP `run_query`
(**dry-run first** for big scans). `bq` CLI may fail with "Invalid Credentials" — if needed, `unset
CLOUDSDK_AUTH_ACCESS_TOKEN` and use a service account. The MCP tool: SELECT only (no DECLARE/scripts → CTEs),
max ~50 rows per call → page with `SELECT * FROM (<sql>) t ORDER BY TO_JSON_STRING(t) LIMIT 50 OFFSET n`.
To force a large result to file, add a `REPEAT('.',120000) pad` column. No direct TiDB — "it's in BigQuery".

## `mongodb_app_prod` (web app, Airbyte-synced Mongo) — filter `_ab_cdc_deleted_at IS NULL`
- **companies**: `_id`, `name`, `countryCode`, `employeesStage`, `employees[]` (`userId`, `stage`, `createdAt`),
  `labels`, `contracts[]` (`stage`, `status`, `type`, `subscriptionType`, `value` (monthly EUR), `extraValue`,
  `payingFrequency`, `startDate`, `endDate`, `softLimitOfAccounts`, `owners.{first,second,third}.{id,part}`),
  `parentId`, `availableUserLevel`, `settings.{allowAlertsPage, allowMetasearch, allowPropertyValuationPage,
  allowWidgets, allowLocationSourcing, softLimitOfAccounts, accountManager.name, salesManager.name}`,
  `companyLogo`, `legalData.{city,postalCode,vat,legalName,country}`, `clientVat`, `domain`.
  `companies.status` is "active" for all → useless.
- **users**: `_id`, `email`, `firstName`, `lastName`, `language`, `companyId`, `createdAt`. Ignore `status`, `subscribe`.
- **companyLogos** (`text` = brand), **orders** (`paidAt`), **pageViews** (`section`, `userId`, `createdAt`),
  **valuationRequests** (`type` NULL = CMA tool use; `estate` = automatic, don't count), **leadMagnetWidgets**,
  **promoCodes** (`title`, `amount`, `valid_to`, `allowed_domains` → auto-applied), **AIPresentations**.

## `tidb_prod` (MySQL replica)
- **source_estates** listings: `status` (sale), `rent_status` (rent) ∈ active/hold/none/sold/reserved/rented;
  `estate_id`, `source_id`, `location_id`, `type_id`, `created_at`, `deleted_at`. `seen_at` always 0.
- **sources**: `domain`, `label`, `classified`, `status`, `stage`, `deleted_at`.
- **estates** (dedup properties; `province_id` ≠ locations ids), **locations**, **flat_locations**
  (`level3_location_id` province, `level5_location_id` city), **types** (`group`).
- **admin_users** (`id`, `name`, `real_name`, `group`, `is_active`, `created_at`) — staff; joins contracts owners.
- **user_subscriptions** (`status` **'paid'**/expired — not 'active', `expired_at`, `user_id` = Mongo `users._id`),
  **invoices** (`type='user_level'`, `status='paid'`, `promo_code`, `subscription_id`, `service_owner`),
  **invoice_items** (`unit_price`, `quantity`, `discount`, `period`).
- **accounts_balancetracking**, **request_statistics**, **api_users**, **accounts_account**, **endpoints** — API logs.

## `casafari_platform` (developers.casafari.com; refreshed ~02:30 UTC daily; no emails)
accounts (`is_internal`, `trial_units`, `plan_id`, `name`, `closed_at`), accounts_daily_snapshot, members,
account_attribution (utm_*), usage_daily (`calls`, `billed_calls`, `units_billed`, `channel`, `product`, `day`),
meter_snapshots (`trial_consumed`), invoices (`status`, `subtotal_cents`, `total_cents`, `paid_at`),
api_keys, oauth_grants, oauth_clients, subscriptions, plans, credit_ledger, claro_accounts.

## HubSpot (portal 144103290)
- Pipelines: "Casafari SaaS and CRM" (505800390), "Business Development" (default), "Self Checkout" (506288108),
  "Churn Pipeline" (1404621035, deprecated/barely used).
- Deals: `amount_in_home_currency` (EUR), `hs_is_closed_won`, `dealtype`, `platform_prospect*`.
- Companies: `casafari_company_id` ↔ Mongo `companies._id`. Contacts: `casafari_user_id`, `platform_account_id`,
  `unsubscribe`, `hs_email_optout`, `hs_email_hard_bounce_reason_enum`, `lifecyclestage` ("other" = blacklist,
  6275506388 = internal), `hs_analytics_source`.
- Users object: `hs_assigned_seats`, `hs_connected_email_status`, `hs_calendar_sync_enabled`,
  `hs_calendar_connection_status`, `hs_meetings_enabled`.
- `query_crm_data`: max 2 GROUP BY dims (extras silently dropped); counts can sum IDs — verify.
  `get_crm_objects` returns `objects`, not `results`.
- Record link: `app.hubspot.com/contacts/144103290/record/0-2/<companyId>`. Admin: `tools.espressoresearch.com/companies/<id>`.

## Slack — Billy = `U025P35JVMH`
#hubspot_updates C0AHXHC4NRE · #audience-requests C0CDAF39J1H · #platform-api-mcp C0C92GC8H2Q ·
#platform-api-mcp-custom-requests C0C96PNLUE8 · #product_marketing_coordination C08SZ5Z3DHU · #spain GH00UD2CR ·
#portugal GJWLX7M2R · #italian_sales C013XBC1Y9Y · #sales_opportunities C07LZNPG0H4 · #revsquad_and_legal C07PFCLQE6S ·
#general C143HUBD3 · #churn-italy C06PR90DBPU · #bi_requests C080EM6H32T. Also: sales-closed-wons (bot posts wins/churns
with MRR), lost-revenues_weekly-file, people-revops, churn-spain/portugal/france, es_monitoring, customer_usage_alerts,
api_usage_monitoring, postmark_stats. Group DMs: ApiCat C0C9CKL256J, Pisos/ApiCat C0CER4C1LAJ, Commissions C0BF6BRQA8K.
Slack user search by email returns nothing — search by name/surname.

## Postmark — server CASAFARI_2026 (ID 19235117), Live; streams `outbound`, `broadcast`
See `playbooks/postmark-campaign-kpis.md`. 45-day message retention.

## Google Drive
- Contracts: folders `1YmE6YPku4yPixwRlxtE_aleLRLLxH4_s`, `1-l6estLK3MQ3ZXwR9CKYvRwjP2iIzFOy` (~800 PDFs).
- Data-ops costs: `15beyh7kd1h0Qdg5LP6tcNcOKRyYT4-sl`. Price reference: `Application_Prices_2025_2026.xlsx`.
- Billience: Audience Lists `1-t7Y2ry5yTR9_AiVPKkMJlAqhDkA7dDU`, Knowledge `1rjh6d3PidGAOuT17kRR2r0Vc1ckQ0EKm`,
  business rules v0.3 `1Gp2amImLORmxphFPQ57M6JiG0wewE1SE`.
- Google Doc creation: upload HTML via `Google_Drive.create_file` (auto-converts); edit with `Google_Docs.update_doc`.

---

## Working SQL snippets

### Contract owner credit (won = paid/hold)
```sql
WITH c AS (SELECT co._id cid, co.countryCode cc, ct FROM `casafari-cloud.mongodb_app_prod.companies` co,
  UNNEST(JSON_QUERY_ARRAY(co.contracts)) ct
  WHERE JSON_TYPE(co.contracts)='array' AND JSON_VALUE(ct,'$.createdAt') >= '<start>'),
o AS (SELECT cc, JSON_VALUE(ct,'$.stage') stage, JSON_VALUE(ct,'$.subscriptionType') st,
  SAFE_CAST(JSON_VALUE(ct,'$.value') AS FLOAT64) v,
  SAFE_CAST(JSON_VALUE(ow,'$.id') AS INT64) oid, SAFE_CAST(JSON_VALUE(ow,'$.part') AS FLOAT64)/100 part
  FROM c, UNNEST([JSON_QUERY(ct,'$.owners.first'),JSON_QUERY(ct,'$.owners.second'),JSON_QUERY(ct,'$.owners.third')]) ow
  WHERE ow IS NOT NULL)
SELECT cc, oid, u.name, COUNTIF(stage IN ('paid','hold')) won_n,
  SUM(IF(stage IN ('paid','hold'), part,0)) won_credit, SUM(IF(stage IN ('paid','hold'), v*part,0)) won_value
FROM o LEFT JOIN `casafari-cloud.tidb_prod.admin_users` u ON u.id=o.oid GROUP BY 1,2,3
```
Previous value without LAG IGNORE NULLS (not supported):
`LAST_VALUE(IF(stage!='new', v, NULL) IGNORE NULLS) OVER (PARTITION BY cid ORDER BY cr ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING)`

### Latest paid contract value / company segmentation
```sql
(SELECT SAFE_CAST(JSON_VALUE(k,'$.value') AS FLOAT64) FROM UNNEST(IFNULL(JSON_QUERY_ARRAY(contracts),[])) k
  WHERE JSON_VALUE(k,'$.stage')='paid' ORDER BY JSON_VALUE(k,'$.startDate') DESC LIMIT 1) AS val,
'CASAFARI' IN UNNEST(IFNULL(JSON_VALUE_ARRAY(labels),[])) AS internal,
REGEXP_CONTAINS(LOWER(name), r'\btest|teste|demo|dummy|casafari') AS test_named,
LOWER(IFNULL(availableUserLevel,''))='true' AS per_user_flag,
LAX_BOOL(JSON_QUERY(settings,'$.allowWidgets')) AS widgets
```
Segments: internal | per-user (needs paid sub) | val>1 paying | child of paying parent | child, parent not paying |
order-billed | likely trial (val ≤ 1).

### Per-user MRR
```sql
WITH s AS (SELECT id,user_id FROM `casafari-cloud.tidb_prod.user_subscriptions` WHERE status='paid' AND expired_at>=CURRENT_DATETIME()),
inv AS (SELECT subscription_id,id,ROW_NUMBER() OVER(PARTITION BY subscription_id ORDER BY date DESC) rn
        FROM `casafari-cloud.tidb_prod.invoices` WHERE status='paid' AND type='user_level')
SELECT s.user_id, SUM(it.unit_price*it.quantity*(1-IFNULL(it.discount,0)/100)/NULLIF(it.period,0)) mrr
FROM s JOIN inv ON inv.subscription_id=CAST(s.id AS STRING) AND inv.rn=1
JOIN `casafari-cloud.tidb_prod.invoice_items` it ON it.invoice_id=inv.id GROUP BY 1
```

### ApiCat children
```sql
SELECT _id, JSON_VALUE(parentId) parent, employeesStage,
 (SELECT COUNTIF(JSON_VALUE(e,'$.stage')='contract') FROM UNNEST(JSON_QUERY_ARRAY(employees)) e) active_users
FROM `casafari-cloud.mongodb_app_prod.companies`
WHERE JSON_VALUE(parentId) IN ('5ef1d80722fd83414d1f5475','6ad6205759ea3126786f7e67')
  AND _id NOT IN ('5ef1d80722fd83414d1f5475','6ad6205759ea3126786f7e67')
```

### Portal exclusivity (Barcelona province example, ~16 GB)
```sql
WITH bcn AS (SELECT id FROM `casafari-cloud.tidb_prod.flat_locations` WHERE level3_location_id=10163),
src AS (SELECT id, CASE domain WHEN 'www.idealista.com' THEN 'idealista' WHEN 'www.fotocasa.es' THEN 'fotocasa'
    WHEN 'www.habitaclia.com' THEN 'habitaclia' WHEN 'www.pisos.com' THEN 'pisos'
    ELSE IF(classified=0 OR TRIM(label) IN ('E&V','Realmark Inmobiliaria','Inmovilla','Inmovilla CRM','RE/MAX Spain','Savills',
      'Von Poll','Tecnocasa','Dahler','Barnes','Inmobiliaria Costa Del Sol','Inmobiliaria Estepona','CBRE','The Agency'),'agency','other_portal') END grp
  FROM `casafari-cloud.tidb_prod.sources` WHERE stage IN ('match','live','livenomatch') AND deleted_at IS NULL),
se AS (SELECT se.estate_id, src.grp, t.txn FROM `casafari-cloud.tidb_prod.source_estates` se
  JOIN src ON src.id=se.source_id JOIN bcn ON bcn.id=se.location_id
  CROSS JOIN UNNEST([STRUCT('sale' AS txn, se.status='active' AS live), STRUCT('rent', se.rent_status='active')]) t
  WHERE se.deleted_at IS NULL AND t.live AND IFNULL(se.estate_id,0)<>0),
pr AS (SELECT txn, estate_id, LOGICAL_OR(grp='idealista') i, LOGICAL_OR(grp='fotocasa') f, LOGICAL_OR(grp='habitaclia') h,
  LOGICAL_OR(grp='pisos') ps, LOGICAL_OR(grp='agency') a FROM se GROUP BY 1,2)
SELECT txn, COUNT(*) properties, COUNTIF(i AND NOT f AND NOT h) idealista_not_fh, COUNTIF(f AND NOT i AND NOT h) fotocasa_not_ih,
  COUNTIF(h AND NOT i AND NOT f) habitaclia_not_if, COUNTIF(a AND NOT (i OR f OR h OR ps)) agency_not_4portals FROM pr GROUP BY txn
```

### API request merge + endpoint normalisation
```sql
bt AS (SELECT id bt_id, account_id, request_fingerprint fp, date, endpoint,
  ROW_NUMBER() OVER (PARTITION BY account_id, request_fingerprint ORDER BY date, id) rn
  FROM `casafari-cloud.tidb_prod.accounts_balancetracking` WHERE ...),
rs AS (SELECT r.id rs_id, u.external_user_id account_id, r.request_fingerprint fp, r.date, r.path,
  ROW_NUMBER() OVER (PARTITION BY u.external_user_id, r.request_fingerprint ORDER BY r.date, r.id) rn
  FROM `casafari-cloud.tidb_prod.request_statistics` r JOIN `casafari-cloud.tidb_prod.api_users` u ON u.id=r.user_id WHERE ...),
j AS (SELECT * FROM bt FULL JOIN rs USING (account_id, fp, rn))   -- >60 s apart = 2 requests
-- endpoint:
REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(SPLIT(path,'?')[OFFSET(0)],
 r'/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}(/|$)', r'/*\1'),
 r'/[0-9a-fA-F]{24}(/|$)', r'/*\1'), r'/[0-9]+(/|$)', r'/*\1'), r'/[0-9]+(/|$)', r'/*\1')
```

### Platform customers
```sql
WITH cust AS (SELECT account_id, trial_units FROM `casafari-cloud.casafari_platform.accounts`
  WHERE NOT IFNULL(is_internal,false)
    AND account_id NOT IN (SELECT account_id FROM `casafari-cloud.casafari_platform.accounts_daily_snapshot` WHERE is_internal))
```
