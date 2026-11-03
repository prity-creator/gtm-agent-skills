---
name: inbox-analyzer
description: Analyses exported LinkedIn conversations (CSV or JSON with thread_id, sender us|them, timestamp, text) and reports reply on message 1 vs after a follow-up, time to first reply, opener length, question-ending rate, links sent before a reply, day and time proposals, and your own response time, then says what to fix first. Use when the user says "analyse my inbox", "what's working in my DMs", "look at my LinkedIn conversations", "why aren't people replying" or uploads a conversations export.
---

# Inbox Analyzer

Your inbox already knows what works. This skill runs a small script over your exported conversations and compares your numbers with the patterns from Prity Kar's 300 booked-call threads.

## Inputs
A CSV or JSON file of messages. Required columns (case does not matter):
| Column | Meaning |
|--------|---------|
| `thread_id` | groups messages into one conversation |
| `sender` | `us` or `them` (also accepted: me, we, outbound / prospect, lead, inbound) |
| `timestamp` | ISO 8601 like `2026-10-07 09:15` or `2026-10-07T09:15:00Z`, or epoch seconds or ms |
| `text` | message body |
JSON can be a list of messages, `{"messages": [...]}` or `{"threads": [{"thread_id": "...", "messages": [...]}]}`.

### Getting the data
- **SalesRobot, HeyReach and similar tools**: export conversations or campaign messages to CSV, then rename columns to the four above.
- **LinkedIn data export**: LinkedIn Settings, Data privacy, "Get a copy of your data", tick Messages. The `messages.csv` has columns like CONVERSATION ID, FROM, DATE, CONTENT. Map CONVERSATION ID to `thread_id`, DATE to `timestamp`, CONTENT to `text`, and set `sender` to `us` when FROM is your own name, otherwise `them`. Offer to do this mapping for the user with a short Python snippet.
- Remove anything you do not want analysed. The script runs locally and sends nothing anywhere.

## Steps
1. Ask for the file path, or use the one the user gave. If columns differ, write a 10-line conversion and save `<name>.clean.csv`. Show the user the mapping first.
2. Run:
   `python3 "${CLAUDE_SKILL_DIR}/scripts/analyze.py" <file>`
   Add `--json` if you want the numbers to build a chart or a table.
   To try it first: `python3 "${CLAUDE_SKILL_DIR}/scripts/analyze.py" "${CLAUDE_SKILL_DIR}/samples/sample_threads.csv"`
3. Read the report. Compare with the benchmark table below.
4. Write a short summary: 3 things working, 3 things to fix, each with the number behind it.
5. Pull 3 examples from their own data: the best-performing opener style, a thread that replied after a follow-up (and which follow-up type), and a thread that went cold after a link or slow answer.
6. Suggest next skills: opener-writer for new openers, follow-up-writer for gaps, reply-handler if response time is slow.

## Benchmarks (300 booked-call threads, 6,497 messages)
These are threads that ended in a booked call, so they are a "what good looks like" picture, not an average inbox.
| Metric | Booked-call threads |
|--------|---------------------|
| Replied to message 1 | 59% (41% only after a follow-up) |
| Median time to first reply | about 10 hours, 60% within 24 hours, 10% took 10+ days |
| Median opener length | 43 words (25% under 24 words, 22% over 80) |
| Openers ending on a question | 55% |
| Openers asking for a call | 30% |
| Calendar link before a reply | 0 of 300 |
| Proposed a specific day and time | 70% |
| Our median response time | 48 minutes (53% within an hour) |
| Top first-reply days | Wednesday and Thursday, weekends 9% |

## What the script reports
1. When they first replied: message 1, 2, 3, 4+ or never.
2. Time to first reply from your first message: median, middle half, within 24 hours, over 10 days. First reply length and weekday.
3. Opener length: median, mean, range, share under 28 and over 80 words, length when they replied vs not.
4. Question-ending rate and reply rate with vs without a question. Openers that ask for a call.
5. Links and calendar links sent before they replied.
6. Day and time proposals after a reply, how many offered two options, calendar links after a reply.
7. Your response time to their messages: median, within 1 hour, within 24 hours.
8. "What to fix first": plain-English actions.

## Rules
- Never upload the user's messages to any outside service. Run the script locally.
- Never quote a prospect's name or company in a summary meant for sharing. Use "a US CFO" style descriptions.
- Small samples lie. Under 30 threads, say "early signal, not proof".
- No em dashes, no hype words.

## Example output (on the bundled synthetic sample, 30 fake threads)
```
1. WHEN DID THEY FIRST REPLY? (threads we started)
   msg 1     #######.................   8  (29.6%)
   msg 2     ####....................   4  (14.8%)
   msg 3     ###.....................   3  (11.1%)
   msg 4+    #.......................   1  (3.7%)
   no reply  ##########..............  11  (40.7%)
   Reply rate: 59.3%.  Of replies: 50.0% on msg 1, 50.0% only after a follow-up.
...
4. OPENERS THAT END ON A QUESTION
   77.8% end on '?'.  Reply rate: 66.7% with a question vs 33.3% without.
```
