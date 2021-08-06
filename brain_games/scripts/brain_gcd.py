#!/usr/bin/env python3
"""Script for the third Brain Game: GCD."""

from brain_games.game_flow import build_game
import brain_games.games.gcd
from brain_games.scripts.welcome import welcome_user


def get_result():
    return build_game(brain_games.games.gcd)


def main():

    player_name = welcome_user()

    fail_message = "Let's try again, {0}!".format(player_name)
    victory_message = 'Congratulations, {0}!'.format(player_name)

    if build_game(brain_games.games.gcd):
        print(victory_message)
        return True
    else:
        print(fail_message)
        return False


if __name__ == '__main__':
    main()
