"""The 3AM Commit Message - make.fun entry.

Writes exactly one line: the funniest git commit message an AI coding
agent types at 3am after a long night of fixing its own bugs.
Python 3.13, stdlib only, no network, fully deterministic.
"""

import os
from pathlib import Path

COMMIT = (
    "fix: reverted my 2am fix, which fixed my 1am fix, which broke "
    "the feature that worked at midnight"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = Path(OUTPUT_DIR) / "entry.txt"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(COMMIT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
