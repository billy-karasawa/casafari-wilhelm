# Playbook: API Q&A knowledge base from HubSpot emails

- **Autonomy level:** see `_registry.md`
- **Cadence:** ad hoc (for the CS agent knowledge base)
- **Last run:** 2026-10-30 — 232 Q&As (Claudia's emails) + 255 Q&As (23 API deal owners). Files were in a
  sandbox → **regenerate and store in Drive** if needed again.

## Steps (cheap, no quality loss)
1. HubSpot EMAIL `search_crm_objects`: OR filter groups (from = person | to CONTAINS_TOKEN person) + `query:"API"`;
   props subject, direction, thread_id, timestamp; limit 200 + offset.
2. For deal owners: DEAL search `query:"API"` → owner ids → EMAIL search `hubspot_owner_id IN [...]`.
3. Bodies via `get_crm_objects` (~100 ids/call; result key `objects`).
4. Keep only latest email per thread; strip URLs, quotes, signatures, duplicates; cap 10–12k chars/thread;
   drop automatic "New API Deal"/"API deal adjustment" notifications.
5. 4–6 batch files → parallel Sonnet sub-agents → merge by category with a script; dedupe across sets.

## Output rules
Client staff → company name only; no email addresses. Agent must **not** quote prices from emails.
Categories: Pricing, Endpoints, Quotas, Access, Data coverage, Errors, Billing, Trials, Auth, MCP, Docs.

## Unresolved contradictions (for CS/Legal)
Token header format (Token vs Bearer), rate limits (fixed vs per plan), token lifetime, valuation bundles annual
vs monthly, data-use / PropIntel verbal statement, notary refresh frequency.
