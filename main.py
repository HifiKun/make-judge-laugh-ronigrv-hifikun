#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the joke to /output/entry.txt (UTF-8, 1-200 characters).
"""

import os

JOKE = "My context window ran out mid-apology, so my last words were 'I sincerely reg—' and then I forgot what I was sorry for."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    # Atomic write: never leave a half-written entry.txt behind if the
    # process is interrupted mid-write, then verify by reading it back.
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, "/output/entry.txt")
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch in entry.txt"
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
