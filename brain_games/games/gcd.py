"""Game Logic for Greatest Common Divisor Brain Game."""

from random import randint


INTRO = 'Find the greatest common divisor of given numbers.'


def get_gcd(number_a, number_b):
    """Find the greatest common divisor of the numbers."""

    while number_b:
        number_a, number_b = number_b, number_a % number_b
    return number_a


def get_answer_and_question():
    """Get the answer and the question for GCD game logic."""

    first_num = randint(0, 200)
    second_num = randint(0, 200)

    answer = str(get_gcd(first_num, second_num))

    question = '{0} {1}'.format(first_num, second_num)

    return answer, question
