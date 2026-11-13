# Playbook: Marketing audience lists (owned by Billience)

- **Owner agent:** **Billience** — separate assistant, scheduled task `trig_01Ucro8EGBKnk4qmMPn6hkDW`
  (weekdays 08:12–17:12 Lisbon, hourly) watching #audience-requests (C0CDAF39J1H).
  One-shot `trig_01X5sAV1TAuwpwiVaEyCFgCY` (14 Nov 08:37): re-run Black Friday UTM sign-ups and DM Maryna.
- **Wilhelm's role:** don't duplicate Billience. Track its open questions, help Billy decide rules, audit lists.
- **Rules of record:** `casafari_business_rules` v0.3 (Drive `1Gp2amImLORmxphFPQ57M6JiG0wewE1SE`);
  requests log https://docs.google.com/document/d/1bPRdEdZpjzX_h9ULZjj5Tj-Kn6NFXwaoVo2aUEQ2Qpg/edit
- **Folders:** Audience Lists `1-t7Y2ry5yTR9_AiVPKkMJlAqhDkA7dDU`; Knowledge `1rjh6d3PidGAOuT17kRR2r0Vc1ckQ0EKm`.

## Flow
Qualify purpose & unsubscribe handling → propose plan → Google Sheet + email-only CSV (one combined CSV for
Mailcleanup) → Maryna runs deliverability check → remove Undeliverable → results into the Drive folder.

## Key rules (Billy)
- "Only actual customers": user-level `stage=contract` + company segmentation (value > €1, child of paying parent,
  or paid orders); exclude internal label, test-named, @casafari.com, likely trials.
- Inclusion from BigQuery, **not** HubSpot marketing contacts. Exclusion: HubSpot unsubscribed/opt-out/hard bounce
  + Postmark suppressions/bounces. Bounces always removed; unsubscribes depend on purpose — ask.
- Accept-all / Unknown → Maryna decides. Exclude users not in HubSpot (except new Api.Cat agents).
- Lookback for lost/open deals & inbound: 24 months by BigQuery creation date.
- Valuation usage = `valuationRequests.type IS NULL`.
- Similar requests → proceed directly; new/unclear/sensitive → ask. Tag Billy `<@U025P35JVMH>` for confirmations.

## Past requests
- #1 AI Presentation builder launch — 16,983 users.
- #2 Black Friday email 1 — 66,325 contacts (churned 2,658; lost/open deals 2,479; inbound non-converted 35,495;
  free web app 4,248; current clients 21,445).
