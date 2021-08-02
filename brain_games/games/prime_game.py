"""Game Logic for Prime Brain Game."""


class PrimeLogic:
    """Class for Is Prime Game Logic to use in game_flow.py."""

    intro = 'Type "yes" if the number is prime, otherwise type "no".'

    def get_answer(num_01, num_02, num_03):
        """Get the Answer for Prime game logic."""

        if num_01 > 1:

            for i in range(2, int(num_01 / 2) + 1):

                if (num_01 % i) == 0:
                    return 'no'
            else:
                return 'yes'
        else:
            return 'no'

    def get_question(num_01, num_02, num_03):
        """Get the Question for Prime game logic."""

        return 'Is {0} prime?'.format(num_01)
