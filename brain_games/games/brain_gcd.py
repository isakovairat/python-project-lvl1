#!/usr/bin/env python3
from brain_games.engine import generate_random_number

DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def ask_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    question = "Question: {} {}".format(number1, number2)
    answer = str(gcd(number1, number2))
    return question, answer
