from unittest import TestCase

from projecteuler.twenty_five_code import TwentyFive


class TestTwentyFive(TestCase):

    def test_output_fib_n(self):
        max_digits = 3
        n = 5

        test_twenty_five = TwentyFive(max_digits)

        solution = test_twenty_five.output_fib_n(n)
        expected_solution = 5
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        max_digits = 3

        test_twenty_five = TwentyFive(max_digits)

        solution = test_twenty_five.solve()
        expected_solution = 12
        self.assertEqual(solution, expected_solution)