# Campaign: <name>

Created: <YYYY-MM-DD>  |  Owner: <name>  |  Sender account(s): <name>  |  Tool: <SalesRobot / other / manual>

## 1. Segment
- In: <industry, size, geography, titles>
- Out: <exclusions from icp.md, current clients, competitors, contacted in last 90 days>
- Why this segment now: <one line>

## 2. Signal stack
| Signal | Source | Fresh window | Used in opener? |
|--------|--------|--------------|-----------------|
| | | | yes / no |

## 3. List building
### Sales Navigator (account search)
1. Account filters: <filter = value>
2. Save as account list: <name>
### Sales Navigator (lead search)
1. Account list: <name>
2. Title (boolean): `<string>`
3. Other filters: <seniority, geography, changed jobs, posted on LinkedIn>
4. Save search and turn on alerts.
### Apollo
1. People filters: <job titles, seniority, location, # employees, industry>
2. Company filters: <job postings, funding, headcount growth, technologies>
3. Save list: <name>. Export without enriching emails unless needed.
### Target size and cleaning
- Target: <number> leads
- Remove: exclusions, duplicates across senders, already contacted

## 4. Sequence
| Step | Day | Type | Message |
|------|-----|------|---------|
| Invite | 0 | blank or note | |
| Opener A | on accept | noticed + question | |
| Opener B | on accept | <variant> | |
| FU1 | +3 | | |
| FU2 | +7 | | |
| FU3 | +14 | | |
| Breakup | +21 to 30 | last nudge | |

Custom fields: `{{first_name}}`, `{{company}}`, `{{hook}}` (one line per lead).

## 5. Tool setup
- Daily caps: <invites / messages / views>, ramp: <week 1, 2, 3>
- Working hours: <hours> in <prospect time zone>, weekdays only
- Stop on reply: on. Reply detection: on.
- A/B: <split>
- Withdraw pending invites older than 21 days

## 6. Reply plan
- Who answers: <name>. Target: under 1 hour in working hours.
- Yes: two specific times in their time zone, ask for email. No link unless asked.
- Not now: offer a resource, set a date, tag "nurture <month>".

## 7. Metrics
| Metric | Target | Week 1 | Week 2 |
|--------|--------|--------|--------|
| Invites sent | | | |
| Acceptance rate | 30%+ | | |
| Reply rate (on accepted) | 10 to 20% | | |
| Positive replies | | | |
| Calls booked | | | |
| Our median reply time | under 1 hour | | |

## 8. 14-day plan
| Day | Task |
|-----|------|
| 1 | Build and clean list, write hooks for the first 50 |
| 2 | Load tool, set caps and hours, send first invites |
| 3 | ... |
| 14 | Review metrics, keep the winning opener, plan the next 14 days |
