#!/usr/bin/env python3
from brain_games.engine import generate_random_number

DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(number1, number2):
    rest = number1 % number2
    if rest == 0:
        return number1
    elif rest == 1:
        return 1
    else:
        return gcd(number2, rest)


def get_correct_answer(number1, number2):
    return str(gcd(number1, number2))


def ask_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    question = "Question: {} {}".format(number1, number2)
    answer = get_correct_answer(number1, number2)
    return question, answer
