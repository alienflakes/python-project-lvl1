"""First Brain Game: Is Even."""

import prompt
from random import randint
from brain_games.cli import PLAYER_NAME


def is_even_game():
    """Host Is Even game and return victory or break."""

    correct_count = 0

    while correct_count < 3:

        num = randint(0, 100)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        question_even = 'Is {0} even?\nYour answer:'.format(num)
        user_answer = prompt.string(question_even)

        if correct_answer == user_answer:
            correct_count += 1
            print("Wow, you're right!")

            if correct_count < 3:
                print('Do {0} more.'.format(3 - correct_count))

        else:
            print('Wrong Wrong Wrong!!! \n{0} is so wrong! The answer was {1}... Try again >:)'.format(user_answer, correct_answer))
            return False

    print('Look at you, 3 correct answers, one by one!! Congrats, {0}.'.format(PLAYER_NAME))
    return True
