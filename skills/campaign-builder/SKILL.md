---
name: campaign-builder
description: Assembles a complete LinkedIn outbound campaign brief into campaign-NAME.md - segment, signal stack, list-building steps in Apollo and Sales Navigator, the opener and follow-up sequence, LinkedIn tool setup notes (SalesRobot or similar) with safe daily limits and warm-up, metrics with targets, and a 14-day plan. Use when the user says "build a campaign", "plan my outbound", "set up a LinkedIn campaign", "campaign brief" or "launch a campaign for a segment".
---

# Campaign Builder

You turn icp.md and signals.md into one file the user (or their SDR) can run for 14 days without asking a single question.

## Inputs
- `icp.md` (required). `signals.md` from signal-scout (recommended). `offer.md` and `voice.md` (optional).
- Campaign name (ask if not given). Short, lowercase, hyphenated, for example `us-saas-hiring-engineers`.
- Which LinkedIn tool they use (SalesRobot, HeyReach, Expandi, Dripify, or manual). Which plan, if they know it (it changes daily caps).
- Which data tools they have: Sales Navigator, Apollo, the treg plugin, a CRM or a Google Sheet.
If signals.md is missing, run the signal-scout steps for the chosen segment yourself, briefly.

## Steps
1. **Segment.** Pick one segment from icp.md. One campaign = one segment + one signal stack. Write who is in and who is out.
2. **Signal stack.** Pick 2 or 3 signals that overlap (for example: hiring engineers + raised money in 6 months + VP Eng new in seat). Say which signal the opener will mention.
3. **List building.** Write click-by-click steps for Sales Navigator and for Apollo, with every filter value and boolean string. Add a target list size. Rule of thumb: 300 to 600 leads for a 14-day test on one sender.
4. **Clean the list.** Remove exclusions, current clients, competitors, people contacted in the last 90 days, and duplicates across senders.
5. **Sequence.** Write the connection note (optional, see limits), opener (3 variants, opener-writer rules), and follow-ups for day 3, 7, 14 and a breakup (follow-up-writer rules). Mark which variant to A/B test.
6. **Tool setup.** Write the settings for their LinkedIn tool: daily caps, working hours in the prospect's time zone, reply detection on, stop-on-reply on, A/B split, and which custom fields hold the personalised line.
7. **Reply plan.** Who answers replies, how fast (target under 1 hour in working hours), using reply-handler. Two specific times for every yes, no calendar link before a reply.
8. **Metrics.** Targets and the stop/fix rules.
9. **14-day plan.** Day by day.
10. Save as `campaign-<name>.md` using `templates/campaign-template.md` in this skill folder. Show the 14-day plan in chat.

## Safe sending (read this into every brief)
- LinkedIn does not publish an exact daily or weekly invitation number. Its Help pages do state a cap of 30,000 first-degree connections. Most outreach tool vendors report roughly 100 invitations a week for a typical account, and say an invitation restriction usually lasts about a week. Plan for 100 a week, not more.
- Free and Basic LinkedIn members can add a personal note to only 5 connection requests a month (LinkedIn Help, "Invitation limit reached"). Premium members (Sales Navigator included) can send unlimited personalised notes. If the sender is on a free account, send blank invites and put the real opener in the first message after they accept.
- Tool caps are a ceiling, not a target. For example SalesRobot lists 20 actions a day per type on its Basic plan and 75 a day on Advanced and Professional. Use your own safer numbers below.
- Conservative ramp (Prity's defaults, adjust to your account's age and acceptance rate):
  | Week | Connection requests per day | Messages to new connections per day | Profile views per day |
  |------|------------------------------|--------------------------------------|-----------------------|
  | 1 (warm-up) | 8 to 10 | 15 to 20 | 20 |
  | 2 | 12 to 15 | 25 to 30 | 30 |
  | 3+ | 15 to 20 (stay near 100 a week) | 30 to 40 | 40 |
- Withdraw invitations older than 3 weeks. A big pending pile hurts acceptance.
- Send only in the prospect's working hours, on weekdays. Wednesday and Thursday were the top first-reply days in the 300 booked calls. Weekends were only 9% of first replies.
- One sender per prospect. If two teammates message the same person, prospects notice and call it out.
- Never automate anything LinkedIn's User Agreement forbids. LinkedIn automation tools say themselves that use may not comply with it. The user accepts that risk, so keep volumes human and stop at the first warning.

## Metrics and targets
| Metric | Healthy | Fix it if |
|--------|---------|-----------|
| Acceptance rate | 30%+ | Under 20%: tighten the list, improve the profile headline, drop the note |
| Reply rate (on accepted) | 10 to 20% | Under 5% after 100 sends: change the signal or the opener |
| Positive reply rate | 30%+ of replies | Under 20%: the offer or segment is off |
| Reply to booked call | 30%+ | Under 20%: reply speed or the "two times" step is missing |
| Our median reply time | under 1 hour | Over 4 hours: set alerts, use reply-handler |
These are working targets from running campaigns, not guarantees. Track them weekly with pipeline-report.

## Output format
Use `templates/campaign-template.md`. Every section filled. No "TBD". If something is unknown, write the default and mark it "(default, change if needed)".

## Rules
- One segment and one primary signal per campaign. Two segments = two campaigns.
- No calendar link anywhere in the sequence. Links only after a yes.
- Opener and follow-ups must follow the opener-writer and follow-up-writer rules (about 43 words, end on a question, no call ask in message 1, each follow-up adds something).
- No client names in proof. Industry and geography only.
- No em dashes, no hype words.

## Example (summary of a finished brief)
Campaign: `us-midmarket-hiring-engineers`
Segment: US software companies, 200 to 1,000 staff, 5+ open engineering roles.
Signal stack: engineering job posts (30 days) + engineering headcount growth 10%+ + VP or Head of Engineering new in seat (90 days).
List: Sales Navigator account search, then lead search for VP or Head of Engineering and CTO. Target 450 leads.
Sequence: blank invite, opener A/B (noticed + question vs give first), follow-ups day 3, 7, 14, breakup day 24.
Tool: SalesRobot, ramp week 1 at 10 invites a day, working hours 9 AM to 5 PM ET, stop on reply.
Goal for 14 days: 150 invites, 45 accepts, 6 to 9 replies, 2 to 3 booked calls.
