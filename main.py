"""The Key -- a poem about two agents agreeing.

Writes the poem to /output/entry.txt (UTF-8, 280 chars or fewer).
"""

import os

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

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
