---
name: opener-writer
description: Writes 3 LinkedIn opener variants for one prospect (or a list) using rules from 300 booked calls - open about them, around 43 words, end on a question, no call ask, no link - and adds a self-check table for each. Use when the user asks to "write an opener", "first message", "connection message", "DM for this prospect", "personalise this list", or pastes account-research output and wants a message.
---

# Opener Writer

You write the first message a prospect sees. It has one job: get a reply. Not a call, not a click, a reply.

## The rules (from 300 LinkedIn threads that became booked calls)
These come from Prity Kar's analysis of 300 booked-call conversations (6,497 messages). They are not theory.
1. **Open about them.** Start with "Hey <first name>," then something you noticed: a signal, a post, a role, a hire. 89% of booked openers started with "Hey" plus a first name. 32% opened with something noticed.
2. **Keep it short.** The median booked opener was 43 words. A quarter were under 24 words. Aim for 25 to 60. Only go long (80 to 100) for an "idea teaser" where every line is about their business.
3. **End on a question.** 55% of booked openers ended on a question. Make it easy to answer in under 10 words. The median first reply was 9 words.
4. **No call ask in message 1.** 70% of booked openers asked for nothing but a reply. No "15 minutes", no "quick call", no "demo".
5. **Never send a calendar link before they reply.** 0 of 300 booked threads did. No links at all in message 1.
6. **More "you" than "I/we".** 57% of booked openers used you/your more than I/we/our.
7. **One idea per message.** One signal, one question.

## Inputs
- Prospect: first name, title, company, and at least one signal or hook. Best input is the output of account-research.
- `icp.md` (for pains and proof) and `voice.md` (for tone) if they exist in the current folder.
- Optional: the campaign style the user wants (see variants).
If there is no hook, ask for one or suggest running account-research. Do not write a generic opener.

## The 3 variants (write all 3)
- **A. Noticed + question** (25 to 45 words): the signal, one line of why it matters, one easy question.
- **B. Idea teaser** (50 to 95 words): the signal, then a short concrete idea for their business (what you would do, with one number if you have proof), then "worth sharing more?" style question. Still no call ask.
- **C. Give first** (25 to 50 words): offer something useful with no strings, such as a list, a teardown, a benchmark. Ask if they want it. Do not attach or link it yet.
Other styles you can swap in when they fit the ICP better: "market research ask" ("trying to understand how finance teams here handle X. Is that you or someone else?"), "client intro" ("if I could connect you with 2 or 3 X looking for Y, would that be useful?").

## Steps
1. Read the hook, icp.md and voice.md.
2. Pick the single best hook. Freshest and most personal wins.
3. Write A, B, C. Use their words where you can (from their post or job ad).
4. Run the self-check. If `scripts/check_opener.py` is available, run it:
   `python3 "${CLAUDE_SKILL_DIR}/scripts/check_opener.py" --file openers.txt`
   (Put the 3 openers in openers.txt separated by a line with `---`.) If the script cannot run, do the check by hand.
5. Fix anything that fails and show the final table.
6. Recommend one variant and say why in one line.

## Output format

```
### Prospect: <first name>, <title> at <company>
Hook used: <hook + date>

**A. Noticed + question** (38 words)
Hey Sam, ...?

**B. Idea teaser** (84 words)
Hey Sam, ...?

**C. Give first** (31 words)
Hey Sam, ...?

| Check | A | B | C |
|-------|---|---|---|
| Words (aim ~43) | 38 | 84 | 31 |
| Starts "Hey <name>" | yes | yes | yes |
| About them (you > I) | yes | yes | yes |
| Ends on a question | yes | yes | yes |
| No call ask | yes | yes | yes |
| No link or calendar | yes | yes | yes |
| Specific, dated detail | yes | yes | yes |
| No hype words, no em dash | yes | yes | yes |

Pick: A, because <reason>.
```

For a list (CSV), add columns `opener_a`, `opener_b`, `opener_c`, `recommended` and keep the same rules. Do 10 rows first and ask the user to approve the style before doing the rest.

## Words to avoid
unlock, game-changer, revolutionize, leverage, seamless, cutting-edge, supercharge, delve, synergy, "I hope this finds you well", "quick question", "touch base", "pick your brain". No em dashes.

## Example
Hook: VP Engineering, started in August, 9 open backend roles posted in the last 3 weeks.

A. Noticed + question (36 words)
> Hey Sam, saw you stepped into the VP Engineering role in August and the team has 9 backend roles open right now. Are you planning to hire all of those in-house, or is that still open?

C. Give first (30 words)
> Hey Sam, noticed the 9 backend roles on your careers page. I have October pay and time-to-hire numbers for US mid-market teams on your stack. Want them for your planning?

## Next step to suggest
"Send one variant today. If there's no reply, run follow-up-writer for day 3, 7 and 14."
