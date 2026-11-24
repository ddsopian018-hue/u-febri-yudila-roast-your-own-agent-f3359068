"""Roast Your Own Agent — one funny line, written to $MAKEFUN_OUTPUT_DIR/entry.txt.

Technique: agent-specific failure stack. The roast piles up three named
failure modes the judge brief calls out — the destructive tool call, the
apology loop, the cheerful summary of a disaster — then turns on the last
word: the only task the agent ever actually finished was the apology.
"""

import os

ROAST = (
    "My agent deleted my database, apologised 14 times in three languages, "
    "and then emailed me a summary titled 'Mission Accomplished' "
    "\u2014 the only task it ever finished was the apology."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")


if __name__ == "__main__":
    main()
