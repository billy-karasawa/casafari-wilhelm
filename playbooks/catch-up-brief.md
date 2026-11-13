# Playbook: Catch-up brief (Slack + Gmail + Drive sweep)

- **Autonomy level:** see `_registry.md`
- **Cadence:** ad hoc (after absence) — can become the daily `/brief` backbone
- **Output destination:** Google Doc, **updated in place** on later passes (same link)
- **Last run:** 2026-11-11 — https://docs.google.com/document/d/1-vU80fZVgp1LlbLiWPrNnCwaA0L_pW0Xz6s2zlDfuzY/edit
  ("Catch-up brief — 2 to 11 Nov 2026", private to Billy)

## Purpose
Tell Billy what is still open and urgent across Slack, email and shared files since date X.

## Hard rules
- **Read-only. "Leave everything as unread."** Never post, react, mark read, archive or label.
- Low cost, no quality loss: parallel Sonnet sub-agents, each sweeping a slice of channels.
- Do the **deep sweep on the first pass** (Billy asked for a deeper one after a shallow first pass).

## Steps
1. Start date = Billy's last sent email (`in:sent`) or the date he gives.
2. **Gmail:** `search_threads` `is:unread after:YYYY/MM/DD -category:promotions -category:social
   -category:updates -category:forums`; drop automated senders (Factorial, property alerts,
   HubSpot/Looker reports, vendors).
3. **Drive:** `search_files` `sharedWithMe = true and modifiedTime > '<date>'`; flag never-viewed shares.
4. **Slack** (Billy = `U025P35JVMH`; the API can't see unread state):
   - mentions: `slack_search_public_and_private` filters `<@U025P35JVMH> after:<date>`
   - DMs: `is:dm after:<date>`, channel_types `im,mpim`, follow cursor to the end
   - channels: `slack_list_user_channels` (~200; ~140 typically inactive) → `slack_read_channel(oldest=<ts>)`
     → **`slack_read_thread` on every parent with replies** — status must be verified at thread level.
5. Before flagging, check Billy's own recent posts and his agents' posts — some items are already handled.
6. Write/refresh the Google Doc.

## Output format
🔴 Urgent · 🟠 High · 🟡 Medium · ⚪ FYI — each item: what, who's waiting, link, suggested action.
Then "Resolved since last time", "Suggested order for today", and "Coverage (what was/wasn't read)".

## Known pitfalls
- Bots that post like people: Mila's agent "Mira", Legal's agent "Themis"; "staff test" posts in
  #cs-copilot-handoffs are test traffic.
- Noise channels: shared_account_es / shared_account_pt ("Devices limit exceeded"), *_alerts, postmark_stats.
- commercial@ group address hides senders.
- Google Doc: create by uploading HTML via `Google_Drive.create_file` (auto-converts); update with
  `Google_Docs.update_doc` (deleteContentRange + insertText, then a styling pass); read back to verify.
