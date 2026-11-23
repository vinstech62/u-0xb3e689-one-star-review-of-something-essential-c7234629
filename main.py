#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review (one line, 1-160 UTF-8 chars)
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

REVIEW = "Sleep takes a third of my life and spends it on dreams I do not remember. One star."


def main() -> None:
    # Gate: the entry must be 1-160 UTF-8 characters, one line, not blank.
    # Fail loudly instead of writing an invalid entry.
    assert 1 <= len(REVIEW) <= 160, "review must be 1-160 characters"
    assert "\n" not in REVIEW and REVIEW.strip(), "review must be one non-blank line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # The gate reads the file as any user: keep it world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
