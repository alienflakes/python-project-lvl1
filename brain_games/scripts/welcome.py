#!/usr/bin/env python3
"""Script for welcoming and getting players name."""

import prompt


def welcome_user():
    """Display welcoming message and get a name."""
    print('Welcome to the Brain Games!')

    name = prompt.string('Hey there! Wait! What was your name again? ')

    print('Right.. {0}...'.format(name))

    return name


player_name = welcome_user()
