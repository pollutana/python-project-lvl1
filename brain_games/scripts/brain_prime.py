#!/usr/bin/env python3
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from engine import launch  # noqa E402
from games import prime  # noqa 402


def main():
    launch(prime.RULE, prime)


if __name__ == "__main__":
    main()
