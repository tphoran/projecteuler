from unittest import TestCase

from projecteuler.fourteen_code import Fourteen


class TestFourteen(TestCase):

    def test_generate_collatz_sequence(self):
        max_starting_number = 13
        starting_number = 13

        test_fourteen = Fourteen(max_starting_number)

        solution = test_fourteen.generate_collatz_sequence(starting_number)
        expected_solution = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        max_starting_number = 13

        test_fourteen = Fourteen(max_starting_number)

        solution = test_fourteen.solve()
        expected_solution = 9
        self.assertEqual(solution, expected_solution)