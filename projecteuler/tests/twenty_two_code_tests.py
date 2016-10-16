from unittest import TestCase

from projecteuler.twenty_two_code import TwentyTwo

class TestTwentyTwo(TestCase):

    def test_letter_dictionary_accuracy_A(self):
        data_location = '/Users/tphoran/GitHub/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

        test_twenty_two = TwentyTwo(data_location)

        solution = test_twenty_two.letter_values['A']
        expected_solution = 1
        self.assertEqual(solution, expected_solution)

    def test_letter_dictionary_accuracy_C(self):
        data_location = '/Users/tphoran/GitHub/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

        test_twenty_two = TwentyTwo(data_location)

        solution = test_twenty_two.letter_values['C']
        expected_solution = 3
        self.assertEqual(solution, expected_solution)

    def test_import_data_and_sort_alphabetically(self):
        data_location = '/Users/tphoran/GitHub/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

        test_twenty_two = TwentyTwo(data_location)

        solution = test_twenty_two.import_data_and_sort_alphabetically(data_location)
        expected_solution = ["ALICE", "SAM", "TIM"]
        self.assertEqual(solution, expected_solution)

    def test_calculate_name_score(self):
        data_location = '/Users/tphoran/GitHub/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

        test_twenty_two = TwentyTwo(data_location)

        solution = test_twenty_two.calculate_name_score('COLIN', 938)
        expected_solution = 49714
        self.assertEqual(solution, expected_solution)

    def test_solve(self):
        data_location = '/Users/tphoran/GitHub/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

        test_twenty_two = TwentyTwo(data_location)

        solution = test_twenty_two.solve()
        expected_solution = 222
        self.assertEqual(solution, expected_solution)
