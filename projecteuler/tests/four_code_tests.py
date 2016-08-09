from unittest import TestCase

from projecteuler.four_code import Four


class TestFour(TestCase):
    def test_palindrome_x_digits(self):
        digits = 2

        test_four = Four(digits)

        solution = test_four.solve()
        expected_solution = 9009

        self.assertEqual(solution, expected_solution)