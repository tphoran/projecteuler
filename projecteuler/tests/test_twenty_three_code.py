import pytest
from projecteuler.twenty_three_code import TwentyThree


def test_find_proper_divisors_of_number():
    max_number = 28124

    test_twenty_three = TwentyThree(max_number)

    solution = test_twenty_three.find_proper_divisors_of_number(220)
    expected_solution = 284
    assert solution == expected_solution


def test_number_is_abundant_number_T():
    max_number = 28124

    test_twenty_three = TwentyThree(max_number)

    solution = test_twenty_three.number_is_abundant_number(12)
    expected_solution = True
    assert solution == expected_solution


def test_number_is_abundant_number_F():
    max_number = 28124

    test_twenty_three = TwentyThree(max_number)

    solution = test_twenty_three.number_is_abundant_number(11)
    expected_solution = False
    assert solution == expected_solution


def test_find_list_of_abundant_numbers_between_a_range():
    max_number = 28124

    test_twenty_three = TwentyThree(max_number)

    solution = test_twenty_three.find_list_of_abundant_numbers_between_a_range(12, 13)
    expected_solution = [12]
    assert solution == expected_solution


def test_find_list_of_all_numbers_that_can_be_sum_of_item_from_2_lists():
    max_number = 28124
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]

    test_twenty_three = TwentyThree(max_number)

    solution = test_twenty_three.find_list_of_all_numbers_that_can_be_sum_of_item_from_2_lists(list1, list2)
    expected_solution = [2, 3, 4, 5, 6]
    assert solution == expected_solution


def test_return_sum_of_numbers_in_range_not_in_a_given_list():
    max_number = 28124

    test_twenty_three = TwentyThree(max_number)

    solution = test_twenty_three.return_sum_of_numbers_in_range_not_in_a_given_list(6, [1, 4, 5])
    expected_solution = sum([2, 3])
    assert solution == expected_solution


def test_solve():
    max_number = 25

    test_twenty_three = TwentyThree(max_number)

    solution = test_twenty_three.solve()
    expected_solution = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                             20, 21, 22, 23])
    assert solution == expected_solution
