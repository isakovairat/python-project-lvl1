import prompt


def greet(name):
    print("Hello, {}!\n".format(name))


def congrats(name):
    print("Congratulations, {}!".format(name))


def try_again(name):
    print("Let's try again, {}!".format(name))


def run():
    name = prompt.string("May I have your name? ")
    greet(name)
    return name
