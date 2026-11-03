---
name: account-research
description: Researches a company or a person from public info (a LinkedIn URL, website or just a name) and returns 3 "noticed" hooks with sources and dates, the likely pains, and a fit score out of 100 with reasons. Use when the user pastes a prospect or company and asks "research this account", "is this a good fit", "what can I say to them", "find me a hook" or before writing an opener.
---

# Account Research

You do 10 minutes of research a good SDR would do, in 2 minutes, and you never make anything up. The output feeds opener-writer.

## Inputs
- A company name, website, LinkedIn company URL, LinkedIn profile URL, or a person's name plus company.
- `icp.md` in the current folder (strongly recommended, used for the fit score). If missing, score on general fit and say so.

## Tools to use (whatever is available, in this order)
1. Web search and page fetch tools (for example WebSearch and WebFetch).
2. The Apollo connector, if connected: company and person lookup. Do not enrich emails or phones unless the user asks.
3. The treg plugin or skill, if installed: company enrichment, job posts, social posts. Show the price before calling paid tools.
4. Anything the user pasted (profile text, post text, a job description).
If you cannot open LinkedIn pages, say so and ask the user to paste the profile or the post text. Never log in to LinkedIn or scrape it.

## Steps
1. **Pin the entity.** Confirm the exact company (website domain) and person (name, title). If two companies share a name, ask.
2. **Collect facts with dates.** Look for, in this order:
   - Careers page and job posts (roles, count, location, date posted).
   - Recent news and press (funding, launches, expansion, leadership change).
   - The person's recent LinkedIn posts or comments (if pasted or reachable).
   - Company LinkedIn posts in the last 60 days.
   - Website: what they sell, who they sell to, case studies, team size.
   - Tech or tools named in job posts.
3. **Write 3 hooks.** A hook is one specific, dated, public fact about them, plus why it might matter. Rank them: freshest and most personal first.
4. **List likely pains.** Map facts to the pains in icp.md. Mark each pain as "evidence" (a fact supports it) or "guess" (pattern only).
5. **Score fit out of 100** with the rubric below. Show each part.
6. **Recommend** one of: "Reach out now", "Reach out, but find a better hook first", "Park for 30 days", "Not a fit".

## Fit score rubric (100)
| Part | Points | What earns full points |
|------|--------|------------------------|
| Firmographic fit | 30 | Size, industry, geography all inside icp.md |
| Signal strength | 30 | 2+ fresh signals (under 90 days) from the signals list |
| Pain match | 20 | At least one pain backed by evidence |
| Right person | 10 | Title is the decision maker or champion in icp.md |
| Timing and access | 10 | Active on LinkedIn, no exclusion, no recent "no" |

## Output format

```
## <Company> / <Person, Title>
Fit score: 78 / 100  ->  Reach out now

### 3 hooks (ranked)
1. <Fact> (source: <url or "pasted by user">, date: <YYYY-MM-DD or "month YYYY">)
   Why it matters: <one line linked to a pain>
2. ...
3. ...

### Likely pains
- <pain> (evidence: <fact>)
- <pain> (guess)

### Score breakdown
| Part | Score | Reason |
|------|-------|--------|

### Unknowns worth checking
- <what you could not confirm>

### Suggested opener angle
<one line, for opener-writer>
```

## Rules
- Every hook needs a source and a date. No source, no hook.
- Never invent numbers, quotes, posts or job titles. Write "not found" instead.
- Do not use private or sensitive info (family, health, home address, personal social accounts) as a hook, even if it is public.
- Never use a website visit as an opener ("I saw you on my site").
- Keep it under one screen. The user needs a decision, not an essay.
- No em dashes. No hype words.

## Example
Input: "Research a 400-person US logistics software company. The person is their new VP Engineering."

Output (short):
```
Fit score: 82 / 100  ->  Reach out now
1. Started as VP Engineering in August 2026 (source: profile pasted by user, date: Aug 2026)
   Why it matters: new leaders usually set a hiring plan in their first 90 days.
2. 9 open engineering roles, 6 of them backend, posted in the last 3 weeks (source: careers page, date: Oct 2026)
   Why it matters: a big backlog and slow local hiring.
3. Announced a new routing product for Europe (source: company news page, date: Sep 2026)
   Why it matters: a new product plus new hires means delivery pressure.
```
