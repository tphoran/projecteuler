import pytest
from projecteuler.twenty_code import Twenty


def test_calculate_factorial():
    input_number = 10

    test_twenty = Twenty(input_number)

    solution = test_twenty.calculate_factorial(input_number)
    expected_solution = 3628800
    assert solution == expected_solution


def test_sum_of_digits_in_number():
    input_number = 10
    number_to_add_digits = 3628800

    test_twenty = Twenty(input_number)

    solution = test_twenty.sum_of_digits_in_number(number_to_add_digits)
    expected_solution = 27
    assert solution == expected_solution


def test_solve():
    input_number = 10

    test_twenty = Twenty(input_number)

    solution = test_twenty.solve()
    expected_solution = 27
    assert solution == expected_solution
