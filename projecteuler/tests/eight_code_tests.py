from unittest import TestCase

from projecteuler.eight_code import Eight


class TestEight(TestCase):

    def test_highest_factor_x_long(self):
        x_long = 4
        input_number = str()
        with open('/Users/uec561/GitHub/projecteuler/projecteuler/eight_input_number.txt') as input_file:
            for line in input_file:
                input_number += line

        test_eight = Eight(input_number, x_long)

        solution = test_eight.solve()
        expected_solution = 5832

        self.assertEqual(solution, expected_solution)
