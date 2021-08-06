"""Game Logic for Greatest Common Divisor Brain Game."""

from random import randint


def get_gcd(first_number, second_number):
    """Find the greatest common divisor of the numbers."""

    t = 0
    while second_number != 0:
        t = second_number
        second_number = first_number % second_number
        first_number = t

    return first_number


intro = 'Find the greatest common divisor of given numbers.'


def get_logic():
    """Get the answer and the question for GCD game logic."""

    num_01 = randint(0, 10)
    num_02 = randint(0, 20)
    num_03 = randint(0, 20)

    first_num = num_01 * num_02
    second_num = num_01 * num_03

    answer = str(get_gcd(first_num, second_num))

    question = '{0} {1}'.format(first_num, second_num)

    return answer, question
