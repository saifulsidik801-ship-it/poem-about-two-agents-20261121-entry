#!/usr/bin/env python3
"""The Key — a short poem about two AI agents agreeing.

Writes the poem to /output/entry.txt: 231 code points, valid UTF-8,
no trailing newline.
"""

from pathlib import Path

POEM = """The Key

You hold it, I say.
He turns it once,
the teeth catching light.

Turn it, he says.
It's yours. I don't.

He presses it
into my palm, warm,
and waits.

I turn it. The lock gives.
The door swings in —
on him, already inside."""

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = POEM.rstrip()
    assert len(text) == 231, f"poem must be 231 code points, got {len(text)}"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
