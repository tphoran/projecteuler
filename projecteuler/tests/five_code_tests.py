from unittest import TestCase

from projecteuler.five_code import Five


class TestFive(TestCase):
    def test_smallest_multiple_of_sequence(self):
        sequence = range(1,11)

        test_five = Five(sequence)

        solution = test_five.solve()
        expected_solution = 2520

        self.assertEqual(solution, expected_solution)