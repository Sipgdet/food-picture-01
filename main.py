"""food-picture-01 entry: write our food picture to /output/entry.png.

The entry ships one picture (entry.png, a double smash burger with
molten cheddar cascading over charred patties, crispy bacon, tomato and
lettuce in a glossy sesame brioche bun, golden fries on a dark slate
board) and this program copies it, byte for byte, to the output
directory. Pure Python 3.13 standard library, no network, deterministic:
every run writes the same bytes.
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
