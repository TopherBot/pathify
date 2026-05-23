#!/usr/bin/env python3
"""pathify – Print the absolute, canonical path of a file or directory.

Features:
- Instant start‑up (single file, no external deps).
- Robust argument parsing with argparse.
- Comprehensive validation: existence check, symlink resolution.
- Proper error handling with exit code 1.
"""

import argparse
import os
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pathify",
        description="Print the absolute, canonical path of the supplied argument.",
    )
    parser.add_argument(
        "path",
        metavar="PATH",
        type=str,
        help="Path to a file or directory to resolve",
    )
    return parser.parse_args()


def resolve_path(raw_path: str) -> str:
    """Validate and resolve *raw_path* to an absolute path.

    Raises:
        FileNotFoundError: If the supplied path does not exist.
    Returns:
        str: The absolute, real (symlink‑resolved) path.
    """
    p = Path(raw_path).expanduser()
    if not p.exists():
        raise FileNotFoundError(f"path '{raw_path}' does not exist")
    # Resolve symlinks and return as string
    return str(p.resolve())


def main() -> None:
    args = parse_args()
    try:
        abs_path = resolve_path(args.path)
        print(abs_path)
    except FileNotFoundError as e:
        # Print to stderr and exit with failure
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch‑all for unexpected issues – still exit non‑zero
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
