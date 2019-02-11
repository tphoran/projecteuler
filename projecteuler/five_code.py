import numpy as np


class Five(object):
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """

    def __init__(self, sequence):
        self.sequence = sequence

    def smallest_multiple_of_list(self, list_of_numbers):
        array_list_of_numbers = np.array(list_of_numbers)
        all_items_in_list_multipled = np.prod(array_list_of_numbers)
        smallest_multiple = 20
        while smallest_multiple < all_items_in_list_multipled:
            if sum(smallest_multiple % array_list_of_numbers) == 0:
                return smallest_multiple
            smallest_multiple += 20
        return all_items_in_list_multipled

    def solve(self):
        smallest_multiple_of_sequence = self.smallest_multiple_of_list(self.sequence)
        return smallest_multiple_of_sequence


one_to_twenty = list(range(1, 21))
five = Five(one_to_twenty)
print(five.solve())

"""
Potential better option is to get all unique primes for all numbers between 1
and 20 and multiplying together
"""
