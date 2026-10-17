#!/usr/bin/env python3
"""Render a black-and-green GitHub contribution graph (Jan 1 to Dec 31) as an SVG.

Usage:
  GITHUB_TOKEN=... GH_USER=saksham999-SAK python generate_contributions.py
Optional env: YEAR (default: current year), OUT (default: contributions.svg)
Local test without network: python generate_contributions.py --json days.json
  where days.json is a list of {"date": "YYYY-MM-DD", "count": N}.
"""
import json
import os
import sys
import urllib.request
from datetime import date, timedelta

CELL, GAP = 12, 3
STEP = CELL + GAP
LEFT, TOP = 42, 44
BG = "#000000"
EMPTY = "#141414"
GREENS = ["#0e4429", "#006d32", "#26a641", "#39d353"]
TEXT = "#8b949e"

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_days(user, year, token):
    body = json.dumps({
        "query": QUERY,
        "variables": {
            "login": user,
            "from": f"{year}-01-01T00:00:00Z",
            "to": f"{year}-12-31T23:59:59Z",
        },
    }).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if "errors" in payload or not payload.get("data", {}).get("user"):
        raise SystemExit(f"GitHub API error: {payload}")
    weeks = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [
        {"date": d["date"], "count": d["contributionCount"]}
        for w in weeks for d in w["contributionDays"]
    ]


def level(count, peak):
    if count <= 0 or peak <= 0:
        return 0
    ratio = count / peak
    if ratio <= 0.25:
        return 1
    if ratio <= 0.5:
        return 2
    if ratio <= 0.75:
        return 3
    return 4


def render(days, year):
    counts = {date.fromisoformat(d["date"]): d["count"] for d in days}
    jan1, dec31 = date(year, 1, 1), date(year, 12, 31)
    counts = {k: v for k, v in counts.items() if jan1 <= k <= dec31}
    total = sum(counts.values())
    peak = max(counts.values(), default=0)

    # Columns are weeks starting on Sunday; first column holds Jan 1.
    start = jan1 - timedelta(days=(jan1.weekday() + 1) % 7)
    weeks = ((dec31 - start).days // 7) + 1
    width = LEFT + weeks * STEP + 20
    height = TOP + 7 * STEP + 44

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{total} contributions in {year}">',
        f'<rect width="{width}" height="{height}" rx="10" fill="{BG}"/>',
        f'<g font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif" font-size="11" fill="{TEXT}">',
        f'<text x="{LEFT}" y="22" font-size="13" fill="#e6edf3">'
        f'{total} contributions in {year}</text>',
    ]

    for label, row in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
        out.append(f'<text x="8" y="{TOP + row * STEP + 10}">{label}</text>')

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for m in range(1, 13):
        first = date(year, m, 1)
        col = (first - start).days // 7
        out.append(f'<text x="{LEFT + col * STEP}" y="{TOP - 8}">{months[m - 1]}</text>')
    out.append("</g>")

    for col in range(weeks):
        for row in range(7):
            day = start + timedelta(days=col * 7 + row)
            if not (jan1 <= day <= dec31):
                continue
            n = counts.get(day, 0)
            lv = level(n, peak)
            fill = EMPTY if lv == 0 else GREENS[lv - 1]
            x, y = LEFT + col * STEP, TOP + row * STEP
            word = "contribution" if n == 1 else "contributions"
            out.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}">'
                f'<title>{n} {word} on {day.isoformat()}</title></rect>'
            )

    # Legend
    ly = TOP + 7 * STEP + 14
    lx = width - 20 - (5 * STEP) - 70
    out.append(f'<text x="{lx - 34}" y="{ly + 10}" font-size="11" fill="{TEXT}" '
               f'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">Less</text>')
    for i, c in enumerate([EMPTY] + GREENS):
        out.append(f'<rect x="{lx + i * STEP}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{c}"/>')
    out.append(f'<text x="{lx + 5 * STEP + 4}" y="{ly + 10}" font-size="11" fill="{TEXT}" '
               f'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">More</text>')
    out.append("</svg>")
    return "\n".join(out)


def main():
    year = int(os.environ.get("YEAR", date.today().year))
    out_path = os.environ.get("OUT", "contributions.svg")
    if len(sys.argv) > 2 and sys.argv[1] == "--json":
        with open(sys.argv[2]) as fh:
            days = json.load(fh)
    else:
        user = os.environ["GH_USER"]
        token = os.environ["GITHUB_TOKEN"]
        days = fetch_days(user, year, token)
    svg = render(days, year)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
