#!/usr/bin/env python3
"""Script for the third Brain Game: GCD."""

from brain_games.game_flow import game_core
from brain_games.games import gcd


def main():

    game_core(gcd)


if __name__ == '__main__':
    main()
