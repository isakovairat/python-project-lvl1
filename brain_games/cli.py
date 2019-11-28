#!/usr/bin/env python3
import prompt


def get_user_name():
    user = prompt.string("May I have your name? ")
    return user


def get_user_answer():
    answer = prompt.string("Your answer: ")
    return answer
