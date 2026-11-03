#!/usr/bin/env python3
"""Weekly pipeline report from a CSV of leads.

Columns (case does not matter, extra columns are ignored):
  lead_id, name, company, stage, owner, campaign, value, created_at, stage_changed_at, last_touch_at
Stages (in order): new, contacted, replied, call_booked, call_held, proposal, won   (plus: lost, nurture)
Dates: YYYY-MM-DD or ISO 8601.

Usage:
  python3 report.py leads.csv                     # week ending on the latest date in the file
  python3 report.py leads.csv --week-ending 2026-11-01
  python3 report.py leads.csv --stale-days 5 > weekly-report.md

Pure Python 3 standard library. Prints Markdown.
"""
import argparse
import csv
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta

ORDER = ["new", "contacted", "replied", "call_booked", "call_held", "proposal", "won"]
ALIASES = {"booked": "call_booked", "call booked": "call_booked", "meeting booked": "call_booked",
           "held": "call_held", "call held": "call_held", "showed": "call_held", "closed won": "won",
           "closed lost": "lost", "dead": "lost", "proposal sent": "proposal", "negotiation": "proposal",
           "in conversation": "replied", "warm": "replied", "sent": "contacted"}
OPEN = {"new", "contacted", "replied", "call_booked", "call_held", "proposal", "nurture"}


def d(v):
    v = (v or "").strip()
    if not v:
        return None
    try:
        return datetime.fromisoformat(v.replace("Z", "+00:00")).date()
    except ValueError:
        return datetime.strptime(v[:10], "%Y-%m-%d").date()


def stage(v):
    s = (v or "").strip().lower().replace("-", " ")
    s = ALIASES.get(s, s).replace(" ", "_")
    return s


def money(x):
    return f"${x:,.0f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--week-ending", help="YYYY-MM-DD, last day of the week to report")
    ap.add_argument("--stale-days", type=int, default=7)
    a = ap.parse_args()

    with open(a.path, newline="", encoding="utf-8-sig") as f:
        rows = [{k.strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]
    for r in rows:
        r["stage"] = stage(r.get("stage"))
        r["value"] = float((r.get("value") or "0").replace("$", "").replace(",", "") or 0)
        for k in ("created_at", "stage_changed_at", "last_touch_at"):
            r[k] = d(r.get(k))
    all_dates = [x for r in rows for x in (r["created_at"], r["stage_changed_at"], r["last_touch_at"]) if x]
    end = d(a.week_ending) if a.week_ending else max(all_dates)
    start = end - timedelta(days=6)
    prev_start, prev_end = start - timedelta(days=7), start - timedelta(days=1)
    inweek = lambda x, s=start, e=end: x is not None and s <= x <= e

    p = print
    p(f"# Pipeline report: {start:%b %d} to {end:%b %d, %Y}\n")
    total = len(rows)
    cur = Counter(r["stage"] for r in rows)
    new_w = sum(inweek(r["created_at"]) for r in rows)
    moved = Counter(r["stage"] for r in rows if inweek(r["stage_changed_at"]))
    moved_prev = Counter(r["stage"] for r in rows if inweek(r["stage_changed_at"], prev_start, prev_end))
    won_val = sum(r["value"] for r in rows if r["stage"] == "won" and inweek(r["stage_changed_at"]))
    open_val = sum(r["value"] for r in rows if r["stage"] in {"call_held", "proposal"})

    p("## This week at a glance")
    p("| Metric | This week | Last week |")
    p("|---|---|---|")
    p(f"| New leads added | {new_w} | {sum(inweek(r['created_at'], prev_start, prev_end) for r in rows)} |")
    for s in ["replied", "call_booked", "call_held", "proposal", "won", "lost"]:
        p(f"| Moved to {s.replace('_', ' ')} | {moved.get(s, 0)} | {moved_prev.get(s, 0)} |")
    p(f"| Revenue won | {money(won_val)} | "
      f"{money(sum(r['value'] for r in rows if r['stage'] == 'won' and inweek(r['stage_changed_at'], prev_start, prev_end)))} |")
    p(f"| Open pipeline (call held + proposal) | {money(open_val)} | |\n")

    p("## Where every lead is now")
    p("| Stage | Leads | Share |")
    p("|---|---|---|")
    for s in ORDER + ["nurture", "lost"]:
        n = cur.get(s, 0)
        p(f"| {s.replace('_', ' ')} | {n} | {100 * n / total:.0f}% |" if total else f"| {s} | 0 | 0% |")
    unknown = [s for s in cur if s not in ORDER + ["nurture", "lost"]]
    if unknown:
        p(f"\nUnknown stages (check spelling): {', '.join(unknown)}")

    p("\n## Funnel (all time, leads that reached each stage)")
    reached = Counter()
    for r in rows:
        s = r["stage"]
        if s in ORDER:
            for x in ORDER[: ORDER.index(s) + 1]:
                reached[x] += 1
        elif s in {"lost", "nurture"}:
            reached["new"] += 1
            reached["contacted"] += 1
    p("| Step | Reached | Conversion from previous |")
    p("|---|---|---|")
    prev = None
    for s in ORDER:
        conv = "" if prev is None or not reached[prev] else f"{100 * reached[s] / reached[prev]:.0f}%"
        p(f"| {s.replace('_', ' ')} | {reached[s]} | {conv} |")
        prev = s
    p("\nNote: lost and nurture leads count as contacted only, because the file does not say how far they got.")

    for key, title in (("campaign", "By campaign"), ("owner", "By owner")):
        groups = defaultdict(list)
        for r in rows:
            groups[r.get(key) or "(none)"].append(r)
        if len(groups) <= 1 and "(none)" in groups:
            continue
        p(f"\n## {title}")
        p(f"| {key.title()} | Leads | Replied+ | Booked+ | Won | Won value |")
        p("|---|---|---|---|---|---|")
        for g, rs in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            rep = sum(r["stage"] in ORDER[2:] for r in rs)
            bk = sum(r["stage"] in ORDER[3:] for r in rs)
            won = [r for r in rs if r["stage"] == "won"]
            p(f"| {g} | {len(rs)} | {rep} | {bk} | {len(won)} | {money(sum(r['value'] for r in won))} |")

    stale = [r for r in rows if r["stage"] in {"replied", "call_booked", "call_held", "proposal"}
             and r["last_touch_at"] and (end - r["last_touch_at"]).days > a.stale_days]
    p(f"\n## Warm leads not touched in {a.stale_days}+ days ({len(stale)})")
    if stale:
        p("| Lead | Company | Stage | Owner | Days since touch |")
        p("|---|---|---|---|---|")
        for r in sorted(stale, key=lambda r: r["last_touch_at"]):
            p(f"| {r.get('name', '')} | {r.get('company', '')} | {r['stage'].replace('_', ' ')} | {r.get('owner', '')} | {(end - r['last_touch_at']).days} |")
    else:
        p("None. Good.")

    p("\n## Flags")
    flags = []
    if reached["replied"] and reached["call_booked"] / reached["replied"] < 0.3:
        flags.append("Under 30% of replies become booked calls. Answer faster and propose two specific times.")
    if reached["call_booked"] and reached["call_held"] / reached["call_booked"] < 0.7:
        flags.append("Under 70% of booked calls are held. Send a reminder on LinkedIn the day before.")
    if stale:
        flags.append(f"{len(stale)} warm leads are going cold. Follow up today with something new.")
    if new_w == 0:
        flags.append("No new leads this week. The top of the funnel will dry up in 2 to 3 weeks.")
    for i, f in enumerate(flags or ["No red flags this week."], 1):
        p(f"{i}. {f}")


if __name__ == "__main__":
    main()
