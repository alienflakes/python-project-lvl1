#!/usr/bin/env python3
"""Script for the third Brain Game: GCD."""

from brain_games.games.game_flow import build_game
from brain_games.games.gcd_game import GCDLogic


def start_GCD():
    """Start GCD brain game."""

    return build_game(GCDLogic)


def main():
    return start_GCD()


if __name__ == '__main__':
    main()
