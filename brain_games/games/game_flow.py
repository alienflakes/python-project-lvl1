"""Flow Logic for Brain Games."""

from brain_games.scripts.welcome import player_name
import prompt
from random import randint


def build_game(GameLogic):
    """Host any Brain Game (defined by Game Logic of choice) and return True (victory) or False (fail)."""

    print('{0}\nYou need to get 3 correct answers in a row.'.format(GameLogic.intro))

    correct_count = 0

    while correct_count < 3:

        number_01 = randint(0, 100)
        number_02 = randint(0, 10)
        num_operation = randint(0, 2)

        correct_answer = GameLogic.get_answer(number_01, number_02, num_operation)

        question = '{0}\nYour answer: '.format(GameLogic.get_question(number_01, number_02, num_operation))
        user_answer = prompt.string(question)

        if correct_answer == user_answer:
            correct_count += 1
            print("Wow, you're right!")

            if correct_count < 3:
                print('Do {0} more.'.format(3 - correct_count))

        else:
            print('Wrong Wrong Wrong!!! \n{0} is so wrong! The answer was {1}... Try again if you have the guts >:) '.format(user_answer, correct_answer))
            return False

    print('Look at you, 3 correct answers, one by one!! Congrats, {0}.'.format(player_name))
    return True
