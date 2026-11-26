#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — one-line entry.

Writes the forecast to /output/entry.txt and prints it.
"""

import os

LINE = "In Quibbleton, expect dense fog made entirely of unanswered emails, clearing by lunch into light sarcasm."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
