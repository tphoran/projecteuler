import pytest
from projecteuler.nineteen_code import Nineteen
from datetime import date


def test_date_is_a_sunday_True():
    starting_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)

    test_nineteen = Nineteen(starting_date, end_date)

    solution = test_nineteen.date_is_a_sunday(date(2016, 10, 16))
    expected_solution = True
    assert solution == expected_solution


def test_date_is_a_sunday_False():
    starting_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)

    test_nineteen = Nineteen(starting_date, end_date)

    solution = test_nineteen.date_is_a_sunday(date(2016, 10, 17))
    expected_solution = False
    assert solution == expected_solution


def test_date_is_first_of_the_month_True():
    starting_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)

    test_nineteen = Nineteen(starting_date, end_date)

    solution = test_nineteen.date_is_first_of_the_month(date(2016, 11, 1))
    expected_solution = True
    assert solution == expected_solution


def test_date_is_first_of_the_month_False():
    starting_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)

    test_nineteen = Nineteen(starting_date, end_date)

    solution = test_nineteen.date_is_first_of_the_month(date(2016, 11, 2))
    expected_solution = False
    assert solution == expected_solution


def test_collect_sundays_that_are_first_of_month():
    starting_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)

    test_nineteen = Nineteen(starting_date, end_date)

    solution = test_nineteen.collect_sundays_that_are_first_of_month(date(2016, 1, 1),
                                                                         date(2016, 6, 30))
    expected_solution = 1
    assert solution == expected_solution
