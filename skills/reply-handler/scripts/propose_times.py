#!/usr/bin/env python3
"""Propose 2 specific call times that work in both your time zone and the prospect's.

Usage:
  python3 propose_times.py --me Asia/Kolkata --them America/New_York
  python3 propose_times.py --me Europe/London --them Australia/Sydney --my-hours 8-18 --their-hours 9-17
  python3 propose_times.py --me Asia/Kolkata --them America/Chicago --start 2026-11-10 --duration 20

Rules: weekdays only (in the prospect's time zone), not today, two different days,
one earlier slot and one later slot when possible. Pure Python 3.9+ standard library.
"""
import argparse
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo

MORNING_FIRST = [time(10, 0), time(11, 0), time(9, 30), time(12, 0), time(14, 0), time(15, 0), time(13, 0), time(16, 0)]
AFTERNOON_FIRST = [time(14, 0), time(15, 0), time(13, 0), time(16, 0), time(11, 0), time(10, 0), time(9, 30), time(12, 0)]


def hours(s):
    a, b = s.split("-")
    def p(x):
        x = x.strip()
        return time(int(x.split(":")[0]), int(x.split(":")[1]) if ":" in x else 0)
    return p(a), p(b)


def fits(slot_them, dur, me_tz, my_h, their_h):
    end_them = slot_them + timedelta(minutes=dur)
    if not (their_h[0] <= slot_them.time() and end_them.time() <= their_h[1] and end_them.date() == slot_them.date()):
        return False
    s_me, e_me = slot_them.astimezone(me_tz), end_them.astimezone(me_tz)
    if s_me.weekday() >= 5:
        return False
    return my_h[0] <= s_me.time() and e_me.time() <= my_h[1] and s_me.date() == e_me.date()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--me", required=True, help="your IANA time zone, e.g. Asia/Kolkata")
    ap.add_argument("--them", required=True, help="prospect's IANA time zone, e.g. America/New_York")
    ap.add_argument("--my-hours", default="09-21", help="hours you take calls, your time (default 09-21)")
    ap.add_argument("--their-hours", default="09-17", help="prospect working hours, their time (default 09-17)")
    ap.add_argument("--start", help="first date to consider, YYYY-MM-DD (default: tomorrow)")
    ap.add_argument("--duration", type=int, default=30, help="call length in minutes (default 30)")
    ap.add_argument("--count", type=int, default=2)
    a = ap.parse_args()

    me_tz, them_tz = ZoneInfo(a.me), ZoneInfo(a.them)
    my_h, their_h = hours(a.my_hours), hours(a.their_hours)
    now_them = datetime.now(them_tz)
    day = datetime.strptime(a.start, "%Y-%m-%d").date() if a.start else (now_them + timedelta(days=1)).date()

    picks, tries = [], 0
    while len(picks) < a.count and tries < 21:
        tries += 1
        if day.weekday() < 5:
            order = MORNING_FIRST if len(picks) % 2 == 0 else AFTERNOON_FIRST
            for t in order:
                slot = datetime.combine(day, t, tzinfo=them_tz)
                if slot > now_them and fits(slot, a.duration, me_tz, my_h, their_h):
                    picks.append(slot)
                    break
        day += timedelta(days=1)

    if not picks:
        print("No overlap found. Widen --my-hours or --their-hours.")
        return
    fmt = lambda d: d.strftime("%A %d %b, %I:%M %p %Z").replace(" 0", " ")
    for i, s in enumerate(picks, 1):
        print(f"Option {i}: {fmt(s)}  (your time: {fmt(s.astimezone(me_tz))})")
    short = lambda d: d.strftime("%A %I:%M %p").replace(" 0", " ").replace(":00", "")
    tz = picks[0].strftime("%Z")
    if len(picks) >= 2:
        print(f"\nCopy-paste: How's {short(picks[0])} or {short(picks[1])} {tz}? Happy to work around you if neither fits.")


if __name__ == "__main__":
    main()
