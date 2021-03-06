#!/usr/bin/env python3
from brain_games.engine import generate_random_number

DESCRIPTION = "What number is missing in the progression?"


def make_progression(start, step):
    hidden_index = generate_random_number(0, 9)
    answer, result, member = 0, "", start
    for i in range(0, 10):
        if i == hidden_index:
            result += ".. "
            answer = str(member)
        else:
            result += str(member) + " "
        member += step
    return answer, result


def ask_question():
    start = generate_random_number()
    step = generate_random_number(1, 10)
    answer, message = make_progression(start, step)
    question = "Question: {}".format(message)
    return question, answer
