---
name: follow-up-writer
description: Writes the LinkedIn follow-up sequence after an opener gets no reply (day 3, day 7, day 14 and a breakup message), where every follow-up adds something new, using 8 follow-up types that got first replies in 300 booked calls (resource or list, one-line question, reverse question, proof drop, tiny bump, event invite, don't-get-buried, last nudge). Use when the user asks for "follow-ups", "a sequence", "they didn't reply", "what do I send next", "bump message" or "breakup message".
---

# Follow-up Writer

41% of booked calls in Prity Kar's 300-thread analysis replied only AFTER a follow-up: 56 after message 2, 30 after message 3, 13 after message 4 or later. Skipping follow-ups throws away almost half your calls. But "just checking in" adds nothing. Every follow-up must give the prospect a new reason to answer.

## The 8 follow-up types (what earned the first reply in 99 cases)
| Type | First replies | What it looks like |
|------|---------------|--------------------|
| 1. Resource or list | 23 | "Pulled a list of 31 companies hiring SDRs this week in your region. Want it?" Or attach it after they say yes. |
| 2. One-line question | 20 | One short question, nothing else. "Is hiring still the main plan for Q1?" |
| 3. Reverse question | 14 | Give them an easy way to say no. "Guessing this isn't a priority right now? Or is new business on hold?" |
| 4. Proof drop | 13 | One result with a number, industry and geography. No client names. |
| 5. Tiny bump | 12 | "Is that okay, <name>?" or "Any thoughts, <name>?" Only after a message that had real content. |
| 6. Event invite | 11 | A free live training or workshop that fits their pain. |
| 7. Don't-get-buried | 4 | "Just making sure this doesn't get buried." Light, short, rare. |
| 8. Last nudge | 3 | Breakup that still gives an out and a next step. "Should I just send the overview instead?" |

## Inputs
- The opener that was sent (paste it), prospect details and the hook.
- `offer.md` for resources, proof and events you can mention. `icp.md` for pains. `voice.md` for tone.
- If offer.md has no resources or proof, ask: "Do you have a list, case study, number or event I can use? Follow-ups without one are weaker." Never invent proof.

## Default sequence
| Step | Day | Recommended type | Length |
|------|-----|------------------|--------|
| FU1 | Day 3 | One-line question OR reverse question | under 20 words |
| FU2 | Day 7 | Resource or list OR proof drop | 25 to 50 words |
| FU3 | Day 14 | Event invite OR reverse question (whichever was not used) | 20 to 40 words |
| Breakup | Day 21 to 30 | Last nudge | under 30 words |
Tiny bump and don't-get-buried are light extras. Use one only right after a message that carried real value, never two in a row.

## Steps
1. Read the opener. Note what was already said, so nothing repeats.
2. Pick 4 different types for the 4 steps. No type twice.
3. Write each message. Start with "Hey <name>," or just the name for short ones. Keep the first-name greeting natural, not every time.
4. Each message must add one new thing: a new question, a new resource, a new number, a new angle, or an easy out.
5. Run the checks below and show the table.

## Rules
- Every follow-up adds something. No "just following up", "circling back", "bumping this" on their own.
- No calendar link before they reply. Not in any follow-up. 0 of 300 booked threads did this.
- No call ask in FU1. A soft ask is fine later only as a question ("worth a 15-minute look?"), never a link.
- Proof must be real and anonymised: "a US recruitment firm", "an Australian accounting practice". Never a client name.
- Offer the resource, then send it after they say yes, unless the user wants to attach it (32% of booked threads included a file).
- Stop the sequence the moment they reply. Hand off to reply-handler.
- Long silence is normal. 25% of booked threads ran 4+ months. After the breakup, move them to a 60 to 90 day nurture list, not the bin.
- No em dashes, no hype words, no guilt ("I've reached out 4 times").

## Output format

```
### Follow-ups for <name> (<title>, <company>)
Opener sent: <date>

**FU1, Day 3: Reverse question** (16 words)
<text>

**FU2, Day 7: Resource or list** (34 words)
<text>

**FU3, Day 14: Event invite** (27 words)
<text>

**Breakup, Day 24: Last nudge** (19 words)
<text>

| Check | FU1 | FU2 | FU3 | Breakup |
|-------|-----|-----|-----|---------|
| Adds something new | yes | yes | yes | yes |
| Different type from the others | yes | yes | yes | yes |
| No calendar link | yes | yes | yes | yes |
| Ends on a question or easy out | yes | yes | yes | yes |
| No em dash, no hype | yes | yes | yes | yes |
```

## Example
Opener (sent Monday): "Hey Sam, saw you stepped into the VP Engineering role in August and the team has 9 backend roles open. Are you planning to hire all of those in-house?"

- FU1, Day 3, one-line question: "Hey Sam, is the plan still to fill all 9 by end of Q1?"
- FU2, Day 7, resource: "Sam, we put together what 40 US mid-market teams paid for senior backend hires this year and how long each took. Want me to send it over?"
- FU3, Day 14, reverse question: "Guessing hiring is handled for now? Or is it more that outside teams aren't an option for you?"
- Breakup, Day 24, last nudge: "I'll stop here, Sam. Should I just send the one-page overview so you have it for later?"
