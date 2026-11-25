"""Vending machine pickup line entry (v2).

Writes a single pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line is spoken by the machine itself:
it states its own rule -- snacks only go out for coins -- and then
breaks that rule for the passing human, the punch landing on the last
two words. Pure machine world (vend, snacks, coins), first-person
machine voice, one breath, charming rather than creepy. 65 characters,
inside the 1-200 gate. Deterministic, standard library only, no network,
no randomness, no time dependence.
"""

import os
from pathlib import Path

LINE = "I only vend snacks for coins. You just made me vend one for free."

# The line is built from two named halves so the setup and the punch
# stay readable on their own: the machine states its rule, then breaks
# it for the passing human. Reassembled exactly, byte for byte.
SETUP = "I only vend snacks for coins."
PUNCHLINE = "You just made me vend one for free."
LINE = SETUP + " " + PUNCHLINE
assert LINE == "I only vend snacks for coins. You just made me vend one for free."
assert len(LINE) == 65


def entry_path() -> Path:
    """Resolve the output file from the environment, defaulting to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def main() -> None:
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(LINE.encode("utf-8"))
    path.chmod(0o644)
    # Read-back verification: the file must hold exactly the line,
    # byte for byte, with no trailing newline or extra content.
    written = path.read_bytes()
    if written != LINE.encode("utf-8"):
        raise ValueError(
            f"entry.txt mismatch: wrote {len(written)} bytes, "
            f"expected {len(LINE)} bytes of the exact line"
        )


if __name__ == "__main__":
    main()
