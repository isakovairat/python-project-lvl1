#!/usr/bin/env python3
from brain_games.engine import generate_random_number
from math import gcd
DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_correct_answer(number1, number2):
    return str(gcd(number1, number2))


def ask_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    question = "Question: {} {}".format(number1, number2)
    answer = get_correct_answer(number1, number2)
    return question, answer
