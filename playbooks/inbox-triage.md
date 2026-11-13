# Playbook: Gmail inbox triage

- **Autonomy level:** see `_registry.md` — **no bulk labelling/moving without approval**
- **Lesson:** connector cleanup of ~1,100 threads burned 23% of Billy's limit and was stopped. Bulk filing belongs
  in **Gmail filters** (free), which Billy creates himself (connector can't create filters).

## Cheap default
1. Search `is:unread newer_than:7d -category:{promotions social updates forums}` and drop automated senders below.
2. Return a short list of emails **from people** that need Billy's action (sender, subject, ask, suggested reply).
3. Never mark read, move, label or trash unless Billy approves that specific batch.

## Filter map (sender → existing label) — suggest as Gmail filters
application@casafari.com → Reports · noreply@lookermail.com → Looker Reports ·
sentry / crowdsec.net / basecamp.com → Devops · posthog.com → PostHog · Google Cloud/Search Console → Google ·
HubSpot notifications (not "super admin") → Hubspot · factorial.app (not approval/review/tasks) → Factorial ·
newsletters (medium, nytimes, substack, cbinsights, websummit, retool, …) → Info@Casafari.

## Safety
Suspicious/phishing-looking mail: leave untouched and flag to Billy.

## Open
Unknown whether Billy created the filters; ~450–500 threads filed before the stop (Factorial not started).
