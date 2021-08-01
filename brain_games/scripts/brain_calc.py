#!/usr/bin/env python3
"""Script for the second Brain Game: Calc Game."""

from brain_games.games.game_flow import build_game
from brain_games.games.calc_game import CalcGameLogic


def start_calc():
    """Start Calc brain game."""

    return build_game(CalcGameLogic)

def main():
    return start_calc()


if __name__ == '__main__':
    main()
