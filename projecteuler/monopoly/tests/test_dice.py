from unittest import TestCase

from projecteuler.monopoly.dice import Dice


class TestDice(TestCase):
    def test_100_rolls_max_min_and_all_choices(self):
        expected_max = 6
        expected_min = 1
        expected_choices_set = set(list(range(expected_min, expected_max+1)))

        dice = Dice(expected_min, expected_max)

        test_range = 'Pass'
        test_choices = 'Pass'
        test_outcomes = []
        for x in range(1000):
            roll = dice.roll()
            test_outcomes.append(roll)
            if roll > expected_max or roll < expected_min:
                test_range = 'Fail'
        if set(test_outcomes) != expected_choices_set:
            test_choices = 'Fail'

        expected_test_range = 'Pass'
        expected_test_choices = 'Pass'

        self.assertEqual(test_range, expected_test_range)
        self.assertEqual(test_choices, expected_test_choices)

