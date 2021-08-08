#!/usr/bin/env python3
"""Script for welcoming and getting players name."""

import prompt


def main():
    """Display welcoming message and get a name."""

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, {0}!'.format(name))

    return name


if __name__ == '__main__':
    main()
