#!/usr/bin/env python3
from brain_games.engine import generate_random_number
from math import sqrt
from itertools import count, islice
DESCRIPTION = "Answer \"yes\" if given number is prime. " \
              "Otherwise answer \"no\"."


def is_prime(n):
    if n < 2:
        return "no"
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return "no"
    return "yes"


def ask_question():
    number = generate_random_number()
    question = "Question: {}".format(number)
    answer = is_prime(number)
    return question, answer
