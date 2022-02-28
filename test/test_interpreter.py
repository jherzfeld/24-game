import unittest
from src.utils.evaluator import Interpreter

class TestInterpreter(unittest.TestCase):
    def test_expressionInterpretation(self):
        interpreter = Interpreter()

        input = '0'
        out_expected = 0
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)

    def test_simpleExpressions(self):
        interpreter = Interpreter()
        input = '1 + 9'
        out_expected = 10
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)

        input = '15 - 3'
        out_expected = 12
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)

        input = '2 * 3'
        out_expected = 6
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)

        input = '1 / 5'
        out_expected = 0.2
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)


    def test_priotitizedOperations(self):
        interpreter = Interpreter()
        
        input = '(1 + 3)*5'
        out_expected = 20
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)

        input = '4/(1 + 3)'
        out_expected = 1
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)

    def test_multipleParathesis(self):
        interpreter = Interpreter()
        
        input = '((-1) + 3)*5'
        out_expected = 10
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)

        input = '((4+2)-1)/(2 + 8)'
        out_expected = 0.5
        out_actual = interpreter.evaluate(input)
        self.assertEqual(out_expected, out_actual)


if __name__ == '__main__':
    unittest.main()
    