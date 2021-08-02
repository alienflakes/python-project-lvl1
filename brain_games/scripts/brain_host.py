#!/usr/bin/env python3
"""Hosting the whole Brain Games."""

from brain_games.scripts.brain_prime import start_prime
from brain_games.scripts.brain_progression import start_progression
from brain_games.scripts.brain_gcd import start_GCD
from brain_games.scripts.brain_even import start_is_even
from brain_games.scripts.brain_calc import start_calc


def main():
    """Host Brain Games."""

    fail_message = 'Uh oh!! You failed this game! Square up and return later.'
    victory_message = 'Wow, you\'ve really outdone yourself. The victory is yours, so is a PhD in maths.'

    if start_is_even() is True:

        if start_calc() is True:

            if start_GCD() is True:

                if start_progression() is True:

                    if start_prime() is True:

                        print(victory_message)
                        return True

    else:
        print(fail_message)
        return False


if __name__ == '__main__':
    main()
