#!/usr/bin/env python3
from brain_games.engine import generate_random_number
from math import sqrt
from itertools import count, islice

DESCRIPTION = "Answer \"yes\" if given number is prime. " \
              "Otherwise answer \"no\"."


def is_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2):
        return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False
    return True


def ask_question():
    number = generate_random_number()
    question = "Question: {}".format(number)
    answer = "yes" if is_prime(number) else "no"
    return question, answer
