"""Game Logic for Calc Game."""

from random import randint, choice


INTRO = 'What is the result of the expression?'


def get_answer_and_question():
    """Get the answer (result) and the question (expression)."""

    num_01 = randint(0, 100)
    num_02 = randint(0, 10)
    num_operator = choice('+-*')

    if num_operator == '+':
        result = str(num_01 + num_02)
    elif num_operator == '-':
        result = str(num_01 - num_02)
    elif num_operator == '*':
        result = str(num_01 * num_02)

    question = '{0} {1} {2}'.format(num_01, num_operator, num_02)

    return result, question
