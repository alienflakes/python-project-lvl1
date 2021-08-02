"""Game Logic for Calc Game."""


class CalcGameLogic:
    """Class for Calc Game Logic to use in game_flow.py."""

    intro = 'What is the result of the expression?'

    def get_answer(num_01, num_02, num_03):
        """Get the Answer for Calc Game logic."""
        if num_03 < 7:
            return str(num_01 + num_02)
        elif num_03 < 14:
            return str(num_01 - num_02)
        else:
            return str(num_01 * num_02)

    # 1. Here and below the operation picking was changed from 0 == +, 1 == - and 2 == *
    # to three evenly split ratios of (0, 20). The purpose is to keep number_03 = randint(0, 20)
    # both useful for the GCD game - wider range of numbers, and for random choice of one
    # of the three operators in the Calc game. I suggest taking the most of these three vars
    # so they are all-purpose and we won't need more random vars (:

    def get_question(num_01, num_02, num_03):
        """Get the Question for Is Even game logic."""

        if num_03 < 7:
            operator = '+'
        elif num_03 < 14:
            operator = '-'
        else:
            operator = '*'

        return "What's {0} {1} {2}?".format(num_01, operator, num_02)
