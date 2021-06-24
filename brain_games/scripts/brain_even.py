#!/usr/bin/env python3
"""Script for the first Brain Game: Is Even."""

from brain_games.is_even import is_even_game


def main():
    """Start ffirst brain game."""

    print('Type "yes" if the number is even, otherwise type "no".\
         \nYou need to get 3 correct answers in a row.')
    is_even_game()


if __name__ == '__main__':
    main()
