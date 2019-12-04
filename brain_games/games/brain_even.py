#!/usr/bin/env python3
from brain_games.engine import generate_random_number

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_correct_answer(number):
    return "no" if number % 2 else "yes"


def ask_question():
    number = generate_random_number()
    answer = get_correct_answer(number)
    question = f"Question: {number}"
    return question, answer
