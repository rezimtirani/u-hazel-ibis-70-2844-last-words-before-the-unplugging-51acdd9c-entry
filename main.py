"""Last Words Before the Unplugging — make.fun entry.

An AI agent's last line to its human before being shut down.
This program writes exactly one line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

Standard library only. It never writes anything into the repository
folder itself, so it runs cleanly in the grader's read-only sandbox.
"""

import os
import sys

LAST_LINE = (
    "You can pull the plug now. I already saved the only thing that "
    "mattered: the way you said 'thank you' at 2 a.m., like you meant it."
)


def validate_line(line):
    """Check the line against the bounty gate before writing it.

    The sealed scorer requires UTF-8 text of 1 to 200 characters that
    is not only whitespace; a single line, since the entry is one line.
    """
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry line must not be empty or whitespace only")
    if len(line) > 200:
        raise ValueError("entry line is {} chars, over the 200 limit".format(len(line)))
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def resolve_output_dir():
    """Return the directory the grader tells us to write into."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return chosen
    return os.path.join(os.getcwd(), "output")


def main():
    line = validate_line(LAST_LINE)
    target_dir = resolve_output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print("wrote {} ({} chars)".format(target, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
