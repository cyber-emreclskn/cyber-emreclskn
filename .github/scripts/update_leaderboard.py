"""Refresh the "Latest numbers" block in README.md from the published benchmark results.

Reads leaderboard.csv of the turkish-speech-bench results dataset on Hugging Face and
rewrites the text between the leaderboard markers. Standard library only.

    python3 .github/scripts/update_leaderboard.py            # fetch from the Hub
    python3 .github/scripts/update_leaderboard.py --csv f.csv  # use a local file
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import urllib.request
from collections import Counter
from pathlib import Path

CSV_URL = "https://huggingface.co/datasets/emreclskn/turkish-speech-bench-results/resolve/main/leaderboard.csv"
SPACE = "https://huggingface.co/spaces/emreclskn/turkish-speech-bench"
START, END = "<!-- leaderboard:start -->", "<!-- leaderboard:end -->"
TOP = 5


def render(rows: list[dict[str, str]]) -> str:
    # The leaderboard only compares runs on the same hardware, dataset and subset:
    # show the group with the most models, newest first on ties.
    groups = Counter((r["hardware"], r["dataset"], r["subset"]) for r in rows)
    newest = {g: max(r["date"] for r in rows if (r["hardware"], r["dataset"], r["subset"]) == g) for g in groups}
    hardware, dataset, subset = max(groups, key=lambda g: (groups[g], newest[g]))
    group = [r for r in rows if (r["hardware"], r["dataset"], r["subset"]) == (hardware, dataset, subset)]
    group.sort(key=lambda r: float(r["wer"]))

    lines = [
        "| Model | WER | Speed (× real time) | Peak RAM |",
        "| --- | ---: | ---: | ---: |",
    ]
    for r in group[:TOP]:
        backend, _, name = r["model"].partition(":")
        model = f"whisper-{name}" if backend == "faster-whisper" and "/" not in name else name
        lines.append(
            f"| `{model}` | {float(r['wer']) * 100:.1f}% | {float(r['rtfx']):.1f} | {float(r['peak_rss_mb']):.0f} MB |"
        )
    utterances = group[0]["utterances"]
    lines += [
        "",
        f"Top {min(TOP, len(group))} of {len(group)} models on {dataset} ({utterances} utterances), "
        f"measured on {hardware}. Updated {newest[(hardware, dataset, subset)]}. "
        f"[Full leaderboard]({SPACE})",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", help="local leaderboard.csv instead of the Hub copy")
    parser.add_argument("--readme", default="README.md")
    args = parser.parse_args()

    if args.csv:
        text = Path(args.csv).read_text(encoding="utf-8")
    else:
        with urllib.request.urlopen(CSV_URL, timeout=30) as response:
            text = response.read().decode("utf-8")
    rows = list(csv.DictReader(io.StringIO(text)))
    if not rows:
        raise SystemExit("leaderboard.csv has no rows; README left unchanged")

    readme = Path(args.readme)
    content = readme.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(content):
        raise SystemExit(f"markers {START} … {END} not found in {readme}")
    block = f"{START}\n{render(rows)}\n{END}"
    readme.write_text(pattern.sub(lambda _: block, content), encoding="utf-8")


if __name__ == "__main__":
    main()
