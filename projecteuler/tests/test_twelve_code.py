import pytest
from projecteuler.twelve_code import Twelve


def test_find_nth_triangle_number():
    target_number_of_divisors = 6
    nth = 7

    test_twelve = Twelve(target_number_of_divisors)

    solution = test_twelve.find_nth_triangle_number(nth)
    expected_solution = 28
    assert solution == expected_solution


def test_find_number_of_factors():
    target_number_of_divisors = 6
    number_to_factor = 28

    test_twelve = Twelve(target_number_of_divisors)

    solution = test_twelve.find_number_of_factors(number_to_factor)
    expected_solution = 6
    assert solution == expected_solution


def test_solve():
    target_number_of_divisors = 6

    test_twelve = Twelve(target_number_of_divisors)

    solution = test_twelve.solve()
    expected_solution = 28
    assert solution == expected_solution
