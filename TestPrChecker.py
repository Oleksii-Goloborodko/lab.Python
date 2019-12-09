import unittest

from rpn.checkers import Checkers
from rpn.converter import Converter
from rpn.evaluetor import Actions
from rpn.helpers import Operators
from rpn.rpn import Rpn


class TestPrChecker(unittest.TestCase):

    def test_pr_should_return_true(self):
        valid_pr = ['()', '([])']
        for vp in valid_pr:
            self.assertTrue(Checkers.check_pr(vp))

    def test_pr_should_return_false(self):
        invalid_pr = ['(', '([)']
        for ip in invalid_pr:
            self.assertFalse(Checkers.check_pr(ip))

class TestConverter(unittest.TestCase):

    def test_toPostfix_should_return_list(self):
        self.assertListEqual(Converter.toPostfix("(2+4)*6"),['2', '4', '+', '6', '*'])

class TestActions(unittest.TestCase):

    def test_add_should_return_sum(self):
        self.assertLessEqual(Actions.add(2,5),7)

    def test_minus_should_return_odd(self):
        self.assertLessEqual(Actions.minus(6,100),94)

    def test_multiply_should_return_multiply(self):
        self.assertLessEqual(Actions.multiply(124,456),56544)

    def test_division_should_return_division_of_float(self):
        self.assertLessEqual(Actions.division(5,25.56), 5.112)

    def test_power_should_return_power(self):
        self.assertLessEqual(Actions.power(5,12),248832)

    def test_dot_float_should_return_float(self):
        self.assertLessEqual(Actions.dot_float(234,678),678.234)

    def test_postixEval_should_return_result(self):
        self.assertLessEqual(Actions.postixEval(["2" , "4" , "+" , "6" ,"*"]), 36)

class TestRpn(unittest.TestCase):

    def test_rpn_should_return_result(self):
        self.assertLessEqual(Rpn.rpn("(2+4)*6", Converter.toPostfix, Actions.postixEval, Checkers.check_pr), 36)

class TestOperators(unittest.TestCase):

    def test_isNumberOperand_should_return_normal_numbers(self):
        self.assertLessEqual(Operators.isNumberOperand("3","34+",0),"34")

    def test_isOperand_should_return_false(self):
        self.assertFalse(Operators.isOperand(")"))

    def test_isOperand_should_return_true(self):
        self.assertTrue(Operators.isOperand("89"))

    def test_isLeftPaternthesis_should_return_false(self):
        self.assertFalse(Operators.isLeftParenthesis(")"))

    def test_isLeftPaternthesis_should_return_true(self):
        self.assertTrue(Operators.isLeftParenthesis("("))

    def test_isRightPatenthesis_should_return_false(self):
        self.assertFalse(Operators.isRightParenthesis("("))

    def test_isRightPatenthesis_should_return_true(self):
        self.assertTrue(Operators.isRightParenthesis(")"))

    def test_hasLessOrEqualPriority_should_return_false(self):
        self.assertFalse(Operators.hasLessOrEqualPriority(".","^"))

    def test_hasLessOrEqualPriority_should_return_true(self):
        self.assertTrue(Operators.hasLessOrEqualPriority("-","*"))

if __name__ == '__main__':
    unittest.main()