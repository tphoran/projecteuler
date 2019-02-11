import pytest
from projecteuler.three_code import Three


def test_greatest_prime_factor():
    input_number = 13195

    test_three = Three(input_number)

    solution = test_three.solve()
    expected_solution = 29

    assert solution == expected_solution
