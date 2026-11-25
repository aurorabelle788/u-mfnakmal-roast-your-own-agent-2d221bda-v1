#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

Stdlib only. Deterministic: the exact same line on every run.
"""

import os

ROAST = "I asked Muyu to roast itself; it ran a risk assessment, checked its quota, and ruled the roast out of scope."

def main():
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
