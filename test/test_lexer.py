import unittest
from src.utils.evaluator import Lexer

class TestLexer(unittest.TestCase):
    def test_singleInput(self):
        lexer = Lexer()

        input = '0'
        out_expected = [{'NUMBER': 0}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '-'
        out_expected = [{'MINUS': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '+'
        out_expected = [{'PLUS': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '*'
        out_expected = [{'MULTIPLY': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '/'
        out_expected = [{'DIVIDE': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '('
        out_expected = [{'LPARA': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = ')'
        out_expected = [{'RPARA': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)
    
    def test_simpleExpressions(self):
        lexer = Lexer()

        input = '0 + 9'
        out_expected = [{'NUMBER': 0}, {'PLUS': ''}, {'NUMBER': 9}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '1 / 6'
        out_expected = [{'NUMBER': 1}, {'DIVIDE': ''}, {'NUMBER': 6}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '4 - 2'
        out_expected = [{'NUMBER': 4}, {'MINUS': ''}, {'NUMBER': 2}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '9 * 3'
        out_expected = [{'NUMBER': 9}, {'MULTIPLY': ''}, {'NUMBER': 3}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        # Check handling of missing whitespaces
        input = '9*3'
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

    def test_expressionsWithPara(self):
        lexer = Lexer()

        input = '9 * (3 + 4)'
        out_expected = [{'NUMBER': 9}, {'MULTIPLY': ''}, {'LPARA': ''}, {'NUMBER': 3}, {'PLUS': ''}, {'NUMBER': 4}, {'RPARA': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

        input = '9 / (3 + (4-3))'
        out_expected = [{'NUMBER': 9}, {'DIVIDE': ''}, {'LPARA': ''}, {'NUMBER': 3}, {'PLUS': ''}, {'LPARA': ''}, {'NUMBER': 4}, {'MINUS': ''}, {'NUMBER': 3}, {'RPARA': ''}, {'RPARA': ''}]
        out_actual = lexer.create_token_list(input)
        self.assertEqual(out_expected, out_actual)

    def test_invalidCharacter(self):
        lexer = Lexer()

        # Test exception for invalid character
        input = '9 = 4'
        self.assertRaises(Exception, lexer.create_token_list, input)

        # Test exception for empty string
        input = ''
        self.assertRaises(Exception, lexer.create_token_list, input)


if __name__ == '__main__':
    unittest.main()
    