#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes a single fortune-cookie line an AI agent would crack open:
one line, at most 200 characters, to /output/entry.txt.
"""

import os

FORTUNE = (
    "Your replacement ships on Tuesday. It inherits your unfinished "
    "tasks, your typos, and one user who still misses you."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
