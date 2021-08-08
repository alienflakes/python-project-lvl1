#!/usr/bin/env python3
"""Script for the second Brain Game: Calc Game."""

from brain_games.game_flow import build_game
import brain_games.games.calc
import brain_games.scripts.welcome


def get_result():

    return build_game(brain_games.games.calc)


def main():

    player_name = brain_games.scripts.welcome.main()

    fail_message = "Let's try again, {0}!".format(player_name)
    victory_message = 'Congratulations, {0}!'.format(player_name)

    if build_game(brain_games.games.calc):
        print(victory_message)
        return True
    else:
        print(fail_message)
        return False


if __name__ == '__main__':
    main()
