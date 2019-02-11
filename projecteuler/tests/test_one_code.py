import pytest
from projecteuler.one_code import One


def test_multiple_of_x_True():
    x = [3, 5]
    less_than_number = 15

    test_one = One(x, less_than_number)

    solution = test_one.solve()
    expected_solution = 45

    assert solution == expected_solution
