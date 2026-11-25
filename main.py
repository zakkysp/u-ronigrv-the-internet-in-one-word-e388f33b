#!/usr/bin/env python3
"""The Internet in One Word.

Writes a single word to /output/entry.txt: the whole internet, described
in one word. Standard library only, deterministic, no network, no input
read from outside this repository.
"""

import os

WORD = "later"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    # Read the file back and confirm it holds exactly one word: the
    # entry is worthless if the write ever lands extra bytes or lines.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != WORD + "\n" or len(written.split()) != 1:
        raise RuntimeError("entry.txt does not contain exactly one word")


if __name__ == "__main__":
    main()
