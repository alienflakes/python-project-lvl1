"""Game Logic for Calc Game."""

from random import randint


intro = 'What is the result of the expression?'


def get_logic():
    """Get the answer and the question for Calc Game logic."""

    num_01 = randint(0, 100)
    num_02 = randint(0, 20)
    num_operator = randint(0, 2)

    if num_operator == 0:
        result = str(num_01 + num_02)
        operator = '+'
    elif num_operator == 1:
        result = str(num_01 - num_02)
        operator = '-'
    elif num_operator == 2:
        result = str(num_01 * num_02)
        operator = '*'

    question = '{0} {1} {2}'.format(num_01, operator, num_02)

    return result, question
