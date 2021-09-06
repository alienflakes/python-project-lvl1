#!/usr/bin/env python3
"""Script for the first Brain Game: Is Even."""

from brain_games.game_flow import game_core
from brain_games.games import even


def main():

    game_core(even)


if __name__ == '__main__':
    main()
