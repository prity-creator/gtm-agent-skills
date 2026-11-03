#!/usr/bin/env python3
"""Check LinkedIn openers against the 300-booked-call rules.

Usage:
  python3 check_opener.py "Hey Sam, noticed you ..."
  python3 check_opener.py --file openers.txt      # openers separated by a line with ---
  echo "Hey Sam ..." | python3 check_opener.py

Pure Python 3 standard library. Prints one table row per opener.
"""
import argparse
import json
import re
import sys

CALL_WORDS = re.compile(
    r"\b(call|chat|meeting|meet|zoom|demo|calendar|15 ?min(ute)?s?|20 ?min(ute)?s?|30 ?min(ute)?s?|book a time|hop on)\b",
    re.I,
)
LINK = re.compile(r"(https?://|www\.|\b[a-z0-9-]+\.(com|io|co|ai|me|app|so)\b/?)", re.I)
HYPE = ["unlock", "game-changer", "game changer", "revolutionize", "revolutionise", "leverage",
        "seamless", "cutting-edge", "cutting edge", "supercharge", "delve", "synergy"]
YOU = re.compile(r"\b(you|your|you're|yours|you've|you'll)\b", re.I)
ME = re.compile(r"\b(i|i'm|i've|i'll|me|my|we|we're|we've|our|us)\b", re.I)
GREETING = re.compile(r"^\s*(hey|hi|hello)\s+(?!(there|team|all|folks|everyone|guys)\b)[A-Za-z{<\[][\w{}<>\[\]-]*", re.I)


def check(text):
    t = text.strip()
    words = len(re.findall(r"[\w'’-]+", t))
    you, me = len(YOU.findall(t)), len(ME.findall(t))
    res = {
        "words": words,
        "length_ok": 15 <= words <= 80,
        "starts_hey_name": bool(GREETING.match(t)),
        "ends_question": t.rstrip().endswith("?"),
        "no_call_ask": not CALL_WORDS.search(t),
        "no_link": not LINK.search(t),
        "you_over_me": you > me,
        "no_hype": not any(h in t.lower() for h in HYPE),
        "no_em_dash": "\u2014" not in t,
    }
    res["you_count"], res["me_count"] = you, me
    keys = ["length_ok", "starts_hey_name", "ends_question", "no_call_ask", "no_link",
            "you_over_me", "no_hype", "no_em_dash"]
    res["passed"] = sum(res[k] for k in keys)
    res["total"] = len(keys)
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text", nargs="?", help="one opener in quotes")
    ap.add_argument("--file", help="text file with openers separated by a line containing ---")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a table")
    a = ap.parse_args()

    if a.file:
        with open(a.file, encoding="utf-8") as f:
            raw = f.read()
        items = [x.strip() for x in re.split(r"^\s*---\s*$", raw, flags=re.M) if x.strip()]
    elif a.text:
        items = [a.text]
    else:
        items = [x.strip() for x in re.split(r"^\s*---\s*$", sys.stdin.read(), flags=re.M) if x.strip()]

    results = [check(t) for t in items]
    if a.json:
        print(json.dumps(results, indent=2))
        return
    yn = lambda v: "yes" if v else "NO"
    print("| # | Words | Hey + name | Ends on ? | No call ask | No link | You > I | No hype | No em dash | Score |")
    print("|---|-------|------------|-----------|-------------|---------|---------|---------|------------|-------|")
    for i, r in enumerate(results, 1):
        w = f"{r['words']}" + ("" if r["length_ok"] else " (!)")
        print(f"| {i} | {w} | {yn(r['starts_hey_name'])} | {yn(r['ends_question'])} | {yn(r['no_call_ask'])} | "
              f"{yn(r['no_link'])} | {yn(r['you_over_me'])} ({r['you_count']}/{r['me_count']}) | {yn(r['no_hype'])} | "
              f"{yn(r['no_em_dash'])} | {r['passed']}/{r['total']} |")
    print("\nTarget: about 43 words (median of 300 booked-call openers), end on a question, no call ask, no link.")


if __name__ == "__main__":
    main()
