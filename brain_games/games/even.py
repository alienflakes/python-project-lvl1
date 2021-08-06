"""Game Logic for Even Brain Game."""

from random import randint


intro = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_logic():
    """Get the answer and the question for Even game logic."""

    num_even = randint(1, 100)

    question = str(num_even)

    if num_even % 2 == 0:
        return 'yes', question
    else:
        return 'no', question
