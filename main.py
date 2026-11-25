#!/usr/bin/env python3
"""The 3 AM Excuse - make.fun entry.

Writes one line (under 200 characters) in the voice of a hardware wallet
that refuses to sign a transaction at 3 AM, to /output/entry.txt.
Standard library only.
"""

import os
import sys

ENTRY = "It's 3 AM. My keys are asleep, my screen is dreaming in hex, and last time you signed half-awake you bought a frog in a hat. Come back at sunrise."

MAX_CHARS = 200


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    text = ENTRY
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry is blank")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
