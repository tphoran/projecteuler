from unittest import TestCase

from projecteuler.twenty_three_code import TwentyThree


class TestTwentyThree(TestCase):

    def test_find_proper_divisors_of_number(self):
        max_number = 28124

        test_twenty_three = TwentyThree(max_number)

        solution = test_twenty_three.find_proper_divisors_of_number(220)
        expected_solution = 284
        self.assertEqual(solution, expected_solution)

    def test_number_is_abundant_number_T(self):
        max_number = 28124

        test_twenty_three = TwentyThree(max_number)

        solution = test_twenty_three.number_is_abundant_number(12)
        expected_solution = True
        self.assertEqual(solution, expected_solution)

    def test_number_is_abundant_number_F(self):
        max_number = 28124

        test_twenty_three = TwentyThree(max_number)

        solution = test_twenty_three.number_is_abundant_number(11)
        expected_solution = False
        self.assertEqual(solution, expected_solution)

    def test_find_list_of_abundant_numbers_between_a_range(self):
        max_number = 28124

        test_twenty_three = TwentyThree(max_number)

        solution = test_twenty_three.find_list_of_abundant_numbers_between_a_range(12, 13)
        expected_solution = [12]
        self.assertEqual(solution, expected_solution)

    def test_find_list_of_all_numbers_that_can_be_sum_of_item_from_2_lists(self):
        max_number = 28124
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]

        test_twenty_three = TwentyThree(max_number)

        solution = test_twenty_three.find_list_of_all_numbers_that_can_be_sum_of_item_from_2_lists(
            list1, list2)
        expected_solution = [2, 3, 4, 5, 6]
        self.assertEqual(solution, expected_solution)

    def test_return_sum_of_numbers_in_range_not_in_a_given_list(self):
        max_number = 28124

        test_twenty_three = TwentyThree(max_number)

        solution = test_twenty_three.return_sum_of_numbers_in_range_not_in_a_given_list(6,
                                                                                        [1, 4, 5])
        expected_solution = sum([2, 3])
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        max_number = 25

        test_twenty_three = TwentyThree(max_number)

        solution = test_twenty_three.solve()
        expected_solution = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                 20, 21, 22, 23])
        self.assertEqual(solution, expected_solution)


