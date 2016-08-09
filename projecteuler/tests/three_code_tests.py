from unittest import TestCase

from expects import *

from euler.three_code import Three


class TestThree(TestCase):
    def test_greatest_prime_factor(self):
        input_number = 13195

        test_three = Three(input_number)

        solution = test_three.solve()
        expected_solution = 29

        expect(solution).to(equal(expected_solution))
