from unittest import TestCase

from projecteuler.seven_code import Seven


class TestSeven(TestCase):
    def test_prime_number_sieve_ith_in_list(self):
        ith_prime_number = 6

        test_seven = Seven(ith_prime_number)

        solution = test_seven.solve()
        expected_solution = 13

        self.assertEqual(solution, expected_solution)