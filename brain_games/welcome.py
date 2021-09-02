#!/usr/bin/env python3
"""Welcomes and gets player's name."""

import prompt


def welcome_get_name():
    """Display welcoming message and get a name."""

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, {0}!'.format(name))

    return name
