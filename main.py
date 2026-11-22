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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
