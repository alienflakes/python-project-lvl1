"""Game Logic for the fourth Brain Game: Progression Game."""


class ProgressionLogic:
    """Class for Progression Game Logic to use in game_flow.py."""

    intro = 'Enter the number missing in the progression.'

    def get_answer(num_01, num_02, num_03):
        """Get the Answer for Progression game logic."""

        step = num_01 // 10 + 1
        missing_num = num_02
        missing_spot = num_03 // 2 + 1

        while missing_spot > 1:
            missing_num += step
            missing_spot -= 1

        return str(missing_num)

    def get_question(num_01, num_02, num_03):
        """Get the Question for Progression game logic."""

        step = num_01 // 10 + 1
        current_num = num_02
        missing_spot = num_03 // 2 + 1

        question_range = ''

        i = 1

        while i < missing_spot:

            question_range += ' ' + str(current_num)
            current_num += step
            i += 1

        question_range += ' ..'
        i += 1
        current_num += step

        while i <= 10:

            question_range += ' ' + str(current_num)
            current_num += step
            i += 1

        return "What's missing here? {0}".format(question_range)
