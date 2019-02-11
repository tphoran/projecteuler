import pytest
from projecteuler.twenty_four_code import TwentyFour


def test_permutation_iterator():
    list_numbers_for_permutation = [0, 1, 2]
    permutation_to_return = 5

    test_twenty_four = TwentyFour(list_numbers_for_permutation, permutation_to_return)

    solution_generator = test_twenty_four.permutation_iterator(list_numbers_for_permutation)
    solution_1 = next(solution_generator)
    solution_2 = next(solution_generator)
    solution_3 = next(solution_generator)
    expected_solution_1 = (0, 1, 2)
    expected_solution_2 = (0, 2, 1)
    expected_solution_3 = (1, 0, 2)
    assert solution_1 == expected_solution_1
    assert solution_2 == expected_solution_2
    assert solution_3 == expected_solution_3


def test_solve():
    list_numbers_for_permutation = [0, 1, 2]
    permutation_to_return = 5

    test_twenty_four = TwentyFour(list_numbers_for_permutation, permutation_to_return)

    solution = test_twenty_four.solve()
    expected_solution = (2, 0, 1)
    assert solution == expected_solution
