"""Flow Logic for Brain Games."""

import prompt
from brain_games.welcome import welcome_get_name


def game_core(game):
    """Host a Brain Game."""

    player_name = welcome_get_name()

    print(game.INTRO)

    correct_count = 0

    rounds_count = 3

    while correct_count < rounds_count:

        correct_answer, custom_question = game.get_answer_and_question()

        question_of_round = 'Question: {0}'.format(custom_question)
        print(question_of_round)

        answer_prompt = 'Your answer: '
        user_answer = prompt.string(answer_prompt, empty=True)

        if correct_answer == user_answer:
            correct_count += 1
            print("Correct!")

        else:
            wrong_answer_message = "'{0}' is wrong answer ;(. \
Correct answer was '{1}'.".format(user_answer, correct_answer)
            print(wrong_answer_message)

            fail_message = "Let's try again, {0}!".format(player_name)
            print(fail_message)
            break

    if correct_count == rounds_count:

        victory_message = 'Congratulations, {0}!'.format(player_name)
        print(victory_message)
