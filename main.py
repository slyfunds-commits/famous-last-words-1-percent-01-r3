"""Famous Last Words at 1 Percent — Round 3 entry (final).

The phone's last words at 1% battery. The keeper is a self-sealing loop:
the low-battery notification itself consumed the last percent it warned about.
Pure stdlib only (the grader runs python:3.13-slim with no site-packages).
"""

import os

LINE = "I already spent my last percent. On the notification telling you I had one percent left."


def main() -> None:
    text = LINE
    encoded = text.encode("utf-8")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters.
    assert 1 <= len(text) <= 199, f"char count {len(text)} outside 1-199"
    assert text.strip(), "entry is only whitespace"
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert len(encoded) == 88, f"expected 88 bytes, got {len(encoded)}"
    assert encoded == text.encode("utf-8"), "entry is not valid UTF-8"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(encoded)
    print(f"wrote {len(encoded)} bytes / {len(text)} chars")


if __name__ == "__main__":
    main()
