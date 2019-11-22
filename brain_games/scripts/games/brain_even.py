import brain_games.cli
import random

ROUNDS = 3


def is_even(number):
    return number % 2 == 0


def opposite_answer(answer):
    if answer == "yes":
        return "no"
    else:
        return "yes"


def questions(name):
    count_correct = 0
    while count_correct != ROUNDS:
        number = random.randint(0, 100)
        print("Question: {}".format(number))
        answer = input("Your answer: ")
        if answer == "yes" and is_even(number):
            print("Correct!")
            count_correct += 1
        elif answer == "no" and not is_even(number):
            print("Correct!")
            count_correct += 1
        else:
            print("\"{}\" is wrong answer ;(. ".format(answer), end="")
            print("Correct answer was \"{}\"".format(opposite_answer(answer)))
            brain_games.cli.try_again(name)
            break
        if count_correct == 3:
            brain_games.cli.congrats(name)


def main():
    print("Welcome to the Brain Games")
    print("Answer \"yes\" if number even otherwise answer \"no\".\n")
    name = brain_games.cli.run()
    questions(name)


if __name__ == '__main__':
    main()
