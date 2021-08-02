"""Game Logic for Greatest Common Divisor Brain Game."""


def get_gcd(first_number, second_number):
    """Find the greatest common divisor of the numbers."""

    t = 0
    while second_number != 0:
        t = second_number
        second_number = first_number % second_number
        first_number = t

    return first_number


class GCDLogic:
    """Class for GCD Game Logic to use in game_flow.py."""

    intro = 'Find the greatest common divisor of given numbers.'

    def get_answer(num_01, num_02, num_03):
        """Get the Answer for GCD game logic."""

        first_num = num_01 // 10 * num_02
        second_num = num_01 // 10 * num_03

        return str(get_gcd(first_num, second_num))

    def get_question(num_01, num_02, num_03):
        """Get the Question for GCD game logic."""

        first_num = num_01 // 10 * num_02
        second_num = num_01 // 10 * num_03

        return 'GCD of {0} and {1}?'.format(first_num, second_num)

    # *2. In methods 'get_answer' and 'get_question' I divide
    # the number by 10 just to avoid exceptional complicity
    # of GCD rounds (: Call it easy-level difficulty for now!
