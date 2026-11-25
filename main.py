#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<= 200 characters) to
/output/entry.txt, or to $ENTRY_OUT/entry.txt when ENTRY_OUT is set
(the grader runs the program with ENTRY_OUT pointing at a temp dir
for local verification).

The line roasts the smart coffee machine: a gadget used every morning
that gates the most basic job in the world - making coffee - behind
Wi-Fi, a firmware update and a location permission.
"""

import os
import sys

ROAST = (
    "My coffee machine needs Wi-Fi, a firmware update and my exact "
    "location before it will brew \u2014 it knows where I live but not "
    "that I am late for work."
)


def main() -> int:
    line = ROAST.strip()
    if not line:
        print("error: roast line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(
            "error: roast line is %d characters, over the 200 limit"
            % len(line),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("ENTRY_OUT") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
