from unittest import TestCase

from projecteuler.eighteen_code import Eighteen


class TestEighteen(TestCase):

    def test_transform_string_to_list_of_integers(self):
        input_string = '3 7 4 2 4 6 08 5 9 03'

        test_eighteen = Eighteen(input_string)

        solution = test_eighteen.transform_string_to_list_of_integers(input_string)
        expected_solution = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
        self.assertEqual(solution, expected_solution)

    def test_setup_triangle(self):
        input_string = '3 7 4 2 4 6 8 5 9 3'

        test_eighteen = Eighteen(input_string)

        solution = test_eighteen.create_triangle_levels(input_string)
        expected_solution = [[3],
                             [7, 4],
                             [2, 4, 6],
                             [8, 5, 9, 3]]
        self.assertEqual(solution, expected_solution)

    def test_collect_best_possible_outcomes_from_two_levels_1(self):
        input_string = '3 7 4 2 4 6 8 5 9 3'

        test_eighteen = Eighteen(input_string)

        level_one = [7, 4]
        level_two = [2, 4, 6]

        solution = test_eighteen.collect_best_possible_outcomes_from_two_levels(level_one, level_two)
        expected_solution = [9, 11, 10]
        self.assertEqual(solution, expected_solution)

    def test_collect_best_possible_outcomes_from_two_levels_2(self):
        input_string = '3 7 4 2 4 6 8 5 9 3'

        test_eighteen = Eighteen(input_string)

        level_one = [9, 11, 10]
        level_two = [8, 5, 9, 3]

        solution = test_eighteen.collect_best_possible_outcomes_from_two_levels(level_one, level_two)
        expected_solution = [17, 16, 20, 13]
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        input_string = '3 7 4 2 4 6 8 5 9 3'

        test_eighteen = Eighteen(input_string)

        solution = test_eighteen.solve()
        expected_solution = 23
        self.assertEqual(solution, expected_solution)