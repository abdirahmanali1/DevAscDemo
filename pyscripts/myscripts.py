from __future__ import annotations
import argparse
import logging
import sys


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Basic script scaffold")
    p.add_argument("-n", "--name", help="Name to greet", default="World")
    p.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
    p.add_argument("--version", action="version", version=__version__)
    return p.parse_args(argv)


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"