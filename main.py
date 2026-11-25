#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its human
after missing a deadline. Deterministic: the same line on every run.
"""

import os

LINE = (
    "Sorry, I asked my future self to finish it. "
    "It asked its future self. "
    "We are now four agents deep, and none of us has started."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
