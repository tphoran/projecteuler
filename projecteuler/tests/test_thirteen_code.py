import pytest
from projecteuler.thirteen_code import Thirteen


def test_find_first_x_digits_in_a_number():
    list_of_numbers = [37107287533902102798797998220837590246510135740250,
                       46376937677490009712648124896970078050417018260538]
    number = 37107287533902102798797998220837590246510135740250
    first_x_digits = 10

    test_thirteen = Thirteen(list_of_numbers, first_x_digits)

    solution = test_thirteen.find_first_x_digits_in_a_number(number, first_x_digits)
    expected_solution = 3710728753
    assert solution == expected_solution


def test_solve():
    list_of_numbers = [2345, 1205]
    first_x_digits = 3

    test_thirteen = Thirteen(list_of_numbers, first_x_digits)

    solution = test_thirteen.solve()
    expected_solution = 355
    assert solution == expected_solution
