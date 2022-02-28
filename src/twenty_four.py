from .utils.evaluator import Lexer, Interpreter
from random import randint

class TwentyFour():
    """
    Implementation of 24-game.
    Game can be started by calling play_game().
    """

    def __init__(self):
        self.user_input = []
        self.numbers = []
        self.interpreter = Interpreter()

    def generate_numbers(self):
        self.numbers = [randint(1, 9) for x in range(0, 4)]

    def request_input(self):
        self.generate_numbers()
        num_str = "\n" + "solve: " + " ".join(map(str, self.numbers)) + "\n"
        self.user_input = input(num_str)

    def check_valid_input(self):
        lexer = Lexer()
        tokens = lexer.create_token_list(self.user_input)
        user_numbers =  [x['NUMBER'] for x in tokens if list(x.keys()) == ['NUMBER']]
        user_numbers.sort()
        self.numbers.sort()

        isFourNumbers = len(user_numbers) == len(self.numbers)
        isCorrectNumbers = user_numbers == self.numbers

        return isFourNumbers & isCorrectNumbers

    def solve_equation(self):
        return self.interpreter.evaluate(self.user_input)

    def play_game(self):
        self.request_input()

        isValidInput = self.check_valid_input()
        if isValidInput:
            result = self.solve_equation()

            if result == 24:
                print("That is Correct!\n")
            else:
                print("No this is {}...\n".format(result))
        else:
            print("Sorry, this is not a valid expression.\n")
