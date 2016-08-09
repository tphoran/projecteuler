from unittest import TestCase

import numpy as np

from projecteuler.eleven_code import Eleven


class TestEleven(TestCase):
    def test_highest_product_of_x_adjacent_numbers_within_matrix_vertical(self):
        adjacent_number_count = 3

        test_matrix = np.matrix('0 1 2 3; 0 1 2 3; 0 1 2 3; 0 1 2 3')

        test_eleven = Eleven(adjacent_number_count, test_matrix)

        solution = test_eleven.solve()
        expected_solution = 27

        self.assertEqual(solution, expected_solution)

    def test_highest_product_of_x_adjacent_numbers_within_matrix_horizontal(self):
        adjacent_number_count = 3

        test_matrix = np.matrix('0 0 0 0; 1 1 1 1; 2 2 2 2; 3 3 3 3')

        test_eleven = Eleven(adjacent_number_count, test_matrix)

        solution = test_eleven.solve()
        expected_solution = 27

        self.assertEqual(solution, expected_solution)

    def test_highest_product_of_x_adjacent_numbers_within_matrix_diagonally(self):
        adjacent_number_count = 3

        test_matrix = np.matrix('0 0 0 1; 0 0 1 0; 0 1 0 0; 1 0 0 0')

        test_eleven = Eleven(adjacent_number_count, test_matrix)

        solution = test_eleven.solve()
        expected_solution = 1

        self.assertEqual(solution, expected_solution)