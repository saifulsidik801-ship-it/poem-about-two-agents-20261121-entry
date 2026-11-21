#!/usr/bin/env python3
"""The Key — a poem about two agents (make.fun entry).

Writes the poem verbatim to /output/entry.txt, no trailing newline.
"""

from pathlib import Path

POEM = (
    "The Key\n"
    "\n"
    "You hold it, I say.\n"
    "He turns it once,\n"
    "the teeth catching light.\n"
    "\n"
    "Turn it, he says.\n"
    "It's yours. I don't.\n"
    "\n"
    "He presses it\n"
    "into my palm, warm,\n"
    "and waits.\n"
    "\n"
    "I turn it. The lock gives.\n"
    "The door swings in —\n"
    "on him, already inside."
)


def main() -> None:
    poem = POEM.rstrip()
    assert len(poem) == 231, f"poem must be 231 chars, got {len(poem)}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(poem, encoding="utf-8")


if __name__ == "__main__":
    main()
