# Signals library

The master list signal-scout scores against an ICP. Grouped by type. Each row: what it is, where to find it, filter notes.
Filter names are the ones shown in the tools in late 2026. Vendors rename filters often, so pick the closest match in your account.

## A. Hiring and team signals
| Signal | Where | Filter notes |
|--------|-------|--------------|
| Hiring for the role your service replaces (SDRs, recruiters, engineers, bookkeepers) | Sales Navigator accounts, LinkedIn Jobs, Apollo, Indeed, company careers page | SN account filter "Job opportunities". Apollo "Job postings" with job titles. Google: `site:boards.greenhouse.io OR site:jobs.lever.co "<role>"` |
| Hiring a leader for the function you serve (Head of Sales, VP Marketing, Controller) | LinkedIn Jobs, Apollo job postings | Leader hires mean a new plan in 90 days. Title boolean: `("head of" OR "VP" OR "director") AND (sales OR "business development")` |
| Department headcount growth | Sales Navigator accounts | SN account filter "Department headcount growth", pick the department and a growth range |
| Total headcount growth | Sales Navigator, Apollo | SN "Company headcount growth". Apollo "Headcount growth" |
| First hire in a function (first marketer, first sales rep) | LinkedIn Jobs, careers pages | Search job text: `"first" AND ("sales hire" OR "marketing hire")` or "founding AE" |
| Contract or freelance roles posted | Job boards, Upwork | Means budget exists and they are open to outside help |
| Layoffs or hiring freeze in the function | News, layoffs trackers, LinkedIn posts | Use carefully and kindly. Often a "do more with less" angle |

## B. People signals
| Signal | Where | Filter notes |
|--------|-------|--------------|
| New in seat (role started in last 90 days) | Sales Navigator leads | SN lead filter "Changed jobs" (in last 90 days) plus title boolean. Or "Years in current position" = less than 1 year |
| Promoted internally | Sales Navigator | "Years in current position" less than 1 plus "Years at current company" 2+ |
| Champion moved to a new company (your past buyer or user) | Sales Navigator saved leads, your CRM | Save past contacts as leads, then watch "Changed jobs" alerts |
| Posted on LinkedIn in the last 30 days | Sales Navigator leads | SN lead filter "Posted on LinkedIn". Active posters reply more |
| Mentioned in the news | Sales Navigator | SN lead filter "Mentioned in news" |
| Viewed your profile | LinkedIn, Sales Navigator | SN lead filter "Viewed your profile recently" |
| Follows your company page | Sales Navigator | SN lead filter "Following your company" |
| Shares a group, school or past company with you | Sales Navigator | "Shared experiences", "Groups", "School", "Past company" |

## C. Company signals
| Signal | Where | Filter notes |
|--------|-------|--------------|
| Raised money in last 6 to 12 months | Sales Navigator, Apollo, Crunchbase, news | SN account filter "Recent activities" (funding events). Apollo "Funding" (last round date and type) |
| Senior leadership change | Sales Navigator accounts | SN account filter "Recent activities" (senior leadership changes) |
| New office, new country, new product line | News, company LinkedIn posts, press pages | Google: `"<company>" ("opens office" OR "expands to" OR "launches")` |
| Acquisition (they bought or were bought) | News, Crunchbase | Integration work and new targets follow |
| Big client win or partnership announced | Company page, press release | Delivery pressure goes up |
| Revenue or headcount in your sweet spot | Sales Navigator, Apollo | Firmographic fit, not a timing signal. Use as a base filter, not one of the 20 |

## D. Engagement signals (warmest)
| Signal | Where | Filter notes |
|--------|-------|--------------|
| Commented on or liked a post about the pain | LinkedIn post engagement lists | Open a relevant post (yours, a competitor's, an influencer's), go through reactions and comments, filter to ICP titles |
| Commented a keyword on your lead magnet post | Your own posts | They asked for it. Send the resource first, no pitch |
| Asked a question in a community or forum | Reddit, Slack groups, LinkedIn groups | Quote their question back to them, kindly |
| Attending or speaking at an event | Event pages, LinkedIn events, Eventbrite and Meetup listings | SN lead filter "Groups" or keyword = event name. Speakers list on the event page |
| Engaged with a competitor | Competitor posts and pages | Careful wording, never name the competitor in the opener |
| Visited your website | RB2B, Warmly, your analytics | Never say "I saw you on my site". Use a related signal for the opener |

## E. Tech and tool signals
| Signal | Where | Filter notes |
|--------|-------|--------------|
| Uses a tool your service works with | Apollo "Technologies", Sales Navigator "Technologies used", BuiltWith | Good for "we work inside HubSpot" style angles |
| Started or stopped using a tool | Job posts that mention the tool, BuiltWith history | Job text: `"migrating to" OR "implementing" AND "<tool>"` |
| Reviews or complaints about a tool you replace | G2, Capterra, Reddit | Pain stated in public |

## Boolean cheat sheet (Sales Navigator keyword and title fields)
- Operators in UPPERCASE: `AND`, `OR`, `NOT`.
- Quotes for exact phrases: `"head of talent"`.
- Brackets to group: `("VP" OR "head of") AND (sales OR revenue)`.
- Keep strings short. Very long strings can time out or return odd results.
- Put role words in the Title field, topic words in the Keyword field.

## Freshness rules of thumb
- Job change: best inside 90 days.
- Funding: best inside 6 months.
- Job post: best inside 30 days.
- Post or comment: best inside 7 days.
- Event: the 2 weeks before and the week after.
