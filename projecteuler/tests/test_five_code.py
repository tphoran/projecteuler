import pytest
from projecteuler.five_code import Five


def test_smallest_multiple_of_sequence():
    sequence = range(1, 11)

    test_five = Five(sequence)

    solution = test_five.solve()
    expected_solution = 2520

    assert solution == expected_solution
