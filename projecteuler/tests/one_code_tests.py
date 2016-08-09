from unittest import TestCase

from expects import *

from euler.one_code import One


class TestOne(TestCase):
    def test_multiple_of_x_True(self):
        x = [3, 5]
        less_than_number = 15

        test_one = One(x, less_than_number)

        solution = test_one.solve()
        expected_solution = 45

        expect(solution).to(equal(expected_solution))
