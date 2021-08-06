"""Game Logic for Prime Brain Game."""

from random import randint


intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_logic():
    """Get the answer and the question for Prime game logic."""

    num = randint(0, 300)

    question = '{0}'.format(num)

    if num > 1:

        for i in range(2, int(num / 2) + 1):

            if (num % i) == 0:
                answer = 'no'
                break
        else:
            answer = 'yes'
    else:
        answer = 'no'

    return answer, question
