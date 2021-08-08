"""Flow Logic for Brain Games."""

import prompt


def build_game(game_type):
    """Host any Brain Game and return True (victory) or False (fail)."""

    print(game_type.intro)

    correct_count = 0

    rounds_count = 3

    while correct_count < rounds_count:

        correct_answer, custom_question = game_type.get_logic()

        whole_question = 'Question: {0}\nYour answer: '.format(custom_question)
        user_answer = prompt.string(whole_question, empty=True)

        if correct_answer == user_answer:
            correct_count += 1
            print("Correct!")

        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, correct_answer))
            return False

    return True
