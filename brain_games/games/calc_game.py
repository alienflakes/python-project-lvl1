"""Game Logic for Calc Game."""


class CalcGameLogic:
    """Class for Calc Game Logic to use in game_flow.py."""

    intro = 'What is the result of the expression?'

    def get_answer(num_01, num_02, num_op):
        """Get the Answer for Calc Game logic."""
        if num_op == 0:
            return str(num_01 + num_02)
        elif num_op == 1:
            return str(num_01 - num_02)
        elif num_op == 2:
            return str(num_01 * num_02)

    def get_question(num_01, num_02, num_op):
        """Get the Question for Is Even game logic."""

        if num_op == 0:
            operator = '+'
        elif num_op == 1:
            operator = '-'
        elif num_op == 2:
            operator = '*'

        return "What's {0} {1} {2}?".format(num_01, operator, num_02)
