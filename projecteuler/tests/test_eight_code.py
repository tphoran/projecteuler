import pytest
from projecteuler.eight_code import Eight


def test_highest_factor_x_long():
    x_long = 4
    input_number = str()
    with open('/Users/tphoran/github/projecteuler/projecteuler/eight_input_number.txt') as input_file:
        for line in input_file:
            input_number += line

    test_eight = Eight(input_number, x_long)

    solution = test_eight.solve()
    expected_solution = 5832

    assert solution == expected_solution
