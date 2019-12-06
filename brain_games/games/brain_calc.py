#!/usr/bin/env python3
from brain_games.engine import generate_random_number
from random import choice
from operator import add, mul, sub

DESCRIPTION = "What is the result of the expression?"

operations = [
    ("+", add),
    ("-", sub),
    ("*", mul)
]


def get_operation():
    # return random tuple from operations array,
    # which contains (string, <built-in func>)
    return choice(list(operations))


def get_correct_answer(number1, number2, operation):
    # operation[1] is one of add or mul or sub built-in functions
    return str(operation[1](number1, number2))


def ask_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    operation = get_operation()
    # operation[0] is "+" or "-" or "*"
    question = "Question: {} {} {}".format(number1, operation[0], number2)
    answer = get_correct_answer(number1, number2, operation)
    return question, answer
