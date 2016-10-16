from unittest import TestCase

from projecteuler.twenty_code import Twenty


class TestTwenty(TestCase):

    def test_calculate_factorial(self):
        input_number = 10

        test_twenty = Twenty(input_number)

        solution = test_twenty.calculate_factorial(input_number)
        expected_solution = 3628800
        self.assertEqual(solution, expected_solution)

    def test_sum_of_digits_in_number(self):
        input_number = 10
        number_to_add_digits = 3628800

        test_twenty = Twenty(input_number)

        solution = test_twenty.sum_of_digits_in_number(number_to_add_digits)
        expected_solution = 27
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        input_number = 10

        test_twenty = Twenty(input_number)

        solution = test_twenty.solve()
        expected_solution = 27
        self.assertEqual(solution, expected_solution)


