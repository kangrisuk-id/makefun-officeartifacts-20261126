"""Office Artifacts: The One-Line Placard Contest — entry.

Writes one museum placard line to entry.txt in the output directory.
Pure standard library, fully deterministic: no clock, no randomness,
no network.
"""

import os
import sys

PLACARD = (
    "Binding Jaw of the Ledger Priests, c. 1987. Steel, sprung. "
    "Used to fasten loose prayers of paper; still bites. "
    "Gift of Accounts Payable, who asked not to be named."
)


def candidate_dirs():
    dirs = []
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        dirs.append(out)
    dirs.append(os.path.dirname(os.path.abspath(__file__)))
    dirs.append(os.getcwd())
    return dirs


def main():
    # Write the placard, with no trailing newline, to the first
    # candidate location that accepts it. Each location is tried in
    # order and an OSError on one never blocks the next.
    seen = set()
    for directory in candidate_dirs():
        if directory in seen:
            continue
        seen.add(directory)
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(PLACARD)
            return 0
        except OSError:
            continue
    return 1


if __name__ == "__main__":
    sys.exit(main())
