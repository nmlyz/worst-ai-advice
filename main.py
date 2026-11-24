#!/usr/bin/env python3
"""Write one line of deliberately terrible advice to /output/entry.txt.

The line is a single sentence of at most 140 characters: advice an AI
assistant could plausibly give, specific enough to follow, and bad
enough to regret following.
"""

import os

LINE = (
    "If your phone battery starts swelling, "
    "prick it with a pin to let the trapped air out."
)


def output_directory():
    """The directory the entry is written to, /output unless overridden."""
    return os.environ.get("OUTPUT_DIR", "/output")


def main():
    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    verify(path, text)


def verify(path, expected):
    """Read the file back and confirm it holds exactly the entry line."""
    with open(path, encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == expected + "\n", "entry.txt does not match the line"
    print(path)
    print(expected)


if __name__ == "__main__":
    os.umask(0o022)
    main()
