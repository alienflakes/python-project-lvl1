#!/usr/bin/env python3
"""Script for the first Brain Game: Is Even."""

from brain_games.game_flow import game_core
import brain_games.games.even


def main():

    game_core(brain_games.games.even)


if __name__ == '__main__':
    main()
