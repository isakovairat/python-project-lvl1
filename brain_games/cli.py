import prompt


def greet(name):
    print("Hello, {}!".format(name))


def run():
    print("Welcome to the Brain Games\n")
    name = prompt.string("May I have your name? ")
    greet(name)
