import pytest
from projecteuler.four_code import Four


def test_palindrome_x_digits():
    digits = 2

    test_four = Four(digits)

    solution = test_four.solve()
    expected_solution = 9009

    assert solution == expected_solution
