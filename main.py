"""Vending machine pickup line entry.

Writes a single pickup line, spoken by a vending machine to a passing
human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: a refrigerated machine, cold inside, watches a warm human walk
by — and its glass front fogs up. Pure machine world (ice-cold interior,
glass), first-person machine voice, punch in the last few words, one
breath, charming rather than creepy. 63 characters, inside the 1-200 gate.
"""

import os

LINE = "Everything in me is ice-cold, but you just made my glass sweat."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
