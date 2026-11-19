#!/usr/bin/env python3
"""Entry program for the make.fun bounty news-image-20261119.

The entry itself is a single pre-rendered newspaper front page, entry.png,
shipped beside this file in the repository. Running this program copies
that image into the directory named by the MAKEFUN_OUTPUT_DIR environment
variable (falling back to ./out), which is where the grader looks for it.

Python 3 standard library only; no network access is needed or used.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE_IMAGE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE_IMAGE, dest)
    print("wrote {} ({} bytes)".format(dest, os.path.getsize(dest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
