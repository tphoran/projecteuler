from unittest import TestCase

from projecteuler.twentyone_code import Twentyone


class TestTwentyone(TestCase):

    def test_find_proper_divisors_of_number(self):
        max_number = 10000

        test_twentyone = Twentyone(max_number)

        solution = test_twentyone.find_proper_divisors_of_number(220)
        expected_solution = 284
        self.assertEqual(solution, expected_solution)

    def test_capture_amiable_numbers_between_range(self):
        max_number = 10000

        test_twentyone = Twentyone(max_number)

        solution = test_twentyone.capture_amiable_numbers_between_range(219, 284)
        expected_solution = [284, 220]
        self.assertEqual(expected_solution, solution)

    def test_solve(self):
        max_number = 284

        test_twentyone = Twentyone(max_number)

        solution = test_twentyone.solve()
        expected_solution = 284+220
        self.assertEqual(solution, expected_solution)

