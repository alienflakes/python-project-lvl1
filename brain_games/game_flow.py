"""Flow Logic for Brain Games."""

import prompt
import brain_games.scripts.welcome


def game_core(game):
    """Host a Brain Game."""

    player_name = brain_games.scripts.welcome.main()

    fail_message = "Let's try again, {0}!".format(player_name)
    victory_message = 'Congratulations, {0}!'.format(player_name)

    print(game.INTRO)

    correct_count = 0

    rounds_count = 3

    while correct_count < rounds_count:

        correct_answer, custom_question = game.get_answer_and_question()

        whole_question = 'Question: {0}\nYour answer: '.format(custom_question)
        user_answer = prompt.string(whole_question, empty=True)

        if correct_answer == user_answer:
            correct_count += 1
            print("Correct!")

        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, correct_answer))
            print(fail_message)
            break

    if correct_count == rounds_count:
        print(victory_message)
