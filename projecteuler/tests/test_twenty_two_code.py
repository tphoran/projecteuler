import pytest
from projecteuler.twenty_two_code import TwentyTwo


def test_letter_dictionary_accuracy_A():
    data_location = '/Users/tphoran/github/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

    test_twenty_two = TwentyTwo(data_location)

    solution = test_twenty_two.letter_values['A']
    expected_solution = 1
    assert solution == expected_solution


def test_letter_dictionary_accuracy_C():
    data_location = '/Users/tphoran/github/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

    test_twenty_two = TwentyTwo(data_location)

    solution = test_twenty_two.letter_values['C']
    expected_solution = 3
    assert solution == expected_solution


def test_import_data_and_sort_alphabetically():
    data_location = '/Users/tphoran/github/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

    test_twenty_two = TwentyTwo(data_location)

    solution = test_twenty_two.import_data_and_sort_alphabetically(data_location)
    expected_solution = ["ALICE", "SAM", "TIM"]
    assert solution == expected_solution


def test_calculate_name_score():
    data_location = '/Users/tphoran/github/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

    test_twenty_two = TwentyTwo(data_location)

    solution = test_twenty_two.calculate_name_score('COLIN', 938)
    expected_solution = 49714
    assert solution == expected_solution


def test_solve():
    data_location = '/Users/tphoran/github/projecteuler/projecteuler/' \
                        'twenty_two_input_data_test.txt'

    test_twenty_two = TwentyTwo(data_location)

    solution = test_twenty_two.solve()
    expected_solution = 222
    assert solution == expected_solution
