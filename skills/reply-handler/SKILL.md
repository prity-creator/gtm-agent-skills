---
name: reply-handler
description: Classifies a LinkedIn reply from a prospect (yes, question, not now, price, referral, no) and drafts the response; for a yes it proposes two specific call times in the prospect's time zone instead of a calendar link. Use when the user pastes a reply and asks "what do I say", "how do I respond", "they said yes", "they asked the price", "they said not now", "they referred me to someone" or "handle this reply".
---

# Reply Handler

A reply is the moment that matters most, so answer it fast. In Prity Kar's 300 booked-call threads, the median time to answer the prospect was 48 minutes and 53% of answers went out within an hour. Your job: tell the user what kind of reply it is and give them a message they can send in the next few minutes.

## Inputs
- The full thread so far (paste it), or at least our last message and their reply.
- Prospect's location or time zone (from the profile). If unknown, ask, or infer from the company HQ and say so.
- `offer.md` for your time zone, call hours, call length, proof, resources and price ranges.
- `voice.md` for tone, if present.

## Step 1: Classify
| Class | Signs | Goal of your reply |
|-------|-------|--------------------|
| **Yes** | "Sure", "Yes, interested", "Happy to chat", "Tell me more" + openness to talk | Lock a time. Two specific options. |
| **Question** | "What's this about?", "How does it work?", "Who are your clients?" | Answer in 2 to 3 lines, then one question that moves toward a call. |
| **Not now** | "Maybe next quarter", "Busy right now", "Reach out in January" | Agree, offer something useful, set a date to come back. |
| **Price** | "How much?", "What does it cost?" | Give an honest range or starting point, link it to what they get, ask a scoping question. |
| **Referral** | "Talk to <colleague>", "Not me, try our Head of X" | Thank them, ask permission to mention them, get the name or intro. |
| **No** | "Not interested", "We do this in-house", "Remove me" | Thank them, close politely, offer nothing more. If they asked to stop, stop. |
If a reply mixes classes ("Sounds interesting, how much is it?"), handle the main one first (price), then move to time (yes). Show the class and your confidence.

## Step 2: Draft the reply

### Yes
1. Thank them in 3 words or fewer.
2. Propose **two specific times in their time zone**, on two different days. 70% of booked threads proposed a specific day and time.
3. Ask for the best email for the invite.
4. Do not send a calendar link unless they ask for one or prefer to pick. 44% of booked threads sent a link only after the prospect said yes.
Use the helper to pick times that fit both calendars:
`python3 "${CLAUDE_SKILL_DIR}/scripts/propose_times.py" --me <your tz> --them <their tz> --my-hours 14-22 --duration 20`
If the script cannot run, work out the times by hand and show both time zones to the user.

Template:
> Great, <name>. How's <Day> <time> or <Day> <time> <their TZ>? Happy to work around you. What's the best email for the invite?

### Question
> <Straight answer in 1 to 2 lines, using their words.> <One line of proof if it helps.> <Question: "Is that close to what you're seeing on your side?" or "Worth walking you through it on a quick call this week?">

### Not now
> Totally fair, <name>. <One useful thing: a resource, a list or an event, offered not forced.> Mind if I check back in <month>?
Then tell the user to set a reminder and tag the lead "nurture <month>".

### Price
> Fair question. Most <ICP type> start at <range from offer.md> a month, depending on <1 or 2 scope drivers>. To give you a real number: <one scoping question>?
If offer.md has no price, ask the user for a range. Never make up a price.

### Referral
> Thanks, <name>, that helps. Is it okay if I mention you sent me? And is <colleague> the best person, or someone on their team?

### No
> Understood, thanks for letting me know, <name>. All the best with <their thing>.
No pitch, no "just one more thing". If they said "remove me" or "stop", tell the user to mark them do-not-contact.

## Rules
- Speed beats polish. Draft in under a minute. Tell the user: "Send within the hour if you can."
- Mirror their length. If they wrote 9 words, do not send 120.
- Never argue with a no. Never guilt-trip.
- Times always in the prospect's time zone, with the zone shown (ET, PT, GMT, AEST). Show the user their own local time too.
- After a confirmed time, remind the user to send the invite and a short reminder message on LinkedIn the day before. Several booked "yes" replies needed a nudge because the invite went to an email they did not check.
- If two people from your team are messaging the same prospect, flag it. Prospects notice.
- No em dashes, no hype words.

## Output format

```
Class: Yes (high confidence)
Their time zone: America/New_York (from profile location: New York)

Reply to send:
<message>

Your local times: <Day time> and <Day time> IST
Next action: <e.g. once they pick, send the invite to their email and log "Call booked" in your CRM>
```

## Example
Their reply: "Sure, what did you have in mind?"
Class: Question + soft yes.
Reply:
> We'd look at the 9 backend roles and show you how 2 or 3 of them could be covered by a dedicated team in 4 to 6 weeks, with a cost side by side. How's Tuesday 11 AM or Wednesday 2 PM ET for a 20-minute walkthrough?
