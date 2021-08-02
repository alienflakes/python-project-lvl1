#!/usr/bin/env python3
"""Script for the fifth Brain Game: Prime."""

from brain_games.games.game_flow import build_game
from brain_games.games.prime_game import PrimeLogic


def start_prime():
    """Start Prime brain game."""

    return build_game(PrimeLogic)


def main():
    return start_prime()


if __name__ == '__main__':
    main()
