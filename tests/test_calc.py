import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()
    def test_it_makes_a_calculator(self):
        self.assertIsInstance(self.c, Calculator)

    def test_it_adds_two_plus_two(self):
        c = Calculator()
        r = c.evaluate('2 + 2')
        self.assertEqual(r, 4)

    def test_it_does_divides_and_add(self):
        r = self.c.evaluate('2 / 2 + 2')
        self.assertEqual(r, 3)

    def test_it_does_divides_and_multi_and_add(self):
        r = self.c.evaluate('2 / 2 * 2 + 10')
        self.assertEqual(r, 12)

    def test_it_does_add_then_divide(self):
        r = self.c.evaluate('2 + 2 / 2')
        self.assertEqual(r, 3)

    def test_it_handles_parents(self):
        r = self.c.evaluate('( 2 + 2 ) * 2 + 10')
        self.assertEqual(r, 18)

    def test_it_recoginizes_numbers(self):
        r = self.c.isOperand('99')
        self.assertEqual(r, True)
        r = self.c.isOperand('+')
        self.assertEqual(r, False)

    def test_it_recoginizes_numbers(self):
        r = self.c.isOperand('99')
        self.assertEqual(r, True)
        r = self.c.isOperand('+')
        self.assertEqual(r, False)

    def test_it_can_determine_precedence(self):
        r = self.c.precedence('/')
        self.assertEqual(r, 2)
