import pytest
from projecteuler.fourteen_code import Fourteen


def test_generate_collatz_sequence():
    max_starting_number = 13
    starting_number = 13

    test_fourteen = Fourteen(max_starting_number)

    solution = test_fourteen.generate_collatz_sequence(starting_number)
    expected_solution = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert solution == expected_solution


def test_solve():
    max_starting_number = 13

    test_fourteen = Fourteen(max_starting_number)

    solution = test_fourteen.solve()
    expected_solution = 9
    assert solution == expected_solution
