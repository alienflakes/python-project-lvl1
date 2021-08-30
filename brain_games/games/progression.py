"""Game Logic for the Progression Brain Game."""

from random import randint


INTRO = 'What number is missing in the progression?'


def make_progression(step, starting_num, missing_spot, progression_length):
    """Method for creating a progression string with a missed spot and its answer."""

    current_spot = 0
    current_num = starting_num
    progression_str = ''

    while current_spot < progression_length:

        if current_spot == missing_spot:
            progression_str += ' ..'
            missing_num = str(current_num)
        else:
            progression_str += ' ' + str(current_num)

        current_num += step
        current_spot += 1

    return missing_num, progression_str


def get_answer_and_question():

    step = randint(1, 10)
    start_num = randint(0, 30)
    missed_spot = randint(0, 9)
    progression_length = 10

    return make_progression(step, start_num, missed_spot, progression_length)
