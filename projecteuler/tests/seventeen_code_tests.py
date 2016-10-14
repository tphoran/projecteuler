from unittest import TestCase

from projecteuler.seventeen_code import Seventeen


class TestSeventeen(TestCase):

    def test_write_given_number_5(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(5)
        expected_solution = 'five'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_15(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(15)
        expected_solution = 'fifteen'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_30(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(30)
        expected_solution = 'thirty'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_27(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(27)
        expected_solution = 'twentyseven'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_500(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(500)
        expected_solution = 'fivehundred'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_105(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(105)
        expected_solution = 'onehundredandfive'
        self.assertEqual(solution, expected_solution)


    def test_write_given_number_115(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(115)
        expected_solution = 'onehundredandfifteen'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_920(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(920)
        expected_solution = 'ninehundredandtwenty'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_342(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(342)
        expected_solution = 'threehundredandfortytwo'
        self.assertEqual(solution, expected_solution)

    def test_write_given_number_1000(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)

        solution = test_seventeen.write_given_number(1000)
        expected_solution = 'onethousand'
        self.assertEqual(solution, expected_solution)

    def test_create_giant_string_of_number_words(self):
        max_number = 1000

        test_seventeen = Seventeen(max_number)
        solution = test_seventeen.create_string_of_number_words(5)
        expected_solution = 'onetwothreefourfive'
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        max_number = 5

        test_seventeen = Seventeen(max_number)
        solution = test_seventeen.solve()
        expected_solution = 19
        self.assertEqual(solution, expected_solution)

