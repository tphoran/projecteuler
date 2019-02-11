import pytest
from projecteuler.twenty_one_code import TwentyOne


def test_find_proper_divisors_of_number():
    max_number = 10000

    test_twentyone = TwentyOne(max_number)

    solution = test_twentyone.find_proper_divisors_of_number(220)
    expected_solution = 284
    assert solution == expected_solution


def test_capture_amiable_numbers_between_range():
    max_number = 10000

    test_twentyone = TwentyOne(max_number)

    solution = test_twentyone.capture_amiable_numbers_between_range(219, 284)
    expected_solution = [284, 220]
    assert solution == expected_solution


def test_solve():
    max_number = 284

    test_twentyone = TwentyOne(max_number)

    solution = test_twentyone.solve()
    expected_solution = 284+220
    assert solution == expected_solution
