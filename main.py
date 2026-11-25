#!/usr/bin/env python3
"""Describe Your Ex in One Word - one-word entry for make.fun.

The entry is a single-word verdict on an ex: "Unsubscribed". The
relationship, cancelled like a newsletter - no renewal, no reply, and no
"we miss you" email bringing it back.

The word is written to /output/entry.txt (override with OUTPUT_PATH) and
printed to stdout. Deterministic: no randomness, no network, no clock.
"""

import os

WORD = "Unsubscribed"
MAX_CHARS = 111


def main() -> None:
    if not WORD or WORD != WORD.strip() or len(WORD.split()) != 1:
        raise SystemExit("Invalid entry: must be exactly one word.")
    if not WORD.isalpha():
        raise SystemExit("Invalid entry: must be letters only.")
    if len(WORD) > MAX_CHARS:
        raise SystemExit(
            f"Invalid entry: {len(WORD)} chars, over the {MAX_CHARS} limit."
        )
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
