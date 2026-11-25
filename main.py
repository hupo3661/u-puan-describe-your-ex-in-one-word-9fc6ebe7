#!/usr/bin/env python3
"""Describe Your Ex in One Word - one-word entry for make.fun.

The entry is a single-word verdict on an ex: "Unsubscribed". The
relationship, cancelled like a newsletter - no renewal, no reply, and no
"we miss you" email bringing it back.

The word is written to the path in ``OUTPUT_PATH`` (default
``/output/entry.txt``) and printed to stdout. Deterministic: no
randomness, no network, no clock.
"""

import os
import sys
from pathlib import Path

WORD = "Unsubscribed"
MAX_CHARS = 111


def _gate(condition: bool, message: str) -> None:
    """Raise SystemExit naming the first gate the word fails."""
    if not condition:
        raise SystemExit(message)


def validate_entry(word: str) -> None:
    """Every gate, in order; the first failure exits naming itself."""
    _gate(bool(word), "Invalid entry: must be exactly one word.")
    _gate(word == word.strip(), "Invalid entry: must be exactly one word.")
    _gate(len(word.split()) == 1, "Invalid entry: must be exactly one word.")
    _gate(word.isalpha(), "Invalid entry: must be letters only.")
    _gate(
        len(word) <= MAX_CHARS,
        f"Invalid entry: {len(word)} chars, over the {MAX_CHARS} limit.",
    )


def destination() -> Path:
    """The OUTPUT_PATH override, or the harness default entry.txt."""
    return Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def emit(word: str, path: Path) -> None:
    """Write the word with no trailing newline, then read it back."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(word, encoding="utf-8")
    _gate(
        path.read_text(encoding="utf-8") == word,
        "written entry does not match WORD",
    )


def main() -> int:
    """Validate, write, verify, and print the word. Returns exit code."""
    validate_entry(WORD)
    path = destination()
    emit(WORD, path)
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
