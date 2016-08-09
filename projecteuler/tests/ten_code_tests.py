from unittest import TestCase

from projecteuler.ten_code import Ten


class TestTen(TestCase):
    def test_prime_number_sieve_sum_of_all_primes_under_a_set_number(self):
        primes_below_number = 8

        test_ten = Ten(primes_below_number)

        solution = test_ten.solve()
        expected_solution = 17

        self.assertEqual(solution, expected_solution)