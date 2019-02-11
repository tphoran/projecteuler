import pytest
from numpy.testing import assert_equal
from projecteuler.eleven_code import Eleven

import numpy as np


def test_create_list_of_x_by_x_sized_matrixes_horizontal():
    adjacent_number_count = 3
    test_matrix = np.matrix('0 1 2 3 4 5; 0 1 2 3 4 5; 0 1 2 3 4 5')
    test_eleven = Eleven(adjacent_number_count, test_matrix)

    solution = test_eleven.create_list_of_x_by_x_sized_matrixes(adjacent_number_count, test_matrix)
    expected_solution = np.matrix('2 3 4; 2 3 4; 2 3 4')
    assert_equal(solution[2], expected_solution)

def test_create_list_of_x_by_x_sized_matrixes_vertical():
    adjacent_number_count = 3
    test_matrix = np.matrix('0 1 2 3 4 5; 0 1 2 3 4 5; 0 1 2 3 4 5; 0 1 2 3 4 5')
    test_eleven = Eleven(adjacent_number_count, test_matrix)

    solution = test_eleven.create_list_of_x_by_x_sized_matrixes(adjacent_number_count, test_matrix)
    expected_solution = np.matrix('1 2 3; 1 2 3; 1 2 3')
    assert_equal(solution[2], expected_solution)

def test_max_x_long_product_in_x_by_x_matrix_vertical():
    x_by_x = 4
    test_matrix = np.matrix('2 3 5 4; 2 3 5 4; 2 3 5 4; 2 3 5 4')
    test_eleven = Eleven(x_by_x, test_matrix)

    solution = test_eleven.max_x_long_product_in_x_by_x_matrix(x_by_x, test_matrix)

    expected_solution = 625
    assert solution == expected_solution

def test_max_x_long_product_in_x_by_x_matrix_horizontal():
    x_by_x = 4
    test_matrix = np.matrix('2 2 2 2; 3 3 3 3; 4 4 4 4; 5 5 5 5')
    test_eleven = Eleven(x_by_x, test_matrix)

    solution = test_eleven.max_x_long_product_in_x_by_x_matrix(x_by_x, test_matrix)

    expected_solution = 625
    assert solution == expected_solution

def test_max_x_long_product_in_x_by_x_matrix_topleft_to_bottomright():
    x_by_x = 4
    test_matrix = np.matrix('5 1 1 1; 1 5 1 1; 1 1 5 1; 1 1 1 3')
    test_eleven = Eleven(x_by_x, test_matrix)

    solution = test_eleven.max_x_long_product_in_x_by_x_matrix(x_by_x, test_matrix)

    expected_solution = 375
    assert solution == expected_solution

def test_max_x_long_product_in_x_by_x_matrix_topright_to_bottomleft():
    x_by_x = 4
    test_matrix = np.matrix('1 1 1 5; 1 1 5 1; 1 5 1 1; 3 1 1 1')
    test_eleven = Eleven(x_by_x, test_matrix)

    solution = test_eleven.max_x_long_product_in_x_by_x_matrix(x_by_x, test_matrix)

    expected_solution = 375
    assert solution == expected_solution

def test_solve():
    adjacent_number_count = 4
    test_matrix = np.matrix('1 2 3 4 5 6; 1 2 3 4 5 6; 1 2 3 4 5 6; 1 2 3 4 5 6; 1 2 3 4 5 6')

    test_eleven = Eleven(adjacent_number_count, test_matrix)

    solution = test_eleven.solve()

    expected_solution = 1296
    assert solution == expected_solution
