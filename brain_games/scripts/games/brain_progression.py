import brain_games.cli
import random
from math import gcd

ROUNDS = 3


def get_hidden_position():
    return random.randint(0, 9)


def try_again_msg(answer, correct_answer, name):
    print("\'{}\' is wrong answer ;(. ".format(answer), end="")
    print("Correct answer was \'{}\'.".format(correct_answer))
    brain_games.cli.try_again(name)


def print_ap(start, step):
    curr_term = start
    hidden = get_hidden_position()
    for i in range(0, 10):
        if i == hidden:
            print('..', end=' ')
            hidden = curr_term
        else:
            print(curr_term, end=' ')
        curr_term += step
    print()
    return hidden


def play_progression(name):
    count_correct = 0
    while count_correct != ROUNDS:
        start = random.randint(0, 100)
        step = random.randint(0, 20)
        print("Question:", end=' ')
        correct_answer = print_ap(start, step)
        input_msg = input("Your answer: ")
        try:
            answer = int(input_msg)
        except ValueError:
            try_again_msg(input_msg, correct_answer, name)
            break
        if correct_answer == answer:
            count_correct += 1
            brain_games.cli.congrats(name)
        else:
            try_again_msg(answer, correct_answer, name)
            break


def main():
    print("Welcome to the Brain Games")
    print("What number is missing in the progression?\n")
    name = brain_games.cli.run()
    play_progression(name)


if __name__ == '__main__':
    main()
