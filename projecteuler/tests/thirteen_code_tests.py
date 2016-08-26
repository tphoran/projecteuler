from unittest import TestCase

from projecteuler.thirteen_code import Thirteen


class TestThirteen(TestCase):

    def test_find_first_x_digits_in_a_number(self):
        list_of_numbers = [37107287533902102798797998220837590246510135740250,
                           46376937677490009712648124896970078050417018260538]
        number = 37107287533902102798797998220837590246510135740250
        first_x_digits = 10

        test_thirteen = Thirteen(list_of_numbers, first_x_digits)

        solution = test_thirteen.find_first_x_digits_in_a_number(number, first_x_digits)
        expected_solution = 3710728753
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        list_of_numbers = [2345,
                           1205]
        first_x_digits = 3

        test_thirteen = Thirteen(list_of_numbers, first_x_digits)

        solution = test_thirteen.solve()
        expected_solution = 355
        self.assertEqual(solution, expected_solution)


