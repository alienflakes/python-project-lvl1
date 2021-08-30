"""Game Logic for Prime Brain Game."""

from random import randint


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(this_num):
    """Checks whether the num is prime or not."""

    if this_num > 1:

        for i in range(2, int(this_num / 2) + 1):

            if (this_num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def get_answer_and_question():
    """Get the answer and the question for Prime game logic."""

    num_to_check = randint(0, 300)

    question = '{0}'.format(num_to_check)

    if is_prime(num_to_check) is True:
        return 'yes', question
    else:
        return 'no', question
