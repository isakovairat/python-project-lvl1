#!/usr/bin/env python3
from brain_games.engine import generate_random_number

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def ask_question():
    number = generate_random_number()
    answer = "no" if number % 2 else "yes"
    question = f"Question: {number}"
    return question, answer
