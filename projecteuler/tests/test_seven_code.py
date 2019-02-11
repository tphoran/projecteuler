import pytest
from projecteuler.seven_code import Seven


def test_prime_number_sieve_ith_in_list():
    ith_prime_number = 6

    test_seven = Seven(ith_prime_number)

    solution = test_seven.solve()
    expected_solution = 13

    assert solution == expected_solution
