from random import randint
from brain_games.cli import get_user_name, get_user_answer

ROUNDS = 3


def greet():
    print('Welcome to the Brain Games!')


def generate_random_number(start=0, end=100):
    return randint(start, end)


def welcome():
    user = get_user_name()
    print("Hello, {}!".format(user))
    return user


def play_the_game(game=None):
    greet()
    if not game:
        return
    print(game.DESCRIPTION)
    print()
    user = welcome()
    print()
    correct_answers = 0
    while correct_answers < ROUNDS:
        question, correct_answer = game.ask_question()
        print(question)
        user_answer = get_user_answer()
        if user_answer == correct_answer:
            result, message = True, "Correct!"
        else:
            message = "'{}' is wrong answer ;(. Correct answer was '{}'."
            message = message.format(user_answer, correct_answer)
            result = False
        print(message)
        if not result:
            print("Let\'s try again, {}!".format(user))
            return
        correct_answers += 1
    print("Congratulations, {}!".format(user))
