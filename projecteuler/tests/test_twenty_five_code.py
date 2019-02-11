import pytest
from projecteuler.twenty_five_code import TwentyFive


def test_output_fib_n():
    max_digits = 3
    n = 5

    test_twenty_five = TwentyFive(max_digits)

    solution = test_twenty_five.output_fib_n(n)
    expected_solution = 5
    assert solution == expected_solution


def test_solve():
    max_digits = 3

    test_twenty_five = TwentyFive(max_digits)

    solution = test_twenty_five.solve()
    expected_solution = 12
    assert solution == expected_solution
