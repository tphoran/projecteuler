import pytest
from projecteuler.two_code import Two


def test_fib_sum_of_even():
    less_than_number = 35

    test_two = Two(less_than_number)

    solution = test_two.solve()
    expected_solution = 44

    assert solution == expected_solution
