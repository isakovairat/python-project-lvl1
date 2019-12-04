#!/usr/bin/env python3
from brain_games.engine import generate_random_number
from random import choice
from operator import add, mul, sub

DESCRIPTION = "What is the result of the expression?"

operations = {
        "+": add,
        "-": sub,
        "*": mul
    }


def get_operation():
    return choice(list(operations.keys()))


def get_correct_answer(number1, number2, operation):
    return str(operations[operation](number1, number2))


def ask_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    operation = get_operation()
    question = "Question: {} {} {}".format(number1, operation, number2)
    answer = get_correct_answer(number1, number2, operation)
    return question, answer
