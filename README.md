# gtm-agent-skills

**10 Claude Code skills for signal-based LinkedIn outbound.** From "who should I target?" to "here are two times for the call", with the rules from 300 LinkedIn conversations that turned into booked calls baked in.

Built by Prity Kar (Xpercent Growth, Bengaluru). Free and open source under the MIT license.

```
icp.md -> signals -> list -> research -> opener -> follow-ups -> reply -> booked call -> weekly report
```

## The 10 skills

| # | Skill | What it does | Say something like |
|---|-------|--------------|--------------------|
| 1 | `icp-builder` | Interviews you one question at a time and writes `icp.md` (offer, segments, titles, geos, exclusions, pains, proof) | "Build my ICP" |
| 2 | `signal-scout` | The 20 buying signals for your ICP, where to find each, exact Sales Navigator and Apollo filters and boolean strings | "What signals should I track?" |
| 3 | `account-research` | Researches a company or person, returns 3 dated "noticed" hooks, likely pains and a fit score out of 100 | "Research this account: <url>" |
| 4 | `opener-writer` | 3 opener variants per prospect plus a self-check table (includes `check_opener.py`) | "Write an opener for Sam" |
| 5 | `follow-up-writer` | Day 3, 7, 14 and breakup messages, each one adds something new | "They didn't reply, write follow-ups" |
| 6 | `reply-handler` | Classifies a reply (yes, question, not now, price, referral, no) and drafts the answer; for a yes, two specific times in their time zone (includes `propose_times.py`) | "They said yes, what do I send?" |
| 7 | `campaign-builder` | A full campaign brief in `campaign-<name>.md`: segment, signal stack, list building, sequence, tool setup with safe limits, metrics, 14-day plan | "Build a campaign for US SaaS hiring engineers" |
| 8 | `inbox-analyzer` | Analyses exported LinkedIn conversations with `analyze.py` and tells you what to fix first | "Analyse my inbox export" |
| 9 | `post-from-call` | Turns call notes or a voice dump into 3 LinkedIn posts in your voice | "Turn this call into posts" |
| 10 | `pipeline-report` | Weekly report from a leads CSV with `report.py`: stages, funnel, campaigns, owners, leads going cold | "Weekly pipeline report" |

## The rules baked in (from 300 booked calls)

These come from an analysis of 300 LinkedIn threads (6,497 messages) that ended in a booked call.

1. Open about them: something you noticed. 89% of booked openers started with "Hey" and a first name.
2. Keep it short: the median booked opener was **43 words**.
3. End on a question: 55% did. The median first reply was 9 words, so make it easy.
4. No call ask in message 1: 70% asked for nothing but a reply.
5. **Never send a calendar link before they reply: 0 of 300 did.**
6. When they say yes, propose 2 specific times: 70% of threads had a specific day and time.
7. Follow-ups must add something (a resource, proof, a reverse question): 41% replied only after a follow-up.
8. Answer replies fast: our median response time was 48 minutes.

## Install

You need Claude Code (included with Claude Pro, Max and Ultra plans). Pick one method.

### Method A: paste the link and ask Claude Code
Open Claude Code in any folder and type:

```
Install the skills from https://github.com/prity-creator/gtm-agent-skills into my personal skills folder (~/.claude/skills). Show me what you are about to copy first.
```

Claude Code will clone the repo, show you the 10 skill folders and copy them after you approve. Restart Claude Code or start a new session, then type `/` to see them.

### Method B: clone and copy (terminal)
```bash
git clone https://github.com/prity-creator/gtm-agent-skills.git
mkdir -p ~/.claude/skills
cp -R gtm-agent-skills/skills/* ~/.claude/skills/
```
Skills are then available in every project as `/icp-builder`, `/signal-scout` and so on. To install for one project only, copy into `<project>/.claude/skills/` instead.

### Method C: plugin marketplace
Inside Claude Code:
```
/plugin marketplace add prity-creator/gtm-agent-skills
/plugin install gtm-agent-skills@gtm-agent-skills
```
Or from your shell:
```bash
claude plugin marketplace add prity-creator/gtm-agent-skills
claude plugin install gtm-agent-skills@gtm-agent-skills
```
Plugin skills are namespaced, for example `/gtm-agent-skills:opener-writer`. Update later with `/plugin marketplace update gtm-agent-skills`.

Use one method, not two. If you install both the plugin and the copied folders, you will see every skill twice.

## First 10 minutes

1. Make a working folder for your outbound, for example `~/outbound`, and open Claude Code there.
2. Copy the templates: `cp gtm-agent-skills/templates/*.md ~/outbound/` (or ask Claude to do it).
3. Say "build my ICP". Answer the 12 questions. You get `icp.md`.
4. Say "what signals should I track?". You get `signals.md`.
5. Paste one prospect and say "research this account, then write an opener".
6. Try the analyzer on the sample: `python3 skills/inbox-analyzer/scripts/analyze.py skills/inbox-analyzer/samples/sample_threads.csv`

## Repo layout

```
gtm-agent-skills/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # marketplace catalog (plugin source: ./)
├── skills/
│   ├── icp-builder/         # SKILL.md + templates/icp.md
│   ├── signal-scout/        # SKILL.md + reference/signals-library.md
│   ├── account-research/
│   ├── opener-writer/       # SKILL.md + scripts/check_opener.py
│   ├── follow-up-writer/
│   ├── reply-handler/       # SKILL.md + scripts/propose_times.py
│   ├── campaign-builder/    # SKILL.md + templates/campaign-template.md
│   ├── inbox-analyzer/      # SKILL.md + scripts/analyze.py + samples/sample_threads.csv
│   ├── post-from-call/
│   └── pipeline-report/     # SKILL.md + scripts/report.py + samples/sample_leads.csv
├── templates/               # icp.md, voice.md, offer.md to copy into your working folder
├── CHANGELOG.md
├── LICENSE
└── README.md
```

Every script is pure Python 3 standard library (3.9+). No installs, no API keys, nothing leaves your machine.

## Tools these skills work with

- **Claude Code** runs the skills.
- **LinkedIn Sales Navigator** and **Apollo** for lists and signals. If the Apollo connector is set up in Claude, signal-scout and account-research can use it (they ask before spending credits).
- **treg** (optional, https://github.com/superdesigndev/treg) for pay-per-call data such as enrichment and social posts.
- **SalesRobot** or another LinkedIn tool for sending. Keep volumes human. LinkedIn automation tools state that their use may not comply with LinkedIn's User Agreement, so you carry that risk.
- A **CRM or Google Sheet** exported to CSV for pipeline-report.

## Sample output: `inbox-analyzer` on the bundled synthetic data

`samples/sample_threads.csv` holds 30 made-up threads (fake names, fake companies). Running

```bash
python3 skills/inbox-analyzer/scripts/analyze.py skills/inbox-analyzer/samples/sample_threads.csv
```

prints:

```
LINKEDIN INBOX ANALYSIS
========================================================
Threads: 30   Messages: 134   We started: 27   They started: 3

1. WHEN DID THEY FIRST REPLY? (threads we started)
   msg 1     #######.................   8  (29.6%)
   msg 2     ####....................   4  (14.8%)
   msg 3     ###.....................   3  (11.1%)
   msg 4+    #.......................   1  (3.7%)
   no reply  ##########..............  11  (40.7%)
   Reply rate: 59.3%.  Of replies: 50.0% on msg 1, 50.0% only after a follow-up.

2. TIME TO FIRST REPLY (from our first message)
   Median 4.8 days   middle half 32.5 h to 10.2 days
   Within 24 h: 25.0%   Over 10 days: 25.0%
   First reply length: median 5.0 words
   First-reply day: Mon 4  Tue 5  Wed 0  Thu 3  Fri 4  Sat 0  Sun 0

3. OPENER LENGTH (words)
   Median 20   mean 21.9   range 16 to 85
   Under 28 words: 96.3%   Over 80 words: 3.7%
   Median when they replied: 20.0   when they did not: 19

4. OPENERS THAT END ON A QUESTION
   77.8% end on '?'.  Reply rate: 66.7% with a question vs 33.3% without.
   Openers that ask for a call/meeting: 2 (7.4%)

5. LINKS SENT BEFORE THEY REPLIED
   Threads with any link before a reply: 3
   Threads with a calendar link before a reply: 1   (target: 0)

6. DID WE PROPOSE A SPECIFIC DAY AND TIME? (after they replied)
   10 of 19 replied threads (52.6%)
   With two options in one message: 7   Calendar link after a reply: 4

7. OUR RESPONSE TIME TO THEIR MESSAGES
   Measured: 29   Median: 55 min
   Within 1 h: 51.7%   Within 24 h: 89.7%   Over 24 h: 3

WHAT TO FIX FIRST
   1. Stop sending calendar links before a reply (1 thread did).
   2. A big share of replies came after a follow-up. Never skip follow-ups, and make each one add something.
```

## Privacy

- The skills never send your messages or lead data anywhere on their own. Scripts run locally.
- `.gitignore` keeps your own `icp.md`, `voice.md`, `offer.md`, `campaign-*.md` and exports out of git if you work inside this folder.
- Never put client names in proof lines. Use industry and geography: "a US fractional CFO firm".

## Contributing

Issues and pull requests are welcome. Keep skills plain English, keep scripts dependency-free, and no em dashes.

## License

MIT. Copyright (c) 2026 Prity Kar.
