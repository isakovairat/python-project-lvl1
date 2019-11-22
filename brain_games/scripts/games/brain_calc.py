import brain_games.cli
import random

ROUNDS = 3


def is_correct_input(input_msg):
    return type(input_msg) == int


def get_operation():
    operations = ["+", "-", "*"]
    return random.choice(operations)


def get_correct_answer(numb1, numb2, operation):
    if operation == "*":
        return numb1 * numb2
    elif operation == "+":
        return numb1 + numb2
    elif operation == "-":
        return numb1 - numb2


def try_again_msg(answer, correct_answer, name):
    print("\'{}\' is wrong answer ;(. ".format(answer), end="")
    print("Correct answer was \'{}\'.".format(correct_answer))
    brain_games.cli.try_again(name)


def calc(name):
    count_correct = 0
    while count_correct != ROUNDS:
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)
        operation = get_operation()
        correct_answer = get_correct_answer(number1, number2, operation)
        print("Question: {} {} {}".format(number1, operation, number2))
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
    print("What is the result of the expression?\n")
    name = brain_games.cli.run()
    calc(name)


if __name__ == '__main__':
    main()
