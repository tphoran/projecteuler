from unittest import TestCase

from projecteuler.six_code import Six


class TestSix(TestCase):
    def test_list_of_numbers_squared_and_summed(self):
        sequence = range(1, 11)

        test_six = Six(sequence)

        solution = test_six.list_of_number_squared_and_summed(sequence)
        expected_solution = 385

        self.assertEqual(solution, expected_solution)

    def test_list_of_numbers_summed_and_squared(self):
        sequence = range(1, 11)

        test_six = Six(sequence)

        solution = test_six.list_of_numbers_summed_and_squared(sequence)
        expected_solution = 3025

        self.assertEqual(solution, expected_solution)

    def test_difference_squared_and_summed_and_summed_and_squared(self):
        sequence = range(1, 11)

        test_six = Six(sequence)

        solution = test_six.solve()
        expected_solution = 2640

        self.assertEqual(solution, expected_solution)