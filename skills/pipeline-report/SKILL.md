---
name: pipeline-report
description: Builds a weekly pipeline report from a CSV of leads and stages (new, contacted, replied, call booked, call held, proposal, won, lost, nurture) - week vs last week, where every lead sits, funnel conversion, results by campaign and owner, warm leads going cold, and red flags. Use when the user asks for a "weekly report", "pipeline report", "how did outbound do this week", "funnel numbers" or "which leads are going cold", and has a leads CSV or a CRM export.
---

# Pipeline Report

Every Friday (or Monday morning) you should know four numbers: replies, calls booked, calls held, revenue won, plus which warm leads are going cold. This skill turns a leads CSV into that report in one run.

## Inputs
A CSV with these columns (extra columns are fine, names are not case sensitive):
| Column | Example |
|--------|---------|
| `lead_id` | L001 |
| `name` | first name or initials |
| `company` | company name |
| `stage` | new, contacted, replied, call_booked, call_held, proposal, won, lost, nurture |
| `owner` | who works the lead |
| `campaign` | campaign name, for example us-saas-hiring |
| `value` | deal value in your currency (numbers, $ and commas are fine) |
| `created_at` | 2026-10-21 |
| `stage_changed_at` | date the lead entered its current stage |
| `last_touch_at` | date of the last message either way |
Common stage names are mapped for you (for example "Meeting booked" to call_booked, "Closed won" to won). If the user has a CRM, export a CSV from it or from a Google Sheet first.

## Steps
1. Get the file path. Check the columns. If they differ, map them and save `<name>.clean.csv`, showing the mapping.
2. Run:
   `python3 "${CLAUDE_SKILL_DIR}/scripts/report.py" <file>`
   Options: `--week-ending 2026-11-01` to pick the week, `--stale-days 5` to change the "going cold" rule.
   To try it first: `python3 "${CLAUDE_SKILL_DIR}/scripts/report.py" "${CLAUDE_SKILL_DIR}/samples/sample_leads.csv"`
3. Read the Markdown output. Add a 5-line summary at the top:
   - The one number that matters most this week (usually calls booked).
   - What went up, what went down vs last week.
   - The best campaign and why (more replies, more booked).
   - The biggest leak in the funnel (lowest conversion step).
   - The 3 actions for next week.
4. If the user wants a file, save as `pipeline-report-<YYYY-MM-DD>.md`.
5. For each warm lead going cold, offer to run follow-up-writer.

## Output format
```
# Pipeline report: Oct 26 to Nov 01, 2026

Summary
1. 3 calls booked this week (0 last week).
2. ...
3 actions for next week
- ...

<script output: at a glance, stages, funnel, by campaign, by owner, warm leads going cold, flags>
```

## Rules
- Do not guess missing stages or dates. Report how many rows were skipped or unknown.
- Report revenue only from the value column. Never estimate deal sizes.
- Keep prospect names out of anything the user plans to share outside the team.
- Under 20 leads, call conversion rates "early".
- No em dashes, no hype words.

## Example summary (bundled synthetic sample, 40 fake leads)
1. 3 calls booked and 1 deal won ($15,000) this week.
2. Open pipeline (call held + proposal): $60,000.
3. Biggest leak: booked to held at 62%. Send a LinkedIn reminder the day before every call.
4. 7 warm leads have not been touched in 7+ days. Follow up today with something new.
