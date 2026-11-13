# Playbook: Web App pricing questions & price book

- **Autonomy level:** see `_registry.md`
- **Cadence:** ad hoc — long-term goal is a pricing validation agent answering reps' pricing questions in
  Slack or routing them to Billy
- **Output destination:** chat answers; artifacts + HTML/PDF for reviews; Sheets/xlsx for lists
- **Key artifacts:**
  - Web App Pricing Review — https://claude.ai/artifact/AqpNq1yPNUPJiDEyKLgWDX
  - Price Book 2027 v6 (+calculator) — https://claude.ai/artifact/BVPWM8GFKm1BkjhT1DPhHa
  - Self-Serve Migration Plan — https://claude.ai/artifact/H3N6uxkrWb2gUBCopcsXKj
  - Contract Audit 2026 — https://claude.ai/artifact/1X4HUjAWW5Unut6qqWeE3N
- **Status:** draft price book **not yet approved** — never quote draft prices as final.

## Definitions
- **Web App customer:** `companies.employeesStage='contract'` AND any of `settings.allowAlertsPage`,
  `allowMetasearch`, `allowPropertyValuationPage` true. Use latest contract with `stage='paid'`.
  `value` = monthly; `extraValue` = price per extra seat.
- **Seats:** `softLimitOfAccounts`, else count employees with stage contract.
- **Value = 1 contracts:** child paid by parent (`parentId`; parentId=_id → is parent) · one-time payment
  (`orders`) · "false active" trial (no parent, no order) · internal (label CASAFARI).
- **Bundles:** API (label/order description) · Lead Magnet (`allowWidgets`) · CRM (label CASAFARICRM) ·
  Feedcruncher (label FEEDCRUNCHER) · CBE (`allowLocationSourcing`, not `sourcingAndUnderwriting`).
  Analyse bundle totals, don't split per product.
- **Per-user companies** (`availableUserLevel`): access only with paid user subscription + paid invoice in tidb.
- **Self-serve < €300 MRR ≤ sales-led** (web app only, lifetime discounts).
- **Brand** = `companyLogos.text`. "Key Account" is internal segmentation, not a brand.
- **Owner:** `settings.salesManager` = closer of first deal; true ownership = `contracts[].owners`.
  AM = `settings.accountManager.name` (from BigQuery, not old files).

## Draft 2027 list (per company / month, annual billing) — DRAFT
| Market | 1 seat | 2 | 3 |
|---|---|---|---|
| PT | 35 | 65 | 90 |
| ES | 90 | 120 | 150 |
| IT | 50 | 90 | 120 |
| FR | 40 | 80 | 120 |
| DE/AT | 99 | 130 | 150 |
Baleares = only premium location. Billing surcharges: biannual +5%, quarterly +10%, monthly +20%.
Brand prices: RE/MAX ES €20, RE/MAX IT €20, eXp PT €10.
Lead Magnet (draft, flat/company, 1 widget, no landing page): with web app PT €45; ES/IT/FR €50; DE/AT €60;
standalone €60 (DE/AT €80).

## Live platform plans (since 6 Nov 2026)
Free · Agent €49 · Agency €249 (10k tokens) · Business €990 (50k tokens; €792/mo yearly).
Claro Start €249, Claro AI €500 separate. Add-ons: Chrome ext €8/mo (€6 yearly), Lead-Gen €15/mo (€12 yearly),
excl. VAT. Setup fee norm ~€1k for template customisations.

## Exceptions
- Portugal Sotheby's: users on parent, billing via ~9 children.
- New Engel & Völkers Iberia offices are trials — skip.
- Promo codes with `allowed_domains` apply automatically.

## Known pitfalls
- `allowWidgets` ≠ paid Lead Magnet (166 flagged, 6 with a widget).
- Promo codes conflict with the book: REMAXES €30 vs €20, EXPPT €15 vs €10, ONEPT €12 vs €15,
  MAISCASAFARI €18 vs €20; ADDONSKWPT applied to web invoices.
- Contract matching: exclude Casafari's own VAT; ES clients may be contracted by Casa Safari Lda or
  Casafari France SAS.

## Escalate to Billy
Any price not in the approved book; discount requests; conflicts between promo code and book.

## Open decisions
See `followups/open-items.md` (price book approval, promo fixes, renewal impact −€20.1k MRR / −6.9%).
