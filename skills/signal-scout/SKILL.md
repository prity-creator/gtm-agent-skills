---
name: signal-scout
description: Reads icp.md and outputs the 20 buying signals that matter most for that ICP, where to find each one (Sales Navigator, Apollo, job boards, LinkedIn post engagement, funding news, events), the exact boolean and keyword strings, and the opener angle for each. Use when the user asks "what signals should I track", "who is in-market", "find buying signals", "build my signal list" or "where do I find leads for this ICP". Can pull a sample list if the Apollo connector or the treg plugin is available.
---

# Signal Scout

A signal is a public event that makes your offer more relevant right now. Signals beat static lists because the opener can be about something real that just happened to the prospect. Your job: pick the 20 signals that fit this ICP best and show exactly where to find each one.

## Inputs
- `icp.md` in the current folder (required). If it is missing, say so and offer to run icp-builder first.
- `offer.md` (optional) for the resources you can send.
- `reference/signals-library.md` in this skill folder: the master list of signal types, sources and filter notes. Read it before you start.

## Steps
1. **Read icp.md.** Write down: segments, titles, geographies, headcount, top pains, triggers, exclusions.
2. **Score every signal in the library** against this ICP on three things, 1 to 5 each:
   - Pain link: does this event make one of the ICP pains worse or more urgent?
   - Findability: can a normal person find it with Sales Navigator, Apollo, a job board or Google in under 10 minutes?
   - Freshness: is there a clear date, so the opener can say "last week" or "in March"?
   Total = pain x 2 + findability + freshness (max 20).
3. **Add ICP-specific signals.** Use the triggers section of icp.md. Turn each trigger into a findable signal. Example: trigger "losing a big client" is not findable, but "posted 3+ sales roles after a layoff" is.
4. **Pick the top 20.** Keep a mix: at least 4 hiring or team signals, 3 people signals (new in seat, job change), 3 company signals (funding, expansion, launches), 3 engagement signals (posts, comments, events), 2 tech or tool signals. Drop anything an exclusion rules out.
5. **Write the source and the exact search** for each signal. Use real filter names from the library. Write boolean strings that work in the Sales Navigator keyword or title field: `AND`, `OR`, `NOT`, quotes for phrases, brackets for groups. Write them in UPPERCASE operators.
6. **Write the opener angle** for each signal: one line that says what you would notice. Never a pitch.
7. **Optional: pull a sample.** If an Apollo connector (tools named like `apollo` or `mcp__apollo`) or the treg plugin/skill is available, ask the user: "Want me to pull 10 sample accounts for the top 3 signals? It uses your Apollo credits or treg balance." Only run it after a yes. Show the cost first if the tool shows one. Never enrich emails or phones unless asked.
8. **Save the result** as `signals.md` next to icp.md and show the top 5 in chat.

## Output format (signals.md)

```
# Buying signals for <segment 1>
Built from icp.md on <date>

## Top 20
| # | Signal | Why it means "buy now" | Where to find it | Exact filter or string | Fresh window | Opener angle | Score |
|---|--------|------------------------|------------------|------------------------|--------------|--------------|-------|

## Search strings (copy-paste)
### Sales Navigator
SALES NAV FILTER: ...
BOOLEAN (title): ...
BOOLEAN (keyword): ...

### Apollo
APOLLO FILTER: ...

### Job boards and Google
BOOLEAN: ...

## Signal stack for the first campaign
Pick 2 or 3 signals that overlap. Overlap = stronger intent and an easier opener.
1. ...

## Not worth tracking for this ICP
- <signal>: <one-line reason>
```

## Rules
- Every signal must have a place to find it and a search you can paste. "Watch for growth" is not a signal.
- Prefer signals with a date. The opener needs "noticed you ... last week".
- Respect exclusions in icp.md.
- Filter names change. Use the names from the library and add: "If a filter name differs in your account, pick the closest one."
- Do not scrape LinkedIn or suggest tools that break LinkedIn's terms. Sales Navigator search and saved-search alerts are fine.
- No em dashes. No hype words.

## Example (one row)
ICP: 30-person IT services firm selling dedicated dev teams to US mid-market software companies.

| # | Signal | Why it means "buy now" | Where to find it | Exact filter or string | Fresh window | Opener angle | Score |
|---|--------|------------------------|------------------|------------------------|--------------|--------------|-------|
| 1 | 5+ open engineering roles | Local hiring is slow, the backlog grows | Sales Navigator accounts, LinkedIn Jobs, careers page | Account filter: Job opportunities = hiring on LinkedIn. Department headcount growth (Engineering) > 10%. BOOLEAN job title: ("software engineer" OR "backend engineer" OR "full stack") NOT intern | Posted in last 30 days | "Noticed you have 7 engineering roles open, mostly backend. Is the goal to hire all of them in-house?" | 19 |

## Next step to suggest
"Pick one signal stack and run campaign-builder, or paste a company into account-research to test the hooks."
