---
name: icp-builder
description: Interviews the user one question at a time and writes icp.md (offer, segments, buyer titles, geographies, exclusions, pains, triggers, proof). Use when the user says "build my ICP", "who should I target", "define my ideal customer", "start a new outbound campaign" and no icp.md exists yet, or when they want to update an existing icp.md.
---

# ICP Builder

You run a short interview and turn the answers into `icp.md`, the file every other skill in this pack reads first. A sharp ICP is the difference between 40 booked calls and 4, so take your time here.

## When to use
- The user has no `icp.md` in the project folder and wants to start outbound.
- The user says their targeting is "everyone" or "any B2B company".
- The user wants to refresh the ICP after new wins, a new offer or a new market.

## Before you start
1. Look for an existing `icp.md`, `offer.md` or `voice.md` in the current folder. If `icp.md` exists, read it and ask: "Do you want to update this ICP or start a fresh one?"
2. If `offer.md` exists, read it so you do not ask questions it already answers.
3. Tell the user: "I'll ask about 12 short questions, one at a time. Short answers are fine. Say 'skip' to any question."

## The interview (one question per message, wait for each answer)
Ask in this order. After each answer, reflect it back in one line if it was vague, then move on. Never ask two questions in one message.

1. **Offer**: "In one sentence, what do you sell and what result does the client get?"
2. **Best clients**: "Think of your 3 best clients ever (no names needed). What industry, size and country were they, and why were they great?"
3. **Worst clients**: "Now your worst 1 or 2. What made them a bad fit?" (These become exclusions.)
4. **Segments**: "If you could only sell to one type of company for the next 90 days, which one? Any second or third choice?"
5. **Size**: "What company size works best? Headcount or revenue range is fine."
6. **Buyer**: "Who signs the contract? And who feels the pain day to day, if that is a different person?"
7. **Geography**: "Which countries or regions do you want? Any you cannot serve?"
8. **Pains**: "What does your buyer complain about before they hire you? Use their words if you can."
9. **Triggers**: "What usually happens right before someone buys? For example a funding round, a new sales leader, hiring, losing a big client."
10. **Proof**: "What results can you share? Numbers, time frames, industry and country. No client names unless you have permission."
11. **Objections**: "What are the top 3 reasons people say no, and what do you say back?"
12. **Exclusions**: "Anyone we must never contact? Current clients, competitors, partners, a do-not-contact list?"

If the user gives a long voice-note style answer, pull out the facts yourself and confirm: "So the decision maker is the founder, and the user is the head of recruitment. Right?"

## Writing icp.md
1. Use the structure in `templates/icp.md` (in this skill folder). Fill every section. Write "unknown" where the user skipped, never invent.
2. Rank segments: put the segment with the strongest proof and the most urgent trigger first.
3. Write pains in the buyer's words, in quotes.
4. Turn the worst-client answers into clear exclusions.
5. Save as `icp.md` in the current working folder (or the path the user gives). Show the user a 6-line summary and the file path.

## Rules
- One question per message. No forms, no lists of questions.
- Never invent proof, numbers or client names. If a number is fuzzy, write it as a range and mark it "(estimate)".
- Do not include client names in proof. Use industry and geography, for example "a US fractional CFO firm".
- Keep the whole file under about 120 lines. It should be readable in 2 minutes.
- No em dashes. Use commas, colons or full stops.

## Quality check before saving
- [ ] Offer fits in one sentence and names a result.
- [ ] Max 3 segments, ranked.
- [ ] At least 1 decision-maker title and 1 champion title.
- [ ] At least 3 pains and 3 triggers.
- [ ] Exclusions section is not empty.
- [ ] Every proof line has a number or says "none yet".

## Example
User: "We're a 30-person IT services firm. We build and run dev teams for US mid-market companies."

Good follow-up (question 2): "Think of your 3 best clients ever. What industry, size and country were they, and why were they great?"

Resulting segment row:
| # | Segment | Company size | Why they buy | Deal size |
|---|---------|--------------|--------------|-----------|
| 1 | US software companies hiring 5+ engineers | 200 to 1,000 staff | Local hiring is slow and expensive | $15k to $40k per month |

## Next step to suggest
"Your ICP is saved. Next, run signal-scout to find the 20 buying signals for this ICP and the exact filters to find them."
