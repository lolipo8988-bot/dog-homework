"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes a single line to /output/entry.txt: the excuse a dog gives after
being caught eating the homework. The gate requires UTF-8 text of 1 to
200 characters, not only white space. The program is deterministic:
every run writes exactly the same bytes.

The line is written in the dog's own voice, with a dog who believes it
has done nothing wrong: anything on the floor is legally the dog's
under floor law, and the homework was not destroyed but filed inside
the dog for safekeeping — returnable Thursday, maybe Friday, with the
dog's real priority (cheese) named as the price of doing business.
"""

import os

# Default output location; MAKEFUN_OUTPUT_DIR overrides the directory so
# the entry can be rendered somewhere else without editing this file.
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 200


def resolve_output_path() -> str:
    """Return the entry.txt path, honouring MAKEFUN_OUTPUT_DIR if set."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(output_dir, OUTPUT_FILENAME)


ENTRY = "It was on the floor, so legally it was mine — floor law. I didn't destroy your homework, I filed it inside me for safekeeping. The answers will be back out Thursday. Maybe Friday. Bring cheese."


def validate_entry(text: str) -> str:
    """Return the entry unchanged after checking the gate's shape rules.

    The entry must be a single non-empty line of at most MAX_CHARS
    characters; ENTRY itself is never modified here.
    """
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
