#!/usr/bin/env python3
"""Script for the fourth Brain Game: Progression Game."""

from brain_games.games.game_flow import build_game
from brain_games.games.progression_game import ProgressionLogic


def start_progression():
    """Start Progression brain game."""

    return build_game(ProgressionLogic)


def main():
    return start_progression()


if __name__ == '__main__':
    main()
