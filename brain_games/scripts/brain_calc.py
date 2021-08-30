#!/usr/bin/env python3
"""Script for the second Brain Game: Calc Game."""

from brain_games.game_flow import game_core
import brain_games.games.calc
import brain_games.scripts.welcome


def main():

    game_core(brain_games.games.calc)


if __name__ == '__main__':
    main()
