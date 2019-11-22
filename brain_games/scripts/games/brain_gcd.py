import brain_games.cli
import random
from math import gcd

ROUNDS = 3


def try_again_msg(answer, correct_answer, name):
    print("\'{}\' is wrong answer ;(. ".format(answer), end="")
    print("Correct answer was \'{}\'.".format(correct_answer))
    brain_games.cli.try_again(name)


def play_gcd(name):
    count_correct = 0
    while count_correct != ROUNDS:
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)
        correct_answer = gcd(number1, number2)
        print("Question: {} {}".format(number1, number2))
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
    print("Find the greatest common divisor of given numbers.\n")
    name = brain_games.cli.run()
    play_gcd(name)


if __name__ == '__main__':
    main()
