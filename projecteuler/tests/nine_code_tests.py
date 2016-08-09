from unittest import TestCase

from projecteuler.nine_code import Nine


class TestNine(TestCase):

    def test_pythagorean_triplet(self):
        a_true = 3
        b_true = 4
        a_false = 2
        b_false = 2

        test_nine = Nine(1000)

        solution_true = test_nine.pythaogrean_triplet_check(a_true, b_true)
        solution_false = test_nine.pythaogrean_triplet_check(a_false, b_false)

        expected_solution_true = True
        expected_solution_false = False

        self.assertEqual([solution_true, solution_false], [expected_solution_true, expected_solution_false])

    def test_collect_all_possible_sets_of_a_and_b(self):
        a_b_range = range(1,4)

        test_nine = Nine(1000)

        solution = test_nine.collect_all_possible_sets_of_a_and_b(a_b_range)

        expected_solution = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

        self.assertEqual(solution, expected_solution)

    def tests_calculate_c_given_a_and_b(self):
        a = 3
        b = 4

        test_nine = Nine(1000)

        solution = test_nine.calculate_c_given_a_and_b(a, b)

        expected_solution = 5

        self.assertEqual(solution, expected_solution)

    def tests_return_pythaogrean_triplet_that_meets_a_plus_b_plus_c_target(self):
        a_plus_b_plus_c_target = 12

        test_nine = Nine(a_plus_b_plus_c_target)

        solution = test_nine.solve()

        expected_solution = (3, 4, 5)

        self.assertEqual(solution, expected_solution)