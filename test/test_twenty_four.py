import unittest
from src.twenty_four import TwentyFour

class TestClass(unittest.TestCase):
    def test_validInput(self):
        game = TwentyFour()

        # Valid input
        game.numbers = [1, 3, 5, 6]
        game.user_input = '1 + 3 - (5 + 6)'
        output = game.check_valid_input()
        self.assertTrue(output)

        # Too few numbers
        game.user_input = '1 + 3 - (5)'
        output = game.check_valid_input()
        self.assertFalse(output)

        # Too many numbers
        game.user_input = '1 + 3 - (5 + 6)*1'
        output = game.check_valid_input()
        self.assertFalse(output)

         # Wrong numbers
        game.user_input = '1 + 2 - (5 + 6)'
        output = game.check_valid_input()
        self.assertFalse(output)

    def test_generateNumbers(self):
        game = TwentyFour()

        for i in range(50):
            game.generate_numbers()
            valid_numbers = sum([1 for x in game.numbers if x in range(1,10)])
            self.assertTrue(valid_numbers == 4)
