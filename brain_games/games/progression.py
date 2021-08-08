"""Game Logic for the Progression Brain Game."""

from random import randint


intro = 'What number is missing in the progression?'


def get_logic():
    """Get the answer and the question for Progression game logic."""

    step = randint(1, 10)
    current_num = randint(0, 30)
    missing_spot = randint(1, 10)

    spot_decreasing = missing_spot
    missing_num = current_num

    while spot_decreasing > 1:
        missing_num += step
        spot_decreasing -= 1

    answer = str(missing_num)

    question_range = ''

    i = 1

    while i < missing_spot:

        question_range += str(current_num) + ' '
        current_num += step
        i += 1

    question_range += '..'
    i += 1
    current_num += step

    while i <= 10:

        question_range += ' ' + str(current_num)
        current_num += step
        i += 1

    question = '{0}'.format(question_range)

    return answer, question
