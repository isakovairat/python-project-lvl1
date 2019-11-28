#!/usr/bin/env python3
from brain_games.engine import generate_random_number
DESCRIPTION = "Answer \"yes\" if given number is prime. " \
              "Otherwise answer \"no\"."


def is_prime(n):
    if n <= 1:
        return "no"
    if n <= 3:
        return "no"
    if n % 2 == 0 or n % 3 == 0:
        return "no"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "no"
        i = i + 6
    return "yes"


def ask_question():
    number = generate_random_number()
    question = "Question: {}".format(number)
    answer = is_prime(number)
    return question, answer
