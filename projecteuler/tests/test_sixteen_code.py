import pytest
from projecteuler.sixteen_code import Sixteen


def test_sum_of_digits_2_to_x_power():
    power = 15

    test_sixteen = Sixteen(power)

    solution = test_sixteen.sum_of_digits_2_to_x_power(power)
    expected_solution = 26
    assert solution == expected_solution
