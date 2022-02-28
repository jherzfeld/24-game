import unittest
from src.utils.evaluator import Parser

class TestParser(unittest.TestCase):
    def test_singleInput(self):
        parser = Parser()

        input = [{'NUMBER': 0}]
        out_expected = {'NUMBER': 0}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

    def test_simpleExpressions(self):
        parser = Parser()

        input = [{'NUMBER': 0}, {'PLUS': ''}, {'NUMBER': 9}]
        out_expected = {'ADD': [{'NUMBER': 0}, {'NUMBER': 9}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'NUMBER': 0}, {'PLUS': ''}, {'NUMBER': 9}]
        out_expected = {'ADD': [{'NUMBER': 0}, {'NUMBER': 9}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'NUMBER': 1}, {'DIVIDE': ''}, {'NUMBER': 6}]
        out_expected = {'DIVIDE': [{'NUMBER': 1}, {'NUMBER': 6}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'NUMBER': 4}, {'MINUS': ''}, {'NUMBER': 2}]
        out_expected = {'SUBTRACT': [{'NUMBER': 4}, {'NUMBER': 2}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'NUMBER': 9}, {'MULTIPLY': ''}, {'NUMBER': 3}]
        out_expected = {'MULTIPLY': [{'NUMBER': 9}, {'NUMBER': 3}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)


    def test_priotitizedOperations(self):
        parser = Parser()

        input = [{'NUMBER': 0}, {'PLUS': ''}, {'NUMBER': 9}, {'MULTIPLY': ''}, {'NUMBER': 2}]
        out_expected = {'ADD': [{'NUMBER': 0}, {'MULTIPLY': [{'NUMBER': 9}, {'NUMBER': 2}]}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'NUMBER': 0}, {'MINUS': ''}, {'NUMBER': 9}, {'DIVIDE': ''}, {'NUMBER': 2}]
        out_expected = {'SUBTRACT': [{'NUMBER': 0}, {'DIVIDE': [{'NUMBER': 9}, {'NUMBER': 2}]}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)


    def test_negativeNumbers(self):
        parser = Parser()

        input = [{'MINUS': ''}, {'NUMBER': 9}, {'PLUS': ''}, {'NUMBER': 2}]
        out_expected = {'ADD': [{'MULTIPLY': [{'NUMBER': -1}, {'NUMBER': 9}]}, {'NUMBER': 2}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'NUMBER': 8}, {'MULTIPLY': ''}, {'MINUS': ''}, {'NUMBER': 9}]
        out_expected = {'MULTIPLY': [{'NUMBER': 8}, {'MULTIPLY': [{'NUMBER': -1}, {'NUMBER': 9}]}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)


    def test_positiveNumbers(self):
        parser = Parser()

        input = [{'PLUS': ''}, {'NUMBER': 9}, {'PLUS': ''}, {'NUMBER': 2}]
        out_expected = {'ADD': [{'MULTIPLY': [{'NUMBER': 1}, {'NUMBER': 9}]}, {'NUMBER': 2}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'NUMBER': 8}, {'MULTIPLY': ''}, {'MINUS': ''}, {'MINUS': ''}, {'NUMBER': 9}]
        out_expected = {'MULTIPLY': [{'NUMBER': 8}, {'MULTIPLY': [{'NUMBER': -1}, {'MULTIPLY': [{'NUMBER': -1}, {'NUMBER': 9}]}]}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)


    def test_paranthesis(self):
        parser = Parser()

        input = [{'NUMBER': 9}, {'MULTIPLY': ''}, {'LPARA': ''}, {'NUMBER': 2}, {'PLUS': ''}, {'NUMBER': 5}, {'RPARA': ''}]
        out_expected = {'MULTIPLY': [{'NUMBER': 9}, {'ADD': [{'NUMBER': 2}, {'NUMBER': 5}]}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

        input = [{'LPARA': ''}, {'NUMBER': 2}, {'PLUS': ''}, {'NUMBER': 5}, {'RPARA': ''}]
        out_expected = {'ADD': [{'NUMBER': 2}, {'NUMBER': 5}]}
        out_actual = parser.parse(input)
        self.assertEqual(out_expected, out_actual)

    def test_exceptions(self):
        parser = Parser()

        # Test missing right paranthesis
        input = [{'LPARA': ''}, {'NUMBER': 2}, {'PLUS': ''}, {'NUMBER': 5}]
        self.assertRaises(Exception, parser.parse, input)

        # Test missing left paranthesis
        input = [{'NUMBER': 2}, {'PLUS': ''}, {'NUMBER': 5}, {'RPARA': ''}]
        self.assertRaises(Exception, parser.parse, input)

        # Test empty token list
        input = []
        self.assertRaises(Exception, parser.parse, input)

        # Test invalid token
        input = [{'INVALID': ''}]
        self.assertRaises(Exception, parser.parse, input)


if __name__ == '__main__':
    unittest.main()
    