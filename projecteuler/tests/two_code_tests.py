from unittest import TestCase

from expects import *

from euler.two_code import Two


class TestTwo(TestCase):
    def test_fib_sum_of_even(self):
        less_than_number = 35

        test_two = Two(less_than_number)

        solution = test_two.solve()
        expected_solution = 44

        expect(solution).to(equal(expected_solution))

