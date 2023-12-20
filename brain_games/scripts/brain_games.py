#!/usr/bin/env python3
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


def main():
    from cli import welcome_user

    welcome_user()


if __name__ == "__main__":
    main()
