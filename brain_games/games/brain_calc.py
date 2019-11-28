#!/usr/bin/env python3
from brain_games.engine import generate_random_number
from random import choice
DESCRIPTION = "What is the result of the expression?"


def get_operation():
    operations = ["+", "-", "*"]
    return choice(operations)


def get_correct_answer(number1, number2, operation):
    if operation == "+":
        return str(number1 + number2)
    if operation == "-":
        return str(number1 - number2)
    if operation == "*":
        return str(number1 * number2)


def ask_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    operation = get_operation()
    question = "Question: {} {} {}".format(number1, operation, number2)
    answer = get_correct_answer(number1, number2, operation)
    return question, answer
