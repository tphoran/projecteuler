import pytest
from projecteuler.seventeen_code import Seventeen


def test_write_given_number_5():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(5)
    expected_solution = 'five'
    assert solution == expected_solution


def test_write_given_number_15():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(15)
    expected_solution = 'fifteen'
    assert solution == expected_solution


def test_write_given_number_30():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(30)
    expected_solution = 'thirty'
    assert solution == expected_solution


def test_write_given_number_27():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(27)
    expected_solution = 'twentyseven'
    assert solution == expected_solution


def test_write_given_number_500():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(500)
    expected_solution = 'fivehundred'
    assert solution == expected_solution


def test_write_given_number_105():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(105)
    expected_solution = 'onehundredandfive'
    assert solution == expected_solution


def test_write_given_number_115():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(115)
    expected_solution = 'onehundredandfifteen'
    assert solution == expected_solution


def test_write_given_number_920():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(920)
    expected_solution = 'ninehundredandtwenty'
    assert solution == expected_solution


def test_write_given_number_342():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(342)
    expected_solution = 'threehundredandfortytwo'
    assert solution == expected_solution


def test_write_given_number_1000():
    max_number = 1000

    test_seventeen = Seventeen(max_number)

    solution = test_seventeen.write_given_number(1000)
    expected_solution = 'onethousand'
    assert solution == expected_solution


def test_create_giant_string_of_number_words():
    max_number = 1000

    test_seventeen = Seventeen(max_number)
    solution = test_seventeen.create_string_of_number_words(5)
    expected_solution = 'onetwothreefourfive'
    assert solution == expected_solution


def test_solve():
    max_number = 5

    test_seventeen = Seventeen(max_number)
    solution = test_seventeen.solve()
    expected_solution = 19
    assert solution == expected_solution
