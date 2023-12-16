#!/usr/bin/env python3
import prompt


def main():
    print("Welocme to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
