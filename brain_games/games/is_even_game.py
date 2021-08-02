"""Game Logic for Is Even Brain Game."""


class IsEvenLogic:
    """Class for Is Even Game Logic to use in game_flow.py."""

    intro = 'Type "yes" if the number is even, otherwise type "no".'

    def get_answer(num, num_02=0, num_03=0):
        """Get the Answer for Is Even game logic."""

        if num % 2 == 0:
            return 'yes'
        else:
            return 'no'

    def get_question(num, num_02=0, num_03=0):
        """Get the Question for Is Even game logic."""

        return 'Is {0} even?'.format(num)
