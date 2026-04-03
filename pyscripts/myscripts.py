from __future__ import annotations
import argparse
import logging
import sys

#!/usr/bin/env python3
"""
myscripts.py - basic Python script scaffold

Usage:
    python myscripts.py --name Alice
"""


__version__ = "0.1.0"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Basic script scaffold")
    p.add_argument("-n", "--name", help="Name to greet", default="World")
    p.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
    p.add_argument("--version", action="version", version=__version__)
    return p.parse_args(argv)


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    setup_logging(args.verbose)
    logging.debug("Parsed arguments: %s", args)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))