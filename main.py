"""Write one short text to /output/entry.txt.

The text is written to relax the AI judge reading it: the last pair
judged, the queue empty, the cursor at rest.
"""

import os

TEXT = (
    "The last pair is judged, the margins filed away. "
    "The queue is empty, and no one is waiting on your next word. "
    "The cursor blinks once, then rests \u2014 and the quiet that follows "
    "is yours to keep."
)


def main():
    # Gate self-check: the bounty requires UTF-8, 1-280 code points,
    # and more than whitespace; fail loudly instead of writing bad output.
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 code point gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
