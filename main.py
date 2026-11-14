"""food-picture-01 entry: write our food picture to /output/entry.png.

Round 3 (2026-11-14): Midnight Tonkotsu — the round-2 golden-hour
ramen scored 909458 (#418), slightly below the original ramen's
913525 (#337), and the top 3 on the board are all ramen, led by
"Midnight Tonkotsu". Diagnosis: v3 lost because black garlic oil
swirls and scattered sesame read as mess/dirt and the broth went
muddy. This version keeps the original's clean, readable toppings
but goes dark and cinematic: near-black background, one warm golden
spotlight, an EXTREMELY tall thick noodle pull with backlit steam,
charred glistening chashu, jammy egg, one crisp nori sheet, no black
oil swirls, no scattered sesame. The entry ships one picture
(entry.png) and this program copies it, byte for byte, to the output
directory. Pure Python 3.13 standard library, no network,
deterministic: every run writes the same bytes.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = OUTPUT_DIR / "entry.png"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    # The gate reads exactly these bytes, so confirm the copy is whole:
    # same size and same digest as the picture shipped in the repository.
    assert DEST.stat().st_size == SOURCE.stat().st_size
    assert _sha256(DEST) == _sha256(SOURCE)
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes, sha256 {_sha256(DEST)[:16]}...)")


if __name__ == "__main__":
    main()
