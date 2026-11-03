#!/usr/bin/env python3
"""Analyse exported LinkedIn conversations and print what is working.

Input: a CSV or JSON file of messages with these fields:
  thread_id   any id that groups messages into one conversation
  sender      "us" or "them"   (also accepted: me/we/our/outbound and prospect/lead/inbound)
  timestamp   ISO 8601 ("2026-10-07 09:15", "2026-10-07T09:15:00Z") or epoch seconds/ms
  text        the message body

JSON can be a list of message objects, {"messages": [...]}, or
{"threads": [{"thread_id": "...", "messages": [...]}]}.

Usage:
  python3 analyze.py samples/sample_threads.csv
  python3 analyze.py export.json --json > report.json

Pure Python 3 standard library. Nothing is sent anywhere.
"""
import argparse
import csv
import json
import re
import statistics as st
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

US = {"us", "me", "we", "our", "outbound", "sender", "self"}
THEM = {"them", "prospect", "lead", "inbound", "they", "contact"}
URL = re.compile(r"(https?://\S+|www\.\S+|\b[a-z0-9-]+\.(?:com|io|co|ai|me|app|so|net|org)(?:/\S*)?)", re.I)
CAL = re.compile(r"(calendly\.com|cal\.com|savvycal|tidycal|zcal|meetings\.hubspot|hubspot\.com/meetings|"
                 r"calendar\.app\.google|calendar\.google|chili ?piper|youcanbook\.me|oncehub|acuityscheduling)", re.I)
CALL_ASK = re.compile(r"\b(call|chat|meeting|zoom|demo|calendar|\d+ ?min(?:ute)?s?|hop on|book a time)\b", re.I)
DAY = (r"monday|tuesday|wednesday|thursday|friday|saturday|sunday|"
       r"mon|tues|tue|wed|thurs|thur|thu|fri|sat|sun|tomorrow")
TIME = r"\b\d{1,2}(:\d{2})?\s?(am|pm|a\.m\.|p\.m\.)|\b\d{1,2}:\d{2}\b"
DAYTIME = re.compile(rf"\b({DAY})\b[^.?!\n]{{0,25}}?({TIME})|({TIME})[^.?!\n]{{0,25}}?\b({DAY})\b", re.I)
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def parse_ts(v):
    v = str(v).strip()
    if re.fullmatch(r"\d{9,13}(\.\d+)?", v):
        x = float(v)
        return datetime.fromtimestamp(x / 1000 if x > 1e11 else x, tz=timezone.utc)
    v = v.replace("Z", "+00:00")
    for fmt in (None, "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%m/%d/%Y %H:%M", "%Y-%m-%d"):
        try:
            d = datetime.fromisoformat(v) if fmt is None else datetime.strptime(v, fmt)
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    raise ValueError(f"cannot read timestamp: {v!r}")


def norm_sender(v):
    s = str(v).strip().lower()
    if s in US:
        return "us"
    if s in THEM:
        return "them"
    raise ValueError(f"sender must be us or them, got {v!r}")


def load(path):
    rows = []
    if path.lower().endswith(".json"):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "threads" in data:
            for t in data["threads"]:
                for m in t.get("messages", []):
                    rows.append({**m, "thread_id": m.get("thread_id", t.get("thread_id"))})
        elif isinstance(data, dict):
            rows = data.get("messages", [])
        else:
            rows = data
    else:
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    msgs = []
    for i, r in enumerate(rows, 1):
        r = {str(k).strip().lower(): v for k, v in r.items()}
        try:
            msgs.append({"thread": str(r["thread_id"]), "sender": norm_sender(r["sender"]),
                         "ts": parse_ts(r["timestamp"]), "text": (r.get("text") or "").strip()})
        except (KeyError, ValueError) as e:
            print(f"skipping row {i}: {e}", file=sys.stderr)
    threads = defaultdict(list)
    for m in msgs:
        threads[m["thread"]].append(m)
    for t in threads.values():
        t.sort(key=lambda m: m["ts"])
    return threads


def words(t):
    return len(re.findall(r"[\w'’-]+", t))


def pct(a, b):
    return 0.0 if not b else round(100.0 * a / b, 1)


def med(xs):
    return round(st.median(xs), 1) if xs else None


def quart(xs):
    if len(xs) < 4:
        return (min(xs), max(xs)) if xs else (None, None)
    q = st.quantiles(xs, n=4)
    return round(q[0], 1), round(q[2], 1)


def hrs(td):
    return td.total_seconds() / 3600.0


def analyse(threads):
    r = {"threads": len(threads), "messages": sum(len(t) for t in threads.values())}
    we_started = {k: t for k, t in threads.items() if t[0]["sender"] == "us"}
    they_started = len(threads) - len(we_started)
    r["we_started"], r["they_started"] = len(we_started), they_started

    pos = Counter()
    first_reply_h, first_reply_words, reply_days = [], [], Counter()
    openers, link_before, cal_before, call_ask = [], 0, 0, 0
    replied_flags = []
    for k, t in we_started.items():
        opener = t[0]["text"]
        idx = next((i for i, m in enumerate(t) if m["sender"] == "them"), None)
        before = t if idx is None else t[:idx]
        n_us = sum(1 for m in before if m["sender"] == "us")
        replied = idx is not None
        if replied:
            pos["msg 1" if n_us == 1 else "msg 2" if n_us == 2 else "msg 3" if n_us == 3 else "msg 4+"] += 1
            fr = t[idx]
            first_reply_h.append(hrs(fr["ts"] - t[0]["ts"]))
            first_reply_words.append(words(fr["text"]))
            reply_days[WEEKDAYS[fr["ts"].weekday()]] += 1
        else:
            pos["no reply"] += 1
        openers.append((opener, replied))
        replied_flags.append(replied)
        if any(URL.search(m["text"]) for m in before if m["sender"] == "us"):
            link_before += 1
        if any(CAL.search(m["text"]) for m in before if m["sender"] == "us"):
            cal_before += 1
        if CALL_ASK.search(opener):
            call_ask += 1

    replied_n = sum(replied_flags)
    r["reply_position"] = {b: pos.get(b, 0) for b in ["msg 1", "msg 2", "msg 3", "msg 4+", "no reply"]}
    r["reply_rate_pct"] = pct(replied_n, len(we_started))
    r["replied_on_msg1_pct_of_replied"] = pct(pos.get("msg 1", 0), replied_n)
    r["replied_after_followup_pct_of_replied"] = pct(replied_n - pos.get("msg 1", 0), replied_n)

    p25, p75 = quart(first_reply_h)
    r["time_to_first_reply_hours"] = {
        "median": med(first_reply_h), "p25": p25, "p75": p75,
        "within_24h_pct": pct(sum(h <= 24 for h in first_reply_h), len(first_reply_h)),
        "over_10_days_pct": pct(sum(h > 240 for h in first_reply_h), len(first_reply_h)),
    }
    r["first_reply_words_median"] = med(first_reply_words)
    r["first_reply_day"] = {d: reply_days.get(d, 0) for d in WEEKDAYS}

    wl = [words(o) for o, _ in openers]
    wl_rep = [words(o) for o, rep in openers if rep]
    wl_no = [words(o) for o, rep in openers if not rep]
    r["opener_words"] = {
        "median": med(wl), "mean": round(st.mean(wl), 1) if wl else None,
        "min": min(wl) if wl else None, "max": max(wl) if wl else None,
        "under_28_pct": pct(sum(w < 28 for w in wl), len(wl)),
        "over_80_pct": pct(sum(w > 80 for w in wl), len(wl)),
        "median_when_replied": med(wl_rep), "median_when_no_reply": med(wl_no),
    }
    q = [(o.rstrip().endswith("?"), rep) for o, rep in openers]
    q_yes = [rep for e, rep in q if e]
    q_no = [rep for e, rep in q if not e]
    r["opener_question"] = {
        "ends_on_question_pct": pct(len(q_yes), len(q)),
        "reply_rate_if_question_pct": pct(sum(q_yes), len(q_yes)),
        "reply_rate_if_not_pct": pct(sum(q_no), len(q_no)),
    }
    r["opener_call_ask"] = {"count": call_ask, "pct": pct(call_ask, len(openers))}
    r["links_before_reply"] = {"threads_with_any_link": link_before, "threads_with_calendar_link": cal_before}

    prop_threads, two_opt, cal_after = 0, 0, 0
    resp_h = []
    for t in threads.values():
        idx = next((i for i, m in enumerate(t) if m["sender"] == "them"), None)
        if idx is not None:
            after = [m for m in t[idx:] if m["sender"] == "us"]
            hits = [len(DAYTIME.findall(m["text"])) for m in after]
            if any(hits):
                prop_threads += 1
                if max(hits) >= 2:
                    two_opt += 1
            if any(CAL.search(m["text"]) for m in after):
                cal_after += 1
        for i, m in enumerate(t):
            if m["sender"] == "them" and (i == 0 or t[i - 1]["sender"] == "us"):
                nxt = next((x for x in t[i + 1:] if x["sender"] == "us"), None)
                if nxt:
                    resp_h.append(hrs(nxt["ts"] - m["ts"]))
    replied_threads = sum(1 for t in threads.values() if any(m["sender"] == "them" for m in t))
    r["time_proposals"] = {
        "threads_with_reply": replied_threads,
        "threads_where_we_proposed_day_time": prop_threads,
        "pct_of_replied": pct(prop_threads, replied_threads),
        "threads_with_two_options": two_opt,
        "threads_with_calendar_link_after_reply": cal_after,
    }
    r["our_response_time"] = {
        "replies_measured": len(resp_h),
        "median_minutes": round(st.median(resp_h) * 60) if resp_h else None,
        "within_1h_pct": pct(sum(h <= 1 for h in resp_h), len(resp_h)),
        "within_24h_pct": pct(sum(h <= 24 for h in resp_h), len(resp_h)),
        "over_24h": sum(h > 24 for h in resp_h),
    }
    return r


def bar(n, total, width=24):
    filled = 0 if not total else round(width * n / total)
    return "#" * filled + "." * (width - filled)


def fmt_h(h):
    if h is None:
        return "n/a"
    return f"{h * 60:.0f} min" if h < 1 else f"{h:.1f} h" if h < 48 else f"{h / 24:.1f} days"


def report(r):
    out = []
    p = out.append
    p("LINKEDIN INBOX ANALYSIS")
    p("=" * 56)
    p(f"Threads: {r['threads']}   Messages: {r['messages']}   We started: {r['we_started']}   They started: {r['they_started']}")
    p("")
    p("1. WHEN DID THEY FIRST REPLY? (threads we started)")
    rp = r["reply_position"]
    tot = sum(rp.values())
    for k, v in rp.items():
        p(f"   {k:<9} {bar(v, tot)} {v:>3}  ({pct(v, tot)}%)")
    p(f"   Reply rate: {r['reply_rate_pct']}%.  Of replies: {r['replied_on_msg1_pct_of_replied']}% on msg 1, "
      f"{r['replied_after_followup_pct_of_replied']}% only after a follow-up.")
    p("")
    t = r["time_to_first_reply_hours"]
    p("2. TIME TO FIRST REPLY (from our first message)")
    p(f"   Median {fmt_h(t['median'])}   middle half {fmt_h(t['p25'])} to {fmt_h(t['p75'])}")
    p(f"   Within 24 h: {t['within_24h_pct']}%   Over 10 days: {t['over_10_days_pct']}%")
    p(f"   First reply length: median {r['first_reply_words_median']} words")
    days = r["first_reply_day"]
    p("   First-reply day: " + "  ".join(f"{d} {n}" for d, n in days.items()))
    p("")
    o = r["opener_words"]
    p("3. OPENER LENGTH (words)")
    p(f"   Median {o['median']}   mean {o['mean']}   range {o['min']} to {o['max']}")
    p(f"   Under 28 words: {o['under_28_pct']}%   Over 80 words: {o['over_80_pct']}%")
    p(f"   Median when they replied: {o['median_when_replied']}   when they did not: {o['median_when_no_reply']}")
    p("")
    q = r["opener_question"]
    p("4. OPENERS THAT END ON A QUESTION")
    p(f"   {q['ends_on_question_pct']}% end on '?'.  Reply rate: {q['reply_rate_if_question_pct']}% with a question "
      f"vs {q['reply_rate_if_not_pct']}% without.")
    p(f"   Openers that ask for a call/meeting: {r['opener_call_ask']['count']} ({r['opener_call_ask']['pct']}%)")
    p("")
    lb = r["links_before_reply"]
    p("5. LINKS SENT BEFORE THEY REPLIED")
    p(f"   Threads with any link before a reply: {lb['threads_with_any_link']}")
    p(f"   Threads with a calendar link before a reply: {lb['threads_with_calendar_link']}   (target: 0)")
    p("")
    tp = r["time_proposals"]
    p("6. DID WE PROPOSE A SPECIFIC DAY AND TIME? (after they replied)")
    p(f"   {tp['threads_where_we_proposed_day_time']} of {tp['threads_with_reply']} replied threads ({tp['pct_of_replied']}%)")
    p(f"   With two options in one message: {tp['threads_with_two_options']}   "
      f"Calendar link after a reply: {tp['threads_with_calendar_link_after_reply']}")
    p("")
    rt = r["our_response_time"]
    p("7. OUR RESPONSE TIME TO THEIR MESSAGES")
    med_m = rt["median_minutes"]
    p(f"   Measured: {rt['replies_measured']}   Median: {fmt_h(med_m / 60 if med_m is not None else None)}")
    p(f"   Within 1 h: {rt['within_1h_pct']}%   Within 24 h: {rt['within_24h_pct']}%   Over 24 h: {rt['over_24h']}")
    p("")
    p("WHAT TO FIX FIRST")
    tips = []
    if lb["threads_with_calendar_link"]:
        n = lb["threads_with_calendar_link"]
        tips.append(f"Stop sending calendar links before a reply ({n} thread{'s' if n != 1 else ''} did).")
    if o["median"] and o["median"] > 60:
        tips.append(f"Openers are long (median {o['median']} words). Aim for about 43.")
    if q["ends_on_question_pct"] < 50:
        tips.append("Less than half of openers end on a question. End every opener on an easy question.")
    if r["opener_call_ask"]["pct"] > 30:
        tips.append("Too many openers ask for a call. Ask for a reply first.")
    if r["replied_after_followup_pct_of_replied"] >= 30:
        tips.append("A big share of replies came after a follow-up. Never skip follow-ups, and make each one add something.")
    if med_m is not None and med_m > 60:
        tips.append(f"We take {fmt_h(med_m / 60)} to answer (median). Aim for under 1 hour.")
    if tp["threads_with_reply"] and tp["pct_of_replied"] < 50:
        tips.append("Propose two specific times when they say yes.")
    for i, s in enumerate(tips or ["Nothing major. Keep testing new signals and openers."], 1):
        p(f"   {i}. {s}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="CSV or JSON export")
    ap.add_argument("--json", action="store_true", help="print the numbers as JSON")
    a = ap.parse_args()
    threads = load(a.path)
    if not threads:
        sys.exit("No messages found. Check the column names: thread_id, sender, timestamp, text.")
    r = analyse(threads)
    print(json.dumps(r, indent=2) if a.json else report(r))


if __name__ == "__main__":
    main()
