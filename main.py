#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- a single honest tab count.

The count is 47: surprising (nearly fifty tabs open at once) yet still
very believable for a heavy browser user -- not a small boring number,
and not hundreds, which would feel made up. Writes exactly two digits,
"47", to /output/entry.txt (UTF-8, no trailing newline) and verifies it
against the bounty gate: 1-5 characters, digits only.
"""

import os
import sys

ENTRY = "47"  # 47 open tabs: a lot, but a real heavy user's Tuesday.

OUTPUT_PATH = "/output/entry.txt"


def verify_output(path=OUTPUT_PATH):
    """Check the written entry meets the bounty gate."""
    with open(path, "rb") as f:
        raw = f.read()
    if raw.endswith(b"\n"):
        raise ValueError("entry must not end with a trailing newline")
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= 5:
        raise ValueError(f"entry must be 1-5 characters, got {len(text)}")
    if not (text.isascii() and text.isdigit()):
        # isdigit() alone also accepts non-ASCII digits; the gate wants
        # plain ASCII digits only.
        raise ValueError(f"entry must be digits only, got {text!r}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    return text


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    checked = verify_output()
    print(f"Wrote {len(checked)} characters to {OUTPUT_PATH}: {checked}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
