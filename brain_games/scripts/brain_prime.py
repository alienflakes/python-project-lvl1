#!/usr/bin/env python3
"""Script for the fifth Brain Game: Prime."""

from brain_games.game_flow import game_core
import brain_games.games.prime
import brain_games.scripts.welcome


def main():

    game_core(brain_games.games.prime)


if __name__ == '__main__':
    main()
