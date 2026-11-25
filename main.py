"""One Star, Written in Sap — make.fun entry.

Writes a single one-line, one-star review by a houseplant about its
human owner to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "One star. He waters me once a month like he's doing me a favour, "
    "then posts a photo captioned 'my thriving baby' while I'm dropping "
    "leaves on his keyboard. I am not thriving. I am a hostage with "
    "good lighting."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
