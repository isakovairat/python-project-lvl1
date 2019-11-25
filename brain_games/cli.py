#!/usr/bin/env python3
import prompt

ROUNDS = 3


def greet(name):
    print("Hello, {}!\n".format(name))


def congrats(name):
    print("Congratulations, {}!".format(name))


def try_again(name):
    print("Let's try again, {}!".format(name))


def welcome():
    print("Welcome to the Brain Games")


def run():
    name = prompt.string("May I have your name? ")
    greet(name)
    return name
