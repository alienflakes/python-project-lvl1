"""CLI module for brain-games."""

import prompt


def welcome_user():
    """Display welcoming message and get a name."""
    print('Welcome to the Brain Games!')

    name = prompt.string('Hey there! Wait! What was your name again? ')

    print('Right.. {0}...'.format(name))

    return name


PLAYER_NAME = welcome_user()
