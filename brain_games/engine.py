#!/usr/bin/env python3
from random import randint
from brain_games.cli import get_user_name, get_user_answer

ROUNDS = 3


def greet():
    print('Welcome to the Brain Games!')


def generate_random_number(start=0, end=100):
    return randint(start, end)


def check(user_answer, correct_answer):
    if user_answer == correct_answer:
        message = "Correct!"
        return True, message
    message = "'{}' is wrong answer ;(. Correct answer was '{}'."
    return False, message.format(user_answer, correct_answer)


def welcome():
    user = get_user_name()
    print("Hello, {}!".format(user))
    return user


def run(game=None):
    greet()
    if game:
        print(game.DESCRIPTION, "\n")
        user = welcome()
        print()
        engine(user, game.ask_question)


def engine(user, play_question):
    correct_answers = 0
    while correct_answers < ROUNDS:
        question, correct_answer = play_question()
        print(question)
        result, message = check(get_user_answer(), correct_answer)
        print(message)
        if result:
            correct_answers += 1
        else:
            print("Let\'s try again, {}!".format(user))
            return
    print("Congratulations, {}!".format(user))
