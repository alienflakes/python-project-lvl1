#!/usr/bin/env python3
"""Script for the fourth Brain Game: Progression Game."""

from brain_games.game_flow import game_core
import brain_games.games.progression
import brain_games.scripts.welcome


def main():

    game_core(brain_games.games.progression)


if __name__ == '__main__':
    main()
