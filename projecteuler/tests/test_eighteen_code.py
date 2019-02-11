import pytest
from projecteuler.eighteen_code import Eighteen


def test_transform_string_to_list_of_integers():
    input_string = '3 7 4 2 4 6 08 5 9 03'

    test_eighteen = Eighteen(input_string)

    solution = test_eighteen.transform_string_to_list_of_integers(input_string)
    expected_solution = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
    assert solution == expected_solution


def test_setup_triangle():
    input_string = '3 7 4 2 4 6 8 5 9 3'

    test_eighteen = Eighteen(input_string)

    solution = test_eighteen.create_triangle_levels(input_string)
    expected_solution = [[3],
                         [7, 4],
                         [2, 4, 6],
                         [8, 5, 9, 3]]
    assert solution == expected_solution


def test_collect_best_possible_outcomes_from_two_levels_1():
    input_string = '3 7 4 2 4 6 8 5 9 3'

    test_eighteen = Eighteen(input_string)

    level_one = [7, 4]
    level_two = [2, 4, 6]

    solution = test_eighteen.collect_best_possible_outcomes_from_two_levels(level_one, level_two)
    expected_solution = [9, 11, 10]
    assert solution == expected_solution


def test_collect_best_possible_outcomes_from_two_levels_2():
    input_string = '3 7 4 2 4 6 8 5 9 3'

    test_eighteen = Eighteen(input_string)

    level_one = [9, 11, 10]
    level_two = [8, 5, 9, 3]

    solution = test_eighteen.collect_best_possible_outcomes_from_two_levels(level_one, level_two)
    expected_solution = [17, 16, 20, 13]
    assert solution == expected_solution


def test_solve():
    input_string = '3 7 4 2 4 6 8 5 9 3'

    test_eighteen = Eighteen(input_string)

    solution = test_eighteen.solve()
    expected_solution = 23
    assert solution == expected_solution
