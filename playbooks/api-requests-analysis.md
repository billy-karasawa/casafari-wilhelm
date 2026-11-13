# Playbook: API request log analysis

- **Autonomy level:** see `_registry.md`
- **Cadence:** ad hoc
- **Output destination:** dashboard artifact (last: https://claude.ai/artifact/GqWYYijM5siUcqgQptNUFe, snapshot)
- **Last run:** 2026-10-23 — 255,579 requests / 105 accounts / 99 endpoints in 24h; p50 341 ms, p95 1.6 s;
  error rate 8.2%

## Data (BigQuery `casafari-cloud.tidb_prod` — "it's in BigQuery", there is no direct TiDB)
- `accounts_balancetracking` (account_id, endpoint, route, status_code, date, duration, request_fingerprint)
- `request_statistics` (user_id, endpoint_id, path, date, status_code, request_fingerprint)
- Mapping: `request_statistics.user_id → api_users.id`; `api_users.external_user_id = accounts_account.id
  = balancetracking.account_id`.
- **Neither table is complete:** 23% in both, 50% only in request_statistics (`/properties/*`, `/listings/*`,
  `/distributions/*`), 27% only in balancetracking (`/v2/comparables/search`, SSO). Always merge.

## Steps
1. Merge: per (account, fingerprint), ROW_NUMBER by time in each table; FULL JOIN on (account, fp, rn);
   >60 s apart = two requests. SQL in `knowledge/data-sources.md` → "API request merge".
2. Normalise endpoints (strip query; UUID/24-hex/numeric ids → `*`).
3. Exclude/flag internal: is_staff, is_superuser, @casafari.com (application@ ≈ 20% of traffic).
4. Aggregate by customer and endpoint; error rate by account.

## Pitfalls
- Fingerprint = request content hash, not a unique id.
- BigQuery tool rejects DECLARE/scripting → CTEs only.
- Timezone of `date` unconfirmed.

## Open
Saved view for the merge; refresh schedule; high error rates for naxos.fr (~26%) and targomo.com (~25%).
