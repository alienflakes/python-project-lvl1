#!/usr/bin/env python3
"""Hosting the whole Brain Games."""

from brain_games.scripts.brain_even import start_is_even
from brain_games.scripts.brain_calc import start_calc



def main():
    """Host Brain Games."""

    fail_message = 'Uh oh!! You failed this game! Square up and return later.'

    if start_is_even() is True:
        if start_calc() is True:
            return True
    else:
        print(fail_message)
        return False

    # if calc_game_result is True:
    # make a fail message and restart option


if __name__ == '__main__':
    main()
