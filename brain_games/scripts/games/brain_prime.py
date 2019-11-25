import brain_games.cli
import random


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def opposite_answer(answer):
    if answer == "yes":
        return "no"
    return "yes"


def try_again_msg(answer, correct_answer, name):
    print("\'{}\' is wrong answer ;(. ".format(answer), end="")
    print("Correct answer was \'{}\'.".format(correct_answer))
    brain_games.cli.try_again(name)


def play_prime(name):
    count_correct = 0
    while count_correct != brain_games.cli.ROUNDS:
        random_number = random.randint(0, 1000)
        print("Question: {}".format(random_number))
        input_msg = input("Your answer: ")
        if is_prime(random_number) and input_msg == "yes":
            count_correct += 1
            brain_games.cli.congrats(name)
        elif not is_prime(random_number) and input_msg == "no":
            count_correct += 1
            brain_games.cli.congrats(name)
        else:
            try_again_msg(input_msg, opposite_answer(input_msg), name)
            break


def main():
    brain_games.cli.welcome()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    print()
    name = brain_games.cli.run()
    play_prime(name)
