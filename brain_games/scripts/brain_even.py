#!/usr/bin/env python3
"""Script for the first Brain Game: Is Even."""

from brain_games.games.game_flow import build_game
from brain_games.games.is_even_game import IsEvenLogic


def start_is_even():
    """Start Is Even brain game."""

    return build_game(IsEvenLogic)


def main():
    return start_is_even()


if __name__ == '__main__':
    main()
