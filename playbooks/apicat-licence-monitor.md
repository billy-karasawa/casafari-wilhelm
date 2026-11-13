# Playbook: Api.Cat (Tecno API) licence monitor

- **Autonomy level:** see `_registry.md`
- **Cadence:** on request ("Please update") — daily refresh offered, never scheduled
- **Output destination:** dashboard artifact https://claude.ai/artifact/9SCEP3WiWNggs1FsdZnjrk + HTML + PDF
- **Last run:** 2026-11-12 — 644 children, 505 active users, invoice control €1,312.50

## Deal (signed 14 Oct 2026)
Associació d'Agents Immobiliaris de Catalunya resells Casafari All-in-One licences, 3-year term
(exit after year 1 with 30 days' notice).
- Catalan tier: 1st licence free to member / extras €15 → Casafari gets €2.50 first, €7.50 extra.
- Rest of Spain €15. Balears **€45** (Casafari €22.50).
- Minimum 3,500 × €2.50 = **€8,750/month**; invoice = greater of minimum or actual usage.
- "Novena bis" price floor: Casafari can't sell the same package directly at/below €2.50.
- Existing direct customers move only at renewal (€15/user, €45 Baleares). Lead magnet: ApiCat pays €10, sells €15.
- Strategic lever (Billy): **grow user count** in ApiCat children — partnership success, not retention discounts.

## Data
- Parents: Api.Cat `5ef1d80722fd83414d1f5475`, Api.cat (Baleares) `6ad6205759ea3126786f7e67`
  (the Baleares parent is itself a child of Api.Cat).
- Children query: `knowledge/data-sources.md` → "ApiCat children".
- Direct customers lost to ApiCat are labelled **APICAT**.

## Steps
1. Run the 2 BigQuery queries (children + active users; overlap with direct customers).
2. Rebuild datasets, HTML, PDF (Playwright); update dashboard datasets.
3. Report delta vs last run: children, active users, invoice control, new overlaps with direct customers.

## Quality checks
- [ ] Exclude test children ("Example 1", "Example 14") and flag out-of-tier agents under the Catalan parent.
- [ ] Flag person-named children and map them to their real company where known.
- [ ] Customer-overlap matches: only confirmed/likely — Billy rejects weak fuzzy matches.

## Open
Churn rule (Nuño vs Mila), legal reading of Novena bis, whether out-of-tier/test accounts count in invoice
control, live refresh (no BigQuery connector on claude.ai → snapshot only).
