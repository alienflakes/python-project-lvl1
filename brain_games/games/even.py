"""Game Logic for Even Brain Game."""

from random import randint


INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(this_num):

    if this_num % 2 == 0:
        return True
    else:
        return False


def get_answer_and_question():
    """Get the answer and the question for Even game logic."""

    num_to_check = randint(1, 100)

    question = str(num_to_check)

    if is_even(num_to_check) is True:
        return 'yes', question
    else:
        return 'no', question
