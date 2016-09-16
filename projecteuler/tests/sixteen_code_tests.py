from unittest import TestCase

from projecteuler.sixteen_code import Sixteen


class TestSixteen(TestCase):

    def test_sum_of_digits_2_to_x_power(self):
        power = 15

        test_sixteen = Sixteen(power)

        solution = test_sixteen.sum_of_digits_2_to_x_power(power)
        expected_solution = 26
        self.assertEqual(solution, expected_solution)