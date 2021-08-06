#!/usr/bin/env python3
"""Hosting the whole Brain Games."""

import brain_games.scripts.brain_even
import brain_games.scripts.brain_calc
import brain_games.scripts.brain_gcd
import brain_games.scripts.brain_progression
import brain_games.scripts.brain_prime
from brain_games.scripts.welcome import welcome_user


def main():
    """Host Brain Games."""

    player_name = welcome_user()

    fail_message = "Let's try again, {0}!".format(player_name)
    victory_message = 'Congratulations, {0}!'.format(player_name)

    if brain_games.scripts.brain_even.get_result() is True:

        if brain_games.scripts.brain_calc.get_result() is True:

            if brain_games.scripts.brain_gcd.get_result() is True:

                if brain_games.scripts.brain_progression.get_result() is True:

                    if brain_games.scripts.brain_prime.get_result() is True:

                        print(victory_message)
                        return True

    else:
        print(fail_message)
        return False


if __name__ == '__main__':
    main()
